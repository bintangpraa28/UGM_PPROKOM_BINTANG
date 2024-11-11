import math  # Untuk menggunakan nilai pi yang lebih akurat

def menu():
    print("Pilih Bentuk 2D:")
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    return pilihan

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)
    return luas

def hitung_luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = math.pi * jari_jari**2
    print("Luas lingkaran adalah:", luas)
    return luas

def hitung_luas_segitiga():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Luas segitiga adalah:", luas)
    return luas

while True:
    pilihan = menu()
    if pilihan == '1':
        hitung_luas_persegi_panjang()
    elif pilihan == '2':
        hitung_luas_lingkaran()
    elif pilihan == '3':
        hitung_luas_segitiga()
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")