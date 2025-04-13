# Nesting - (o‘zbekcha: ichma-ich tuzilma) — bu bir ma’lumot tuzilmasi ichida boshqa bir tuzilmani joylashtirish degani.
# yani, list ichida lug‘at, lug‘at ichida list, yoki lug‘at ichida boshqa lug‘at bo‘lishi mumkin.

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    
print(cars[0])

malibus=[] 
for n in range(10):
    new_car = { 
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) 
for malibu in malibus[:3]:
    malibu['rang']='qizil'
    malibu['korobka']='avto'

for malibu in malibus[3:6]:
    malibu['rang']='qora'
    malibu['korobka']='avto'

for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['korobka']='mexanika'

for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000

print(malibus)



dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())


for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
    for til in tillar:
        print(f'{til.upper()} ', end='')



# Amaliyot
ilm_fan = {'ism':'alishar navoiy', 'yil':'1441-yil', 'asari':'xamsa', 'tugilgan joyi':'hirot'}
sanat  = {'ism':'sherali jorayev', 'yil':'1942-yil', 'asari':'gulbadan', 'tugilgan joyi':'andijon'}
internet = {'ism':'mark sukerberg', 'yil':'1984-yil', 'asari':'facebook', 'tugilgan joyi':'germaniya'}
mashxurlar = [ilm_fan, sanat, internet]
print(f"{ilm_fan["ism"].upper()} {ilm_fan["yil"]}da {ilm_fan['tugilgan joyi']}da tug'ilgan")
print(f"{sanat["ism"].upper()} {sanat["yil"]}da {sanat['tugilgan joyi']}da tug'ilgan")
print(f"{internet["ism"].upper()} {internet["yil"]}da {internet['tugilgan joyi']}da tug'ilgan")


ilm_fan = {'ism':'alishar navoiy', 'yil':'1441-yil', 'asari':['xamsa','hayrat ul abror'], 'tugilgan joyi':'hirot'}
sanat  = {'ism':'sherali jorayev', 'yil':'1942-yil', 'asari':['gulbadan','ozbegim'], 'tugilgan joyi':'andijon'}
internet = {'ism':'mark sukerberg', 'yil':'1984-yil', 'asari':['facebook','whatsapp'], 'tugilgan joyi':'germaniya'}
mashxurlar = [ilm_fan, sanat, internet]
for mashxur in mashxurlar:
    print(f"{mashxur['ism']}ning {mashxur['asari']}")