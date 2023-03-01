# Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 4 dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Import Library
from human import Dosen
from human import Mahasiswa
from univ import Course
from univ import Prodi

dataMahasiswa = []  # tampungan untuk data mahasiswa
dataDosen = []  # tampungan untuk data dosen

# Membuat data mahasiswa baru dan menambahkan ke dalam list
# Mahsiswa 1
mhs1 = Mahasiswa("12345", "Ayesha", "Laki-laki", "UPI",
                 "ayesha@upi.edu", "210", "FPMIPA", "Ilkom")
dataMahasiswa.append(mhs1)
# Mahasiswa 2
mhs2 = Mahasiswa("12346", "Ali", "Laki-laki", "UPI",
                 "ali@upi.edu", "211", "FPMIPA", "Ilkom")
dataMahasiswa.append(mhs2)
# Mahasiswa 3
mhs3 = Mahasiswa("12347", "Firdaus", "Laki-laki", "UPI",
                 "firdaus@upi.edu", "212", "FPMIPA", "Ilkom")
dataMahasiswa.append(mhs3)

# Membuat data dosen baru dan menambahkan ke dalam list
# Dosen 1
dosen1 = Dosen("0987", "Bu Rosa", "Perempuan", "UPI",
               "rosa@upi.edu", "123", "FPMIPA", "Ilkom", "S2", "Programmer")
dataDosen.append(dosen1)
# Dosen 2
dosen2 = Dosen("0988", "Bu Rani", "Perempuan", "UPI",
               "rani@upi.edu", "124", "FPMIPA", "Ilkom", "S2", "Data Analyst")
dataDosen.append(dosen2)

# Menambahkan mata kuliah dan mahasiswa ke setiap mata kuliah
# Matkul 1
Matkul1 = Course("DPBO", "Bu Rosa")
Matkul1.tambahMahasiswa(mhs1)
Matkul1.tambahMahasiswa(mhs2)
# Matkul 2
Matkul2 = Course("Alpro", "Bu Rosa")
Matkul2.tambahMahasiswa(mhs2)
Matkul2.tambahMahasiswa(mhs3)
# Matkul 3
Matkul3 = Course("Sisbasdat", "Bu Rani")
Matkul3.tambahMahasiswa(mhs1)
Matkul3.tambahMahasiswa(mhs3)

# Membuat objek Program Studi dan manambahkan matkul, dosen, dan mahasiswa ke dalam program studi
# Membuat Prodi Ilmu Komputer
prodi = Prodi("Ilmu Komputer", "01")
prodi.addMatkul(Matkul1)
prodi.addMatkul(Matkul2)
prodi.addMatkul(Matkul3)
prodi.addDosen(dosen1)
prodi.addDosen(dosen2)
prodi.addMhs(mhs1)
prodi.addMhs(mhs2)
prodi.addMhs(mhs3)

prodi.cetakProdi() # Mencetak informasi Program Studi

# Mencetak daftar Mahasiswa
print("           Daftar Mahasiswa            ")
print("=======================================")
for i in range(len(dataMahasiswa)):
    print(str(i+1) + f".NIK              : {dataMahasiswa[i].getNIK()}")
    print(f"  Nama             : {dataMahasiswa[i].getNama()}")
    print(f"  Jenis Kelamin    : {dataMahasiswa[i].getJenisKelamin()}")
    print(f"  Asal Universitas : {dataMahasiswa[i].getAsalUniv()}")
    print(f"  Email Education  : {dataMahasiswa[i].getEmail()}")
    print(f"  NIM              : {dataMahasiswa[i].getNim()}")
    print(f"  Fakultas         : {dataMahasiswa[i].getFakultas()}")
    print(f"  Program Studi    : {dataMahasiswa[i].getProdi()}")
    print("--------------------------------------")

# Mencetak daftar Dosen
print("              Daftar Dosen            ")
print("======================================")
for i in range(len(dataDosen)):
    print(str(i+1) + f".NIK                : {dataDosen[i].getNIK()}")
    print(f"  Nama               : {dataDosen[i].getNama()}")
    print(f"  Jenis Kelamin      : {dataDosen[i].getJenisKelamin()}")
    print(f"  Asal Universitas   : {dataDosen[i].getAsalUniv()}")
    print(f"  Email Education    : {dataDosen[i].getEmail()}")
    print(f"  NIP                : {dataDosen[i].getNip()}")
    print(f"  Fakultas           : {dataDosen[i].getFakultas()}")
    print(f"  Program Studi      : {dataDosen[i].getProdi()}")
    print(f"  Pendidikan Terakhir: {dataDosen[i].getPendidikan()}")
    print(f"  Keahlian           : {dataDosen[i].getKeahlian()}")
    print("--------------------------------------")
