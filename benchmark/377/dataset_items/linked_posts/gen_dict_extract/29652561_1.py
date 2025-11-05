o = { 'temparature': '50', 
      'logging': {
        'handlers': {
          'console': {
            'formatter': 'simple', 
            'class': 'logging.StreamHandler', 
            'stream': 'ext://sys.stdout', 
            'level': 'DEBUG'
          }
        },
        'loggers': {
          'simpleExample': {
            'handlers': ['console'], 
            'propagate': 'no', 
            'level': 'INFO'
          },
         'root': {
           'handlers': ['console'], 
           'level': 'DEBUG'
         }
       }, 
       'version': '1', 
       'formatters': {
         'simple': {
           'datefmt': "'%Y-%m-%d %H:%M:%S'", 
           'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
         }
       }
     }, 
     'treatment': {'second': 5, 'last': 4, 'first': 4},   
     'treatment_plan': [[4, 5, 4], [4, 5, 4], [5, 5, 5]]
}
