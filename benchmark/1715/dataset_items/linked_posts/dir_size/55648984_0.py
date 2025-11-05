import os


def du(path):
    if os.path.islink(path):
        return (os.lstat(path).st_size, 0)
    if os.path.isfile(path):
        st = os.lstat(path)
        return (st.st_size, st.st_blocks * 512)
    apparent_total_bytes = 0
    total_bytes = 0
    have = []
    for dirpath, dirnames, filenames in os.walk(path):
        apparent_total_bytes += os.lstat(dirpath).st_size
        total_bytes += os.lstat(dirpath).st_blocks * 512
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.islink(fp):
                apparent_total_bytes += os.lstat(fp).st_size
                continue
            st = os.lstat(fp)
            if st.st_ino in have:
                continue  # skip hardlinks which were already counted
            have.append(st.st_ino)
            apparent_total_bytes += st.st_size
            total_bytes += st.st_blocks * 512
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            if os.path.islink(dp):
                apparent_total_bytes += os.lstat(dp).st_size
    return (apparent_total_bytes, total_bytes)
