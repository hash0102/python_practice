class User2:
    # データ属性としてuser_typeを初期値Noneで取得
    user_type = None
    # コンストラクターメソッド
    def __init__(self, name, age, address):
        # インスタンス変数name、age、addressにコンストラクター引数の値を代入
        self.name = name
        self.age = age
        self.address = address

    # __repr__メソッドを追加
    def __repr__(self):
        return F'<User id:{id(self)} name:{self.name}>'
    
    # __len__メソッドを追加
    def __len__(self):
        return len(self.name)
    
    # __eq__メソッドを追加
    def __eq__(self, other):
        # 年齢が同じ場合にtrue
        return self.age == other.age
    
    # propertyデコレーターを追加
    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return " "

user2 = User2('Noran', 24, 'paris')
# データ属性のようにカッコなしでアクセス
print(user2.start_name)