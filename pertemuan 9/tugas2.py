angka = []

for i in range(5):
    nilai_angka = float(input(f"Masukkan angka ke-{i+1} : "))
    angka.append(nilai_angka)
    print(angka)
    
total_data = sum(angka)

while True:
    perintah = input("ingin melihat jumlah/rata-rata ? (ketik 1 untuk keluar) ")
    perintah.lower()
    if perintah == "jumlah" :
        print(total_data) 
    elif perintah == "rata-rata":
        print(total_data/5)
    elif perintah == "1":
        break
    else :
        print('perintah tidak valid! tulis perintah "jumlah" atau "rata-rata"')

