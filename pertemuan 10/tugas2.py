matriks = []

for i in range(2):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukkan nilai ke-[{i}][{j}]: "))
        baris.append(nilai)
    matriks.append(baris)
    print("------------------------")

for baris in matriks:
    print(' '.join(map(str, baris)))

