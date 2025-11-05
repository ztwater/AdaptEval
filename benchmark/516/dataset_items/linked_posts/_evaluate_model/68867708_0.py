import argparse

ap = argparse.ArgumentParser()

# List of args
ap.add_argument('--foo', default=True, type=bool, help='Some helpful text that is not bar. Default = True')

# Importable object
args = ap.parse_args()
