import os
from pathlib import Path

# chdir()
"""
os.chdir('/xxx/xxx')
"""

# chmod()
""""
os.chmod('file.txt', 0o644)
"""

# chown()
# windowsOSは非対応
""""
os.chown('file.txt', 1000, 1000)
"""

# listdir()
print(os.listdir('C:/users'))

# pathlibでの代替
print(list(Path('C:/users').iterdir()))
print('----------------------------------')

# makedirs
os.makedirs('sample', exist_ok=True)

# pathlibでの代替
Path('sample2').mkdir(parents=True, exist_ok=True)

# remove
os.remove('file.txt')

# pathlibでの代替
Path('file.txt').unlink()

# rmdir
os.rmdir('empty_dir')

# pathlibでの代替
Path('empty_dir').rmdir()

# symlink
os.symlink('target.txt', 'link.txt')

# pathlibでの代替
Path('link.txt').symlink_to('target.txt')