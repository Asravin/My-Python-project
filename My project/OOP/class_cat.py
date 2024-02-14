class Cat(object):
    """Виртуальная кошка"""
    total = 0
    @staticmethod
    
    def count():
        print("Всего кошек: ", Cat.total)
    
    def __init__(self, name):
        print("Родилась новая кошка!")
        self.name = name
        Cat.total += 1
        
    def __str__(self):
        res = "Объект класса Cat\n name: " + self.name
        return res
        
    def talk(self):
        print(self.name, ": Мяу")