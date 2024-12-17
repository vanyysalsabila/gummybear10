usia = int(input("Masukkan usia anda: "))
if usia <= 5:
    print("Balita")
elif usia >= 6 and usia <= 11:
    print("Kanak-kanak")
elif usia >= 12 and usia <= 25:
    print("Remaja")
elif usia >= 26 and usia <= 45:
    print("Dewasa")
elif usia > 45:
    print("Lansia")
    
inputuser = input("Masukkan usia anda: ")
try:
    usia = int(inputuser)
    if usia <= 5:
        print("Balita")
    elif usia >= 6 and usia <= 11:
        print("Kanak-kanak")
    elif usia >= 12 and usia <= 25:
        print("Remaja")
    elif usia >= 26 and usia <= 45:
        print("Dewasa")
    elif usia > 45:
        print("Lansia")
except:
    print("Anda salah memasukkan input usia")

def masukkan_tabungan(nama):
    while True:
        try:
            tabungan = int(input(f"Masukkan tabungan {nama}: "))
            return tabungan
        except:
            print("Input tidak valid. Pastikan untuk memasukkan jumlah uang dalam angka.")

def hitung_total_tabungan():
    # Memasukkan kontribusi masing-masing
    tabungan_tia = masukkan_tabungan("Tia")
    tabungan_rini = masukkan_tabungan("Rini")
    tabungan_dimas = masukkan_tabungan("Dimas")

    # Menghitung total kontribusi
    total_tabungan = tabungan_tia + tabungan_rini + tabungan_dimas
    print(f"Total biaya liburan: {total_tabungan}")

# Menjalankan fungsi
hitung_total_tabungan()

def perkalian(bil1, bil2):
    if bil2 == 1:
        print("%d = " % (bil1), end='')
        return bil1
    else:
        print("%d + " % (bil1), end='')
        return bil1 + perkalian(bil1, bil2 - 1)

print(perkalian(2, 4))

def pangkat(bil1, bil2):
    if bil2 == 1:
        print("%d = " % (bil1), end='')
        return bil1
    else:
        print("%d * " % (bil1), end='')
        return bil1 * perkalian(bil1, bil2 - 1)

print(pangkat(2, 4))

def fibo(n):
    f1, f2 = 1, 1
    print(f1, ",", f2, ",", end='')

    for i in range(2, n):
        fib = f1 + f2
        f1 = f2
        f2 = fib
        print(fib, ",", end='')

fibo(7)

        