talaba_1 = {
    'ism':'amir', 
    'familiya':'karimov', 
    'yosh':'19', 
    't-yil':'2006'
    }
print(talaba_1.items())
for kalit, qiymat in talaba_1.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat}")


phones = {
    'vali':'iphone 15 pro max',
    'ali':'samsung galaxy s20',
    'olim':'redmi not 14'
    }
for k,q in phones.items():
    print(f"{k}ning telefoni {q}")



maxsulotlar = {'olma':15000, 'anor':35000, 'uzum':19000, 'shaftoli':18000, 'banan':25000}
print(maxsulotlar.keys())

bozorlik = ['olma', 'anor', 'uzum', 'nok', 'non']
for maxsulot in maxsulotlar:
    if maxsulot in bozorlik:
        print(f"{maxsulot.title()} {maxsulotlar[maxsulot]} so'm")
for meva in bozorlik:
    if meva not in bozorlik:
        print(f"Iltimos, do'koningizga {meva}ni ham olib keling")