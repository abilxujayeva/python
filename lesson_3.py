# Turli xil qiymatdagi ma'lumotlarni consoleda chop etish uchun f"{}  " dan foydalanamiz
# \n matnni yangi qatorda chop etadi
# \t so'zlar orasida bo'sh joy qoldirish (tab vazifasini bajaradi)
# variable.upper() matndagi barcha harfni katta qilib beradi
# variable.title() matndagi har bir so'z bosh harfini katta qilib beradi
# variable.lower() matndagi barcha so'zlarni kichik harflarda qilib beradi
# variable.capitalize() Matn boshidagi birinchi so'zni bosh harfda yozib beradi
# l.strip()  matnning chap tomondagi bo'sh joylarni o'chiradi
# r.strip() matnning o'ng tomondagi bo'sh joylarni o'chiradi
# strip() matnning chap va o'ng tomonidagi bo'sh joylarni o'chiradi
# input(" ") foydalanuvchidan qiymat kiritishini so'raydi va doim string qiymat qaytaradi.(ammo u qiymatni o'zgartirish imkoni bor)
#pow(son, daraja) - ushbu buyruq sonni darajaga ko'tarish uchun foydalaniladi
#abs(son)- buning vazifasi manfiy sonni ham musbat deb qabul qilishda foydalaniladi
#round(son, nechta raqam yaxlitlanishi kerakligiyoziladi) - o'nlik sonni yaxlitlash uchun foydalaniladi

matn="Men yangi 👜 sotib oldim"
print(matn)
ism="Fatimaxon"
print("Mening ismim "+ ism)

ism='Muhammadaziz '
familiya='Sodiqov'
print(ism+familiya)

ism="To'xtaniyoz"
familiya="Boltaboyev"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)

ism='Stiv'
familiya='Jobs'
print(f"Salom, mening ismim {ism}. {ism} {familiya}")
ism="Kevin"
sharif="Makkaliston"
print(f"Assalomu alaykum, mening ismim {ism}. {ism} {sharif}")


# Bo`shliq qoldirish uchun \t dan foydalanamiz
print("Salom \tAzizam")  
# Keyingi qatordan davom etish uchun esa\n dan foydalanamiz 
print("Salom\nAzizam")


ism="Fatimaxon"
familiya="Abilxujaeva"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif.upper())

ism="Fatimaxon"
familiya="Abilxujaeva"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif.lower())

ism="Fatimaxon"
familiya="Abilxujaeva"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif.title())


ism="Fatimaxon"
familiya="Abilxujaeva"
ism_sharif=f"{ism} {familiya}"
print(ism_sharif.capitalize())


meva="      anorni      "
print("Men " + meva.lstrip() + "yaxshi ko'raman")
print("Men"+ meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip()+ " yaxshi ko'raman")

yosh=input("Yoshingiz nechida?")
print("Assalomu alaykum, yoshim "+yosh+ "da" )

# Amaliyot
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
print(kocha + " ko'chasi," + mahalla + " mahallasi," + \
      tuman + " tumani," + viloyat + " viloyati")

kocha = input("Ko'changiz nomi?")
mahalla = input("Mahallangiz nomi?")
tuman = input("Tumaningiz nomi?")
viloyat = input("Viloyatingiz nomi?")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati. ")


kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"
manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati. "
print(manzil)

print(manzil.upper())
print(manzil.title())
print(manzil.lower())
print(manzil.capitalize())


result = pow(2, 5)
print(result)


number = abs(-152)
print(number)


number = round(125.3456987, 3)
number1 = round(8754.1257894)
print(number)
print(number1)