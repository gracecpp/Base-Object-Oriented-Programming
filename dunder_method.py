class Dataset:
    def __init__(self, nama_dataset):
        self.nama_dataset = nama_dataset
        self.daftar_data = []

    def tambah_data(self, lokasi):
        self.daftar_data.append(lokasi)
        return self.daftar_data

    def __len__(self):
        return len(self.daftar_data)

    def __getitem__(self, index):
        return self.daftar_data[index]

    def __str__(self):
        return f"{self.nama_dataset}  ({self.daftar_data})"

d1 = Dataset("Frekuensi Tempat yang di Kunjungi")
d1.tambah_data("Surabaya, Capyca")
d1.tambah_data("Bima, RM. Sabar Subur")
d1.tambah_data("Sragen, Soewatu")
d1.tambah_data("Ngawi, Desa Kebon")
d1.tambah_data("Tulungagung, Pantai Pacar")

print(len(d1)) 
print(d1[0])

print(str(d1))

for Dataset in d1:
    print(d1)



    