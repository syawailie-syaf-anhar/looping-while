# Meminta pengguna memasukkan bilangan awal dan bilangan akhir
awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

# Inisialisasi variabel angka dengan nilai awal
angka = awal

# Loop while untuk menampilkan bilangan ganjil antara awal dan akhir
while angka <= akhir:
    if angka % 2 != 0:
        print(angka)
    #angka += 1
    
