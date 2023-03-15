from tovarna_na_cukrovi import TovarnaNaCukrovi


for i in range(5):
    cukrovi = TovarnaNaCukrovi.vyrob_bananove()
    print(cukrovi)


for i in range (8):
    print(TovarnaNaCukrovi.vyrob_jahodove())


for i in range(12):
    cukrovi = TovarnaNaCukrovi.vyrob_cokoladove()
    print(cukrovi)

