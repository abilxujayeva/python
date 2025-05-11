def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
talaba1 = toliq_ism_yasa('muzaffar', 'karimov')
talaba2 = toliq_ism_yasa('karim', 'muzaffarov')
print(f"Darsga kelmagan talabalar: {talaba1}, {talaba2}")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasining_ismi: 
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

def oraliq(min,max):
    sonlar = [] 
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar
print(oraliq(0,10))
print(oraliq(10,21))


Amaliyot

def mijoz_info(ism, familiya, t_yil, t_joy, email="", tel=""):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "t_yil": t_yil,
        "t_joy": t_joy,
        "email": email,
        "telefon": tel,
    }
    return mijoz
print(mijoz_info('fatima', 'abilxujayeva', '2000','fargona'))




def mijoz_info(ism, familiya, t_yil, t_joy, email="", tel=""):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "t_yil": t_yil,
        "t_joy": t_joy,
        "email": email,
        "telefon": tel,
    }
    return mijoz
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break
print("Mijozlar:")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
       f"telefoni: {mijoz['telefon']}"
    )





def kattasini_aniqla(son1, son2, son3):
    """Uchta sonning eng kattasini aniqlovchi funksiya"""
    if son1>son2 and son1>son3:
        print(f"Eng katta son: {son1}")
        return son1
    elif son2>son1 and son2>son3:
        print(f"Eng katta son: {son2}")
        return son2
    else:
        print(f"Eng katta son: {son3}")
        return son3
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))
kattasini_aniqla = kattasini_aniqla(son1, son2, son3)


def aylanani_hisobla(radius):
    diametr  = 2*radius
    perimetr = 2*3.14*radius
    yuzi = 3.14*(radius**2)
    aylana = {
        "diametr" : diametr,
        "perimetr": perimetr,
        "yuzi":yuzi
    }
    return aylana
radius = int(input("aylananing radiusini kiriting: "))
print(aylanani_hisobla(radius))




def tub_sonni_aniqla(x, y):
    """Foydalanuvchi tomonidan kiritilgan oraliqdagi tub sonlarni aniqlash"""
    tub_sonlar = []
    for son in range(x, y+1):
        if son >1:
            for i in range(2, int(son**0.5)+1):
                if son%i ==0:
                    break
            else: 
                tub_sonlar.append(son)
    return tub_sonlar
x = int(input("Boshlanish nuqtani kiriting: "))
y  = int(input("Tugash nuqtasini kiriting: "))
print(tub_sonni_aniqla(x,y))



def fibonacci_hisobla(son):
    fibonacci = []
    for x in range(son):
        if x == 0 or x == 1:
            fibonacci.append(x)
        else:
            fibonacci.append(fibonacci[x-1]+fibonacci[x-2])
    return fibonacci
ask_user = int(input("Istalgan sonni kiriting: "))
print(fibonacci_hisobla(ask_user))