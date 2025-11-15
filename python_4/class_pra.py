# Userというクラスを定義
class User:
    # データ属性としてuser_typeを初期値Noneで取得
    user_type = None
    # コンストラクターメソッド
    def __init__(self, name, age, address):
        # インスタンス変数name、age、addressにコンストラクター引数の値を代入
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        """年齢を一つ増やす"""
        self.age +=1
    
    def start_name(self):
        """nameの１文字目を取得"""
        if len(self.name) > 0:
            return self.name[0]
        else:
            return " "