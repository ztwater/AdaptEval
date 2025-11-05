Original Dictionary: {'tuple_key': [(1, 2, 3), 4], 'nested': {'key': (5, 6, 7)}}
Serialized JSON Data: {"tuple_key": {"__tuple__": true, "items": [1, 2, 3]}, "nested": {"key": {"__tuple__": true, "items": [5, 6, 7]}}}
Decoded Dictionary: {'tuple_key': [(1, 2, 3), 4], 'nested': {'key': (5, 6, 7)}}
