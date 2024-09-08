#input nama dan nilai 5 siswa
#jika nilai siswa sama atau diatas 70, maka output lulus tercetak
#jika nilai siswa dibawah 70, maka output tidak lulus tercetak
#hal tersebut terulang hingga 5 kali sesuai jumlah siswa

nama1 = str(input("Masukkan Nama Siswa 1 = "))
nilai1 = int(input("Masukkan Nilai Tes Siswa 1 = "))
nama2 = str(input("Masukkan Nama Siswa 2 = "))
nilai2 = int(input("Masukkan Nilai Tes Siswa 2 = "))
nama3 = str(input("Masukkan Nama Siswa 3 = "))
nilai3 = int(input("Masukkan Nilai Tes Siswa 3 = "))
nama4 = str(input("Masukkan Nama Siswa 4 = "))
nilai4 = int(input("Masukkan Nilai Tes Siswa 4 = "))
nama5 = str(input("Masukkan Nama Siswa 5 = "))
nilai5 = int(input("Masukkan Nilai Tes Siswa 5 = "))


if nilai1 >= 70:
    print("Siswa", nama1, "= lulus")
else :
    print("Siswa", nama1, "= tidak lulus")
if nilai2 >= 70:
    print("Siswa", nama2, "= lulus")
else :
    print("Siswa", nama2, "= tidak lulus")
if nilai3 >= 70:
    print("Siswa", nama3, "= lulus")
else :
    print("Siswa", nama3, "= tidak lulus")
if nilai4 >= 70:
    print("Siswa", nama4, "= lulus")
else :
    print("Siswa", nama4, "= tidak lulus")
if nilai5 >= 70:
    print("Siswa", nama5, "= lulus")
else :
    print("Siswa", nama5, "= tidak lulus")