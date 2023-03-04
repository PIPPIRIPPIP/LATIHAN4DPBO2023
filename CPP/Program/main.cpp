#include "header.hh"
using namespace std;

int main(){
    vector<Mahasiswa> dataMahasiswa;
    vector<Dosen> dataDosen;

    // Membuat data mahasiswa baru dan menambahkan ke dalam list
    // Mahsiswa 1
    Mahasiswa mahasiswa1("12345", "Ayesha", "Laki-laki", "UPI", "ayesha@upi.edu", "210", "FPMIPA", "Ilkom");
    dataMahasiswa.push_back(mahasiswa1);
    // Mahasiswa 2
    Mahasiswa mahasiswa2("12346", "Ali", "Laki-laki", "UPI", "ali@upi.edu", "211", "FPMIPA", "Ilkom");
    dataMahasiswa.push_back(mahasiswa2);
    // Mahasiswa 3
    Mahasiswa mahasiswa3("12347", "Firdaus", "Laki-laki", "UPI", "firdaus@upi.edu", "212", "FPMIPA", "Ilkom");
    dataMahasiswa.push_back(mahasiswa3);

    // Membuat data dosen baru dan menambahkan ke dalam list
    // Dosen 1
    Dosen dosen1("0987", "Bu Rosa", "Perempuan", "UPI", "rosa@upi.edu", "123", "FPMIPA", "Ilkom", "S2", "Programmer");
    dataDosen.push_back(dosen1);
    // Dosen 3
    Dosen dosen2("0988", "Bu Rani", "Perempuan", "UPI", "rani@upi.edu", "124", "FPMIPA", "Ilkom", "S2", "Data Analyst");
    dataDosen.push_back(dosen2);

    // Menambahkan mata kuliah dan mahasiswa ke setiap mata kuliah
    // Matkul 1
    Course matkul1("DPBO", "Bu Rosa");
    matkul1.addMahasiswa(mahasiswa1);
    matkul1.addMahasiswa(mahasiswa2);
    // Matkul 2
    Course matkul2("Alpro", "Bu Rosa");
    matkul2.addMahasiswa(mahasiswa2);
    matkul2.addMahasiswa(mahasiswa3);
    // Matkul 3
    Course matkul3("Sisbasdat", "Bu Rani");
    matkul3.addMahasiswa(mahasiswa1);
    matkul3.addMahasiswa(mahasiswa3);

    // Membuat objek Program Studi dan manambahkan matkul, dosen, dan mahasiswa ke dalam program studi
    // Membuat Prodi Ilmu Komputer
    Prodi prodi("Ilmu Komputer", "01");
    prodi.addMatkul(matkul1);
    prodi.addMatkul(matkul2);
    prodi.addMatkul(matkul3);
    prodi.addDosen(dosen1);
    prodi.addDosen(dosen2);
    prodi.addMhs(mahasiswa1);
    prodi.addMhs(mahasiswa2);
    prodi.addMhs(mahasiswa3);

    prodi.cetakProdi();

    cout << "           Daftar Mahasiswa            " << endl;
    cout << "=======================================" << endl;
    for(int i = 0; i < dataMahasiswa.size(); i++){
        cout << i+1 << ".NIK              : " << dataMahasiswa[i].getNIK() << endl;
        cout << "  Nama             : " << dataMahasiswa[i].getNama() << endl;
        cout << "  Jenis Kelamin    : " << dataMahasiswa[i].getGender() << endl;
        cout << "  Asal Universitas : " << dataMahasiswa[i].getUniversitas() << endl;
        cout << "  Email Education  : " << dataMahasiswa[i].getEmail() << endl;
        cout << "  NIM              : " << dataMahasiswa[i].getNIM() << endl;
        cout << "  Fakultas         : " << dataMahasiswa[i].getFakultas() << endl;
        cout << "  Program Studi    : " << dataMahasiswa[i].getProdi() << endl;
        cout << "---------------------------------------" << endl;
    }
    cout << "              Daftar Dosen             " << endl;
    cout << "=======================================" << endl;
    for(int i = 0; i < dataDosen.size(); i++){
        cout << i+1 << ".NIK                : " << dataDosen[i].getNIK() << endl;
        cout << "  Nama               : " << dataDosen[i].getNama() << endl;
        cout << "  Jenis Kelamin      : " << dataDosen[i].getGender() << endl;
        cout << "  Asal Universitas   : " << dataDosen[i].getUniversitas() << endl;
        cout << "  Email Education    : " << dataDosen[i].getEmail() << endl;
        cout << "  NIP                : " << dataDosen[i].getNIP() << endl;
        cout << "  Fakultas           : " << dataDosen[i].getFakultas() << endl;
        cout << "  Program Studi      : " << dataDosen[i].getProdi() << endl;
        cout << "  Pendidikan Terakhir: " << dataDosen[i].getPendidikan() << endl;
        cout << "  Keahlian           : " << dataDosen[i].getKeahlian() << endl;
        cout << "---------------------------------------" << endl;
    }
}