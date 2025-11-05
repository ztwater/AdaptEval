sys.stdout = StringIO()
sys.stderr = StringIO()
foo(bar)
sys.stdout = sys.__stdout__ # These are provided by python
sys.stderr = sys.__stderr__
