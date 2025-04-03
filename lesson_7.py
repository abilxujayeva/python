# if - operatori shart operatori bo'lib, berilgan shartni tekshirib malum kod blokini bajaradi. 
# else operatori esa ifga yordamchi bolib keladi, yani kodning if qismi bajarilmasa else qismiga o'tiladi

avtolar = ['damas', 'tico', 'mers', 'nexia', 'matiz', 'avtobus', 'poyezd']
for avto in avtolar:
    if avto == 'mers':
        print(avto.upper())
    else:
        print(avto.title())

ism = 'Vali'
result = ism == 'vali'
print(result)
ism = 'Mamatqul'
result = ism == 'Mamatqul'
print(result)

ism = input('Ismingiz nima? ')
if ism.lower() !='ali':
    print(f"Uzur {ism.title()}. Biz Alini kutyapmiz")
else: 
    print("Salom, Ali")


#12*6 = ?
javob = float(input("12*6 nechiga teng ?"))
if javob != 72:
    print("Javob xato")
else:
    print("To'g'ri javob berdingiz")

yosh = int(input("Yoshingiz nechida? "))
if yosh >= 18:
    print("Hush kelibsiz")
else:
    print("Kirish mumkin emas!!")


login = input("Yangi loginni kiriting: ")
if len(login) <=8:
    print("Login 8 ta harfdan kam bo'lmasligi kerak")
else:
    print("Login muvaffaqiyatli saqlandi")


# Amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

login = input("Loginni kiriting:  ")
if login == 'admin':
    print("Hush kelibsiz admin, foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
    print(f" Salom {login.title()}")


son1 = float(input("birinchi sonni kiriting: "))
son2 = float(input("ikkinchi sonni kiriting: "))
if son1 == son2:
    print(f"Ikkalasi bir biriga teng: {son1}={son2}")
else:
    print()


son = int(input("Istalgan birorta sonni kiriting: "))
if son > 0:
    print("Musbat son")
else:
    print("Manfiy son")


number = int(input("Istalgan birorta sonni kiriting: "))
if number > 0: 
    print(number**0.5)
else:
    print("Musbat son kiriting! ")