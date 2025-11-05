from collections.abc import Iterable, Mapping

def convertEr(iterab):
    """Tries to convert an iterable to list of floats, ints or the original thing
    from the iterable. Converts any iterable (tuple,set, ...) to itself in output.
    Does not work for Mappings  - you would need to check abc.Mapping and handle 
    things like {1:42, "1":84} when converting them - so they come out as is."""

    if isinstance(iterab, str):
        return maybeMakeNumber(iterab)

    if isinstance(iterab, Mapping):
        return iterab

    if isinstance(iterab, Iterable):
        return  iterab.__class__(convertEr(p) for p in iterab)


data = ["unkind", {1: 3,"1":42}, "data", "42", 98, "47.11", "of mixed", 
        ("0", "8", {"15", "things"}, "3.141"), "types"]

converted = convertEr(data)
print(converted)
