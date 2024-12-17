# def angka_beda(a, b, c):
#     if a != b != c:
#         return True
#     else:
#         return False
# a = int(input("masukkkan angka:")) 

# b = int(input("Masukkan angka kedua: "))
# c = int(input("Masukkan angka ketiga: "))

# print(angka_beda(a,b,c))     

def cek_prima(n, i=2):
    if n <= 1:
        return False
    if i * 1 > n:
        return True
    if n % i == 0:
        return False
    return cek_prima(n, i + 1)

bil= int(input("masukkan angka yg mau di cek:"))

if cek_prima(bil):
    print(f"{bil} adalah prima")
else:
    print(f"{bil} bukan prima")
