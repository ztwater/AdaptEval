import inspect
from typing import Type

from fastapi import Form
from pydantic import BaseModel
from pydantic.fields import ModelField

def as_form(var_0: Type[BaseModel]):
    var_1 = []

    for field_name, model_field in var_0.__fields__.items():
        var_2: ModelField  # type: ignore

        var_1.append(
            inspect.Parameter(
                var_2.alias,
                inspect.Parameter.POSITIONAL_ONLY,
                default=Form(...) if var_2.required else Form(var_2.default),
                annotation=var_2.outer_type_,
            )
        )

    async def as_form_func(**var_3):
        return var_0(**var_3)

    var_4 = inspect.signature(as_form_func)
    var_4 = var_4.replace(parameters=var_1)
    as_form_func.__signature__ = var_4  # type: ignore
    setattr(var_0, "as_form", as_form_func)
    return var_0
