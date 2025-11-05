def convertNotebook(var_0, var_1):

  with open(var_0) as fh:
    var_2 = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  var_3 = PythonExporter()
  source, meta = var_3.from_notebook_node(var_2)

  with open(var_1, 'w+') as fh:
    fh.writelines(source.encode('utf-8'))
