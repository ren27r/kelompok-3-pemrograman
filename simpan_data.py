def tampilkan_data(daftar):
    if not daftar:
        print("Belum ada data siswa.")
        return

    print("===Data Siswa===")

    for siswa in daftar:
        print(f"Nama: {siswa['nama']}  Tugas: {siswa['tugas']}  Ujian: {siswa['ujian']}  Rata-rata: {siswa['rata']}  Grade: {siswa['grade']}")


def simpan_data(daftar):
    if not daftar:
        print("Tidak ada data yang disimpan")
        return
