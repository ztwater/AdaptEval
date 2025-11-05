import pwd
import stat
import os

def check_user_dir(user, directory):
    dir_stat = os.stat(directory)

    user_id, group_id = pwd.getpwnam(user).pw_uid, pwd.getpwnam(user).pw_gid
    directory_mode = dir_stat[stat.ST_MODE]

    # use directory_mode as mask 
    if user_id == dir_stat[stat.ST_UID] and stat.S_IRWXU & directory_mode == stat.S_IRWXU:     # owner and has RWX
        return True
    elif group_id == dir_stat[stat.ST_GID] and stat.S_IRWXG & directory_mode == stat.S_IRWXG:  # in group & it has RWX
        return True
    elif stat.S_IRWXO & directory_mode == stat.S_IRWXO:                                        # everyone has RWX
        return True

    # no permissions
    return False
