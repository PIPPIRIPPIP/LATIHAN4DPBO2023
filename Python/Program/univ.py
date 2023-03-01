# Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 4 dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Membuat kelas course
# Kelas ini dipresentasikan untuk atribut Nama Matkul, Nama Dosen, dan Mahasiswa yang mengintrak matkul tersebut
# Kelas ini mengkomposisi kelas Mahasiswa untuk mengisi list mahasiswa
class Course:
    # Private
    __namaMatkul = ""
    __namaDosen = ""
    __listMhs = []

    # Public
    # Konstruktor
    def __init__(self, nama="", namaDosen=""):
        self.__namaMatkul = nama
        self.__namaDosen = namaDosen

    # Getter
    # Get Nama Matkul
    def getMatkul(self):
        return self.__namaMatkul

    # Get Nama Dosen
    def getNamaDosen(self):
        return self.__namaDosen

    # Fungsi manambahkan mahasiswa ke dalam list
    def tambahMahasiswa(self, mhs):
        self.__listMhs.append(mhs)


# Membuat Kelas Prodi
# Kelas ini dipresentasikan untuk atribut Nama Prodi, Kode Prodi, Daftar matkul, Daftar mahasiswa, dan Daftar dosen
# Kelas ini mengkomposisi kelas Course untuk mengisi list matkul, Mahasiswa untuk mengisi list mahasiswa, dan Dosen untuk mengisi list dosen
class Prodi:
    # Private
    __namaProdi = ""
    __kode = ""
    __listMatkul = []
    __listMhs = []
    __listDosen = []

    # Public
    # Konstruktor
    def __init__(self, nama="", kode=""):
        self.__namaProdi = nama
        self.__kode = kode

    # Getter
    # Get Nama Prodi
    def getNamaProdi(self):
        return self.__namaProdi

    # Get Kode Prodi
    def getKode(self):
        return self.__kode

    # Fungsi untuk menambahkan matkul ke dalam list matkul
    def addMatkul(self, matkul):
        self.__listMatkul.append(matkul)

    # Fugnsi untuk menambahkan dosen ke list dosen
    def addDosen(self, dosen):
        self.__listDosen.append(dosen)

    # Fungsi untuk menambahkan mahsiswa ke list mahasiswa
    def addMhs(self, mhs):
        self.__listMhs.append(mhs)

    # Mencetak Informasi mengenai prodi
    def cetakProdi(self):
        print("              Data Prodi             ")
        print("=====================================")
        # Mencetak daftar dosen
        print(f"  Dosen pada prodi {self.__namaProdi} :")
        i = 1
        for x in self.__listDosen:
            print(f"{i}. {x.getNama()}")
            i = i + 1
        # Mencetak daftar mahasiswa
        print(f"  Mahasiswa pada prodi {self.__namaProdi} :")
        i = 1
        for x in self.__listMhs:
            print(f"{i}. {x.getNama()}")
            i = i + 1
        # Mencetak daftar Mata kuliah
        print(f"  Matkul pada prodi {self.__namaProdi} :")
        i = 1
        for x in self.__listMatkul:
            print(f"{i}. {x.getMatkul()}")
            i = i + 1
        print("--------------------------------------")
