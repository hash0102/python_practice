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
        
user1 = User("bob", 32, "Texas")
print(type(user1))
print(user1.name)
print(user1.age)
user1.increment_age()
print(user1.age)
user1.increment_age()
print(user1.age)
print(user1.start_name())
user2 = User('kate',23, 'Florida')
user2.increment_age