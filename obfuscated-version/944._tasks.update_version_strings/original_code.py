def update_version_strings(file_path, new_version):
    version_regex = re.compile(r"(^_*?version_*?\s*=\s*['\"])(\d+\.\d+\.\d+)", re.M)
    with open(file_path, "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(
            re.sub(
                version_regex,
                lambda match: "{}{}".format(match.group(1), new_version),
                content,
            )
        )
        f.truncate()
