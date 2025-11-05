from sqlalchemy import Column, Integer

class Balance(Base):
    __tablename__ = "balance"

    id = Column(Integer, primary_key=True)

    # ... other columns

    def some_method(self):
        # lookup works on every model
        user_model = self.model_lookup_by_table_name("user")
        # ...
        return user_model
