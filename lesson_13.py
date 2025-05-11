#Funksiya - Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi
# Funksiya - dasturda bir necha marta ishlatilishi mumkin bo'lgan kodlar to'plami


def salom_ber():
    """Salom beruvchi funksiya yozamiz"""
    print("Assalomu alaykum")
salom_ber()

def salom_ber(ism):
    """Foydalanuvchiga ismi bilan salom beruvchi funksiya yaratamiz"""
    print(f"Assalomu alaykum {ism.title()}!")
salom_ber("akmal")
salom_ber("murod")

print(salom_ber.__doc__)


def toliq_ism(ism,familiya):
    """Foydalanuvchi ismi va familyasini ko`rsatuvchi funksiya yozamiz! """
    print(f"Foydalanuchi ismi: {ism.title()}, foydalanuvchi familyasi: {familiya.title()}")
toliq_ism('anvar', 'murodov')

def toliq_ism(ism='karim', familiya='mansurov'):
    """Foydalanuvchi ismi va familyasini ko`rsatuvchi funksiya yozamiz! """
    print(f"Foydalanuchi ismi: {ism.title()}, foydalanuvchi familyasi: {familiya.title()}")
toliq_ism()


def ism_familiya(ism='botir', familiya='karimov'):
    """Ism va familya bi;an murojaat qiluvchi dasturni yozamiz"""
    print(f"{ism.title()} {familiya.title()} hush kelibsiz!")
ism_familiya()

def yilni_hisobla(ism, yosh):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2025-yosh}-yilda tugilgan")
yilni_hisobla('Fatima', 25)

def yoshni_hisobla(yil=2000, ism='fatimaxon'):
    """Foydalanuvchi yoshini hisoblaymiz"""
    print(f"{ism.title()}ning yoshi {2025-yil}da! ")
yoshni_hisobla()

def yosh_hisobla(tugilgan_yil, joriy_yil=2025):
    print(f"Durdonaxon {joriy_yil-tugilgan_yil} yoshda")
yosh_hisobla(2000)


# AMALIYOT
def yilni_hisobla(ism, yosh):
    print(f"{ism.title()} {2025-yosh}-yilda tugilgan ")
ism = input("Ismingiz nima? ")
yosh = int(input("Yoshingiz nechida?" ))
yilni_hisobla(ism,yosh)


def daraja_hisobla(son):
    print(f"{son}ning darajasi {son**2}ga teng")
son = int(input("Istalgan sonni kiriting: "))
daraja_hisobla(son)

def kub_hisobla(son):
    print(f"{son}ning kubi {son**3}ga teng! ")
son = int(input("Istalgan sonni kiriting"))
kub_hisobla(son)

def son_ustida_amallar(son):
    kvadrat = son ** 2
    kub = son ** 3
    print(f"{son} ning kvadrati: {kvadrat}")
    print(f"{son} ning kubi: {kub}")
kiritilgan_son = int((input("Iltimos, biror son kiriting: ")))
son_ustida_amallar(kiritilgan_son)


def juft_toq_ajrat(son):
    if son%2==0:
        print(f"{son} juft")
    else:
        print(f"{son} toq")
son = int(input("Istalgan sonni kiriting: "))
juft_toq_ajrat(son)

    

def katta_kichik_hisobla(son1, son2):
    """Taqqoslashni amalga oshiruvchi daturni yozamiz"""
    if son1>son2:
        print(f"Birinchi son: {son1}, ikkinchi sondan katta")
    elif son1<son2:
        print(f"Ikkinchi son {son2}, birinchi sondan katta")
    elif son1==son2:
        print("Sonlar bir biriga teng! ")

son1 = float(input("istalgan birinchi sonni kiriting: "))
son2 = float(input("istalgan ikkinchi sonni kiriting: "))
katta_kichik_hisobla(son1,son2)

def darajaga_kotar(x,y):
    print(f"{x}ning {y}chi darajasi, {x**y}ga teng")
x = int(input("birinchi sonni kiriting: "))
y = int(input("ikkinchi sonni kiriting: "))
darajaga_kotar(x,y)

def darajaga_kotar(x,y=2):
    print(f"{x}ning {y}chi darajasi, {x**y}ga teng")
x = int(input("birinchi sonni kiriting: "))
darajaga_kotar(x,y=2)
    

def bolinishni_tekshir(son):
    for i in range(2, 11):  # 2 dan 10 gacha (11 kirmaydi)
        if son % i == 0:
            print(f"{son} {i} ga qoldiqsiz bo‘linadi.")
        else:
            print(f"{son} {i} ga bo‘linmaydi.")

son = int(input("Iltimos, biror butun son kiriting: "))
bolinishni_tekshir(son)

