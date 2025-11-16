from datetime import datetime
import pytz

# windowsのため、例ではpytzを使用
tz = pytz.timezone("Asia/Tokyo")
dt = datetime(2025, 8, 2, 12, 0, tzinfo=tz)
print(dt)

# 以下はWIndowsでは動かない
# UTC に変換
dt_utc = dt.astimezone(pytz.utc)
print(dt_utc)

from datetime import datetime
from zoneinfo import ZoneInfo

# 現在のUTC
utc_now = datetime.now(ZoneInfo("UTC"))
print("UTC:", utc_now)

# タイムゾーン変換
tokyo_time = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
print("Tokyo:", tokyo_time)

ny_time = utc_now.astimezone(ZoneInfo("America/New_York"))
print("New York:", ny_time)