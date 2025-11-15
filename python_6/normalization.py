import unicodedata

char = 'é'  # U+00E9
print(unicodedata.name(char))  # LATIN SMALL LETTER E WITH ACUTE

# NFDとNFC
# 分解（NFD）: é → e + ´
decomposed = unicodedata.normalize('NFD', char)
print(decomposed)               # 'é'
print([unicodedata.name(c) for c in decomposed])
# → ['LATIN SMALL LETTER E', 'COMBINING ACUTE ACCENT']

# 合成（NFC）: e + ´ → é
recomposed = unicodedata.normalize('NFC', decomposed)
print(recomposed)  # 'é'

# 全角から半角への変換（NFKC）
zenkaku = 'ＡＢＣ１２３'
hankaku = unicodedata.normalize('NFKC', zenkaku)
print(hankaku)  # 'ABC123'

# 互換文字の統一（NFKD）
import unicodedata

text = '①'  # 丸付き数字「1」
nkfd_text = unicodedata.normalize('NFKD', text)
print(nkfd_text)  # '1'