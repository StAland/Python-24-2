import unittest
from zutat import Zutat
from kategorie import Kategorie

class TestZutat(unittest.TestCase):
    
    def test_zutat_erstellung(self):
        lachs = Zutat("Lachs", Kategorie.PROTEIN)
        self.assertEqual(lachs.name, "Lachs")
        self.assertEqual(lachs.kategorie, Kategorie.PROTEIN)




