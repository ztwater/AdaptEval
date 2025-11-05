{
"log_config_worker": {
    "version": 1, 
    "root": {
        "handlers": [
            "queue"
        ], 
        "level": "DEBUG"
    }, 
    "disable_existing_loggers": true, 
    "handlers": {
        "queue": {
            "queue": null, 
            "class": "myclass1.QueueHandler"
        }
    }
}, 
"number_of_archived_logs": 15, 
"log_max_size": "300M", 
"cron_job_dir": "/etc/cron.hourly/", 
"logs_dir": "/var/log/patternex/", 
"log_rotate_dir": "/etc/logrotate.d/"
}
