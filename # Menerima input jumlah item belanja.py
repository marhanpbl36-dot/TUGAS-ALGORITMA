# Menerima input jumlah item belanja
jumlah_item = int(input("Masukkan jumlah item belanja: "))

# Inisialisasi list harga
harga_item = []

# Menerima input harga untuk setiap item
for i in range(jumlah_item):
    harga = int(input(f"Masukkan harga item ke-{i+1}: "))
    harga_item.append(harga)

# Menghitung total belanja
total_belanja = sum(harga_item)

# Menghitung diskon
if total_belanja >= 300000:
    diskon = total_belanja * 0.1
else:
    diskon = 0

# Menghitung total akhir
total_akhir = total_belanja - diskon

# Menampilkan total akhir
print(f"Total belanja: Rp {total_belanja:,.0f}")
print(f"Diskon: Rp {diskon:,.0f}")
print(f"Total akhir: Rp {total_akhir:,.0f}")