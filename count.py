class Counter:
    def __init__(self, count = 0):
        self.count = count
    
    def tick(self):
        self.count = self.count + 1
        print(self.count)
    def reset(self):
        self.count = 0
        print(self.count)
        
Counters = Counter()

