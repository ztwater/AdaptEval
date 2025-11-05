# Example usage
class ExampleForm(FormBaseModel):
    name: str
    age: int

@api.post("/test")
async def endpoint(form: ExampleForm = Depends(ExampleForm.as_form)):
    return form.dict()
