count = 0
while count <= 10:
    print("i im student")
    count = count + 1
print()

for i in range (1, 10):
    print("im student")

# kasus 2
def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol"

print("Kalkulator Sederhana")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == "1":
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    print("Hasil:", tambah(num1, num2))
elif pilihan == "2":
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    print("Hasil:", kurang(num1, num2))
elif pilihan == "3":
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    print("Hasil:", kali(num1, num2))
elif pilihan == "4":
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))
    print("Hasil:", bagi(num1, num2))
else:
    print("Pilihan tidak valid")


