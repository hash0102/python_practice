import logging.config

# INIファイルから設定を読み込む
logging.config.fileConfig('logging.ini')

# ログを出力
logger = logging.getLogger('my_app')
logger.debug('これはデバッグメッセージです。')
logger.info('これは情報メッセージです。')