class Mobil:
    jumlah_mobil = 0
    semua_mobil = []

    def __init__ (self, merek, tahun, harga_sewa):
        self.merek = merek
        self.tahun = tahun
        self.harga_sewa = harga_sewa
        Mobil.jumlah_mobil += 1
        Mobil.semua_mobil.append(self)

    def hitung_sewa(self, biaya_sewa):
        total_sewa = self.harga_sewa * biaya_sewa 
        return total_sewa 
    

    @classmethod
    def mobil_str(cls, data):
        rata_sewa = data.split("---")
        return cls(rata_sewa)

    @classmethod
    def rata_sewa(cls):
        sum = 0
        for i in range(1, len(cls.semua_mobil)):
            sum += cls.semua_mobil[i].harga_sewa 
        rata_sewa = sum/len(cls.semua_mobil)
        return rata_sewa

    
    
mobil1 = Mobil("Toyota", 2002, 500)
mobil2 = Mobil("Honda",  2005, 300)
mobil3 = Mobil("Toyota", 2006, 200)

print(Mobil.rata_sewa())


   