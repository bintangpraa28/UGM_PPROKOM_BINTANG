def cari(angka_list):
    genap = []
    ganjil = []
    jumlah_genap = 0
    jumlah_ganjil = 0

    for angka in angka_list:
        if angka % 2 == 0:
            genap.append(angka)
            jumlah_genap += angka
        else:
            ganjil.append(angka)
            jumlah_ganjil += angka

    return genap, ganjil, jumlah_genap, jumlah_ganjil

angka_list = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

hasil = cari(angka_list)

genap, ganjil, jumlah_genap, jumlah_ganjil = hasil

print(angka_list)
print("Ini adalah angka genap:", genap)
print("jumlah angka genap:", jumlah_genap)
print("ini adalah angka ganjil:", ganjil)
print("jumlah angka ganjil:", jumlah_ganjil)