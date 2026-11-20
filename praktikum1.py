class Buku:
    total_koleksi = 0
    maksimal_progress = 100

    def __init__(self, judul, kategori, halaman, progres_awal=0):
        self.judul = judul
        self.kategori = kategori
        self.__halaman = halaman
        self._Buku__progres = progres_awal 

        Buku.total_koleksi += 1


    @property
    def halaman(self):
        return self.__halaman 
    
    @halaman.setter
    def halaman(self, nilai):
        halaman_baru = nilai
        if halaman_baru >= 1:
            self.__halaman = halaman_baru
        else:
            raise ValueError("Jumlah halaman harus lebih besar dari 0.")
        return self.__halaman

    @property
    def progres(self):
        return self._Buku__progres

    @progres.setter
    def progres(self, nilai):
        if 0 <= nilai <= 100:
            self._Buku__progres = nilai
        elif 0 > nilai:
            raise ValueError("Progres tidak boleh kurang dari 0.")
        elif nilai > 100:
            raise ValueError("Progres tidak boleh lebih dari 100.")
        else:
            raise ValueError("Progres harus berada di antara 0 dan 100.") 
     

    def baca(self, persen):
        if persen <= 0:
            return False
            
        progress_baru = self._Buku__progres + persen
        
        if progress_baru > 100:
            return False
        
        self._Buku__progres = progress_baru
        return True

    def halaman_tersisa(self):
        return self.__halaman * (100 - self._Buku__progres) // 100        

    def status(self):
        if self._Buku__progres == 100:
            return "Selesai"
        elif self._Buku__progres == 0:
            return "Belum Dibaca"
        elif 0 < self._Buku__progres < 100:
            return "Dibaca"
        return "Status tidak valid"

    @classmethod
    def get_total_koleksi(cls):
        return cls.total_koleksi
      

judul, kategori, halaman, progres_awal, tambahan = input().split()
buku = Buku(judul.replace("_", " "), kategori, int(halaman), int(progres_awal))
berhasil = buku.baca(int(tambahan))

print(f"Judul: {buku.judul}")
print(f"Kategori: {buku.kategori}")
print(f"Halaman: {buku.halaman}")
print(f"Progres: {buku.progres}")
print(f"Status: {buku.status()}")
print(f"Halaman Tersisa: {buku.halaman_tersisa()}")
print(f"Total Koleksi: {Buku.total_koleksi}")