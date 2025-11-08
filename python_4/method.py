class Dog:
    species = "Canis familiaris"  # クラス変数（全インスタンス共通）

    def __init__(self, name, age):
        self.name = name  # インスタンス変数
        self.age = age

    # インスタンスメソッド
    def bark(self):
        print(f"{self.name} はワン！と吠えた！")

    # クラスメソッド
    @classmethod
    def what_species(cls):
        print(f"このクラスの種は {cls.species} です。")

    # 静的メソッド
    @staticmethod
    def human_years(dog_age):
        return dog_age * 7
