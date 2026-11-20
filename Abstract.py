from abc import ABC, abstractmethod

class Pengiriman(ABC):
    def __init__(self, nama_layanan, berat):
        self.nama_layanan = nama_layanan
        self.berat = berat

    def tampilkan_info(self):
        return (f"{self.nama_layanan} {self.berat}")
    
    @abstractmethod 
    def hitung_biaya(self):
        pass

    @abstractmethod
    def estimasi_hari(self):
        pass


class Reguler(Pengiriman):
    def hitung_biaya(self):
        return self.berat * 8000

    def estimasi_hari(self):
        return "3 sampai dengan 5 hari"

class Express(Pengiriman):
    def hitung_biaya(self):
        return self.berat * 15000

    def estimasi_hari(self):
        return "1 sampai 2 hari"

class SameDay(Pengiriman):
    def hitung_biaya(self):
        return self.berat * 25000

    def estimasi_hari(self):
        return "1 hari"


Gudang1 = Reguler("JNE", 10)
Gudang2 = Express("JNT", 5)
Gudang3 = SameDay("TIKI", 2)

print(Gudang1.hitung_biaya())
print(Gudang1.tampilkan_info())
print(Gudang1.estimasi_hari())

print(Gudang2.hitung_biaya())
print(Gudang2.tampilkan_info())
print(Gudang2.estimasi_hari())

print(Gudang3.hitung_biaya())
print(Gudang3.tampilkan_info())
print(Gudang3.estimasi_hari())




