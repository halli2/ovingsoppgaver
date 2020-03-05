import unittest
from sprite import *

class SpriteTest(unittest.TestCase):
    def test_sprite(self):
        sprite1 = Sprite(1, 1, 1, 1)
        self.assertEqual(sprite1.x_start, 1)
        self.assertEqual(sprite1.y_start, 1)
        self.assertEqual(sprite1.bredde, 1)
        self.assertEqual(sprite1.hoyde, 1)
    
    # Tester at det ikke kan settes negativ bredde men 0 og positiv går.
    def test_bredde(self):
        with self.assertRaises(ValueError):
            sprite1 = Sprite(1, 1, -1, 1)
        
        sprite1 = Sprite(1, 1, 1, 1)
        sprite1.bredde = 10
        self.assertEqual(sprite1.bredde, 10)
        sprite1.bredde = 0
        self.assertEqual(sprite1.bredde, 0) # Fikk ValueError: Bredde kan ikke være negativ! byttet > til >=
        with self.assertRaises(ValueError):
            sprite1.bredde = -1

    def test_hoyde(self):
        with self.assertRaises(ValueError): # Fikk IKKE ValueError, lagde getter og setter for høyde i sprite.py
            sprite1 = Sprite(1, 1, 1, -1)
        
        sprite1 = Sprite(1, 1, 1, 1)
        sprite1.hoyde = 10
        self.assertEqual(sprite1.hoyde, 10)
        sprite1.hoyde = 0
        self.assertEqual(sprite1.hoyde, 0) 
        with self.assertRaises(ValueError):
            sprite1.hoyde = -1

    # Tester at den kan være "hvilket som helst tall"
    def test_x_y_start(self):
        sprite = Sprite(22.2, 43.62, 10 ,10)
        self.assertEqual(sprite.x_start, 22.2)
        self.assertEqual(sprite.y_start, 43.62)
        sprite.x_start = -42.2
        sprite.y_start = -3
        self.assertEqual(sprite.x_start, -42.2)
        self.assertEqual(sprite.y_start, -3)

    def test_id(self):
        sprite = Sprite(2, 2, 2, 2)
        with self.assertRaises(AttributeError):
            sprite.id = 33 # Fikk ingen error som vil si at den kunne endres. Lager read-only property for self.id i sprite klassen
        
    def test_areal(self):
        sprite = Sprite(2,2,2,2)
        self.assertEqual(sprite.areal(), 4)
        sprite2 = Sprite(2, 2, 3.3, 4.4)
        self.assertEqual(sprite2.areal(), 14.52)
    
    def test_er_inni(self):
        sprite = Sprite(2, 2, 2, 2)
        self.assertEqual(sprite.er_inni(3, 3), True)
        self.assertEqual(sprite.er_inni(2, 2), True)
        self.assertEqual(sprite.er_inni(4.0, 4.0), True)
        self.assertEqual(sprite.er_inni(1.99, 1.99), False)
        self.assertEqual(sprite.er_inni(5, 5), False)

    def test_flytt(self):
        sprite = Sprite(2,2,2,2)
        sprite.flytt(2, 2)
        self.assertEqual(sprite.x_start, 4) # Fikk "AssertionError: 6 != 4" Så at flyttfunksjonen hadde self.x_start += for begge inputtene, byttet den siste til y_Start
        self.assertEqual(sprite.y_start, 4)
        sprite.flytt(2, 3)
        self.assertEqual(sprite.x_start, 6)
        self.assertEqual(sprite.y_start, 7)

    def test_x_y_slutt(self):
        sprite = Sprite(4,6,4,6)
        self.assertEqual(sprite.y_slutt(), 12)
        self.assertEqual(sprite.x_slutt(), 8)
        sprite.x_start = -10.0
        sprite.y_start = -12.0
        self.assertEqual(sprite.y_slutt(), -6)
        self.assertEqual(sprite.x_slutt(), -6)



if __name__ == "__main__":
    unittest.main()
