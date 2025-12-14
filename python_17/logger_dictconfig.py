import logging.config
import json

# 設定辞書
log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
        'file': {
            'class': 'logging.FileHandler',
            'encoding':'utf-8',
            'formatter': 'default',
            'filename': 'dictconfig.log',
            'level': 'DEBUG',
        },
    },
    'loggers': {
        'my_app': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# 辞書からロギング設定を読み込む
logging.config.dictConfig(log_config)

# ログを出力
logger = logging.getLogger('my_app')
logger.debug('これはデバッグメッセージです。')
logger.info('これは情報メッセージです。')