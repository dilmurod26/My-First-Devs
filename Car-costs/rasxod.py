print("ESLATMA! O'nlik son (7.4, 5.2, 6.1) ko'rinishda yoziladi, vergul (7,4) bilan emas.")
rasxod = float(input('100 km ga necha litr benzin ketishini kiriting: '))
km = int(input('Mashina necha km yurganini kiriting: '))
benzin = int(input('Benzin narxini kiriting: '))
total = rasxod * km / 100

print(km, 'km ga', str(total)[:5], 'litr benzin sarflabdi.')
print(str(total)[:5], 'litr benzinga', total * benzin, "so'm pul sarflabsiz.")






