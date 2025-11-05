from fastapi import Form, Depends

class AnyForm:
    def __init__(self, any_param: str = Form(...), any_other_param: int = Form(1)):
        self.any_param = any_param
        self.any_other_param = any_other_param

    def __str__(self):
        return "AnyForm " + str(self.__dict__)

@app.post('/me')
async def me(form: AnyForm = Depends()):
    print(form)
    return form
