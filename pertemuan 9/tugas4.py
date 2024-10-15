def cari_kelipatan(data_array, kelipatan):
        kelipatan_list = []
        for elemen in data_array:
                if elemen % kelipatan == 0:
                        kelipatan_list.append(elemen)
        return kelipatan_list

jumlah_data = int(input("Masukkan jumlah elemen dalam array: "))
data_array = []

for i in range(jumlah_data):
        elemen = float(input(f"Masukkan elemen ke-{i+1}: "))
        data_array.append(elemen)

kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))
hasil = cari_kelipatan(data_array, kelipatan)

print("Elemen yang merupakan kelipatan dari", kelipatan, "adalah:", hasil)
