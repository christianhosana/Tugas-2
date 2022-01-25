print("Selamat Datang!")


# In[ ]:


daftar_kontak = []

def tampilkan_menu():
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def tampilkan_kontak():
    if daftar_kontak == []:
        print('Belum ada kontak yang ditambahkan\n')
    else:
        print("Daftar Kontak:")
        for kontak in daftar_kontak:
            print("Nama: " + kontak["nama"])
            print("No Telepon: " + kontak["telp"]+'\n')

def tambah_kontak():
    nama = input("Nama: ")
    telp = input("No Telepon: ")
    kontak = {
        "nama": nama,
        "telp": telp
    }
    daftar_kontak.append(kontak)
    print("Kontak berhasil ditambahkan\n")


# In[ ]:


while True:

    tampilkan_menu()

    menu = input("Pilih menu: ")

    if menu == "1":
        tampilkan_kontak()
    elif menu == "2":
        tambah_kontak()
    elif menu == "3":
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")