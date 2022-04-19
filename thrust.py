import math

class thrusteq:
    def __init__(self, me, mo, ve, vo, pe, po, ae):
        self.me = me
        self.mo = mo
        self.ve = ve
        self.vo = vo
        self.pe = pe
        self.po = po
        self.ae = ae
    def general(self):
        f = (self.me*self.ve) - (self.mo*self.vo)
        if self.pe!= self.po:
            f = ((self.me*self.ve) - (self.mo*self.vo)) + ((self.pe - self.po) * self.ae)
        print(f)

a = thrusteq(25,15,19,10,9,9,16)
a.general()