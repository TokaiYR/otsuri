print("金額は150円です")
n = int(input("挿入する金額を入力")) #挿入金額n
x = 150 #商品価格x

if n >= 150:
    m = n-x #おつりm

    #おつりの各枚数abcd
    a = m//500
    b = (m-500*a)//100
    c = (m-500*a-100*b)//50
    d = (m-500*a-100*b-50*c)//10
    print(f"おつりは500円{a}枚、100円{b}枚、50円{c}枚、10円{d}枚です")

else:
    print("必要金額が不足しています")

