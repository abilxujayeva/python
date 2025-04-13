# lug'at - bu kalit-qiymat (key-value) juftliklarini saqlaydigan ma’lumot turi. Har bir elementda kalit bo‘ladi va unga mos qiymat bog‘lanadi
# Lug‘at — bu o‘zgaruvchan, tartibsiz va unikal kalitlarga ega ma’lumotlar to‘plami. Kalitlar orqali qiymatlarga tezda murojaat qilish mumkin. 
# .get() - metodi yordamida lug'atga murojat qilish va mavjud bolmagan kalitning o'rniga biror xabar qaytarish mumkin

car_0 = {'model':'ferrari', 'rang':'qora'}
print(car_0)
print(car_0['model'])


talaba_1 = {'ism':'amir', 'familiya':'karimov', 'yosh':'19', 't-yil':'2006'}
print(f"{talaba_1['ism'].title()} {talaba_1['familiya'].title()} {talaba_1['t-yil']}-yilda tugilgan. Hozir u {talaba_1['yosh']} yoshda")

talaba_1['kurs'] = 1
talaba_1['fakultet'] = 'informatika'
print(talaba_1)


talaba_2 = {}
talaba_2['ism_familiya'] = 'aziz qobilov'
talaba_2['yosh'] = 23
talaba_2['fakultet'] = 'iqtisodiyot'
print(talaba_2)
print(f"{talaba_2['ism_familiya'].title()}, {talaba_2['yosh']} yoshda. {talaba_2['fakultet']} fakultetida oqiydi")
talaba_2['yosh'] = 21
print(talaba_2)


talaba_1 = {'ism':'amir', 'familiya':'karimov', 'yosh':'19', 't-yil':'2006'}
print(talaba_1)
del talaba_1['ism']
print(talaba_1)


phones = {
    'vali':'iphone 15 pro max',
    'ali':'samsung galaxy s20',
    'olim':'redmi not 14'
    }
print(phones)
phone = phones['vali']
print(f"Valining telefoni {phone}")
#phone = phones['hasan']
# print(f"Hasanning telefoni {phone}")
phone = phones.get('hasan', 'Bunday ism mavjud emas')
print(phone)

phone = phones.get('odil')
print(phone)


#Amaliyot
otam = {'ism': 'davron', 'yil':'1961', 'joy':'Fargona'}
print(f"Otam {otam['ism'].title()},{otam['yil']}-yilda, {otam['joy']} viloyatida tugilgan")
onam = {'ism':'zarina', 'yil':'1975', 'joy':'qizgiziston'}
print(f"Onam {onam['ism'].title()}, {onam['yil']}- yilda, {onam['joy'].title()}da tugilgan")

taomlar = {'otam': 'osh', 'onam': 'chuchvara', 'singlim':'shorva', 'ozim':'shashlik', 'akam':'dolma'}
print(f"Otamning sevimli taomi {taomlar['otam']}, Onamniki esa {taomlar['onam']}, meniki {taomlar['ozim']}")

dictionary = {'integer':'butun son', 'float':'onlik son', 'string':'matn', 'if':'agar', 'else':'yoki'}
qiymat = input("Birorta istalgan sozni kiriting: ").lower()
print(dictionary.get(qiymat, "Bunday soz mavjud emas"))


dictionary = {'integer':'butun son', 'float':'onlik son', 'string':'matn', 'if':'agar', 'else':'yoki'}
qiymat = input("Birorta istalgan sozni kiriting: ").lower()
tarjima = dictionary.get(qiymat)
if tarjima==None:
    print("Bunday soz mavjud emas")
else:
    print(tarjima)
