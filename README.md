# labpy02
Nama        : M.Ridho Febrian<p>

Kelas       : TI.24.A.5 <p>

Nim         : 312410500 <p>

Mata kuliah : Bahasa Pemrograman <p>

## Program pemesanan tiket bioskop
### Flowchart
![gambar 1](foto3/flowchart.png)

### Berikut adalah penjelasan terkait flowchart di atas 

- **Mulai:** Proses dimulai dengan langkah ini, ditandai oleh simbol oval. <p>
![gambar 4](foto3/no1.png)

- **Inisialisasi Harga Tiket:** <p>
Tiket Reguler: Rp50.000 <p>
Tiket VIP: Rp100.000 <p>
Diskon Member: 20% <p>
Tentukan harga untuk tiket reguler dan tiket VIP, serta diskon yang diberikan untuk member <p>
![gambar 5](foto3/no2.png)

- **Input Tipe Tiket:** Pengguna diminta untuk memasukkan tipe tiket yang ingin dibeli, apakah "reguler" atau "VIP". <p>
![gambar 6](foto3/no3.png)

- **Input Status Member:** Pengguna diminta untuk memasukkan status keanggotaan mereka, apakah memiliki kartu member ("ya") atau tidak ("tidak"). <p>
![gambar 7](foto3/no4.png)

- **Validasi Tipe Tiket:** Program memeriksa apakah tipe tiket yang diinput adalah "reguler" atau "VIP": <p>
Jika tipe tiket adalah "reguler", lanjutkan ke langkah berikutnya dengan harga tiket diatur ke Rp50.000. <p>
Jika tipe tiket adalah "VIP", lanjutkan ke langkah berikutnya dengan harga tiket diatur ke Rp100.000. <p>
Jika tipe tiket bukan "reguler" atau "VIP", anggap sebagai input yang tidak valid dan minta pengguna untuk memasukkan tipe tiket yang benar. <p>
![gambar 8](foto3/no5.png)

- **Periksa Apakah Harga Tidak Nol:** <p>
Program memeriksa apakah harga tiket sudah diatur (tidak nol): <p>
Jika harga sudah diatur, lanjutkan ke langkah berikutnya. <p>
Jika harga belum diatur (nol), kembali ke input tipe tiket. <p>
![gambar 9](foto3/no6.png)

- **Cek Status Member dan Hitung Diskon:** <p>
Program memeriksa apakah pengguna memiliki kartu member: <p>
Jika pengguna memiliki kartu member ("ya"), harga akhir dihitung dengan memberikan diskon 20%. <p>
Jika pengguna tidak memiliki kartu member ("tidak"), harga akhir tetap sama dengan harga tiket tanpa diskon. <p>
![gambar 10](foto3/no7.png)

- **Tampilkan Harga Akhir:** Program menampilkan total harga tiket yang harus dibayar oleh pengguna. <p>
![gambar 11](foto3/no8.png)

- **Selesai:** Proses selesai, ditandai oleh simbol oval. <p>
![gambar 12](foto3/no9.png)

### Program python
seperti ini jika algoritma di atas yang di buat dalam bentuk flowchart di jadikan sebuah program dengan bahasa python
![gambar 13](foto3/code.png)

### Hasil eksekusi 
ini hasil eksekusi dari kode program di atas
![gambar 14](foto3/hasil.png)




## Membuat program dan flowchart kalkulator sederhana menggunakan if elif else untuk menentukan operasi aritmatika

1.
![gambar](foto3/no10.png)

Titik awal dari flowchart menggunakan simbol oval.

2.
![gambar](foto3/no11.png)

Pengguna diminta menginputkan angka pertama.

![gambar](foto3/no12.png)

Pengguna diminta untuk menginputkan angka kedua.

4.
![gambar](foto3/no13.png)

Pengguna diminta untuk menginputkan operator (+, -, *, /).

5.
![gambar](foto3/no14.png)
Apakah operator = +?

-Jika Ya, maka Hasil = angka pertama + angka kedua. Dan lanjut ke no10.

-Jika Tidak, maka lanjut ke no6.

6.
![gambar](foto3/no15.png)
Apakah operator = -?

-Jika Ya, maka Hasil = angka pertama - angka kedua. Dan lanjut ke no10.

-Jika Tidak, maka lanjut ke no7.

7.
![gambar](foto3/no16.png)
Apakah operator = *?

-Jika Ya, maka Hasil = angka pertama * angka kedua. Dan lanjut ke no10.

-Jika Tidak, maka lanjut ke no8.

8.
![gambar](foto3/no17.png)
Apakah operator = /?

-Jika Ya, maka lanjut ke no9.

-Jika Tidak, maka Hasil = "Error: operator tidak valid!". Dan lanjut ke no10.

9.
![gambar](foto3/no18..png)
Apakah angka kedua ≠ 0?

-Jika Ya, maka Hasil = angka pertama / angka kedua. Dan lanjut ke no10.

-Jika Tidak, maka Hasil = "Error: pembagian dengan nol tidak diperbolehkan". Dan lanjut ke no10

10.
![gambar](foto3/no19.png)

Lalu output atau tampilkan Hasil.

11.
![gambar](foto3/no20.png)
Dan selesai diakhiri menggunakan simbol oval.

### Ini adalah flowchartnya:

![foto](foto3/flowchart1.png)

### Ini adalah programnya dalam bentuk python:

![gambar](foto3/codee.png)

### Ini adalah hasil dari program yang telah diinputkan:

![gambar](foto3/hasill.png)


