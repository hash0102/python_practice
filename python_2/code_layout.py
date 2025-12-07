# インデント 
# 丸かっこの先頭に揃えるパターン
def correct_indent_1(var_one,two,
                     three,four):
    print(var_one)

# 先頭の値を縦で揃え、定義の始めの位置に閉じかっこをそろえるパターン
num_list = [
    1, 2, 3,
    11, 12, 13,
]

# 空行
# トップレベルの関数やクラスの間は２行ずつ開ける
def aiu():
    pass


def kakiku():
    pass


# クラス内のメソッド定義は１行ずつ開ける
class AiueClass:
    line_cnt =0

    def next_empty_line():
        pass

# import文
import os # 異なるモジュールはimport文を分ける
import sys
from subprocess import Popen, PIPE # 同じモジュールはimport文をまとめる

import third_party # サードパーティのモジュールは標準ライブラリの後にimport

import mymodule # ローカルのモジュールは最後にimport

# 空白文字
# 代入演算子や比較演算子の空白文字
i = i + 1
count_up += 1
x = 1
y = 2
long = 3

# カンマやコロンと空白文字
if x == 4:
    sum(x, y)

# カッコや波カッコの前後
latte(milk[1], {art: 2})