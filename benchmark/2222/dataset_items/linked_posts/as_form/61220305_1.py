from uuid import UUID, uuid4
from fastapi import Form, Depends
from pydantic import BaseModel

class AnyForm(BaseModel):
    id: UUID
    any_param: str
    any_other_param: int

    def __init__(self, any_param: str = Form(...), any_other_param: int = Form(1)):
        id = uuid4()
        super().__init__(id, any_param, any_other_param)

@app.post('/me')
async def me(form: AnyForm = Depends()):
    print(form)
    return form
