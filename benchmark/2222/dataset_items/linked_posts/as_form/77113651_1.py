def before_validate_int(value: int) -> int:
    raise ValueError('before int')


MyInt = Annotated[int, BeforeValidator(before_validate_int)]


@as_form
class User(BaseModel):
    age: MyInt


@app.post("/postdata")
def postdata(user: User = Depends()):
    return {"age": user.age}
