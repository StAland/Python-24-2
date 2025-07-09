
class Zutat:
    def __init__(self, name):
        self.__name = name  # Das _ zeigt: "Bitte nicht direkt anfassen"

    def get_name(self):
        return self.__name

    def set_name(self, neuer_name):
        if not neuer_name:
            raise ValueError("Name darf nicht leer sein.")
        self.__name = neuer_name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, neuer_name):
        if not neuer_name:
            raise ValueError("Name darf nicht leer sein.")
        self.__name = neuer_name
        
    
z = Zutat("Tofu")
print(z.name)
z.name = "Seitan"
print(z.name)