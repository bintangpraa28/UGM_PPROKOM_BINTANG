daftar = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

jumlah_genap = 0
jumlah_ganjil = 0

for baris in daftar:
    for i in baris:
        if i % 2 == 0:
            jumlah_genap += 1
        else:
            jumlah_ganjil += 1
            
print(f"Jumlah elemen genap: {jumlah_genap}" )
print(f"Jumlah elemen ganjil: {jumlah_ganjil}" )
