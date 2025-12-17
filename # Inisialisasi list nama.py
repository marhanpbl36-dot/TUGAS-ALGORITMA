# Inisialisasi list nama
nama_list = []

while True:
    # Menampilkan menu
    print("Menu:")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")

    # Menerima input pilihan menu
    pilihan = input("Pilih menu: ")

    # Navigasi menu
    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nama_list.append(nama)
        print(f"Nama '{nama}' telah ditambahkan.")
    elif pilihan == "2":
        if not nama_list:
            print("Tidak ada nama dalam list.")
        else:
            print("Nama-nama dalam list:")
            for i, nama in enumerate(nama_list, start=1):
                print(f"{i}. {nama}")
            index = int(input("Masukkan nomor nama yang ingin dihapus: ")) - 1
            if index < 0 or index >= len(nama_list):
                print("Nomor nama tidak valid.")
            else:
                nama_dihapus = nama_list.pop(index)
                print(f"Nama '{nama_dihapus}' telah dihapus.")
    elif pilihan == "3":
        if not nama_list:
            print("Tidak ada nama dalam list.")
        else:
            print("Nama-nama dalam list:")
            for i, nama in enumerate(nama_list, start=1):
                print(f"{i}. {nama}")
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan menu tidak valid.")