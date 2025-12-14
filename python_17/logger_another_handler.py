import logging

# 1. ロガー1の作成（認証ログ）
auth_logger = logging.getLogger('auth_logger')
auth_logger.setLevel(logging.INFO)

# 2. ハンドラー1の作成（認証ログをauth.logファイルに出力）
auth_handler = logging.FileHandler('auth.log', encoding='utf-8')
auth_handler.setLevel(logging.INFO)

auth_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
auth_handler.setFormatter(auth_formatter)
auth_logger.addHandler(auth_handler)

# 3. ロガー2の作成（データベースログ）
db_logger = logging.getLogger('db_logger')
db_logger.setLevel(logging.WARNING)

# 4. ハンドラー2の作成（データベースログをdb.logファイルに出力）
db_handler = logging.FileHandler('db.log', encoding='utf-8')
db_handler.setLevel(logging.WARNING)
db_formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s') # 別のフォーマット
db_handler.setFormatter(db_formatter)
db_logger.addHandler(db_handler)

# ログの出力
auth_logger.info('ユーザーAがログインしました。')
auth_logger.warning('無効なログイン試行がありました。')

db_logger.info('データベースに接続しました。')  # WARNINGレベル未満なので出力されない
db_logger.warning('データベース接続がタイムアウトしました。')