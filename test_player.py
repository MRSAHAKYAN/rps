import unittest
from player import *

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        cases = [
            {
                'name': 'Artyom', 
                'expected': 'Artyom',                     
            },
            {
                'name': 'Lusya', 
                'expected': 'Lusya', 
            },
            {
                'name': 'Igor',
                'expected': 'Igor',   
            },
            
        ]

        for case in cases:
            player = Player(case['name'])
            
            self.assertEqual(case['expected'], player.get_name())
        

if __name__ == "__main__":
    unittest.main()
        