class Cat(object):
    """Виртуальная кошка"""
    
    def __init__(self, name):
        print("Родилась новая кошка!")
        self.name = name
        
    def talk(self):
        print(self.name, ": Мяу")