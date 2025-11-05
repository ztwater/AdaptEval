def get_updated_dict(obj, path, value):
    key_list = path.split(".")

    for k in key_list[:-1]:
        obj = obj[k]

    obj[key_list[-1]] = value

get_updated_dict(data, "log_config_worker.handlers.queue.class", "myclass2.QueueHandler")
