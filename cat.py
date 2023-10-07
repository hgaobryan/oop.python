class Cat:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice
    
    def getname(self):
        print("name", self.name)
    
    def getvoice(self):
        print(f"con meo {self.name} keu {self.voice}")

c = Cat("tom","aaaaa")
c.getname()
c.getvoice()
        