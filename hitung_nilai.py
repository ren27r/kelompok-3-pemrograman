NILAI_A = 85
NILAI_B = 70
NILAI_C = 50
def hitung_nilai(siswa):
    """
    Fungsi untuk menghitung rata-rata dan menentukan grade siswa.
    """
    rata = (siswa['tugas'] + siswa['ujian']) / 2

    if rata >= NILAI_A:
        grade = 'A'
    elif rata >= NILAI_B:
        grade = 'B'
    elif rata >= NILAI_C:
        grade = 'C'
    else:
        grade = 'D'

    siswa['rata'] = round(rata, 2)
    siswa['grade'] = grade
    return siswa