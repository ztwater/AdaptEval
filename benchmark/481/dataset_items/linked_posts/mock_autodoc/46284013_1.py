# ClassDocumenter.add_directive_header uses ClassDocumenter.add_line to
#   write the class documentation.
# We'll monkeypatch the add_line method and intercept lines that begin
#   with "Bases:".
# In order to minimize the risk of accidentally intercepting a wrong line,
#   we'll apply this patch inside of the add_directive_header method.

from sphinx.ext.autodoc import ClassDocumenter, _

add_line = ClassDocumenter.add_line
line_to_delete = _(u'Bases: %s') % u':class:`object`'

def add_line_no_object_base(self, text, *args, **kwargs):
    if text.strip() == line_to_delete:
        return

    add_line(self, text, *args, **kwargs)

add_directive_header = ClassDocumenter.add_directive_header

def add_directive_header_no_object_base(self, *args, **kwargs):
    self.add_line = add_line_no_object_base.__get__(self)

    result = add_directive_header(self, *args, **kwargs)

    del self.add_line

    return result

ClassDocumenter.add_directive_header = add_directive_header_no_object_base
