import logging

# 1. ロガーの作成
logger = logging.getLogger('my_logger')
# DEBUGレベル以上のメッセージを受け付ける
logger.setLevel(logging.DEBUG)  


# 2. ハンドラーの作成
# コンソール出力用のハンドラー
ch = logging.StreamHandler()
# INFOレベル以上のメッセージを出力
ch.setLevel(logging.INFO)  

# ファイル出力用のハンドラー
fh = logging.FileHandler('app.log', encoding='utf-8')
# DEBUGレベル以上のメッセージを出力
fh.setLevel(logging.DEBUG)  

# 3. フォーマッターの作成
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 4. ハンドラーにフォーマッターを設定
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# 5. ロガーにハンドラーを追加
logger.addHandler(ch)
logger.addHandler(fh)

# ログを出力
logger.debug('これはデバッグメッセージです。ファイルにのみ出力されます。')
logger.info('これは情報メッセージです。コンソールとファイルの両方に出力されます。')
logger.warning('これは警告メッセージです。これも両方に出力されます。')