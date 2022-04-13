class Product:

    def __init__(self,pid=0,prnm='',pqty=0,prc=0.0,pven=''):
        self.prodID=pid
        self.proName=prnm
        self.ProdPrice=prc
        self.prodQty=(pqty)
        self.ProduVendor=pven

    def __str__(self):
        return f"""{self.__dict__}"""

    def __repr__(self):
        return str(self)




