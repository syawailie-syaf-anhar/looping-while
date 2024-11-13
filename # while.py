# masukkan jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Loop untuk setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa {i+1}")
    
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah yang diambil: "))
    
    total_nilai = 0
    
    # Loop untuk setiap mata kuliah yang diambil
    for j in range(jumlah_mata_kuliah ):
        nilai = float(input(f"Masukkan nilai untuk mata kuliah {j+1}: "))
        total_nilai += nilai
    
    # Menghitung rata-rata nilai
    rata_rata_nilai = total_nilai / jumlah_mata_kuliah
    print(f"Rata-rata nilai Mahasiswa {i+1}: {rata_rata_nilai:}")
