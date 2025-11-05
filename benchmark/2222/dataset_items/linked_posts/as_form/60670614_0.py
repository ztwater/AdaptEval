class AnyForm(BaseModel):
    any_param: str
    any_other_param: int = 1

    @classmethod
    def as_form(
        cls,
        any_param: str = Form(...),
        any_other_param: int = Form(1)
    ) -> AnyForm:
        return cls(any_param=any_param, any_other_param=any_other_param)

@router.post('')
async def any_view(form_data: AnyForm = Depends(AnyForm.as_form)):
        ...
