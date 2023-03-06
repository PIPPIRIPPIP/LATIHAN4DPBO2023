## Janji

Saya Ayesha Ali Firdaus (NIM 2101990) mengerjakan evaluasi LATIHAN 4 dalam mata kuliah Desain Pemrograman Berorientasi Objekuntuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Desain Program

![Desain](/CPP/Screenshot/Desain.png)

Terdapat 6 kelas dalam program yang dibuat:

1. Kelas Human, kelas ini digunakan untuk mempresentasikan objek sebagai manusia, dimana terdapat atribut berupa NIK, Nama, dan Jenis Kelamin. Kelas ini menjadi kelas utama dari kelas lainnya yang memiliki objek sama yaitu manusia.

2. Kelas Sivitas Akademik, kelas ini digunakan untuk mempresentasikan objek sebagai sekelompok orang yang aktif di lingkup akademi, dimana ada dua atribut yaitu asal universitas dan email universitas. Kelas ini merupakan anak dari kelas Human.

3. Kelas Mahasiswa, kelas ini digunakan untuk mempresentasikan objek sebagai mahasiswa, dimana ada beberapa atribut yang yang mencirikan sebagai mahasiswa yaitu NIM, Program Studi, dan Fakultas. Kelas ini merupakan anak dari kelas sivitas akademik, karena mahasiswa merupakan bagian dari kelompok sivitas akademik.

4. Kelas Dosen, Kelas ini mempresentasikan objek sebagai dosen, dimana terdapat beberapa atribut yaitu NIP, Fakultas, Program Studi, Pendidikan Terakhir, dan Keahlian. Kelas ini merupakan anak dari kelas Sivitas akademik karena sivitas akademik terdiri dari mahasiswa dan dosen.

5. Kelas Course, kelas ini mempresentasikan sebagai mata kuliah yang ada di sebuah universitas, dimana ada beberapa atribut yang ada di kelas ini yaitu Nama Matkul, Nama Dosen (Dosen yang mengajar), dan ListMhs (Daftar Mahasiswa yang mengontrak matkul tersebut). Kelas ini melakukan composite ke kelas mahasiswa untuk mengisi dari atribut ListMhs.

6. Kelas Prodi, kelas ini mempresentasikan program studi yang ada di universitas, dimana atribut yang ada di kelas ini adalah Nama Prodi, Kode Prodi, ListMatkul (Berisi daftar mata kuliah yang ada di prodi tersebut), ListDosen (Berisi daftar dosen yang mengajar di prodi tersebut), ListMhs(Berisi daftar mahasiswa yang ada di prodi tersebut). Kelas ini melakukan composite ke kelas Mahsiswa untuk mengisi list mahasiwa, kemudian composite ke kelas Dosen untuk mengisi list dosen, dan composite kelas Course untuk mengisi list matkul.

## Alur Program

Pada program ini inputan dilakukan secara manual, dan output yang diberikan berupa list daftar mahsiswa, list daftar dosen, dan informasi prodi. Pada informasi prodi yang di cetak adalah daftar dosen yang mengajar, daftar mahasiswa yang ada, dan daftar matkul yang ada.

## Dokumentasi

- List Daftar Dosen

![daftar dosen](/CPP/Screenshot/Dosen.png)

- List Daftar Mahasiswa

![daftar mahasiswa](/CPP/Screenshot/Mahasiswa.png)

- Informasi Program Studi

![daftar mahasiswa](/CPP/Screenshot/Prodi.png)
