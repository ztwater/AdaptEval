import os


def check_root_privileges() -> None:
    # credit: https://stackoverflow.com/a/69134255/5922329
    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")