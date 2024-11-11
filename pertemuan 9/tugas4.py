jumlah_data = int(input("Masukkan jumlah elemen dalam array: "))
data_array = list(range(1, jumlah_data + 1))

print("Data Array:", data_array)

kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))
kelipatan_list = [elemen for elemen in data_array if elemen % kelipatan == 0]

print("Elemen yang merupakan kelipatan dari", kelipatan, ":", kelipatan_list)
