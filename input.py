import modul as mod

while True :
    print("======================")
    print("selamat datang ")
    print("1. Tambah data")
    print("2. Edit Data")
    print("3. Hapus data")
    print("4. Cari data")
    print("5. tampil data")
    print("6. Tampil jumlah data")
    print("7. keluar")
    print("")
    pilihan = int(input("masukan pilihan = "))
    if pilihan == 1 :
        mod.tambah()
    elif pilihan == 2 :
        mod.edit()
    elif pilihan == 3 :
        mod.hapus()
    elif pilihan == 4 :
        mod.cari()
    elif pilihan == 5 :
        mod.tampil()
    elif pilihan == 6 :
        mod.jumlah()
    elif pilihan == 7 :
        print("terima kasih")
        break
        