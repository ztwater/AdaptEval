regex = re.compile(
    r"(\w+://)?"                # protocol                      (optional)
    r"(\w+\.)?"                 # host                          (optional)
    r"(([\w-]+)\.(\w+))"        # domain
    r"(\.\w+)*"                 # top-level domain              (optional, can have > 1)
    r"([\w\-\._\~/]*)*(?<!\.)"  # path, params, anchors, etc.   (optional)
)
