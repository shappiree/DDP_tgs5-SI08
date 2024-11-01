#soal 1
# Meminta input dari pengguna untuk setiap atribut
nama_kendaraan = input("Masukkan nama kendaraan: ")
jenis_kendaraan = input("Masukkan jenis kendaraan: ")
cc_kendaraan = input("Masukkan cc kendaraan: ")
warna_kendaraan = input("Masukkan warna kendaraan: ")
roda_kendaraan = input("Masukkan jumlah roda kendaraan: ")
harga_kendaraan = input("Masukkan harga kendaraan: ")
tipe_kendaraan = input("Masukkan tipe kendaraan: ")
merk_kendaraan = input("Masukkan merk kendaraan: ")

# Membuat list awal
kendaraan = [nama_kendaraan, jenis_kendaraan, cc_kendaraan, warna_kendaraan, roda_kendaraan]

# Menambahkan value di akhir list
kendaraan.extend([harga_kendaraan, tipe_kendaraan])

# Menambahkan value setelah 'jenis_kendaraan'
index_jenis = kendaraan.index(jenis_kendaraan)
kendaraan.insert(index_jenis + 1, merk_kendaraan)

# Output akhir dari list kendaraan
print("List kendaraan yang dimasukkan:",kendaraan)
print("======")