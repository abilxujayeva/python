# Lug'at elementlari bilan ishlash (takrorlash)
# .items() - ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin
# .keys() - bu lug‘atdagi barcha kalitlarni olish uchun ishlatiladigan metod
# .values() - bu lug‘atdagi barcha qiymatlarni olish uchun ishlatiladigan metod
# set() - bu to‘plam (to'plam) yaratadigan funksiya. set() — bu takrorlanmaydigan elementlardan iborat tartibsiz to‘plam



talaba_0 = {'ism':'mansur', 'yosh':'20', 'kurs':'2-kurs', 'fakultet':'iqtisodiyot' }
print(talaba_0.items())

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


maxsulotlar = {'olma':15000, 'anor':35000, 'uzum':19000, 'shaftoli':18000, 'banan':25000}
print("Do'konimizdagi maxsulotlar: ")
for maxsulot in sorted(maxsulotlar):
    print(maxsulot.title())

maxsulotlar = {'olma':15000, 'anor':35000, 'uzum':19000, 'shaftoli':18000, 'banan':25000}
print(maxsulotlar.values())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)


# Amaliyot
python_izohli_lugat = {'boolen':'mantiqiy qiymat', 'float':'onlik son',  'integer':'butun son', 'for':'bir amalni qayta qayta bajarish',}
for key, value in sorted(python_izohli_lugat.items()):
    print(f"{key.title()} - {value}")

davlatlar = {
    'Ozbekiston':'Toshkent',
    'Qizgiziston':'Bishkek',
    'Amerika':'Vashington',
    'Canada':'Ottava',
    'Tojikiston':'Dushanbe',
    'Qozogiston':'Ostona'
}
print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
    print(davlat.upper())
print("Davlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.upper())


davlatlar = {
    'Ozbekiston':'Toshkent',
    'Qizgiziston':'Bishkek',
    'Amerika':'Vashington',
    'Canada':'Ottava',
    'Tojikiston':'Dushanbe',
    'Qozogiston':'Ostona'
}
davlat  = input("Istalgan davlatni kiriting: ")
poytaxt = davlatlar.get(davlat, "Bunday malumot mavjud emas!!!")
print(poytaxt)

menyu = {
    'osh':'35000',
    'shorva':'30000',
    'manti':'12000',
    'somsa':'15000',
    'chuchvara':'25000',
    'norin':'40000'
}
buyurtmalar = []
for k in range(3):
    buyurtmalar.append(input(f"{k+1} Istalgan taomni tanlang "))
for buyurtma in buyurtmalar:
    if buyurtma in menyu:
        print(f"{buyurtma} {menyu[buyurtma]} so'm ")
    else:
        print("Bizda bunday taom yoq")