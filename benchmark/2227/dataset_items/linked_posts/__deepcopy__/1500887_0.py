def __copy__(self):
  newone = type(self)()
  newone.__dict__.update(self.__dict__)
  return newone
