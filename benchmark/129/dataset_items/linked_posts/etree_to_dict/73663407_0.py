from xmlschema import ParkerConverter, XMLSchema, to_dict

xml = '...'
schema = XMLSchema('...')
to_dict(xml, schema=schema, converter=ParkerConverter)
