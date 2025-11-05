with ResourceProxy() as resource:  # proxied __enter__ is called
    # now `resource` is NOT a ResourceProxy instance, because what we called is `_resource.__enter__`
    do_something_with_resource()
    # `_resource.__exit__` is called and closed itself properly. 
    # Here is nothing to do with ResourceProxy, because it has never enter `with` context
