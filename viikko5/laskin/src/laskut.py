class Summa:
    def __init__(self, sovelluslogiikka, numero):
        self.sovelluslogiikka = sovelluslogiikka
        self.numero = numero

    def suorita(self):
        self.sovelluslogiikka.plus(self.numero())

class Erotus:
    def __init__(self, sovelluslogiikka, numero):
        self.sovelluslogiikka = sovelluslogiikka
        self.numero = numero

    def suorita(self):
        self.sovelluslogiikka.miinus(self.numero())

class Nollaus:
    def __init__(self, sovelluslogiikka, numero):
        self.sovelluslogiikka = sovelluslogiikka
        self.numero = numero

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, numero):
        self.sovelluslogiikka = sovelluslogiikka
        self.numero = numero

    def suorita(self):
        self.sovelluslogiikka.kumoa()