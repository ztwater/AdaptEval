import inspect
from pydantic import BaseModel, ValidationError
from fastapi import Form
from fastapi.exceptions import RequestValidationError

class FormBaseModel(BaseModel):

    def __init_subclass__(cls, *args, **kwargs):
        field_default = Form(...)
        new_params = []
        schema_params = []
        for field in cls.__fields__.values():
            new_params.append(
                inspect.Parameter(
                    field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(field.default) if not field.required else field_default,
                    annotation=inspect.Parameter.empty,
                )
            )
            schema_params.append(
                inspect.Parameter(
                    field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(field.default) if not field.required else field_default,
                    annotation=field.annotation,
                )
            )

        async def _as_form(**data):
            try:
                return cls(**data)
            except ValidationError as e:
                raise RequestValidationError(e.raw_errors)

        async def _schema_mocked_call(**data):
            """
            A fake version which is given the actual annotations, rather than typing.Any,
            this version is used to generate the API schema, then the routes revert back to the original afterwards.
            """
            pass

        _as_form.__signature__ = inspect.signature(_as_form).replace(parameters=new_params)  # type: ignore
        setattr(cls, "as_form", _as_form)
        _schema_mocked_call.__signature__ = inspect.signature(_schema_mocked_call).replace(parameters=schema_params)  # type: ignore
        # Set the schema patch func as an attr on the _as_form func so it can be accessed later from the route itself:
        setattr(_as_form, "_schema_mocked_call", _schema_mocked_call)

    @staticmethod
    def as_form(parameters=[]) -> "FormBaseModel":
        raise NotImplementedError
