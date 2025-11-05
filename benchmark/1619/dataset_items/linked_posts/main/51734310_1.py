def keep_every_nth_info(n):
    i = -1
    def filter_record(record):
        nonlocal i
        i += 1
        return int(record.levelname != 'INFO' or i % n == 0)
    return filter_record

# Example usage for TensorFlow:
logging.getLogger('tensorflow').addFilter(keep_every_nth_info(5))
