>>> import re
>>> def camel_to_snake(string):
...     groups = re.findall('([A-z0-9][a-z]*)', string)
...     return '_'.join([i.lower() for i in groups])
...
>>> camel_to_snake('ABCPingPongByTheWay2KWhereIsOurBorderlands3???')
'a_b_c_ping_pong_by_the_way_2_k_where_is_our_borderlands_3'
