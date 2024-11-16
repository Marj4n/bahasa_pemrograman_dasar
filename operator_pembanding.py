nilai_akhir = int(input("MASUKAN NILAI: "))
if nilai_akhir > 100 or nilai_akhir < 0:
    print("NILAI YANG DI MASUKAN HARUS 1 - 100")
    if (nilai_akhir == 1000):
        print("MANTAPPP")
elif nilai_akhir >= 60:
    keterangan = "LULUS"
    print(f"Anda dinyatakan : {keterangan} dengan nilai: {nilai_akhir}")
else:
    keterangan = "TIDAK LULUS"
    print(f"Anda dinyatakan : {keterangan} dengan nilai: {nilai_akhir}")

