# Nomor 1
total_tabungan_global = 0  

def masukkan_tabungan(nama):
    while True:
        try:
            tabungan = int(input(f"Masukkan tabungan {nama}: "))
            if tabungan > 2000000:
                print("Saldo tidak boleh lebih dari 2.000.000")
            elif tabungan < 2000000:
                print("Saldo tidak boleh kurang dari 2.000.000")
            else:
                return tabungan
        except:
            print("Input tidak valid. Pastikan untuk memasukkan jumlah uang dalam angka.")

def hitung_total_tabungan():
    global total_tabungan_global 

    if total_tabungan_global >= 100000000:
        print(f"Total biaya liburan: {total_tabungan_global}")
        return total_tabungan_global

    tabungan_dina = masukkan_tabungan("Dina")
    tabungan_arif = masukkan_tabungan("Arif")
    tabungan_lila = masukkan_tabungan("Lila")

    total_tabungan_global += tabungan_dina + tabungan_arif + tabungan_lila

    if total_tabungan_global >= 100000000:
        print(f"Total biaya liburan: {total_tabungan_global}")
    else:
        print(f"Total biaya liburan: {total_tabungan_global} kurang {100000000 - total_tabungan_global}")

    return hitung_total_tabungan()

hitung_total_tabungan()



# Nomor 2
def cek_prima(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return cek_prima(n, i + 1)
angka = int(input("Masukkan bilangan: "))
if cek_prima(angka):
    print(angka, "adalah bilangan prima")
else:
    print(angka, "bukan bilangan prima")


