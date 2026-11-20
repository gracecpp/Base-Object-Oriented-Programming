class Rekening_Bank:
    def __init__(self, nama_nasabah, nomor_rekening, saldo):
        self.nama_nasabah = nama_nasabah
        self._nomor_rekening = nomor_rekening
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo 

    def setor_dana(self, rupiah):
        self.__saldo += rupiah
        return self.__saldo

    def tarik_dana(self, rupiah):
        if tarik_dana > 10000:
            self.__saldo -= rupiah
        else:
            print("Saldo tidak Cukup")
    

    def transfer_dana(self, rupiah):
        if transfer_dana > 10000: 
            self.__saldo -= rupiah
        else:
            print("Saldo tidak cukup") 
       
    @saldo.setter
    def saldo(self, saldo):
        if saldo > 0:
            self.__saldo = saldo
        else:
            raise ValueError("Nilai Saldo Tidak Valid")


    def get_saldo(self):
        return self.__saldo 


    def set_saldo(self, saldo):
        if saldo > 0:
            self.__saldo = saldo
        else:
            raise ValueError("Nilai Saldo Tidak Valid")
                

        
B1 = Rekening_Bank("Grace", 81207, 250000)

print(B1.saldo)
print(B1.get_saldo())
B1.set_saldo(-1000)
print(B1.get_saldo)


#tujuan : perbedaan pemanggilan antara property, get dan set

   