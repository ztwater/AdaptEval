d = {'meta': {'status': 'OK', 'status_code': 200}}
deep_get(d, ['meta', 'status_code'])     # => 200
deep_get(d, ['garbage', 'status_code'])  # => None
