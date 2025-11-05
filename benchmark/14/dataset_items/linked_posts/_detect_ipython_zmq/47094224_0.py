import sys

if '--notebook' in sys.argv:
    ENVIRONMENT = "notebook"
else:
    ENVIRONMENT = "dev"
