angka_array = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

genap = []
ganjil = []

for angka in angka_array:
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)

jumlah_genap = len(genap)
jumlah_ganjil = len(ganjil)

print(angka_array)
print("Ini adalah angka genap:", genap)
print(f"Jumlah angka genap: {jumlah_genap} angka")
print("Ini adalah angka ganjil:", ganjil)
print(f"Jumlah angka ganjil: {jumlah_ganjil} angka")
