# while - ham for kabi takrorlash operatori bo'lib, fordan farqli ravishda toki malum bir shart True bo'lsa kodni takrorlayveradi
# ingliz tilidan "toki", "gacha" deb tarjima qilinadi
# +=  opertatori ham bor, bu o'ng tarafdagi qiymatni chap tarafga qo'shadi, misol son= son+1 yoki son+=1


ism = input("Ismingiz nima?   ")
print(ism.upper())

ism = input("Ismingiz nima? ")
savol = f"Salom {ism.title()}. Yoshingiz nechida?  "
yosh = input(savol)
print(f"{savol}{yosh}")

ism = input("Ismingizni kiriting ")
savol = f"Salom {ism.title()}. Yoshingiz nechida?  "
yosh  = input(savol)
yosh = int(yosh)
vazn= input("Vazningiz necha kg? ")
vazn = float(vazn)

son = 1
while son <=10:
    print(son, end='')
    son = son+1 #yoki son+=1

print("Kiritilgan sonning darajasini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting  "
savol+="(dasturni to`xtatish uchun 'exit' deb yozing) "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)


print("Kiritilgan sonning darajasini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting  "
savol+="(dasturni to`xtatish uchun 'exit' deb yozing) "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)

print("Kiritilgan sonning darajasini qaytaruvchi dastur")
savol = "Istalgan sonni kiriting  "
savol+="(dasturni to`xtatish uchun 'exit' deb yozing) "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat)**2)

sonlar = range(1,11)
for son in sonlar:
    if son ==7:
        break
    print(f"{son}ning kvadrati {son**2}ga teng! ")


sonlar = range(1,11)
for son in sonlar:
    if son ==6:
        continue
    print(f"{son}ning kvadrati {son**2}ga teng! ")

son = 0
while son<10:
    son+=1
    if son %2!=0:
        continue
    else:
        print(son)



Amaliyot
savol = "Yoqtirgan kitobingiz qaysi? "
savol+="(jarayonni to`xtatish uchun 'stop' deb kiriting)"

while True:
    kitob = input(savol)
    if kitob == 'stop':
        break
print("Rahmat")
        

savol = "Yoshingiz nechida??  "
while True:
    yosh = input(savol)
    if yosh =='exit' or yosh == 'quit':
        break
    yosh = int(yosh)

    if yosh<7:
        narx=2000
    elif 7<=yosh<=18:
        narx=3000
    elif 18<yosh<=65:
        narx=10000
    else:
        narx = 0
    print(f"Sizga chipta narxi {narx} so'm")



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
       break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = int(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")











ismlar = []
print("Yaqin do'stlaringiz ro'yhatini tuzamiz: ")
n=1
while True:
    savol = f"{n}- do'stingizning ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob=='ha':
        n+=1
        continue
    else: 
        break
print(ismlar)

print("Do'stlaringiz yoshini saqlaymiz! ")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism]=int(yosh)
    javob = input("Yana malumot qo'shasizmi? (ha/yo'q)")
    if javob =="yo'q":
        ishora= False

print(dostlar)
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


cars = ['malibu', 'bugatti', 'BMW', 'malibu', 'nexia', 'damas', 'malibu', 'traker', 'cobalt', 'malibu']
while 'malibu' in cars:
    cars.remove('malibu')
print(cars)

talabalar = ['olim', 'anvar', 'ali', 'maruf']
baholahngan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosi nechi?  ")
    print(f"{talaba.title()} baholandi. ")
    baholahngan_talabalar[talaba]=baho
print(baholahngan_talabalar)

Amaliyot. 
buyurtmalar = []
while True:
    buyurtma = input("Nima buyurtma qilasiz? ")
    buyurtmalar.append(buyurtma)
    javob = input("davom etasizmi? ha/yoq ")
    if javob=="yoq":
        break
print(buyurtmalar)

print("Bor maxsulotlar va ularning narxini shakllantiramiz")
maxsulotlar = {}
ishora = True
while ishora:
    maxsulot = input("Nima maxsulot bor? ")
    narx = input(f"{maxsulot}ning narxini kiriting; ")
    narx = int(narx)
    maxsulotlar[maxsulot]= narx
    javob=input("Yana maxsulot qo`shasizmi? ha/yoq")
    if javob == "yoq":
        break
print(maxsulotlar)


buyurtmalar = ['olma','uzum','gilos','ananas', 'kivi']
mahsulotlar = {'olma':15000,
               'uzum':30000,
               'gilos':45000,
               'qovin': 50000,
               'kivi': 25000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")