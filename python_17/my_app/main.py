import logging
from my_app import sub_module

# 親ロガー
logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

# ハンドラー
fh = logging.FileHandler("parent.log", encoding="utf-8")
fh.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s"
)
fh.setFormatter(formatter)

logger.addHandler(fh)

logger.info("main.py からのログ")
sub_module.do_something()
