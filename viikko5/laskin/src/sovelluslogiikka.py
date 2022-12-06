class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.kumoa = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo
        self.kumoa = self.tulos

    def plus(self, arvo):
        self.tulos = self.tulos + arvo
        self.kumoa = self.tulos

    def nollaa(self):
        self.tulos = 0
        self.kumoa = self.tulos

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        self.kumoa = self.tulos
