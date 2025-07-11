from zutat import Zutat
from kategorie import Kategorie

def main():
    zutaten = [
        Zutat("Haehnchen", Kategorie.PROTEIN, 12),
        Zutat("Reis", Kategorie.SAETTIGUNGSBEILAGE, 7),
        Zutat("Brokkoli", Kategorie.GEMUESE, 9),
        Zutat("Tofu", Kategorie.PROTEIN, 15)
    ]

    proteine = list(filter(lambda zutat: zutat.kategorie == Kategorie.PROTEIN, zutaten))
    print(proteine)



def filter_zutaten(zutaten, filterfunktion):
    proteine = []
    for zutat in zutaten:
        if filterfunktion(zutat):
            proteine.append(zutat)
    return proteine

def is_protein(zutat):
    return zutat.kategorie == Kategorie.PROTEIN

def is_naehrwert_kleiner14(zutat):
    return zutat.naehrwert < 14;

main()
        
    
