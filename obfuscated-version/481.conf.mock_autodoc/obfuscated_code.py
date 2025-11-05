from sphinx.ext import autodoc

class MockedClassDocumenter(autodoc.ClassDocumenter):
    def add_line(self, var_0: str, var_1: str, *var_2: int) -> None:
        if var_0 == "   Bases: :py:class:`object`":
            return
        super().add_line(var_0, var_1, *var_2)

autodoc.ClassDocumenter = MockedClassDocumenter
