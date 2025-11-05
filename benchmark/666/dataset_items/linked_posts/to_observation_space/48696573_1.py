class Foo():
  def toJSON(self):
        return json.loads(
            json.dumps(self, sort_keys=True, indent=4, separators=(',', ': '), default=json_default_format), cls=DateTimeDecoder)


Foo().toJSON() 
