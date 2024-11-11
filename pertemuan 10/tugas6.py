Array1 = [[4,6],
          [1,7]]
Array2 = [[2,3],
          [5,6]]

#penjumlahan
print("Hasil Penjumlahan:")
for x in range(0, len(Array1)):
    for y in range(0, len(Array1[0])):
        print (Array1[x][y] + Array2[x][y], end=' ')
    print()
#pengurangan
print("hasil pengurangan :")
for x in range(0, len(Array1)):
    for y in range(0, len(Array1[0])):
        print (Array1[x][y] - Array2[x][y], end=' ')
    print()

