def update_version_strings(var_0, var_1):
    var_2 = re.compile(r"(^_*?version_*?\s*=\s*['\"])(\d+\.\d+\.\d+)", re.M)
    with open(var_0, "r+") as f:
        var_3 = f.read()
        f.seek(0)
        f.write(
            re.sub(
                var_2,
                lambda match: "{}{}".format(match.group(1), var_1),
                var_3,
            )
        )
        f.truncate()
