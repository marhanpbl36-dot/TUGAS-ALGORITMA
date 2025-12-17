# Menerima input username
username = input("Masukkan username: ")

# Mengecek syarat
if len(username) < 5:
    print("Username tidak valid. Alasan: Username harus minimal 5 karakter.")
elif ' ' in username:
    print("Username tidak valid. Alasan: Username tidak boleh mengandung spasi.")
elif not username[0].isalpha():
    print("Username tidak valid. Alasan: Karakter pertama username harus huruf.")
else:
    print("Username valid.")