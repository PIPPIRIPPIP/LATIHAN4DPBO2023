// Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 4 dalam mata kuliah Desain Pemrograman Berorientasi Objek
// untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

#include "header.hh"
using namespace std;

Course::Course(string nama, string namaDosen){
    this->namaMatkul = nama;
    this->namaDosen = namaDosen;
}

string Course::getMatkul(){
    return namaMatkul;
}

string Course::getDosen(){
    return namaDosen;
}

void Course::addMahasiswa(Mahasiswa mhs){
    listMhs.push_back(mhs);
}

Course::~Course(){

}

Prodi::Prodi(string prodi, string kode){
    this->namaProdi = prodi;
    this->kode = kode;
}

string Prodi::getProdi(){
    return namaProdi;
}

string Prodi::getKode(){
    return kode;
}

void Prodi::addMatkul(Course matkul){
    listMatkul.push_back(matkul);
}

void Prodi::addDosen(Dosen dosen){
    listDosen.push_back(dosen);
}

void Prodi::addMhs(Mahasiswa mhs){
    listMhs.push_back(mhs);
}

void Prodi::cetakProdi(){
    cout << "              Data Prodi             " << endl;
    cout << "=====================================" << endl;
    // Mencetak daftar dosen
    cout << " Dosen pada prodi " << namaProdi << endl;
    for(int i = 0; i < listDosen.size(); i++){
        cout << i+1 << ". " << listDosen[i].getNama() << endl;
    }
    // Mencetak daftar Mahasiswa
    cout << " Mahasiswa pada prodi " << namaProdi << endl;
    for(int i = 0; i < listMhs.size(); i++){
        cout << i+1 << ". " << listMhs[i].getNama() << endl;
    }
    // Mencetak daftar matkul
    cout << " Matkul pada prodi " << namaProdi << endl;
    for(int i = 0; i < listMatkul.size(); i++){
        cout << i+1 << ". " << listMatkul[i].getMatkul() << endl;
    }
}

Prodi::~Prodi(){

}