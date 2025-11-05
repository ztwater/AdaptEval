import sqlalchemy as sa


def get_class_by_table(base, table, data=None):
    """
    Return declarative class associated with given table. If no class is found
    this function returns `None`. If multiple classes were found (polymorphic
    cases) additional `data` parameter can be given to hint which class
    to return.

    ::

        class User(Base):
            __tablename__ = 'entity'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String)


        get_class_by_table(Base, User.__table__)  # User class


    This function also supports models using single table inheritance.
    Additional data paratemer should be provided in these case.

    ::

        class Entity(Base):
            __tablename__ = 'entity'
            id = sa.Column(sa.Integer, primary_key=True)
            name = sa.Column(sa.String)
            type = sa.Column(sa.String)
            __mapper_args__ = {
                'polymorphic_on': type,
                'polymorphic_identity': 'entity'
            }

        class User(Entity):
            __mapper_args__ = {
                'polymorphic_identity': 'user'
            }


        # Entity class
        get_class_by_table(Base, Entity.__table__, {'type': 'entity'})

        # User class
        get_class_by_table(Base, Entity.__table__, {'type': 'user'})


    :param base: Declarative model base
    :param table: SQLAlchemy Table object
    :param data: Data row to determine the class in polymorphic scenarios
    :return: Declarative class or None.
    """
    found_classes = set(
        c for c in base._decl_class_registry.values()
        if hasattr(c, '__table__') and c.__table__ is table
    )
    if len(found_classes) > 1:
        if not data:
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. "
                "Please provide data parameter for this function to be able "
                "to determine polymorphic scenarios.".format(
                    table.name
                )
            )
        else:
            for cls in found_classes:
                mapper = sa.inspect(cls)
                polymorphic_on = mapper.polymorphic_on.name
                if polymorphic_on in data:
                    if data[polymorphic_on] == mapper.polymorphic_identity:
                        return cls
            raise ValueError(
                "Multiple declarative classes found for table '{0}'. Given "
                "data row does not match any polymorphic identity of the "
                "found classes.".format(
                    table.name
                )
            )
    elif found_classes:
        return found_classes.pop()
    return None
