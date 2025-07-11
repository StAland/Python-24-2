from kategorie import Kategorie

class Zutat:
    def __init__(self, name: str, kategorie: Kategorie, naehrwert: int):
        if not name or not name.strip():
            raise ValueError("Der Name der Zutat darf nicht leer sein.")
        if not isinstance(kategorie, Kategorie):
            raise ValueError("Die Kategorie muss ein gueltiger Kategorie-Wert sein.")

        self.__name = name.strip()
        self.__kategorie = kategorie
        self.__naehrwert = naehrwert

    def __str__(self):
        return f"{self.name} ({self.kategorie.value})"
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Der Name der Zutat darf nicht leer sein.")
        self.__name = value.strip()

    @property
    def kategorie(self) -> Kategorie:
        return self.__kategorie

    @kategorie.setter
    def kategorie(self, value):
        if not isinstance(value, Kategorie):
            raise ValueError("Die Kategorie muss ein gueltiger Kategorie-Wert sein.")
        self.__kategorie = value
        
    @property
    def naehrwert(self):
        return self.__naehrwert

    @naehrwert.setter
    def naehrwert(self, value):      
        self.__naehrwert = value

