x = int(input("Masukkan sebuah bilangan : "))
if x < 200:
    keterangan = " : Nilai kurang dari 200"
    print(x, keterangan)
    if x == 150:
        keterangan = " : Sama dengan 150"
        print(x, keterangan)
    elif x == 100: 
        keterangan = " : Sama dengan 100"
        print(x, keterangan)
    elif x == 50: 
        keterangan = " : Sama dengan 50"
        print(x, keterangan)
    elif x < 50: 
        keterangan = " : kurang dari 50"
        print(x, keterangan)
else:
    keterangan = "Nilai yang dimasukan salah"
    print(keterangan)

print("selesai")