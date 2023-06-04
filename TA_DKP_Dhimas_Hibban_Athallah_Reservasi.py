import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, timedelta
from tkinter import ttk
from tkinter import messagebox
import re

class NewWindow:
    def __init__(self, parent, data_stack):
        self.parent = parent
        self.data_stack = data_stack

        self.new_window = tk.Tk()
        self.new_window.title("Reservasi")
        self.new_window.geometry("600x400")
        self.new_window.configure(bg="#00E1E1")  # Mengatur latar belakang window

        new_label = tk.Label(self.new_window, text="INFORMASI MENGENAI KAPASITAS MEJA YANG TERSEDIA\n______________________________________________________________________________________________________________________")
        new_label.pack()
        label2 = tk.Label(self.new_window, justify="left", font=("times new roman", 10), text="Berikut adalah kapasitas yang disediakan: \n \n1.) Meja berkapasitas 2 orang =====> Rp 400.000 \n \n2.)Meja berkapasitas 4 orang =====> Rp 750.000 \n \n3.)Meja berkapasitas 6 orang =====> Rp 1.100.000 \n \n4.)Private table(+8 orang) =====> Rp 2.850.000 ",bg = "#00E1E1")
        label2.pack()
        input_frame = ttk.Frame(self.new_window)
        input_frame.pack(padx=15, pady=15, fill="x", expand=True)

        Pilihan_label = ttk.Label(input_frame, text="Pilihlah nomor sesuai pilihan anda")
        Pilihan_label.pack(padx=15, fill="x", expand=True)
        self.Pilihan = tk.StringVar()
        pilihan_entry = ttk.Entry(input_frame, textvariable=self.Pilihan)
        pilihan_entry.pack(padx=25, fill="x", expand=True)

        # Tanggal
        tanggal_label = ttk.Label(input_frame, text="Tanggal reservasi: (YY/MM/DD)")
        tanggal_label.pack(padx=15, fill="x", expand=True)
        self.Tanggal = tk.StringVar()
        tanggal_entry = ttk.Entry(input_frame, textvariable=self.Tanggal)
        tanggal_entry.pack(padx=15, fill="x", expand=True)

        submit_button = tk.Button(self.new_window, text="Submit", command=self.Message)
        submit_button.pack(pady=30)

        view_data_button = tk.Button(self.new_window, text="Lihat Data", command=self.view_data)
        view_data_button.pack()

    def Message(self):
        tanggal = self.Tanggal.get()
        pilihan = self.Pilihan.get()

        if not tanggal:
            messagebox.showerror("Error", "Tanggal reservasi harus diisi")
            return
        if not pilihan.isdigit():
            messagebox.showerror("Error", "Pilihan harus berupa angka")
            return
        if int(pilihan) > 4:
            messagebox.showerror("Error", "Pilihan tidak valid")
            return

        self.data_stack.append({
            "NAMA": self.parent.NAMA.get(),
            "NoHp": self.parent.Nohp.get(),
            "Email": self.parent.Email.get(),
            "KTP": self.parent.KTP.get(),
            "Tanggal": tanggal,
            "Pilihan": pilihan
        })
        messagebox.showinfo("Informasi lanjutan", "Reservasi anda telah dikonfirmasi\n======================================\nTerimakasih " + str(self.parent.NAMA.get()) + " telah reservasi disini pada tanggal " +str(self.Tanggal.get()) + " kami tunggu kedatangan nya :) ")

        # Tambahkan perintah untuk menutup jendela setelah menambahkan data ke stack

    def view_data(self):
        data_str = ""
        for data in self.data_stack:
            data_str += f"NAMA: {data['NAMA']}\n"
            data_str += f"No HP: {data['NoHp']}\n"
            data_str += f"Email: {data['Email']}\n"
            data_str += f"KTP: {data['KTP']}\n"
            data_str += f"Tanggal: {data['Tanggal']}\n"
            data_str += f"Pilihan: {data['Pilihan']}\n\n"

        if data_str == "":
            messagebox.showinfo("Data", "Tidak ada data yang tersedia")
        else:
            messagebox.showinfo("Data", data_str)
    

class ReservasiApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        self.window.title("Reservasi")
        bg_color1 = "#00E1E1"
        self.window.configure(bg=bg_color1)

        label = tk.Label(self.window, text="SELAMAT DATANG DI APLIKASI RESERVASI RESTORAN\n   \nisilah biodata terlebih dahulu untuk melakukan reservasi\n______________________________________________________________________________________________________________________")
        label.pack()

        self.data_stack = []

        input_frame = ttk.Frame(self.window)
        input_frame.pack(padx=15, pady=15, fill="x", expand=True)
        bg_color1 = ("#00E1E1")

        # NAMA
        nama_pereservasi_label = ttk.Label(input_frame, text="Nama lengkap peresrvasi:")
        nama_pereservasi_label.pack(padx=15, fill="x", expand=True)
        self.NAMA = tk.StringVar()
        nama_entry = ttk.Entry(input_frame, textvariable=self.NAMA)
        nama_entry.pack(padx=15, fill="x", expand=True)

        # NoHp
        Nohp_label = ttk.Label(input_frame, text="Nomor Handphone peresrvasi:")
        Nohp_label.pack(padx=15, fill="x", expand=True)
        self.Nohp = tk.StringVar()
        Nohp_entry = ttk.Entry(input_frame, textvariable=self.Nohp)
        Nohp_entry.pack(padx=15, fill="x", expand=True)

        # Email
        email_label = ttk.Label(input_frame, text="Email peresrvasi:")
        email_label.pack(padx=15, fill="x", expand=True)
        self.Email = tk.StringVar()
        email_entry = ttk.Entry(input_frame, textvariable=self.Email)
        email_entry.pack(padx=15, fill="x", expand=True)

        # KTP
        KTP_label = ttk.Label(input_frame, text="Nomor KTP peresrvasi:")
        KTP_label.pack(padx=15, fill="x", expand=True)
        self.KTP = tk.StringVar()
        KTP_entry = ttk.Entry(input_frame, textvariable=self.KTP)
        KTP_entry.pack(padx=15, fill="x", expand=True)

        submit_button = tk.Button(self.window, text="Submit", command=self.submit_reservation)
        submit_button.pack(pady=30)

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def submit_reservation(self):
        NAMA = self.NAMA.get()
        NoHp = self.Nohp.get()
        Email = self.Email.get()
        KTP = self.KTP.get()

        if len(NoHp) != 12 and len(NoHp) != 10:
            messagebox.showerror("Error", "Nomor HP anda tidak valid")
            return
        if not self.validate_email(Email):
            messagebox.showerror("Error", "Email anda tidak valid")
            return
        self.window.destroy()
        self.open_new_window()

    def open_new_window(self):
        new_window = NewWindow(self, self.data_stack)
        new_window.new_window.mainloop()



    def run(self):
        self.window.mainloop()


app = ReservasiApp()
app.run()
