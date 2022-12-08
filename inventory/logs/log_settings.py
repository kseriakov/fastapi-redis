LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'inventory/logs/info.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {'': {'level': 'INFO', 'handlers': ['file']}},
}