class user:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

        self.nilai = []

    def login(self):
        print(f"masukan email : {self.email}")
        print(f"Anda Sudah Masuk")

    def logout(self):
        print(f"{self.email} anda sudah logout")

class Dosen(user):
    def __init__(self, nama, email, nip, matkul_diajar):
        super().__init__(nama, email)
        self.nip = nip
        self.matkul_diajar = matkul_diajar

    def tampilkan_nama(self):
        print(f"{self.nama}")

    def tampilkan_nip(self):
        print(f"NIP : {self.nip}")

    def login(self):
        super().login()
        print(f"Selamat Datang {self.nama}")

    def logout(self):
        super().logout()
        print("Anda sudah logout")

    def input_nilai(self):
        print(f"Nilai anda : {self.nilai}")

    def matkul_ajar(self):
        print(f"{self.matkul_diajar}")

class Mahasiswa(user):
    def __init__(self, nama, email, nim, matkul_diambil, nilai):
        super().__init__(nama, email)
        self.nim = nim
        self.matkul_diambil = matkul_diambil 
        self.nilai = nilai

    def login(self):
        super().login()
        print(f"Selamat Datang {self.nama}")

    def logout(self):
         super().login()
         print("Anda sudah logout")

    def cek_nilai(self):
         print(F"Nilai anda adalah {self.nilai}")

    def cek_matkul(self):
        print(f"Matkul yang diambil adalah : {self.matkul}")

pengajar = Dosen("dr. Grace", "grace@gmail", 1122334455667788990, "matematika")
M1 = Mahasiswa("Sora", "soraya@gmail", 99887766550, "aljabar matriks", 90)


pengajar.tampilkan_nip()
pengajar.login()
M1.cek_nilai()


    



