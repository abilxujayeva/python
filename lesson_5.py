# list-ro'yhat. bir nechta elementlardan iborat bo'ladi. elementlar 0 dan boshlab sanalishi kerak. []ichida yozilsa o'zgartirish 
#            mumkin, () ichida yozilsa esa unga o'zgartirish imkonsiz
# list.append("")- list ichida element qo'shish imkonini beradi, yangi element ro'yhat oxiriga qo'shiladi
# list.insert(0, "")- bu yerda ham element qo'shish mumkin, bunda elementni istalgan joyga uning tartib raqamini kirtigan holsa qo'shish mukin
# del list[element tartib qarami 1,2,...]- ayni keraksiz elementni o'shirish imkoniyati
#list.remove("  ")- ayni bir elementga murojaat qilish orqali uni o'chirish imkoniyati mavjud
# list.pop(0,1,2...) - bu buyruq orqali istalgan elementni ro'yhat ichidan sug'urib olishimiz mumkiin. Bundan keyin ushbu element ro'yhatdan yoqoladi
# list.sort()asosiy ro'hatni o'zgartirgan holatda ro'yhatni alifbo tartibida tartiblaydi
#list.sorted()asosiy ro'hatga tegmagan holsa ro'yhatni alifbo tartibida tartiblaydi
#(sorted(list, reverse=True)) teskari tartiblab beradi
#min(), max(), sum()- list elementlarini eng kichik va eng katta, hamda yig'indisini hisoblab beradi
# list1 = list bu ayni ro'yhatga qayta nom berish bo'lib qoladi
# list1 = list[:] bu esa nusxa olish hisoblanadi
#Tuples- o'zgarmas ro'yhat hisoblanadi, undagi elementlar oddiy qavs ichila yoziladi,/
#                 yangi element qo'shish mumkin emas, lekin typeni listga almashtirish orqali element qo'shish imkoni bor






mevalar = ['olma', 'anor', 'behi', 'uzum']
narxlar = [18000, 25000, 45000, 19500]
print(mevalar)
print(narxlar)

mevalar = ['olma', 'anor', 'behi', 'uzum']
print("Birinchi meva", mevalar[0])
print("Ro'yhatdagi oxirgi meva", mevalar[3])
print("Men senga", mevalar[-1], " olib keldim")            

mevalar = ['olma', 'anor', 'behi', 'uzum']
print("Mening eng sevimli mevam", mevalar[1].upper())
print("Oltiariqda eng ko`p yetishtiriladigan meva", mevalar[3].capitalize())

# list elementlari ustida arifmetik amal ham bajarish mumkin
narxlar = [45000, 19000, 65000, 147856, 35492, 98723]
print(narxlar[0] + narxlar[5])
print(narxlar[3] / narxlar[2])


# Berilgan elementlarni ham o'zgartirish imkoni mavjud
narxlar = [25000, 45000, 18000, 96000, 84000]
narxlar[0] = 12000
narxlar[3] = 17700
narxlar[4] = 19900
print(narxlar)


# yangi element qo'shish .append metodi orqali, bu metod orqali ro'yhatdi oxiridan yangi element qo'shib keta oladi

mevalar = ['olma', 'anor', 'behi', 'uzum']
mevalar.append("tarvuz")
print(mevalar)

# .insert metodi esa maxsus belgilangan raqamli o'ringa yangi element qo'shishda yordam beradi

mashinalar = ['malibu', 'tico', 'damas', 'matiz', 'lombargini']
mashinalar.insert(2, 'Nexia3')
print(mashinalar)

# Elementni del operatori yordamida o'chirish
mashinalar = ['malibu', 'tico', 'damas', 'matiz', 'lombargini', 'kamaz', 'avtobus']
del mashinalar[2]
del mashinalar[-1]
print(mashinalar)

# Elementlarni .remove(qiymat) metodi yordamida o'chirish
mashinalar = ['malibu', 'tico', 'damas', 'matiz', 'lombargini', 'kamaz', 'avtobus']
mashinalar.remove('malibu')
mashinalar.remove('kamaz')
print(mashinalar)

# Elementlar ichidan istalgan bittasini sug'urib olish .pop(indeks) orqali amalga oshiriladi
mashinalar = ['malibu', 'tico', 'damas', 'matiz', 'lombargini', 'kamaz', 'avtobus']
print("Men tez orada", mashinalar.pop(0), "sotib olaman In Shaa Alloh")


# Amaliyot
ismlar = ['Zuhra', 'Muhammadaziz']
print("Salom", ismlar[0], "Yaxshimisan", ismlar[1], "Bugun mani kutib olishga kelasizmi")

sonlar = [12, 41, -56, 12.5, -47, -125.4, -987]
sonlar[0] = 13
del sonlar[-1]
sonlar.remove(41)
sonlar.insert(2, 456)
print(sonlar)


t_shaxslar = ['Islom Karimov', 'Ibn Sino', 'Imom al-Buxoriy']
z_shaxslar = ['Bill Geyts', 'Jef Bezos', 'Ilon mask']
print("Agar menga imkoniyat berilsa tarixiy shaxslardan", t_shaxslar.pop(0), "bilan, zamonaviy shaxslardan esa ", z_shaxslar.pop(2), \
      "bilan suhbatlashgan bo'lar edim" )


friends = []
friends.append("Muhammadaziz")
friends.append("Zuhraxon")
friends.append("Zarinaxon")
print("Kecha uyimizga kelgan mehmonlar: ", friends)


# Ro'yhatni tartiblash alifbo tartibida(Agar matnda katta harf bilan boshlangan so'z bo'lsa /
# dastlab uni yozadi, shuning uchun hamma harflar bir xil yozilganiga diqqatli bo'lish kerak)
mashinalar = [ 'nexia 3', 'lacetti', 'gentra', 'tico', 'captiva', 'jiguli', 'damas' ]
mashinalar.sort()    #asosiy ro'hatni o'zgartirgan holatda tartiblaydi
print(mashinalar)
students = ['anvar', 'sarvar', 'hamid', 'vali', 'kamol', 'javlon', 'aziz', 'qudra', 'shuhrat']
print(sorted(students))  #asosiy ro'yhatga tegmagan holda ro'yhatni tartiblab beradi
print(sorted(students, reverse=True))
print(students)

numbers = [12, 58, 45, -65, -7, 1234, 65, -78, -1, 0, 43]
numbers.sort()
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))

fruits = ['olma', 'anor', 'banan', 'nok', 'apelsin', 'olcha']
fruits.reverse()
print(fruits)
print("Fruits ro'yhatida elementlar soni ", len(fruits), "taga teng")

sonlar = list(range(12,99))
print(sonlar)
toq_sonlar = list(range(1,101,2))
juft_sonlar = list(range(2,101,2))
print("Bir dan yuzgacha bo`lgan sonlar ichida toq sonlar: ", toq_sonlar, "juft sonlar esa; ", juft_sonlar, "ni tashkil qiladi")


narxlar = [25000, 45000, 65000, 85000, 89000, 101000, 145762, 1457]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon mevaning kgmi", arzon, "so'm", "eng qimmatini esa ", qimmat, "so'mga sotib oldim. Jami", jami, "so'm sarf qildim")


cars = [ 'nexia 3', 'lacetti', 'gentra', 'tico', 'captiva', 'jiguli', 'damas' ]
my_cars = cars[0:4]    #yangi ro'yhat uchun eski ro'yhatdan kesib olish ham mumkin
print(cars)
print(my_cars)


sonlar = [1, 3, 45, 25, 78, 6, 95, 31, 61, 19, 17, 37]
sonlar2 = sonlar #bu ayni ro'yhatga qayta nom berish bo'lib qoladi
sonlar3 = sonlar[:] #bu esa nusxa olish hisoblanadi
print(sonlar2)
print(sonlar3)


#Tuples- o'zgarmas ro'yhat hisoblanadi, undagi elementlar oddiy qavs ichila yoziladi,/
#yangi element qo'shish mumkin emas, lekin typeni listga almashtirish orqali element qo'shish imkoni bor

toys = ('bus', 'cars', 'doll', 'bear', 'snake', 'dino')
# toys[3] = 'dragon'   #bu kod ishlamaydi, demak quyidagi usuldan foydalanishimiz mumkin
toys = list(toys)
toys.append('dragon')
toys.remove('bus')
print(toys)
toys = tuple(toys)
print(toys)


#Amaliyot
davlatlar = ['amerika', 'rossiya', 'shvetsariya', 'hindiston', 'turkiya', 'ozarbayjon']
print("Ushbu to'yhatda davlatlar soni: ", len(davlatlar), "ta")
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)


davlatlar = ['amerika', 'rossiya', 'shvetsariya', 'hindiston', 'turkiya', 'ozarbayjon']
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

j_sonlar = list(range(120, 1200, 2))
print(j_sonlar)
jami = sum(j_sonlar)   #yoki print(sum(j_sonlar)) degan kod orqali ham hisoblash mukin
print(jami)

print(min(j_sonlar))
print(max(j_sonlar))
print((max(j_sonlar))-(min(j_sonlar)))

print(len(j_sonlar))
print(j_sonlar[:20])
print(j_sonlar[-20:])
print(j_sonlar[240:260])

taomlar = ['osh', 'shorva', 'noxat', 'quymoq', 'makaron']
nonushta = taomlar[:]
nonushta.append('qaynatilgan tuxum')
nonushta.append('kolbasa')
nonushta.remove('osh')
nonushta.remove('shorva')
print(taomlar)
print(nonushta)

nonushta = tuple(nonushta)
print(nonushta)
nonushta[0] = "quymoq va non"
print(nonushta)


