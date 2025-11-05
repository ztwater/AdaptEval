from fastapi.routing import APIRoute
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.dependencies.utils import get_dependant, get_body_field

api = FastAPI()


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema

    def create_reset_callback(route, deps, body_field):
        def reset_callback():
            route.dependant.dependencies = deps
            route.body_field = body_field

        return reset_callback

    # The functions to call after schema generation to reset the routes to their original state:
    reset_callbacks = []

    for route in api.routes:
        if isinstance(route, APIRoute):
            orig_dependencies = list(route.dependant.dependencies)
            orig_body_field = route.body_field

            is_modified = False
            for dep_index, dependency in enumerate(route.dependant.dependencies):
                # If it's a form dependency, set the annotations to their true values:
                if dependency.call.__name__ == "_as_form":  # type: ignore
                    is_modified = True
                    route.dependant.dependencies[dep_index] = get_dependant(
                        path=dependency.path if dependency.path else route.path,
                        # This mocked func was set as an attribute on the original, correct function,
                        # replace it here temporarily:
                        call=dependency.call._schema_mocked_call,  # type: ignore
                        name=dependency.name,
                        security_scopes=dependency.security_scopes,
                        use_cache=False,  # Overriding, so don't want cached actual version.
                    )

            if is_modified:
                route.body_field = get_body_field(dependant=route.dependant, name=route.unique_id)

                reset_callbacks.append(
                    create_reset_callback(route, orig_dependencies, orig_body_field)
                )

    openapi_schema = get_openapi(
        title="foo",
        version="bar",
        routes=api.routes,
    )

    for callback in reset_callbacks:
        callback()

    api.openapi_schema = openapi_schema
    return api.openapi_schema


api.openapi = custom_openapi  # type: ignore[assignment]
