KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def alkio_kuuluu_listaan(self, alkio):
        return alkio in self.lista


    def lisaa(self, alkio):
        if not self.alkio_kuuluu_listaan(alkio):
            self.lista[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.lista):
                self.uusi_lista()
            return True

        return False
    
    def uusi_lista(self):
            kopio = self.kopioi_lista()
            self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            for i in range(len(kopio)):
                self.lista[i]=kopio[i]

    def poista(self, alkio):
        if self.alkio_kuuluu_listaan(alkio):
            self.lista.remove(alkio)
            self.lista.append(0)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self):
        return self.lista.copy()

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lista[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        x.lista = a_taulu + b_taulu
        x.alkioiden_lkm = len(a_taulu) + len(b_taulu)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if a_taulu[i] in b_taulu:
                    y.lisaa(a_taulu[i])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            if not b.alkio_kuuluu_listaan(a_taulu[i]):
                z.lisaa(a_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{" + str(", ".join([str(numero) for numero in self.lista[:self.alkioiden_lkm]])) + "}"
        return tuotos
