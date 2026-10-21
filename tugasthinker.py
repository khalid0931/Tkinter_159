import tkinter as tk
from tkinter import ttk

def tampilkan_hasil():
    hasil_var.set("Hasil prediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Prediksi Program Studi")
root.geometry("520x600")
root.minsize(440, 500)

main = ttk.Frame(root, padding=24)
main.pack(fill="both", expand=True)

ttk.Label(
    main,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Segoe UI", 16, "bold"),
).pack(anchor="w", pady=(0, 6))

ttk.Label(
    main,
    text="Masukkan nilai untuk 10 mata pelajaran:",
).pack(anchor="w", pady=(0, 14))

form = ttk.Frame(main)
form.pack(fill="x")


