def input_data():
    """
    Fungsi untuk menerima input data siswa dari pengguna.
    Mengembalikan dictionary berisi nama, nilai tugas, dan nilai ujian.
    """
    print("\n=== Input Data Siswa ===")
    siswa = {}
    siswa['nama'] = input("Masukkan nama siswa: ")
    siswa['tugas'] = float(input("Masukkan nilai tugas: "))
    siswa['ujian'] = float(input("Masukkan nilai ujian: "))
    return siswa