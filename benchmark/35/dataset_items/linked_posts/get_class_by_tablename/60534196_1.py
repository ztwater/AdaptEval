# app/models.py
class Account(Base):  # Note this is the customized Base class
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    account_number = Column(String)
