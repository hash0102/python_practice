import logging

# ログ設定
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s'
)

# ロガーの取得
logger = logging.getLogger(__name__)

# ログ出力
def example_function():
    logger.info('この関数から情報ログが出力されました。')

example_function()