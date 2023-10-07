class welcome:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print("hello", self.name)
    
    def getage(self):
        print("age", self.age)
        
a = welcome("bao","16")
a.hello()
a.getage()

print('hi')
       