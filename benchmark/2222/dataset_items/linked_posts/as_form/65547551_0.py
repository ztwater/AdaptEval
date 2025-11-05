from fastapi.testclient import TestClient
from fastapi import FastAPI, Depends, Form
from pydantic import BaseModel


app = FastAPI()


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls


@form_body
class Item(BaseModel):
    name: str
    another: str


@app.post('/test', response_model=Item)
def endpoint(item: Item = Depends(Item)):
    return item


tc = TestClient(app)


r = tc.post('/test', data={'name': 'name', 'another': 'another'})

assert r.status_code == 200
assert r.json() == {'name': 'name', 'another': 'another'}
