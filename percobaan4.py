import tkinter as tk
from tkinter import messagebox
from queue import Queue

# Inisialisasi queue untuk sistem login
login_queue = Queue()

# Daftar user valid
valid_users = {"admin": "admin123", "user1": "password1", "user2": "password2"}

# Data soal (list untuk menyimpan soal kuis)
soal_kuis = [
    {
        "soal": "Apa ibu kota Indonesia?",
        "opsi": ["Jakarta", "Surabaya", "Bandung"],
        "jawaban": 0
    },
    {
        "soal": "Berapa hasil dari 5 + 3?",
        "opsi": ["6", "8", "10"],
        "jawaban": 1
    },
    {
        "soal": "Siapa penemu lampu pijar?",
        "opsi": ["Nikola Tesla", "Albert Einstein", "Thomas Edison"],
        "jawaban": 2
    },
    ]

# Fungsi untuk menambahkan user ke queue
def enqueue_login():
    username = input_username.get()
    password = input_password.get()

    # Tambahkan data login ke dalam queue
    login_queue.put((username, password))
    process_login_queue()  # Proses antrean login

# Fungsi untuk memproses queue login
def process_login_queue():
    if not login_queue.empty():
        username, password = login_queue.get()  # Ambil user dari antrean
        if username in valid_users and valid_users[username] == password:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
            login_frame.pack_forget()
            main_menu_frame.pack()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")
    else:
        messagebox.showinfo("Info", "Antrean login kosong.")

# Fungsi untuk tambah soal
def tambah_soal():
    soal = input_soal.get()
    opsi = [input_opsi1.get(), input_opsi2.get(), input_opsi3.get()]
    jawaban = var_jawaban.get()

    if not soal or not all(opsi) or jawaban == "":
        messagebox.showerror("Error", "Semua field harus diisi!")
        return

    try:
        jawaban = int(jawaban)
        if jawaban < 0 or jawaban > 2:
            raise ValueError
        soal_kuis.append({"soal": soal, "opsi": opsi, "jawaban": jawaban})
        messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")
        bersihkan_form_soal()
    except ValueError:
        messagebox.showerror("Error", "Jawaban benar harus berupa indeks 0, 1, atau 2!")

# Fungsi untuk hapus soal
def hapus_soal():
    try:
        indeks = int(input_indeks.get())
        if indeks < 0 or indeks >= len(soal_kuis):
            raise IndexError
        soal_kuis.pop(indeks)
        messagebox.showinfo("Sukses", "Soal berhasil dihapus!")
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Indeks soal tidak valid!")

# Fungsi untuk membersihkan form tambah soal
def bersihkan_form_soal():
    input_soal.delete(0, tk.END)
    input_opsi1.delete(0, tk.END)
    input_opsi2.delete(0, tk.END)
    input_opsi3.delete(0, tk.END)
    var_jawaban.set("")

# Fungsi untuk mulai kuis
def mulai_kuis():
    if not soal_kuis:
        messagebox.showerror("Error", "Belum ada soal yang tersedia!")
        return
    main_menu_frame.pack_forget()
    tampilkan_soal(0, 0)

# Fungsi rekursif untuk menampilkan soal
def tampilkan_soal(indeks, skor):
    if indeks == len(soal_kuis):  # Basis rekursi
        messagebox.showinfo("Kuis Selesai", f"Skor Anda: {skor}")
        main_menu_frame.pack()
        return

    kuis_frame.pack()
    lbl_soal.config(text=f"Soal {indeks + 1}: {soal_kuis[indeks]['soal']}")
    for i, btn in enumerate(opsi_button):
        btn.config(text=soal_kuis[indeks]["opsi"][i], 
                   command=lambda i=i: cek_jawaban(indeks, skor, i))

# Fungsi untuk cek jawaban
def cek_jawaban(indeks, skor, opsi_dipilih):
    if opsi_dipilih == soal_kuis[indeks]["jawaban"]:
        skor += 1
    kuis_frame.pack_forget()
    tampilkan_soal(indeks + 1, skor)

# Inisialisasi GUI
root = tk.Tk()
root.geometry("800x600")  # Mengatur ukuran window sesuai modul
root.title("Aplikasi Kuis Sederhana")  # Judul aplikasi utama

# Frame Login
login_frame = tk.Frame(root)
tk.Label(login_frame, text="Selamat Datang di Aplikasi Kuis", font=("Arial", 16)).pack(pady=10)
tk.Label(login_frame, text="Silakan Login untuk Melanjutkan", font=("Arial", 12)).pack(pady=5)
tk.Label(login_frame, text="Username:").pack()
input_username = tk.Entry(login_frame)
input_username.pack()
tk.Label(login_frame, text="Password:").pack()
input_password = tk.Entry(login_frame, show="*")
input_password.pack()
tk.Button(login_frame, text="Login", command=enqueue_login).pack(pady=10)
login_frame.pack()

# Frame Menu Utama
main_menu_frame = tk.Frame(root)
tk.Label(main_menu_frame, text="Menu Utama", font=("Arial", 16)).pack(pady=10)
tk.Button(main_menu_frame, text="Tambah Soal", command=lambda: tambah_soal_frame.pack()).pack(pady=5)
tk.Button(main_menu_frame, text="Mulai Kuis", command=mulai_kuis).pack(pady=5)
tk.Button(main_menu_frame, text="Keluar", command=root.quit).pack(pady=5)

# Frame Tambah Soal
tambah_soal_frame = tk.Frame(root)
tk.Label(tambah_soal_frame, text="Tambah atau Hapus Soal", font=("Arial", 16)).pack(pady=10)
tk.Label(tambah_soal_frame, text="Masukkan Soal:").pack()
input_soal = tk.Entry(tambah_soal_frame)
input_soal.pack()
tk.Label(tambah_soal_frame, text="Opsi 1:").pack()
input_opsi1 = tk.Entry(tambah_soal_frame)
input_opsi1.pack()
tk.Label(tambah_soal_frame, text="Opsi 2:").pack()
input_opsi2 = tk.Entry(tambah_soal_frame)
input_opsi2.pack()
tk.Label(tambah_soal_frame, text="Opsi 3:").pack()
input_opsi3 = tk.Entry(tambah_soal_frame)
input_opsi3.pack()
tk.Label(tambah_soal_frame, text="Jawaban Benar (0/1/2):").pack()
var_jawaban = tk.StringVar()
input_jawaban = tk.Entry(tambah_soal_frame, textvariable=var_jawaban)
input_jawaban.pack()
tk.Button(tambah_soal_frame, text="Tambah Soal", command=tambah_soal).pack(pady=5)
tk.Label(tambah_soal_frame, text="Indeks Soal untuk Dihapus:").pack()
input_indeks = tk.Entry(tambah_soal_frame)
input_indeks.pack()
tk.Button(tambah_soal_frame, text="Hapus Soal", command=hapus_soal).pack(pady=5)
tk.Button(tambah_soal_frame, text="Kembali", command=lambda: tambah_soal_frame.pack_forget()).pack(pady=10)

# Frame Kuis
kuis_frame = tk.Frame(root)
tk.Label(kuis_frame, text="Kuis Sedang Berlangsung", font=("Arial", 16)).pack(pady=10)
lbl_soal = tk.Label(kuis_frame, text="", font=("Arial", 14))
lbl_soal.pack(pady=10)
opsi_button = [tk.Button(kuis_frame) for _ in range(3)]
for btn in opsi_button:
    btn.pack(pady=5)

root.mainloop()
