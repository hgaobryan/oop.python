class animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice
    def atri(self):
        pass
        
class dog(animal):
    def atri(self):
        print(f"con {self.name} keu {self.voice}")
        
class cat(animal):
    def atri(self):
        print(f"con {self.name} keu {self.voice}")
        
dogs = dog("buddy","wolffff")
cats = cat("kitty","meowww")

dogs.atri()
cats.atri()