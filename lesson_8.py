# if-elif-else - dastur davomida bir nechta shartlarni tekshirish talab qilinishi mumkin, shunda biz ushbu ketma ketlikdan foydalanamiz.
# ushbu ketma ketlikda, bitta shart bajarilishi bilan python qolgan shartlarni tekshirmaydi
# and va or operatorlarini biz 2 va undan ortiq shartlarni tekshirish zarur bo'lganida ishlatamiz
# OR "yoki" deb tarjima qilinadi 2 va undan ortiq shartlardan biri bajarilishini tekshirishda ishlatiladi
# AND "va" deb tarjima qilinadi 2 va undan ortiq shartlarni barchasi bajarilishini tekshiradi
# boolean - bu dasturlashda ikki qiymatdan biri bo'lgan mantiqiy tur. True/False 
# in elementi yordamida biz ro'yhatning tarkibida malum lelement bor yoki yo'qligini tekshiramiz
# not in elementi esa biror elementni ro'yhatda yo'qligini tekshiradi


yosh = int(input("Yoshingiz nechida? "))
if yosh <=4:
    print("Sizga kirish bepul")
elif yosh <=12:
    print("Sizga kirish 5 ming so'm")
else:
    print("Sizga kirish 10000 so'm")

yosh = int(input("Yoshingiz nechida? "))
if yosh <=4:
    price=0
elif yosh <=12:
    price=5000
else:
    price=10000
print(f"Sizga kirish {price} so'm")


yosh = int(input("Yoshingiz nechida? "))
if yosh <=4:
    price=0
elif yosh <=12:
    price=5000
elif yosh <=65:
    price=10000
else:
    price=8000
print(f"Sizga kirish {price} so'm")

kun = input("Bugun qanaqa kun?? ")
if kun.lower()== 'shanba' or kun.lower()=='yakshanba':
    print("Bugun dam olish kuni!! Uhla!  ")
else:
    print("Ishga borishing kerak")

kun = input("Bugun qanday kun? ")
harorat = float(input("Havo harorati qanday?? "))
if kun.lower() =='yakshanba' and harorat>=30:
    print("Kettik cho'milishga")
elif kun.lower() =='yakshanba' and harorat<30:
    print("Bugun uyda dam olamiz")
else:
    print("Bugun ishga boramiz")

x =19
y = 15
result = x>y
print(result)
result = x<y
print(result)

narx = 15000
choy = 1
salat = 0

if choy and salat:
        narx = narx + 10000
elif choy or salat:
        narx = narx + 5000
print(f"Jami {narx} so'm bo'ldi")


mevalar = ['olma', 'anor', 'nok', 'shaftoli', 'xurmo',]
if 'uzum' in mevalar: 
        print("Uzum ro'yhatda bor")
else:
        print("Uzum ro'yhatda yo'q")


menu = ['qozonkabob', 'osh', 'shorva', 'noxatshorak', 'baqlajon']
ovqat = input("Nima ovqat buyurasiz? ")
if ovqat.lower() in menu:
        print("Buyurtma qabul qilindi")
else:
        print("Afsuski bizda bunday ovqat yo'q")



mevalar = ['olma', 'anor', 'nok', 'shaftoli', 'xurmo',]
if 'uzum' not in mevalar: 
    print("Uzum royhatda yoq")
else:
    print("Uzum royhatda bor")

menu = ['qozonkabob', 'osh', 'shorva', 'noxatshorak', 'baqlajon']
ovqat = (input("Nima ovqat xohlaysiz?   "))
if ovqat.lower() not in menu:
    print("Bunday ovqat bizda yo'q")
else:
    print("Buyurtma qabul qilindi")


menu = ['qozonkabob', 'osh', 'shorva', 'noxatshorak', 'baqlajon']
buyurtmalar = ['qozonkabob', 'osh', 'shashlik', 'baqlajon']
for taom in buyurtmalar:
    if taom in menu: 
        print(f"Menyuda {taom} bor")
    else:
        print(f"keshirasiz {taom} menyuda yoq")


#Amaliyot

juft_son = float(input("Istalgan juft sonni kiriting: "))
if juft_son%2:
    print("Bu son juft son emas")
else:
    print("Rahmat")

yosh = float(input("Yoshingiz nechida? "))
if yosh<=4 or yosh>=60:
    price=0
elif yosh<=18:
    price=10000
else:
    price=20000
print(f"Sizga chipta narxi {price} so'm")


son1 = int(input("Birinchi sonni kiriting; "))
son2 = int(input("Ikkinchi sonni kiriting; "))
if son1>son2:
    print(f"{son1}>{son2} ga teng")
elif son1<son2:
    print(f"{son1}<{son2} ga teng")
else:
    print("Sonlar bir biriga teng")



maxsulotlar = ['olma', 'anor', 'behi', 'uzum', 'shaftoli', 'ananas', 'mandarin', 'sabzi', 'kartoshka', 'piyoz']
savat = []
for k in range(5):
    savat.append(input(f"Savatga {k+1} maxsulot qo'shing: "))
for n in savat:
    if n in maxsulotlar:
        print(f"Do'konimizda {n} bor ")
    else: 
        print(f"Do'konimizda {n} yo'q")


foydalanuvchilar = ['anvar', 'sobir', 'jobir', 'sanjar', 'behzod']
login = input("Yangi login tanlang ")
if login in foydalanuvchilar:
    print("Login band")
else:
    print(f"Hush kelibsiz {login}")

son = float(input("Birorta ixtiyoriy sonni kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    else:
        print(f"{son} soni {n} ga qoldiqli bo'linadi")

