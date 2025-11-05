import pydash  # pip install pydash

assert pydash.snake_case("WriteLine") == "write_line"
assert pydash.snake_case("writeLine") == "write_line"
assert pydash.camel_case("write_line") == "writeLine"
assert pydash.upper_first(pydash.camel_case("write_line")) == "WriteLine"
