with Resource() as resource:  # __enter__ is called and returns a value as `resource`
    do_something_with_resource()
    # `resource.__exit__` is called
