from yaml import Dumper

class MyDumper(Dumper):

  def write_indent(self):
    indent = self.indent or 0
    if not self.indention or self.column > indent \
        or (self.column == indent and not self.whitespace):
      self.write_line_break()


    ##########$#######################################
    # On the first level of indentation, add an extra
    # newline

    if indent == 2:
      self.write_line_break()

    ##################################################

    if self.column < indent:
      self.whitespace = True
      data = u' '*(indent-self.column)
      self.column = indent
      if self.encoding:
        data = data.encode(self.encoding)
      self.stream.write(data)
