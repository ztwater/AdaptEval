@as_form
class Test(BaseModel):
    param: str
    a: int = 1
    b: str = '2342'
    c: bool = False
    d: Optional[float] = None


@router.post('/me', response_model=Test)
async def me(request: Request, form: Test = Depends(Test.as_form)):
    return form
