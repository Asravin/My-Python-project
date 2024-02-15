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
        self.__w = 1
        
    def __str__(self):
        res = "Объект класса Cat\n name: " + self.name + "/nBec:" + str(self.__w)
        return res
        
    def talk(self):
        print(self.name, ": Мяу")
    
    @property
    def name(self):
        return self.__name
    @name.setter
    
    def name(self, new_name):
        if new_name == "":
            print("Укажите имя кошки!")
        else:
            self.__name = new_name
            print("Новое имя: ", self.__name)