# Tugas Kecil 2 IF2211 Strategi Algoritma
> Implementasi Branch and Bound dalam program 15-Puzzle Solver

## Table of Contents
- [Tugas Kecil 2 IF2211 Strategi Algoritma](#tugas-kecil-2-if2211-strategi-algoritma)
  - [Table of Contents](#table-of-contents)
  - [Program Description](#program-description)
  - [Requirements and Setup](#requirements-and-setup)
  - [How To Use Program](#how-to-use-program)
  - [Contributor](#contributor)

## Program Description
Algoritma *Branch and Bound* merupakan algoritma yang digunakan untuk memecahkan persoalan optimasi dengan cara melakukan percabangan (branching) dari node awal menjadi node - node anak dan melakukan pembatasan (bounding) dari node - node tersebut untuk mengarah ke solusi. Proses *branching* dan *bounding* tersebut dilakukan berulang kali hingga ditemukan solusi yang optimal. Proses pencarian dengan algoritma ini menggunakan pembentukan pohon ruang status dinamis dengan permasalahan awal menjadi node akar dan bercabang menjadi node - node anak lainnya hingga node solusi. Berbeda dengan Algoritma BFS ataupun DFS, urutan pemeriksaan node dalam algoritma *Branch and Bound* dipilih berdasarkan node yang memiliki cost terkecil (*Least Cost Search*).

Program ini merupakan sebuah library sederhana untuk mendapatkan solusi dari sebuah permainan 15-Puzzle. Dalam kasus ini, optimasi yang dilakukan adalah untuk memecahkan puzzle dengan langkah sesedikit mungkin. Puzzle yang didapatkan oleh program ini dapat dibentuk secara random dalam program, atau membaca puzzle yang tersedia dari file eksternal. Apabila menggunakan file eksternal, maka blank space dalam matriks akan diwakili dengan angka 0. Program ini menggunakan algoritma *Branch and Bound* dengan cara meletakkan puzzle awal sebagai root node kemudian akan melakukan pencabangan (branching) hingga ditemukan solusi permainan. Node anak yang akan dipilih untuk diperiksa selanjutnya akan ditentukan dari bound node tersebut. Nilai bound tiap simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar, dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state). Luaran yang diberikan oleh program ini adalah cetakan puzzle/matriks awal, kurang(i) dan X dari matriks awal tersebut, pesan apakah puzzle solvable atau tidak, dan apabila solvable akan menampilkan urutan matriks dari awal hingga solusi untuk tiap langkah, serta waktu eksekusi program dalam sekon.

Program dibungkus dalam 2 file utama, yakni main.py dan solver.py
1. main.py : Merupakan file yang dijalankan untuk mendapatkan solusi dari 15-Puzzle yang tersedia.
2. solver.py : Merupakan file library untuk algoritma *Branch and Bound* dalam implementasi 15-Puzzle Solver yang telah saya buat.
## Requirements and Setup
- Python 3 diperlukan dalam program ini. Anda bisa mendownloadnya pada link <a href="http://www.python.org/downloads/">berikut</a>, atau agar mempermudah anda dapat menonton proses instalasinya dari link <a href="https://www.youtube.com/watch?v=Kn1HF3oD19c">berikut</a>.

- pip harus terinstall. Anda bisa melakukan instalasi pada link <a href="https://pip.pypa.io/en/stable/installation/">berikut</a>. Pastikan juga pip harus ada pada PATH dengan cara <a href="https://www.youtube.com/watch?v=UTUlp6L2zkw">berikut</a>.

- Terdapat beberapa library yang harus terinstall untuk menjalankan program ini, yakni numpy dan pyfiglet. Anda bisa menggunakan pip yang sudah diinstall sebelumnya. Buka powershell atau terminal pada komputer anda, kemudian masukkan sintaks berikut: 
```
pip install numpy
pip install pyfiglet
```

- Clone repository ini ke dalam komputer anda dengan cara memasukkan sintaks berikut pada powershell atau terminal:
```
git clone https://github.com/saulsayerz/Tucil3_13520094
```

## How to Use Program
1. Buka root direktori dari repository yang telah anda clone

2. Jalankan file main.py yang ada dalam folder src. Terdapat dua cara untuk menjalankan file tersebut. Yang pertama dengan menjalankan run.bat yang tersedia dalam root direktori dan yang kedua dengan cara membuka terminal pada root directory kemudian mengetikkan sintaks berikut :
```
python src/main.py
```

3. Program akan meminta cara untuk men*generate* puzzle. Apabila anda ingin memasukkan puzzle dari file eksternal, masukkan angka 1 lalu ketik nama file yang diinginkan. Program akan meminta ulang nama file apabila file tersebut tidak ditemukan. Apabila anda ingin men*generate* puzzle secara random, maka masukkan angka 2. Apabila anda memasukkan angka selain 1 atau 2, program akan meminta ulang input sampai benar.

4. Program akan menampilkan luaran matriks awal, kurang(i) dan X dari matriks awal tersebut, pesan apakah puzzle solvable atau tidak, dan apabila solvable akan menampilkan urutan matriks dari awal hingga solusi untuk tiap langkah. Program juga akan menampilkan luaran berupa waktu eksekusi dalam sekon.

5. Program kemudian akan meminta input apakah anda ingin solve untuk puzzle yang lain atau tidak. Apabila tidak, maka anda dapat memasukkan input n kemudian program akan selesai. Apabila ingin lanjut memeriksa, anda dapat memasukkan input y kemudian program akan kembali ke langkah 3.

## Contributor :
> Saul Sayers (13520094), K01 - Informatika ITB 2020. 

More detailed contact: 
- Line : saulsayerz
- Instagram : <a href="https://www.instagram.com/saulsayers/?hl=en">saulsayers</a> 
- Linkedin : <a href="https://www.linkedin.com/in/saulsayers/?originalSubdomain=id">saulsayers</a>
- github : <a href="https://github.com/saulsayerz">saulsayerz</a>
- email : saulsayers@gmail.com
