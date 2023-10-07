class acc:
    def __init__(self, name, money = 100):
        self.name = name
        self.money = money

class inc(acc):
    def nap(self, moin):
        self.money = self.money + moin
        print(self.money)
    def rut(self, moout):
        if moout > self.money:
            print("not enough !!")
        else:
            self.money = self.money - moout 
            print(self.money)

baos = inc("bao")

baos.nap(200)
baos.rut(50)


