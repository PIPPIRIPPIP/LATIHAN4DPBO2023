#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Human{
    private:
        string NIK;
        string Nama;
        string jenisKelamin;

    public:
        // Konstruktor
        Human(string nik, string nama, string gender);

        // Getetr
        string getNIK();
        string getNama();
        string getGender();

        ~Human();
};

class SivitasAkademik : public Human{
    private:
        string asalUniversitas;
        string emailEdu;

    public:
        // Konstruktor
        SivitasAkademik(string nik, string nama, string gender, string univ, string email);

        // Getter
        string getUniversitas();
        string getEmail();

        ~SivitasAkademik();
};

class Dosen : public SivitasAkademik{
    private:
        string NIP;
        string fakultas;
        string prodi;
        string pend_terakhir;
        string keahlian;

    public:
        // Konstruktor
        Dosen(string nik, string nama, string gender, string univ, string email,
              string nip, string fakultas, string prodi, string pend_terakhir, string keahlian);

        // Getter
        string getNIP();
        string getFakultas();
        string getProdi();
        string getPendidikan();
        string getKeahlian();

        ~Dosen();
};

class Mahasiswa : public SivitasAkademik{
    private:
        string NIM;
        string fakultas;
        string prodi;

    public:
        // Konstruktor
        Mahasiswa(string nik, string nama, string gender, string univ, string email,
                  string nim, string fakultas, string prodi);
        
        // Getter
        string getNIM();
        string getFakultas();
        string getProdi();

        ~Mahasiswa();
};

class Course{
    private:
        string namaMatkul;
        string namaDosen;
        vector<Mahasiswa> listMhs;

    public:
        // Konstruktor
        Course(string nama, string namaDosen);

        // Getter
        string getMatkul();
        string getDosen();

        void addMahasiswa(Mahasiswa mhs);

        ~Course();
};

class Prodi{
    private:
        string namaProdi;
        string kode;
        vector<Course> listMatkul;
        vector<Mahasiswa> listMhs;
        vector<Dosen> listDosen;

    public:
        // Konstruktor
        Prodi(string prodi, string kode);

        // Getter
        string getProdi();
        string getKode();

        void addMatkul(Course matkul);
        void addDosen(Dosen dosen);
        void addMhs(Mahasiswa mhs);
        void cetakProdi();

        ~Prodi();
};