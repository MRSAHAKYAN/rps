import unittest
from winner_definer import *

class TestChoice(unittest.TestCase):
    def test_greater(self):
        # Сильнее ли?
        choices = [
            {
                'first': Choice.ROCK,
                'second': Choice.SCISSORS,
            },
            {
                'first': Choice.SCISSORS,
                'second': Choice.PAPER,
            },
            {
                'first': Choice.PAPER,
                'second': Choice.ROCK,
            },   
        ]

        for choice in choices:
            self.assertGreater(choice['first'], choice['second'])
            self.assertLess(choice['second'], choice['first'])
            
    
    def test_less(self):
        # Слабее ли?
        choices = [
            {
                'first': Choice.ROCK,
                'second': Choice.ROCK,
            },
            {
                'first': Choice.SCISSORS,
                'second': Choice.SCISSORS,
            },
            {
                'first': Choice.PAPER,
                'second': Choice.PAPER,
            },   
        ]

        for choice in choices:
            self.assertLessEqual(choice['first'], choice['second'])

# print(Choice.PAPER)
# print(Choice.PAPER.value)
# print(Choice.PAPER.name)

if __name__ == "__main__":
    unittest.main()