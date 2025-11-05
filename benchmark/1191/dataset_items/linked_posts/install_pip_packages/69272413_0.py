import sys
from subprocess import run, PIPE, STDOUT
import pkg_resources

def run_cmd(cmd):
    ps = run(cmd, stdout=PIPE, stderr=STDOUT, shell=True, text=True)
    print(ps.stdout)


# packages to be conditionally installed with exact version
required = {"click==8.0.1", "semver==3.0.0.dev2"}
installed = {f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    run_cmd(f'pip install --ignore-installed {" ".join([*missing])}')
