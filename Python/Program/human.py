# Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 2 dalam mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Membuat kelas Human
# kelas ini direpresentasikan untuk atribut NIK, Nama, dan Jenis Kelamin
class Human:
    # Private
    __NIK = ""
    __nama = ""
    __jenisKelamin = ""

    # Public
    # KOnstruktor
    def __init__(self, nik = "", nama = "", jenisKelamin = ""):
        self.__NIK = nik
        self.__nama = nama
        self.__jenisKelamin = jenisKelamin

    # Getter #
    # Get Nik
    def getNIK(self):
        return self.__NIK
    # Get Nama
    def getNama(self):
        return self.__nama
    # Get Jenis Kelamin
    def getJenisKelamin(self):
        return self.__jenisKelamin
    
# /*  Membuat Kelas Civitas Akademik */
# Kelas ini merepresentasikan asal_univ dan email_education
# Kelas ini merupakan anak dari kelas Human, alasannnya karena civitas akademik adalah
# komunitas yang aktif di bidang akademik, yang pasti merupakan seorang manusia
class SivitasAkademik(Human):
    # Private
    __asalUniversitas = ""
    __emailEdu = ""

    # Public
    # Konstruktor
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniv = "", emailEdu = ""):
        super().__init__(nik, nama, jenisKelamin)

        self.__asalUniversitas = asalUniv
        self.__emailEdu = emailEdu
    
    # Getter #
    # Get Asal Universitas
    def getAsalUniv(self):
        return self.__asalUniversitas
    # Get Email Education
    def getEmail(self):
        return self.__emailEdu
    
# /* Membuat kelas Dosen */
# Kelas ini merepresentasikan NIP, Fakultas, Prodi, Pendidikan Terakhir, dan Keahlian
# Alasan kelas ini menjadi anak dari civitas akademik adalah
# karena civitas akademik berisi mahasiswa dan dosen.
class Dosen(SivitasAkademik):
    # Private
    __NIP = ""
    __fakultas = ""
    __prodi = ""
    __pend_terakhir = ""
    __keahlian = ""

    # Public
    # Konstruktor
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniv="", emailEdu="", nip = "", fakultas = "", prodi = "", pend = "", keahlian = ""):
        super().__init__(nik, nama, jenisKelamin, asalUniv, emailEdu)

        self.__NIP = nip
        self.__fakultas = fakultas
        self.__prodi = prodi
        self.__pend_terakhir = pend
        self.__keahlian = keahlian

    # Getter #
    # Get NIM
    def getNip(self):
        return self.__NIP
    # Get Fakultas
    def getFakultas(self):
        return self.__fakultas
    # Get Prodi
    def getProdi(self):
        return self.__prodi
    
    def getPendidikan(self):
        return self.__pend_terakhir
    
    def getKeahlian(self):
        return self.__keahlian

# /* Membuat kelas Mahasiswa */
# Kelas ini merepresentasikan NIM, Fakultas, dan Prodi
# Alasan kelas ini menjadi anak dari civitas akademik adalah
# karena civitas akademik berisi mahasiswa dan dosen.
class Mahasiswa(SivitasAkademik):
    # Private
    __NIM = ""
    __fakultas = ""
    __prodi = ""

    # Public
    # Konstruktor
    def __init__(self, nik="", nama="", jenisKelamin="", asalUniv="", emailEdu="", nim = "", fakultas = "", prodi = ""):
        super().__init__(nik, nama, jenisKelamin, asalUniv, emailEdu)

        self.__NIM = nim
        self.__fakultas = fakultas
        self.__prodi = prodi

    # Getter #
    # Get NIM
    def getNim(self):
        return self.__NIM
    # Get Fakultas
    def getFakultas(self):
        return self.__fakultas
    # Get Prodi
    def getProdi(self):
        return self.__prodi