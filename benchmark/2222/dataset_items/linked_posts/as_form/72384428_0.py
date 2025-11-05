from fastapi import Form

class SomeForm:

    def __init__(
        self,
        username: str = Form(...),
        password: str = Form(...),
        authentication_code: str = Form(...)
    ):
        self.username = username
        self.password = password
        self.authentication_code = authentication_code


@app.post("/login", tags=['Auth & Users'])
async def auth(
        user: SomeForm = Depends()
):
    # return something / set cookie
