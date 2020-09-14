#8-12 一個簡單的類別,說明可變預設值的危險

class Bus:
    """A bus model haunted by ghost passengers"""
    def __init__(self,passengers = []):
            self.passengers = passengers 
    
    def pick(self,name):
        self.passengers.append(name)
    
    def drop(self,name):
        self.passengers.remove(name)

