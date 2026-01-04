from unittest.mock import Mock, MagicMock


def use_with(obj):
    with obj as x:
        return "OK"
    
m1 = Mock()
m2 = MagicMock()

result1 = None
result2 = None

try:
    result1 = use_with(m1)
except Exception as e:
    result1 = type(e).__name__

try:
    result2 = use_with(m2)
except Exception as e:
    result2 = type(e).__name__

print(result1, result2)
print('-'*30)

from datetime import datetime
from zoneinfo import ZoneInfo

dt_naive = datetime(2025, 12, 16, 15, 30)
dt_tokyo = dt_naive.replace(tzinfo=ZoneInfo("Asia/Tokyo"))
dt_ny = dt_tokyo.astimezone(ZoneInfo("America/New_York"))

print(dt_tokyo)
print(dt_ny)

print('-'*30)

import base64

# 元の文字列
s = "Base64"

# 1. Base64 エンコード
b64 = base64.b64encode(s.encode("utf-8")).decode("ascii")
print("base64:", b64)

# 2. 末尾に == を追加
b64_extra = b64 + "=="
print("base64 + ==:", b64_extra)

# 3. Base64 デコード
decoded = base64.b64decode(b64_extra).decode("utf-8")
print("decoded:", decoded)
