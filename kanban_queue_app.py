def tambah_barang(file_stok, nama_barang, jumlah):
    if nama_barang in file_stok:
        file_stok[nama_barang] += jumlah
    else:
        file_stok[nama_barang] = jumlah
    print(f"Stok {nama_barang} berhasil ditambah.")

def kurangi_barang(file_stok, nama_barang, jumlah):
    if nama_barang in file_stok:
        if file_stok[nama_barang] >= jumlah:
            file_stok[nama_barang] -= jumlah
            print(f"Stok {nama_barang} berhasil dikurangi.")
        else:
            print("Stok tidak cukup untuk dikurangi.") 
    else:
        print(f"{nama_barang} tidak ada di dalam stok.")

def simpan_stok(nama_file, file_stok):
    with open(nama_file, "w") as file:
        for nama_barang, jumlah in file_stok.items():
            file.write(f"{nama_barang}: {jumlah}\n")
    print("Stok berhasil disimpan.")

def tampilkan_stok(file_stok):
    if file_stok:
        for nama_barang, jumlah in file_stok.items():
            print(f"{nama_barang}: {jumlah}")
    else:
        print("Tidak ada barang di dalam stok.")

def baca_stok(nama_file):
    file_stok = {}
    try:
        with open(nama_file, "r") as file:
            for line in file:
                nama_barang, jumlah = line.strip().split(": ")
                file_stok[nama_barang] = int(jumlah)
        return file_stok
    except FileNotFoundError:
        print(f"{nama_file} tidak ditemukan.")
        return {}

def main():
    nama_file = "file_stok.txt"
    file_stok = baca_stok(nama_file)

    while True:
        print("\nMenu")
        print("1. Tambah stok \n2. Kurangi stok \n3. Tampilkan stok \nx. Keluar")
        pilihan = input("Masukan menu yang anda pilih: ")

        if pilihan == "1":
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah barang: "))
            tambah_barang(file_stok, nama_barang, jumlah)
        elif pilihan == "2":
            nama_barang = input("Masukkan nama barang: ")
            jumlah = int(input("Masukkan jumlah yang akan dikurangi: "))
            kurangi_barang(file_stok, nama_barang, jumlah)
        elif pilihan == "3":
            tampilkan_stok(file_stok)
        elif pilihan == "x":
            simpan_stok(nama_file, file_stok)
            exit()
        else:
            print("Menu yang anda pilih tidak valid.")

if __name__ == "__main__":
    main()
