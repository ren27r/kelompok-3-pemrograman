from input_data import input_data
from hitung_nilai import hitung_nilai
from simpan_data import tampilkan_data, simpan_data

daftar_siswa = []

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Data Siswa")
    print("2. Lihat Data Siswa")
    print("3. Simpan & Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        siswa = input_data()
        siswa = hitung_nilai(siswa)
        daftar_siswa.append(siswa)
    elif pilihan == "2":
        tampilkan_data(daftar_siswa)
    elif pilihan == "3":
        simpan_data(daftar_siswa)
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan ulangi.")
