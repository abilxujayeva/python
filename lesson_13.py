# #Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi

# def salom_ber():
#     """Salom beruvchi funksiya yozamiz"""
#     print("Assalomu alaykum")
# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchiga ismi bilan salom beruvchi funksiya yaratamiz"""
#     print(f"Assalomu alaykum {ism.title()}!")
# salom_ber("akmal")
# salom_ber("murod")

# print(salom_ber.__doc__)


# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ismi va familyasini ko`rsatuvchi funksiya yozamiz! """
#     print(f"Foydalanuchi ismi: {ism.title()}, foydalanuvchi familyasi: {familiya.title()}")
# toliq_ism('anvar', 'murodov')

# def toliq_ism(ism='karim', familiya='mansurov'):
#     """Foydalanuvchi ismi va familyasini ko`rsatuvchi funksiya yozamiz! """
#     print(f"Foydalanuchi ismi: {ism.title()}, foydalanuvchi familyasi: {familiya.title()}")
# toliq_ism()


# def ism_familiya(ism='botir', familiya='karimov'):
#     """Ism va familya bi;an murojaat qiluvchi dasturni yozamiz"""
#     print(f"{ism.title()} {familiya.title()} hush kelibsiz!")
# ism_familiya()

# def yilni_hisobla(ism, yosh):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2025-yosh}-yilda tugilgan")
# yilni_hisobla('Fatima', 25)

# def yoshni_hisobla(yil=2000, ism='fatimaxon'):
#     """Foydalanuvchi yoshini hisoblaymiz"""
#     print(f"{ism.title()}ning yoshi {2025-yil}da! ")
# yoshni_hisobla()

# def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
#     print(f"Durdonaxon {joriy_yil-tugilgan_yil} yoshda")
# yosh_hisobla(2000)


# # AMALIYOT
# def yilni_hisobla(ism, yosh):
#     print(f"{ism.title()} {2025-yosh}-yilda tugilgan ")
# ism = input("Ismingiz nima? ")
# yosh = int(input("Yoshingiz nechida?" ))
# yilni_hisobla(ism,yosh)


# def daraja_hisobla(son):
#     print(f"{son}ning darajasi {son**2}ga teng")
# son = int(input("Istalgan sonni kiriting: "))
# daraja_hisobla(son)

# def kub_hisobla(son):
#     print(f"{son}ning kubi {son**3}ga teng! ")
# son = int(input("Istalgan sonni kiriting"))
# kub_hisobla(son)

# def son_ustida_amallar(son):
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{son} ning kvadrati: {kvadrat}")
#     print(f"{son} ning kubi: {kub}")
# kiritilgan_son = int((input("Iltimos, biror son kiriting: ")))
# son_ustida_amallar(kiritilgan_son)


# def juft_toq_ajrat(son):
#     if son%2==0:
#         print(f"{son} juft")
#     else:
#         print(f"{son} toq")
# son = int(input("Istalgan sonni kiriting: "))
# juft_toq_ajrat(son)

    

# def katta_kichik_hisobla(son1, son2):
#     """Taqqoslashni amalga oshiruvchi daturni yozamiz"""
#     if son1>son2:
#         print(f"Birinchi son: {son1}, ikkinchi sondan katta")
#     elif son1<son2:
#         print(f"Ikkinchi son {son2}, birinchi sondan katta")
#     elif son1==son2:
#         print("Sonlar bir biriga teng! ")

# son1 = float(input("istalgan birinchi sonni kiriting: "))
# son2 = float(input("istalgan ikkinchi sonni kiriting: "))
# katta_kichik_hisobla(son1,son2)

# def darajaga_kotar(x,y):
#     print(f"{x}ning {y}chi darajasi, {x**y}ga teng")
# x = int(input("birinchi sonni kiriting: "))
# y = int(input("ikkinchi sonni kiriting: "))
# darajaga_kotar(x,y)

# def darajaga_kotar(x,y=2):
#     print(f"{x}ning {y}chi darajasi, {x**y}ga teng")
# x = int(input("birinchi sonni kiriting: "))
# darajaga_kotar(x,y=2)
    

# def bolinishni_tekshir(son):
#     for i in range(2, 11):  # 2 dan 10 gacha (11 kirmaydi)
#         if son % i == 0:
#             print(f"{son} {i} ga qoldiqsiz bo‘linadi.")
#         else:
#             print(f"{son} {i} ga bo‘linmaydi.")

# son = int(input("Iltimos, biror butun son kiriting: "))
# bolinishni_tekshir(son)

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
# talaba1 = toliq_ism_yasa('muzaffar', 'karimov')
# talaba2 = toliq_ism_yasa('karim', 'muzaffarov')
# print(f"Darsga kelmagan talabalar: {talaba1}, {talaba2}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi: 
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# def oraliq(min,max):
#     sonlar = [] 
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,10))
# print(oraliq(10,21))


##Amaliyot

# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz
# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []

# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#     )



# def kattasini_aniqla(son1, son2, son3):
#     """Uchta sonning eng kattasini aniqlovchi funksiya"""
#     if son1>son2 and son1>son3:
#         print(f"Eng katta son: {son1}")
#         return son1
#     elif son2>son1 and son2>son3:
#         print(f"Eng katta son: {son2}")
#         return son2
#     else:
#         print(f"Eng katta son: {son3}")
#         return son3
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# son3 = int(input("Uchinchi sonni kiriting: "))
# kattasini_aniqla = kattasini_aniqla(son1, son2, son3)

