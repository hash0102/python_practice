# sys.stdin
import sys

print("input:")
text = sys.stdin.readline()
print("content:", text)

# $ echo "hello" | python3 sys_module2.py でも実行可能

# sys.stdout
sys.stdout.write("default\n")

# $ python3 sys_module2.py > output.txt で実行

# sys.stderr

import sys
sys.stderr.write("hello world\n")
# $ python3 sys_module2.py > /dev/nullで実行
print('----------------------------------')