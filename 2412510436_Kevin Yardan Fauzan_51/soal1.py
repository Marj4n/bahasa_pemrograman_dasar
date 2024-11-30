def hitung_nilai(N):
  if N > 75:
    N = N - 56
  if N < 40:
    N = N + 36
  if N < 50:
    N = N + 50
  N = N // 2
  if N < 30:
    N = N + 30
  N = N // 2
  return N

N = int(input("Masukkan dua digit terakhir NIM Anda: "))

hasil = hitung_nilai(N)
print("Hasil akhir:", hasil)