@ray.remote
def f():
    # Print the PYTHONPATH on the worker process.
    import sys
    print(sys.path)

f.remote()
