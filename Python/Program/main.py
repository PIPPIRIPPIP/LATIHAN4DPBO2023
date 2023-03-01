# Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 2 dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

from human import Dosen
from human import Mahasiswa
from prodi import Course
from prodi import Prodi

dataMahasiswa = []
dataDosen = []

mhs1 = Mahasiswa("12345", "Ayesha", "Laki-laki", "UPI", "ayesha@upi.edu", "210", "FPMIPA", "Ilkom")
dataMahasiswa.append(mhs1)

mhs2 = Mahasiswa("12346", "Ali", "Laki-laki", "UPI", "ali@upi.edu", "211", "FPMIPA", "Ilkom")
dataMahasiswa.append(mhs2)

dosen1 = Dosen("0987", "Bu Rosa", "Perempuan", "UPI", "rosa@upi.edu", "123", "FPMIPA", "Ilkom", "S2", "Programmer")
dataDosen.append(dosen1)

dosen2 = Dosen("0988", "Bu Rani", "Perempuan", "UPI", "rani@upi.edu", "124", "FPMIPA", "Ilkom", "S2", "Data Analyst")
dataDosen.append(dosen2)

Matkul1 = Course("DPBO", "Bu Rosa")
Matkul2 = Course("Alpro", "Bu Rosa")
Matkul3 = Course("Sisbasdat", "Bu Rani")
# Course.tambahMahasiswa(mhs1, mhs2)

prodi = Prodi("Ilmu Komputer", "01")
prodi.addMatkul(Matkul1)
prodi.addMatkul(Matkul2)
prodi.addMatkul(Matkul3)
prodi.addDosen(dosen1)
prodi.addDosen(dosen2)
prodi.addMhs(mhs1)
prodi.addMhs(mhs2)

prodi.cetakProdi()

print("           Daftar Mahasiswa            ")
print("=======================================")
for i in range(len(dataMahasiswa)):
    print(str(i+1) + f".NIK              : {dataMahasiswa[i].getNIK()}")
    print(          f"  Nama             : {dataMahasiswa[i].getNama()}")
    print(          f"  Jenis Kelamin    : {dataMahasiswa[i].getJenisKelamin()}")
    print(          f"  Asal Universitas : {dataMahasiswa[i].getAsalUniv()}")
    print(          f"  Email Education  : {dataMahasiswa[i].getEmail()}")
    print(          f"  NIM              : {dataMahasiswa[i].getNim()}")
    print(          f"  Fakultas         : {dataMahasiswa[i].getFakultas()}")
    print(          f"  Program Studi    : {dataMahasiswa[i].getProdi()}")
    print("--------------------------------------")

print("              Daftar Dosen            ")
print("======================================")
for i in range(len(dataDosen)):
    print(str(i+1) + f".NIK              : {dataDosen[i].getNIK()}")
    print(          f"  Nama             : {dataDosen[i].getNama()}")
    print(          f"  Jenis Kelamin    : {dataDosen[i].getJenisKelamin()}")
    print(          f"  Asal Universitas : {dataDosen[i].getAsalUniv()}")
    print(          f"  Email Education  : {dataDosen[i].getEmail()}")
    print(          f"  NIP              : {dataDosen[i].getNip()}")
    print(          f"  Fakultas         : {dataDosen[i].getFakultas()}")
    print(          f"  Program Studi    : {dataDosen[i].getProdi()}")
    print(          f"  Pendidikan Terakhir: {dataDosen[i].getPendidikan()}")
    print(          f"  Keahlian         : {dataDosen[i].getKeahlian()}")
    print("--------------------------------------")
