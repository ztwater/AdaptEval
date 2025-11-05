import pytest
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Session

engine = sa.create_engine("postgresql+psycopg2://postgres@localhost/test")
Base = declarative_base(bind=engine)


class A(Base):
    __tablename__ = "table_a"
    a_id = sa.Column(sa.Integer, primary_key=True)


class B(Base):
    __tablename__ = "table_b"
    b_id = sa.Column(sa.Integer, primary_key=True)
    a_id = sa.Column(sa.Integer, sa.ForeignKey("table_a.a_id"))


@pytest.fixture
def table_name_to_class():
    try:
        Base.metadata.create_all()
        Base.registry.configure()
        yield {m.tables[0].name: m.class_ for m in Base.registry.mappers}
    finally:
        Base.metadata.drop_all()


def test_table_lookup(table_name_to_class):
    assert table_name_to_class["table_a"] is A
    assert table_name_to_class["table_b"] is B

    with Session(bind=Base.metadata.bind) as session:
        session.add(table_name_to_class["table_a"](a_id=0))
        session.add(table_name_to_class["table_b"](b_id=0, a_id=0))
        session.add(table_name_to_class["table_b"](b_id=1, a_id=0))
        session.commit()

    assert engine.execute(""" SELECT COUNT(a_id) FROM table_a """).scalar() == 1
    assert engine.execute(""" SELECT COUNT(b_id) FROM table_b """).scalar() == 2
