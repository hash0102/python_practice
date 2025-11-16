## 8.1 日付や時刻を扱う **`datetime`**

### **`date` オブジェクト**
- **`date.today()`**
    - **今日の日付（現在のローカル日付）** を取得
- **`date.weekday()`**
    - 曜日を **数値（`0〜6`）で返す**。
        - ※ **0 = 月曜日, 6 = 日曜日**
- **`date.isoweekday()`**
    - 曜日を **ISO形式（1〜7）で返す**。
        - ※ **1 = 月曜日, 7 = 日曜日**
- **`date.isoformat()`**
    - 日付を **`"YYYY-MM-DD"` の文字列形式に変換**する。
- **`date.fromisoformat(string)`**
    - **ISO形式の文字列（`YYYY-MM-DD`）から `date` オブジェクトを作成**する。
- **`date.strftime(format)`**
    - **好きな書式で文字列化**できる（`format` で指定）

**主なフォーマット指定子：**

| 書式コード | 意味 | 例 |
| --- | --- | --- |
| `%Y` | 西暦4桁 | 2025 |
| `%m` | 月（2桁） | 08 |
| `%d` | 日（2桁） | 02 |
| `%A` | 曜日（英語） | Saturday |
| `%a` | 曜日（省略） | Sat |
| `%w` | 曜日（0=日〜6） | 6 |

**例：date_obj.py**

### 時刻を扱う `time`オブジェクト
- **`time` オブジェクト**
    - **`datetime.time`** は **時刻（`hour`, `minute`, `second`, `microsecond`）** だけを持つオブジェクト
        - 日付の情報は含まない
- **`time.isoformat()`**
    - 時刻を **ISO 8601形式（HH:MM:SS）** の文字列に変換
- **`time.fromisoformat()`**
    - `"HH:MM[:SS[.ffffff]]"` 形式の文字列から `time` オブジェクトを生成。
- **`time.strftime(format)`**
    - 書式を指定して、`time` を文字列化する。
- 
**よく使う書式コード**
| 書式コード | 意味 | 例 |
| --- | --- | --- |
| `%H` | 時（24時間制） | 14 |
| `%I` | 時（12時間制） | 02 |
| `%M` | 分 | 30 |
| `%S` | 秒 | 15 |
| `%p` | AM/PM | PM |

- **`time.tzname`**
    - **タイムゾーン名（str）** を返す。
        - タイムゾーン情報がない場合は `None`。
**例：time_obj.py**

### 日時を扱う`datetime`オブジェクト

- **`datetime`オブジェクト**
    - 日付（year, month, day）時刻（hour, minute, second, microsecond）を扱うクラス
    - タイムゾーン情報（`tzinfo`）も持てる。
- **`datetime.today()`**
    - **現在のローカル日付・時刻を取得（タイムゾーンなし）**
- **`datetime.now(tz=None)`**
    - **現在の日時を取得。**
    - 引数にタイムゾーン（`tz`）を指定可能。
        - 指定なければローカルタイム。
- **`datetime.utcnow()`**
    - **協定世界時（UTC）の現在日時を返す（タイムゾーン情報なし）**
- **`datetime.date()`**
    - `datetime` オブジェクトから**日付部分だけを抽出**し、`date`オブジェクトを返す。
- **`datetime.time()`**
    - `datetime` オブジェクトから**時刻部分だけを抽出**し、`time`オブジェクトを返す。
- **`datetime.isoformat()`**
    - ISO 8601形式（`YYYY-MM-DDTHH:MM:SS.mmmmmm`）の文字列に変換。
- **`datetime.fromisoformat(date_string)`**
    - ISO 8601形式の文字列から`datetime`オブジェクトを生成。
- **`datetime.strftime(format)`**
    - 指定した書式で**文字列**に変換
- **`datetime.strptime(date_string, format)`**
    - 文字列を指定フォーマットで解析し、**`datetime`オブジェクト**を作成
    - 文字列と指定したフォーマットが同じでないとエラーになる
- **`datetime.tzname()`**
    - タイムゾーン名（文字列）を返す。
    - `tzinfo` がセットされていなければ `None`。

**例：datetime_obj.py**

### 日時の差を扱う `timedelta`オブジェクト

- **`timedelta`**
    - 2つの日時（`datetime` や `date`）の差を表したり、ある日時に時間を足したり引いたりできる、**「時間の長さ」** を表すオブジェクト
- 主な引数

| 引数 | 意味 |
| --- | --- |
| `days` | 日数 |
| `seconds` | 秒数 |
| `microseconds` | マイクロ秒（1/1000000 秒） |
| `milliseconds` | ミリ秒（1/1000 秒） |
| `minutes` | 分数（60秒） |
| `hours` | 時間（60分） |
| `weeks` | 週（7日） |

**例：timedelta_obj.py**

## 8.2 時刻を扱う **`time`**

### 時刻を取得する

#### **`time` モジュール**
- UNIXエポック（1970年1月1日 00:00:00 UTC）を基準とした **経過秒数（float型）** や、 **構造化された日時情報（struct_time）** などを扱う。
    - より正確な時間測定・待機・時刻表示に使える
> **UNIX時間（ユニックス時間、Unix time）**：
>1970年1月1日 00:00:00（UTC）から経過した秒数を整数で表したもの

- **`time.time()`**
    - 現在時刻を UNIX時間（1970年1月1日からの秒数）で取得

- **`time.gmtime(secs=None)`**
    - UNIX時間を **UTC（世界標準時）** に変換し、`struct_time` を返す。
        - 引数 `secs` を省略すると **現在時刻**を使う。
- **`time.localtime(secs=None)`**
    - UNIX時間を **ローカル時刻** に変換し、`struct_time` を返す。
        - `gmtime()` と似てるが、**タイムゾーンが反映される**。
          - `gmitime`は **UTC**で`localtime`は**ローカルタイム**
- **`time.strftime(format, t)`**
    - `struct_time` オブジェクトを、**書式付きの文字列**に変換。
- 主なフォーマット指定子

| 書式 | 意味 | 例 |
| --- | --- | --- |
| `%Y` | 年（4桁） | 2025 |
| `%m` | 月（2桁） | 08 |
| `%d` | 日（2桁） | 02 |
| `%H` | 時（24時間制） | 15 |
| `%M` | 分 | 32 |
| `%S` | 秒 | 33 |
| `%A` | 曜日（英語） | Saturday |

**例：  time_module.py**

### 時刻オブジェクト `struct_time`

- **`struct_time`**
    - `time.localtime()` や `time.gmtime()` の戻り値として得られるオブジェクト
    - 要素は **9個**。
    - タプルのように **インデックスでもアクセスできる**し、**名前付き属性でもアクセス可能**。

- **構造（要素一覧）**
```python
time.struct_time(tm_year, tm_mon, tm_mday,
                 tm_hour, tm_min, tm_sec,
                 tm_wday, tm_yday, tm_isdst, tm_zone, tm_gmtoff)
```
| **属性名** | **意味** | **値の範囲** | **例** |
| --- | --- | --- | --- |
| `tm_year` | 年 | 0000〜9999 | `2025` |
| `tm_mon` | 月（1月 = 1） | 1〜12 | `8` |
| `tm_mday` | 日 | 1〜31 | `2` |
| `tm_hour` | 時（24時間制） | 0〜23 | `15` |
| `tm_min` | 分 | 0〜59 | `32` |
| `tm_sec` | 秒 | 0〜60（うるう秒含む） | `45` |
| `tm_wday` | 曜日（0 = 月曜） | 0〜6 | `5`（土曜日） |
| `tm_yday` | 年内通算日 | 1〜366 | `214` |
| `tm_isdst` | 夏時間フラグ | `1`=適用, `0`=通常, `-1`=不明 | `1` |
| `tm_zone` | タイムゾーン名（任意） | OS依存（UNIXのみ） | `'JST'` |
| `tm_gmtoff` | UTCからの時差（秒単位） | OS依存（UNIXのみ） | `32400`（+9時間） |

**例：struct_time_obj.py**

#### スレッドの一時停止 time.sleep() 
- `seconds`: 一時停止する時間（**秒数、float可**）
    - 例：`1`（1秒）、`0.5`（0.5秒）
- **実行停止中は何が起きる**
    - **CPUも止まる**（スリープ中はCPUを使わない）
    - `sleep()` 中に **Ctrl+C** で中断すると `KeyboardInterrupt` が発生
```python
import time

time.sleep(seconds)
```
**例：time_sleep.py**

## 8.3 IANAタイムゾーンデータベースを扱う `zoneinfo`

- **`zoneinfo.ZoneInfo`**
    - `datetime` モジュールと連携し、タイムゾーン付き日時 (`aware datetime`) を扱える。
    - IANA（tzdata）形式のタイムゾーン名を使う。
      - **`pytz` の代替**として標準ライブラリ化。
    - WIndowsの場合は tzdataが使えない
- **よく使うタイムゾーン名の例**

| タイムゾーン名 | 地域 |
| --- | --- |
| `"UTC"` | 協定世界時 |
| `"Asia/Tokyo"` | 日本標準時（JST） |
| `"America/New_York"` | 米国東部時間（EST/EDT） |
| `"Europe/London"` | 英国時間（GMT/BST） |
| `"Asia/Shanghai"` | 中国標準時 |

- ZoneInfoを使う理由

| **特徴** | **内容** |
| --- | --- |
| ✅ 標準ライブラリ | Python 3.9〜 で標準搭載 |
| ✅ 夏時間対応 | 自動でDST（サマータイム）に対応 |
| ✅ `datetime`と連携 | `tzinfo` に渡して aware datetime を作成できる |
| ✅ IANA準拠 | `"Asia/Tokyo"` のような公式タイムゾーンに対応 |
| ❌ 独自の名前は非対応 | `"JST"` や `"EST"` などの省略名は使えません |

**例：zoneinfo_module.py**