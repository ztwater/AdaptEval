DataStructure = {
    'Collections': {
        'Map': [
            ('dict', 'OrderDict', 'defaultdict'),
            ('chainmap', 'types.MappingProxyType')
        ],
        'Set': [('set', 'frozenset'), {'multiset': 'collection.Counter'}]
    },
    'Sequence': {
        'Basic': ['list', 'tuple', 'iterator']
    },
    'Algorithm': {
        'Priority': ['heapq', 'queue.PriorityQueue'],
        'Queue': ['queue.Queue', 'multiprocessing.Queue'],
        'Stack': ['collection.deque', 'queue.LifeQueue']
        },
    'text_sequence': ['str', 'byte', 'bytearray']
}
