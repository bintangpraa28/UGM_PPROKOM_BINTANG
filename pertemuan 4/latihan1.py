#program persyaratan SIM

umur = int(input("Masukkan Umur Anda = "))
nilai = int(input("Masukkan Nilai Tes Anda = "))
lulus = "Selamat Anda Berhak Mendapatkan SIM Anda"
gagal = "Maaf, Anda tidak berhak mendapatkan sim anda\nSilahkan Coba lagi Bulan atau tahun Depan"
if(umur>17) :
    if(nilai<60) :
        print()
        print(gagal)
    else :
        print()
        print(lulus)
else :
    print()
    print(gagal)