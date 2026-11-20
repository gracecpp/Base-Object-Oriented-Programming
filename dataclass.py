from dataclasses import dataclass

@dataclass
class Produk:
    id_produk: int
    nama: str
    harga: float
    stok: int
    terjual: int
    tags: str

    def info_produk(self):
        return f"{self.id_produk} | {self.nama} | {self.harga} | {self.stok} | {self.terjual} | {self.tags}"

    def tambah_stok(self, jumlah):
        return self.stok + jumlah

    def jual(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            self.terjual += jumlah
        return self.stok, self.terjual

    def total_penjualan(self):
        return self.terjual * self.harga


@dataclass
class ProdukDigital(Produk):
    merek: str
    garansi: str


@dataclass
class ProdukFashion(Produk):
    ukuran: str
    bahan: str


p1 = ProdukDigital(1, "Laptop", 1000, 10, 1, "elektronik, pc", "Asus", "2 tahun")
p2 = ProdukFashion(2, "Kaos", 20, 50, 5, "pakaian", "L", "Katun")

print(p1.tambah_stok(5))
print(p1.info_produk())
print(p1.total_penjualan())