_last_result_time = None
_last_result_value = None
def result(val):
    global _last_result_time
    global _last_result_value
    now = datetime.datetime.now()
    if not _last_result_time or now - _last_result_time > datetime.timedelta(hours=1):
        _last_result_value = <expensive computation here>
        _last_result_time = now
    return _last_result_value
