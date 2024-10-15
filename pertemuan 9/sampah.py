def bilangan_prima(angka):
  """Fungsi untuk memeriksa apakah suatu angka adalah bilangan prima"""
  if angka <= 1:
    return False
  if angka <= 3:
    return True
  if angka % 2 == 0 or angka % 3 == 0:
    return False
  i = 5
  while i * i <= angka:
    if angka % i == 0 or angka % (i + 2) == 0:
      return False
    i += 6
  return True

def cari_bilangan_prima(array):
  """Fungsi untuk mencari bilangan prima dalam sebuah array"""
  bilangan_prima_list = []
  for angka in array:
    if bilangan_prima(angka):
      bilangan_prima_list.append(angka)
  return bilangan_prima_list, len(bilangan_prima_list)

# Array yang akan diproses
angka = [4, 5, 11, 12, 14, 16, 16, 19]

# Panggil fungsi dan tampilkan hasil
hasil, jumlah = cari_bilangan_prima(angka)
print("Bilangan prima dalam array:", hasil)
print("Jumlah bilangan prima:", jumlah)