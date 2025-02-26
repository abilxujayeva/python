# type() ma'lumotning qanday turga mansubligini consolega chop etadi



a = 45
b = -85
c = a+b
print(c)

# Kvartratning tomini 30ga teng bo'lsa uning yuzi va perimetrini hisoblang
kvdrt_tmn = 30
kvdrt_yuzi = kvdrt_tmn**2
kvdrt_prmt = kvdrt_tmn*4
print(kvdrt_yuzi)
print(kvdrt_prmt)

pi = 3.14159
radius = 5
diametr = 2*radius
print("Aylananing uzunligi", pi*diametr, "ga teng")

aholi_soni = 7_123_123_432
print("Yer yuzida aholi soni", aholi_soni, "ga teng")


x, y, z, = -30, 15.5, 11.4
print(x+y-z)

ism = "Fatimaxon"
yosh = "25"
xabar = ism + " " + yosh + " " + "yoshda"
print(xabar)

ism = "Fatimaxon"
yosh = 25
xabar = ism + ' ' + str(yosh) + ' ' + 'yoshda'
print(xabar)


ism = "Fatimaxon"
yosh = 25
print(type(ism))
print(type(yosh))

t_yil = int(input("Tug'ilgan yilingizni kiriting:"))
yosh = 2025-t_yil
print("Siz " + str(yosh) + " yoshda ekansiz")


# Amaliyot
son = int(input("Istalgan sonni kiriting: "))
print(son, "ning kvadrati", son**2,  "ga teng")
print(son, "ning kubi", son**3, "ga teng")

yosh = int(input("Yoshingiz nechida? "))
print("Siz", 2025-yosh,"-yilda tug'ilgansiz")

x = int(input("Istalgan birinchi sonni kiriting: "))
y = int(input("Istalgan ikkinchi sonni kiriting: " ))
print(x+y)
print(x-y)
print(x/y)
print(x*y)

# son = int(input("Istalgan sonni kiriting"))
# son1 = str(son)
# print(type(son1))
