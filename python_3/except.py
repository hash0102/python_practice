# 例外処理
try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print('０で割れません')
print('-'*30)

# **複数の例外を補足**
try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print('０で割れません')
except TypeError:
    print('文字列で割れません')
print('-'*30)

# 複数の例外を指定
try:
    num = 10 / 0
    print(num)
except (ZeroDivisionError, TypeError, NameError)as e:
    # 例外オブジェクトを受け取り出力
    print(F'エラー名：{e}')
print('-'*30)

# else
try:
    num = 10 / 10
    print(num)
except (ZeroDivisionError, TypeError, NameError)as e:
    print(F'エラー名：{e}')
# exceptで捕捉されなかった場合に実行
else:
    print('else処理成功')
print('-'*30)

# finally
try:
    num = 10 / 0
    print(num)
except (ZeroDivisionError, TypeError, NameError)as e:
    print(F'エラー名：{e}')
else:
    print('処理成功')
# 例外の発生有無にかかわらず実行
finally:
    print('この処理はエラーが起きても起きなくても実行')
print('-'*30)

# 基底クラスで例外を補足
try:
    num  = 10 / 0
    print(num)

except ArithmeticError as e: # ArithmeticErrorはZeroDivisionErrorの基底クラス
    print(e)
print('-'*30)

#  独自の例外
class MyError(Exception):
    pass

# raiseで発生
raise MyError('MyErrror発生')