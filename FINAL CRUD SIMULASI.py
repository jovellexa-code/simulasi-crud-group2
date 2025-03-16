def menu_utama(): 
    while True:
        pilih_menu = input('''
            \n🥳 Selamat datang di Purwadhika Fest 2025! 🥳

            List Menu:
            1. Menampilkan Daftar Tiket Konser  4. Mengedit Daftar Tiket Konser
            2. Menambah Daftar Tiket Konser     5. Membeli Tiket Konser
            3. Menghapus Daftar Tiket Konser    6. Exit Program Konser
                          
            Masukkan angka Menu yang ingin dijalankan :
            ''')
        if pilih_menu == '1': #Kondisi jika user memilih menu 1 (Menampilkan daftar tiket)
            tampilkan_tiket()
        elif pilih_menu == '2': #Kondisi jika user memilih menu 2 (Menambah Tiket)
            tambahkan_tiket()
        elif pilih_menu == '3': #Kondisi jika user memilih menu 3 (Menghapus Tiket)
            menghapus_tiket()
        elif pilih_menu == '4': #Kondisi jika user memilih menu 4 (Mengedit Tiket)
            mengedit_tiket()
        elif pilih_menu == '5': #Kondisi jika user memilih menu 5 (Membeli Tiket)
            membeli_tiket()
        elif pilih_menu == '6': #Kondisi jika user memilih menu 6 (Exit dari program)
            keluar_program()
        else:
            print("\n⚠️ Pilihan tidak valid! Masukkan angka 1-6.")


def tampilkan_tiket():
    print("\nDaftar Tiket Konser Purwadhika Fest 🎟️")
    headers = ["No", "Kategori Tiket", "Stok", "Harga"]
    table = [[tiket['nomor'], tiket['kategori'], tiket['stok'], tiket['harga']] for tiket in data_tiket]
    print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))


def tambahkan_tiket(): 
    tampilkan_tiket()
    while True:
        while True:
            tiket_tambahan = input('Masukkan Kategori Tiket yang ingin ditambahkan : ').strip().upper()  # User ingin menambah kategori tiket
            if tiket_tambahan.isalpha():
                break
            else:
                print("Kategori hanya boleh berisi huruf. Silahkan coba lagi.")
        for tiket in data_tiket:
            if tiket["kategori"] == tiket_tambahan.upper():  
                print('Kategori tiket sudah terdaftar')
                return  ## kalau diganti jadi break, dia bakal lanjut ke stok tiket dan harga tiket, ini nanti malah gantiin fungsi update
            
        while True:
            # Input stok dan harga jika kategori belum ada
            try:
                stok_tiket = int(input('Masukkan jumlah stok tiket tambahan : '))
                break
            except ValueError:
                print("Input gagal, silahkan gunakan angka untuk stok dan harga.")
        while True:
            try:
                harga_tiket = int(input('Masukkan harga tiket yang baru : '))
                break
            except ValueError:
                print("Input gagal, silahkan gunakan angka untuk stok dan harga.")

                # untuk menampilkan preview tiket menggunakan tabulate double grid
        preview_tiket = [[len(data_tiket) + 1, tiket_tambahan, stok_tiket, harga_tiket]]
        headers = ["No", "Kategori Tiket", "Stok", "Harga"]

        print("\nBerikut adalah preview tiket yang akan anda tambahkan: ")
        print(tabulate(preview_tiket, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))

        konfirmasi = input("\n Apakah Anda yakin ingin menambahkan tiket ini? (y/n): ").lower()
        if konfirmasi == 'y':
            data_tiket.append({
                "nomor": len(data_tiket) + 1,  
                "kategori": tiket_tambahan.upper(),
                "stok": stok_tiket,
                "harga": harga_tiket
                })
            tampilkan_tiket()
            print('\n✅ Tiket berhasil ditambahkan!')

            lanjut = input("\nIngin menambahkan tiket lagi? (y/n): ").lower()
            if lanjut == 'y':
                continue
            elif lanjut == 'n':
                pilihan = input("\nOk, apakah Anda ingin kembali ke menu utama? (y/n): ").lower()
                if pilihan == 'n':
                    print('Terima Kasih! Sampai Jumpa Kembali.')
                    exit()
                elif pilihan == 'y':
                    break
                else:
                    print("\n⚠️ Pilihan tidak valid! Masukkan 'y' atau 'n'.") 

            else:
                print("\n ⚠️ Pilihan tidak valid! Masukkan 'y' atau 'n'.") 

        elif konfirmasi == 'n':
            print('\n     ❌ Penambahan tiket dibatalkan.')
            break

        else:
            print("\n ⚠️ Pilihan tidak valid! Masukkan 'y' atau 'n'.")


def menghapus_tiket():
    tampilkan_tiket()
    while True:
        menghapus_tiket = input('Masukkan kategori tiket yang ingin dihapus: ').upper()

        for kategori in range(len(data_tiket)):
            if menghapus_tiket == data_tiket[kategori]['kategori'].upper():
                checker_hapus = input('Apakah kamu yakin ingin menghapus? (y/n): ').lower()
                if checker_hapus == 'y':
                    print('\n✅ Kategori yang kamu pilih sudah terhapus!')
                    data_tiket.pop(kategori)  
                     
                    for i in range(len(data_tiket)):
                        data_tiket[i]['nomor'] = i + 1  
                    tampilkan_tiket()
                    break
                
                elif checker_hapus == 'n': 
                    print('❌ Penghapusan dibatalkan.')
                    return

                else:
                    print('❌ Penghapusan dibatalkan. Data yang kamu input bukan huruf y/n!') 
                    break 

        else:
            print('⚠️ Kategori tidak valid!')

        while True: 
                checker_hapus2 = input('Mau hapus yang lain? (y/n): ').lower()
                if checker_hapus2 == 'y':
                    break  # Keluar dari loop utama
                elif checker_hapus2 == 'n': 
                    return
                else: 
                    print("‼️ Masukkan huruf y/n!")


def mengedit_tiket(): 
    tampilkan_tiket()
    while True:
        indexTiket = input("Masukkan nomor tiket yang ingin Anda ubah: ")  
        if indexTiket.isdigit():  # Cek apakah input hanya angka
            indexTiket = int(indexTiket) - 1 
            if 0 <= indexTiket < len(data_tiket):
                kolom=input('Masukkan nama kolom yang diubah : ')
                
                if kolom.title()=='Kategori Tiket':
                    valueEdit=input('Masukkan Kategori Tiket yang baru : ')
                    data_tiket[indexTiket]['kategori']=valueEdit.upper()
                    print('\n✅ Kategori Tiket berhasil diubah!\n')
                    tampilkan_tiket() 
                
                elif kolom.title()=='Stok': 
                    valueEdit=(input('Masukkan Stok Tiket yang baru : '))
                    if valueEdit.isdigit():
                        data_tiket[indexTiket]['stok']=int(valueEdit)
                        print('\n✅ Stok tiket berhasil diubah!\n')
                        tampilkan_tiket()    
                    else:
                        print('\n ⚠️Stok harus berupa angka!')
                    
                elif kolom.title()=='Harga':
                    valueEdit=(input('Masukkan Harga Tiket yang baru :'))
                    if valueEdit.isdigit():
                        data_tiket[indexTiket]['harga']=int(valueEdit)
                        print('\n✅Harga Tiket berhasil diubah!\n')
                        tampilkan_tiket ()
                    else:
                        print ('\n ⚠️Harga harus berupa angka!')
                
                else:
                    print('Nama kolom yang anda masukkan tidak tersedia')
               
                while True: 
                        checker_edit=input("Mau mengedit tiket yang lain? (y/n): ")   
                        if checker_edit.lower() == 'y': 
                            break
                        
                        elif checker_edit.lower() == 'n':
                            return

                        else:
                            print("Masukkan huruf y/n!")
                            continue
            else:
                print('Nomor tiket tidak valid, silahkan memasukkan nomor yang tertera pada tabel')
        else:
            print('Nomor tiket yang anda masukkan tidak valid')


def membeli_tiket():
    shoppingcart.clear()
    tampilkan_tiket()
    while True:
        try:
            indexTiket_membeli = int(input('Masukkan nomor tiket yang ingin Anda beli : ')) - 1
            if indexTiket_membeli < 0 or indexTiket_membeli >= len(data_tiket):
                print("⚠️ Nomor tiket yang Anda masukkan tidak valid!")
                continue

            stok_tersedia = data_tiket[indexTiket_membeli]['stok']
            if stok_tersedia == 0:
                print(f'Maaf, stok {data_tiket[indexTiket_membeli]["kategori"]} sudah habis, silakan pilih kategori yang lalin ya! ')
                continue

            while True:
                try: 
                    banyakTiket = int(input(f'Masukkan jumlah tiket {data_tiket[indexTiket_membeli]["kategori"]} yang ingin Anda beli:'))
                    if banyakTiket > stok_tersedia: 
                        print(f'Stok tiket yang Anda pilih tidak cukup, stok {data_tiket[indexTiket_membeli]["kategori"]} tersisa {stok_tersedia}') 
                        continue

                    elif banyakTiket == 0:
                        print("⚠️ Anda memasukkan angka 0! Masukkan jumlah tiket yang kamu inginkan!")   
                        continue 
                        
                    shoppingcart.append({"kategori": data_tiket[indexTiket_membeli]["kategori"], "stok": banyakTiket, "harga": data_tiket[indexTiket_membeli]["harga"]})
                    data_tiket[indexTiket_membeli]["stok"] -= banyakTiket #Coba kurangin stok kalau user udah input jumlah tiket 
                    break

                except ValueError:
                    print("⚠️ Data yang Anda masukkan tidak valid! Silakan masukkan angka yang benar.")

            shopping_cart()

            while True:
                    checker = input("Apakah Anda mau beli yang lain? (y/n)").lower()
                    if checker in ['y', 'n']:
                        break
                    else:
                        print("⚠️ Data yang Anda input tidak valid! Mohon masukkan 'y' atau 'n'.")
            
            if checker == "y":
                continue

            elif checker =="n":
                print("\nDaftar Belanja 🛒")
                total_harga = 0
                headers = ["Kategori", "Kuantitas", "Harga", "Total Harga"]
                table = []
                
                for item in shoppingcart:
                    total_item = item ["stok"] * item["harga"]
                    total_harga += total_item
                    table.append([item["kategori"], item["stok"], item["harga"], total_item])
                print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
                print(f"Total yang harus Anda bayar adalah = {total_harga}")

                while True:
                    try: 
                        jumlah_uang = int(input("Masukkan jumlah uang 💰 = "))
                        if jumlah_uang < total_harga:
                            print(f"❌ Transaksi Anda dibatalkan! Uang Anda kurang {total_harga - jumlah_uang}")
                        elif jumlah_uang >= total_harga:
                            print(f"✅ Transaksi Anda berhasil! Terima Kasih, uang kembalian Anda = {jumlah_uang - total_harga}\nSampai jumpa di Purwadhika Fest 2025🥁")
                            break
                            
                    except ValueError: 
                        print("⚠️ Data yang Anda masukkan tidak valid! Silakan masukkan jumlah yang benar!")
            break 

        except ValueError:
            print("⚠️ Pilihan tidak valid! Silakan masukkan angka yang sesuai.")
            continue


def keluar_program():
    print("Terima kasih! Sampai jumpa di Purwadhika Fest 2025 ya!🥁")
    exit()


def shopping_cart(): 
    print("\nShopping Cart 🛒")
    headers = ["Kategori", "Kuantitas", "Harga"]
    table = [[item["kategori"], item["stok"], item["harga"]] for item in shoppingcart]
    print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left")))


#Data awalan 
#Data disimpan menggunakan dictionary dalam list 
data_tiket = [
    {"nomor":1, "kategori": "VIP", "stok": 10, "harga": 3800000},
    {"nomor":2, "kategori": "PLATINUM", "stok": 15, "harga": 3400000},
    {"nomor":3, "kategori": "CAT 1", "stok": 30, "harga": 2900000},
    {"nomor":4, "kategori": "CAT 2", "stok": 50, "harga": 2600000},
    {"nomor":5, "kategori": "CAT 3", "stok": 70, "harga": 2100000},
]


#List kosong shopping cart
shoppingcart = []


#Import tabulate untuk tabel
from tabulate import tabulate


#Kembali ke menu utama
menu_utama()
