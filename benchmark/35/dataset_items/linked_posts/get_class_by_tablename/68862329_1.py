from sqlalchemy import Column, Integer

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    # ... and other columns

    def some_method(self):
        # successfully use lookup like this
        balance_model = self.model_lookup_by_table_name("balance")
        # ...
        return balance_model
