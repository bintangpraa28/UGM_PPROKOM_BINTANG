awal = int(input("Masukkan saldo awal\t: "))
sisa = awal

while True:
    pengeluaran = int(input("Masukkan pengeluaran hari ini (-1 untuk keluar): "))
    if pengeluaran == -1:
        print("Sisa saldo =", sisa)
        break
    if pengeluaran > sisa:
        print("Saldo tidak cukup")
    else: sisa = sisa-pengeluaran

    