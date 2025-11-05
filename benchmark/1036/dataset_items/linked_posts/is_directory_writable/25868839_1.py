    except (OSError, IOError) as e:
        if e.errno == errno.EACCES or e.errno == errno.EEXIST:  # 13, 17
