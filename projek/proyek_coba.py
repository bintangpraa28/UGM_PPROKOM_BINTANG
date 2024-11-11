def main():
    catatan_keuangan = []

    while True:
        print("\n=== Program Keuangan ===")
        print("1. Input Pemasukan dan Pengeluaran")
        print("2. Tampilkan Riwayat Pemasukan dan Pengeluaran")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            input_pemasukan_pengeluaran(catatan_keuangan)
        elif pilihan == '2':
            tampilkan_riwayat(catatan_keuangan)
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def input_pemasukan_pengeluaran(catatan):
    pemasukan_total = 0
    pengeluaran_total = 0

    for bulan in range(1, 4):  # 3 bulan terakhir
        print(f"\nBulan {bulan}:")
        pemasukan = float(input("Masukkan total pemasukan: "))
        pengeluaran = float(input("Masukkan total pengeluaran: "))
        
        pemasukan_total += pemasukan
        pengeluaran_total += pengeluaran
        
        catatan.append({
            'bulan': bulan,
            'pemasukan': pemasukan,
            'pengeluaran': pengeluaran
        })

    analisis(pemasukan_total, pengeluaran_total)

def analisis(pemasukan_total, pengeluaran_total):
    print("\n=== Analisis Pemasukan dan Pengeluaran ===")
    if pengeluaran_total > pemasukan_total:
        print("Pengeluaran Anda melebihi pemasukan!")
        saran = (pemasukan_total / 3) * 0.8  # Saran pengeluaran ideal 80% dari rata-rata pemasukan
        print(f"Saran pengeluaran ideal per bulan adalah: {saran:.2f}")
    else:
        print("Pengeluaran Anda sudah ideal.")

def tampilkan_riwayat(catatan):
    print("\n=== Riwayat Pemasukan dan Pengeluaran ===") 
    if not catatan:
        print("Belum ada data pemasukan dan pengeluaran.")
        return
    
    for entry in catatan:
        print(f"Bulan {entry['bulan']}: Pemasukan = {entry['pemasukan']}, Pengeluaran = {entry['pengeluaran']}")

if __name__ == "__main__":
    main()
