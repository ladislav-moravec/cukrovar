from cukrovi import Cukrovi


class TovarnaNaCukrovi():

    @staticmethod
    def vyrob_jahodove():
        return Cukrovi("žlutá", "kulatý", 20)

    @staticmethod
    def vyrob_bananove():
        return Cukrovi("červená", "kulatý", 15)

    @staticmethod
    def vyrob_cokoladove():
        return Cukrovi("hnědá", "hranatý", 25)
