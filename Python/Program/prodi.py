# Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 2 dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Membuat kelas course
class Course:
    # Private
    __namaMatkul = ""
    __namaDosen = ""
    __listMhs = []

    def __init__(self, nama = "", namaDosen = ""):
        self.__namaMatkul = nama
        self.__namaDosen = namaDosen

    def getMatkul(self):
        return self.__namaMatkul
    
    def getNamaDosen(self):
        return self.__namaDosen
    
    def tambahMahasiswa(self, mhs):
        self.__listMhs.append(mhs)

    

class Prodi:
    # Private
    __namaProdi = ""
    __kode = ""
    __listMatkul = []
    __listMhs = []
    __listDosen = []

    def __init__(self, nama = "", kode = ""):
        self.__namaProdi = nama
        self.__kode = kode

    def getNamaProdi(self):
        return self.__namaProdi
    
    def getKode(self):
        return self.__kode
    
    def addMatkul(self, matkul):
        self.__listMatkul.append(matkul)

    def addDosen(self, dosen):
        self.__listDosen.append(dosen)

    def addMhs(self, mhs):
        self.__listMhs.append(mhs)

    def cetakProdi(self):
        print("              Data Prodi             ")
        print("=====================================")
        print(f"  Dosen pada prodi {self.__namaProdi} :")
        i = 1
        for mhs in self.__listDosen:
            print(f"{i}. {mhs.getNama()}")
            i = i + 1
        print(f"  Mahasiswa pada prodi {self.__namaProdi} :")
        i = 1
        for mhs in self.__listMhs:
            print(f"{i}. {mhs.getNama()}")
            i = i + 1
        print(f"  Matkul pada prodi {self.__namaProdi} :")
        i = 1
        for mhs in self.__listMatkul:
            print(f"{i}. {mhs.getMatkul()}")
            i = i + 1
        print("--------------------------------------")