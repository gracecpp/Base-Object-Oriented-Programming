def hitung_perubahan(func):
    def wrapper(*args, **kwargs):
        JadwalKelas.total_perubahan += 1
        return func(*args, **kwargs)
    return wrapper

def hasil_boolean(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return bool(result)
    return wrapper

class JadwalKelas:
    total_jadwal = 0
    total_perubahan = 0
    durasi_maksimal = 240

    def __init__(self, mata_kuliah, hari, mulai, durasi, ruang):
        self.mata_kuliah = mata_kuliah
        self.hari = hari
        self.mulai = mulai
        self.ruang = ruang
        self.durasi = durasi  
        JadwalKelas.total_jadwal += 1

    @classmethod
    def dari_teks(cls, teks):
        mata_kuliah, hari, mulai, durasi, ruang = teks.split()
        mata_kuliah = mata_kuliah.replace('_', ' ')
        return cls(mata_kuliah, hari, mulai, int(durasi), ruang)

    @staticmethod
    def ruang_valid(kode):
        return kode.startswith("C") and kode[1:].isdigit() and len(kode[1:]) == 3

    @property
    def durasi(self):
        return self.__durasi

    @durasi.setter
    def durasi(self, nilai):
        if 30 <= nilai <= 240:
            self.__durasi = nilai
        else:
            raise ValueError("Durasi harus berada pada rentang 30 sampai 240.")

    @hitung_perubahan
    @hasil_boolean
    def ubah_durasi(self, tambahan):
        if tambahan > 0 and (self.durasi + tambahan) < JadwalKelas.durasi_maksimal:
            self.durasi = self.durasi + tambahan
            return True
        return False
     

    def kategori(self):
        if self.durasi <= 60:
            return "Singkat"
        elif 61 <= self.durasi <= 120:
            return "Normal"
        else:
            return "Panjang"

mata_kuliah, hari, mulai, durasi, ruang, tambahan = input().split()
teks = f"{mata_kuliah} {hari} {mulai} {durasi} {ruang}"
jadwal = JadwalKelas.dari_teks(teks)
berhasil = jadwal.ubah_durasi(tambahan=int(tambahan))

print(f"Mata Kuliah: {jadwal.mata_kuliah}")
print(f"Hari: {jadwal.hari}")
print(f"Mulai: {jadwal.mulai}")
print(f"Durasi: {jadwal.durasi}")
print(f"Kategori: {jadwal.kategori()}")
print(f"Ruang Valid: {JadwalKelas.ruang_valid(jadwal.ruang)}")
print(f"Perubahan Berhasil: {berhasil}")
print(f"Total Jadwal: {JadwalKelas.total_jadwal}")
print(f"Total Perubahan: {JadwalKelas.total_perubahan}")