kode_barang = input("Masukkan kode barang: ")
nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan barang: "))
jumlah_beli = int(input("Masukkan jumlah beli: "))

total_pembelian = harga_satuan * jumlah_beli

if total_pembelian >= 250000:
    potongan = total_pembelian * 0.0225
    total_bayar = total_pembelian - potongan
    print(f"\nKode Barang: {kode_barang}")
    print(f"Nama Barang: {nama_barang}")
    print(f"Harga Satuan: {harga_satuan}")
    print(f"Jumlah Beli: {jumlah_beli}")
    print(f"Total Pembelian: {total_pembelian}")
    print(f"Potongan Harga: {potongan}")
    print(f"Total Bayar Setelah Potongan: {total_bayar}")
else:
    print(f"\nKode Barang: {kode_barang}")
    print(f"Nama Barang: {nama_barang}")
    print(f"Harga Satuan: {harga_satuan}")
    print(f"Jumlah Beli: {jumlah_beli}")
    print(f"Total Pembelian: {total_pembelian}")
    print("Tidak ada potongan harga.")
