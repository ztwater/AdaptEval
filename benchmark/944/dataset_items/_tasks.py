import re

def update_version_strings(file_path, new_version) -> None:
    # taken from:
    # https://stackoverflow.com/questions/57108712/replace-updated-version-strings-in-files-via-python
    # version_regex = re.compile(r"(^_*?version_*?\s*=\s*['\"])(\d+\.\d+\.\d+)", re.M)
    version_regex = re.compile(r"(^_*?version_*?\s*=\s*\")(\d+\.\d+\.\d+-?\S*)\"", re.M)
    with open(file_path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(
            re.sub(
                version_regex,
                # lambda match: "{}{}".format(match.group(1), new_version),
                lambda match: f'{match.group(1)}{new_version}"',
                content,
            )
        )
        f.truncate()
