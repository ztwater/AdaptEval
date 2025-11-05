import inspect
from fastapi import Form
from pydantic.fields import ModelField


def as_form(cls):
    """
    Allows a Pydantic model to be used as a FastAPI form

    Use this @as_form decorator on your model, then reference it in FastAPI using Depends(YourModel.as_form)
    For type hinting add "as_form: ClassVar[Callable[..., YourModel]]" to your model and import __future__.annotations

    https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi
    """

    new_parameters = []

    for model_field in cls.__fields__.values():
        model_field: ModelField  # type: ignore

        new_parameters.append(
            inspect.Parameter(
                model_field.alias,
                inspect.Parameter.POSITIONAL_ONLY,
                default=Form(...) if model_field.required else Form(model_field.default),
                annotation=model_field.outer_type_,
            )
        )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, "as_form", as_form_func)
    return cls