# for bu sikl hisoblanadi, dasturlash davomida birorda kodni bir necha martta takrorlash talab qilinishi mumkin, 
#                                   o'sha paytda biz fordan foydalanamiz.
# range() - bu funksiya yordamida biz ma'lum oraliqdagi sonlar ketma ketligini hosil qilishimiz mumkin



mehmonlar = ('Guli', 'Lobar', 'Noila', 'Shohidaa', 'Mohira')
for mehmon in mehmonlar:
    print("SALOM", mehmon)


mehmonlar = ('Guli', 'Lobar', 'Noila', 'Shohidaa', 'Mohira')
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 8-mart Ayollar bayrami munosabati bilan kechamizga taklif qilaman")
    print("Hurmat bilan dugonangiz Fatimaxon")
    print("Manzil: Shaxriston metro")

mehmonlar = ('Guli', 'Lobar', 'Noila', 'Shohidaa', 'Mohira')
for mehmon in mehmonlar:
    print(mehmon) 
    print(mehmonlar)

mehmonlar = ('Guli', 'Lobar', 'Noila', 'Shohidaa', 'Mohira')
for mehmon in mehmonlar:
    print(mehmon) 
print(mehmonlar)

sonlar = list(range(10, 21))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2}ga teng")

sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)

print(sonlar)
print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do'stingiz kim? ")
for n in range(5):
    dostlar.append(input(f"{n+1}- do'stingizning ismini kiriting: "))
print(dostlar)


#Amaliyot
ismlar = ['Guli', 'Lola', 'Gunafsha', 'Binafsha', "Malika"]
for ism in ismlar:
    print("Qalesan??", ism)
print(f"Kod {len(ismlar)} martta takrorlandi")

t_sonlar = list(range(11, 100, 2))
for son in t_sonlar:
    print(son**3)

kinolar = []
print("3 ta eng yaxshi ko'rgan kinoyingiz qaysi??")
for k in range(3):
    kinolar.append(input(f"{k+1}- yoqtirgan kinoyingizni kiriting: "))
print(kinolar)




son = int(input("Istalgan butun sonni kiriting "))
start = 1
for i in range(start, son+1):
    start = start * i
print(start)
