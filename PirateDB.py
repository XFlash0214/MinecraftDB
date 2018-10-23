class Pirate:
    name=""
    ship=""
    real=False

    def getDict(self):
        d={"name":self.name,
           "ship":self.ship,
           "real": self.real
           }
        return d
    def lfd(self,d):
        self.name=d["name"]
        self.ship=d["ship"]
        self.real=d["real"]
