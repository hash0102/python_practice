import os

# confstr
# windowsOSは非対応
""""
print(os.confstr('CS_PATH'))  # システムのデフォルトPAT
"""

# confstr_names
# windowsOSは非対応
"""
for key in os.confstr_names:
    print(key, '=', os.confstr(key))
"""

# sysconf
# windowsOSは非対応
""""
print(os.sysconf('SC_PAGE_SIZE'))  # ページサイズ（バイト単位）
"""

# os.sysconf_names
# windowsOSは非対応
"""
NAME_TO_CODE = {name: code for code, name in os.sysconf_names.items()}

# 物理CPUコア数を取得する
if 'SC_NPROCESSORS_ONLN' in NAME_TO_CODE:
    try:
        cpu_count = os.sysconf('SC_NPROCESSORS_ONLN')
        print(f"オンラインCPUコア数 (SC_NPROCESSORS_ONLN): {cpu_count}")
    except ValueError:
        print("SC_NPROCESSORS_ONLN の情報が取得できませんでした。")
"""

# cpu_count
print(os.cpu_count())  # 例: 8
print('----------------------------------')

# getloadavg
""""
print(os.getloadavg())  # (0.72, 0.85, 0.90) など
"""

# urandom
print(os.urandom(10)) #10バイトのランダムなbytesオブジェクトを生成