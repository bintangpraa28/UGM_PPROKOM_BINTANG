def prima(num) :
    if num <= 1: 
        return False
    for i in range(2, num):
      if num % i == 0:
        return False

    return True

def cari_prima(array):
  prima_list = []
  for angka in array:
    if prima(angka):
      prima_list.append(angka)
  return prima_list, len(prima_list)

angka = [4, 5, 11, 12, 14, 16, 16, 19]

hasil, jumlah = cari_prima(angka)
print(f"yang termasuk bilangan prima adalah: {hasil}")
print(f"jumlah data bilangan prima adalah: {jumlah}")