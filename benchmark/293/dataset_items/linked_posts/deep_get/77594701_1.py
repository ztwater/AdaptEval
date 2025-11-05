get_nested(
    {'nest': {'nest2': 777}},
    key='nest.nest2'
)
# returns: 777

get_nested(
    {'abc': {}},
    key='abc.lalala'
)
# returns: None   # 'cause defaut=None

get_nested(
    {},
    key='tyty.nana.qwerty',
    default={}
)
# returns: {}
