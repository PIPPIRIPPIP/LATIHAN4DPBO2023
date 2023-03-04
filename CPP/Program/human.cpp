#include "header.hh"
using namespace std;

Human::Human(string nik, string nama, string gender){
    this->NIK = nik;
    this->Nama = nama;
    this->jenisKelamin = gender;
}

string Human::getNIK(){
    return NIK;
}

string Human::getNama(){
    return Nama;
}

string Human::getGender(){
    return jenisKelamin;
}

Human::~Human(){

}

SivitasAkademik::SivitasAkademik(string nik, string nama, string gender, string univ, string email) :
    Human(nik, nama, gender){
    this->asalUniversitas = univ;
    this->emailEdu = email;
}

string SivitasAkademik::getUniversitas(){
    return asalUniversitas;
}

string SivitasAkademik::getEmail(){
    return emailEdu;
}

SivitasAkademik::~SivitasAkademik(){

}

Dosen::Dosen(string nik, string nama, string gender, string univ, string email,
              string nip, string fakultas, string prodi, string pend_terakhir, string keahlian):
              SivitasAkademik(nik, nama, gender, univ, email){
    this->NIP = nip;
    this->fakultas = fakultas;
    this->prodi = prodi;
    this->pend_terakhir = pend_terakhir;
    this->keahlian = keahlian;
}

string Dosen::getNIP(){
    return NIP;
}

string Dosen::getFakultas(){
    return fakultas;
}

string Dosen::getProdi(){
    return prodi;
}

string Dosen::getPendidikan(){
    return pend_terakhir;
}

string Dosen::getKeahlian(){
    return keahlian;
}

Dosen::~Dosen(){

}

Mahasiswa::Mahasiswa(string nik, string nama, string gender, string univ, string email,
                  string nim, string fakultas, string prodi):
                  SivitasAkademik(nik, nama, gender, univ, email){
    this->NIM = nim;
    this->fakultas = fakultas;
    this->prodi = prodi;
}

string Mahasiswa::getNIM(){
    return NIM;
}


string Mahasiswa::getFakultas(){
    return fakultas;
}

string Mahasiswa::getProdi(){
    return prodi;
}

Mahasiswa::~Mahasiswa(){

}