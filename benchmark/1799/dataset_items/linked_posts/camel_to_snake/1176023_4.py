pattern = re.compile(
    r"""
        (?<=[[:lower:]])            # preceded by lowercase
        (?=[[:upper:]])             # followed by uppercase
        |                           #   OR
        (?<[[:upper:]])             # preceded by lower
        (?=[[:upper:]][[:lower:]])  # followed by upper then lower
    """,
    re.X,
)
