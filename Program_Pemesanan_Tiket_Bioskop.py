# program pemesanan tiket bioskop

# harga tiket 
harga_reguler = 50000
harga_vip = 100000

# diskon untuk member
diskon_member = 0.2 

# input tipe tiket dan status member
tipe_tiket = input("masukkan tipe tiket (reguler/vip): ").lower()
status_member = input("apakah anda memiliki kartu member? (ya/tidak): ").lower()

# menghitung harga tiket berdasarkan tipe dan status member
if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    harga = 0
    print("tipe tiket tidak valid!")

# cek status member 
if harga != 0:
    harga_akhir = harga * (1 - diskon_member) if status_member == "ya" else harga
    print("total harga yang harus dibayar: RP", int(harga_akhir))