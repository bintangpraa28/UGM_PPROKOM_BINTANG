jumlah_data = int(input("Masukkan jumlah data yang akan dihitung rata-ratanya: "))
nilai = 0
for i in range(jumlah_data):
        angka = float(input(f"Masukkan data ke-{i+1}: "))
        nilai += angka

# Hitung rata-rata
rata_rata = nilai / jumlah_data
print(f"Rata-rata dari data yang dimasukkan adalah: {rata_rata}")