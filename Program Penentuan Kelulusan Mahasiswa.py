
# Input nilai mahasiswa
tugas = float(input("Nilai tugas  : "))
uts = float(input("Nilai UTS    : "))
uas = float(input("Nilai UAS    : "))
kehadiran = float(input("Kehadiran    : "))

# Menghitung nilai akhir
nilai_akhir = (20 / 100 * tugas) + (30 / 100 * uts) + (50 / 100 * uas)

# Menentukan status mahasiswa
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 60 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

# Menampilkan hasil
print("\nNilai Akhir :", nilai_akhir)
print("Status      :", status)
