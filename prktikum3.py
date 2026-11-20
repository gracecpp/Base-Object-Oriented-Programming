class Pembayaran:
    total_verifikasi = 0

    def __init__(self, nama, nominal):
        self.nama = nama
        self.nominal = nominal

    def ringkasan(self):
        # TODO: kembalikan teks "<nama> membayar <nominal>"
        pass

    @classmethod
    def jumlah_verifikasi(cls):
        # TODO: kembalikan nilai class attribute total_verifikasi melalui cls
        pass

    @staticmethod
    def nominal_wajar(nominal):
        # TODO: kembalikan True jika nominal lebih besar dari nol
        pass


# Program utama
pembayaran = Pembayaran("Budi", 150000)
print(pembayaran.ringkasan())
print(Pembayaran.jumlah_verifikasi())
print(Pembayaran.nominal_wajar(150000))
print(Pembayaran.nominal_wajar(0))
# Output yang diharapkan:
# Budi membayar 150000
# 0
# True
# False
