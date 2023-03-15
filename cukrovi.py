class Cukrovi():

    def __init__(self, barva, tvar, vaha):
        self.barva = barva
        self.tvar = tvar
        self.vaha = vaha

    def __str__(self):
        return "Cukroví barvy {}, tvaru {} a váhy {} g".format(self.barva, self.tvar, self.vaha)
