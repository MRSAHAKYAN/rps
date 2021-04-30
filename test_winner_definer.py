import unittest
from winner_definer import *

    
class TestWinnerDefiner(unittest.TestCase):
    def test_get_winners(self):
        situations = [
            {
                'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.ROCK,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.ROCK,
                    },
                    {
                        'name': 'Masha',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Yulia',
                        'choice': Choice.PAPER,
                    },
                ], 
                'expected': ['Masha', 'Yulia'],
            },
            {
                'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.ROCK,
                    },
                    {
                        'name': 'Masha',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Yulia',
                        'choice': Choice.PAPER,
                    },
                ], 
                'expected': ['Igor', 'Masha', 'Yulia'],
            },
            {
             'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.ROCK,
                    },
                ], 
                'expected': ['Igor'],
            },
            {
             'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.SCISSORS,
                    },
                ], 
                'expected': ['Artyom'],
            },
            {
             'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.SCISSORS,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.SCISSORS,
                    },
                ], 
                'expected': [],
            },
            {
             'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.ROCK,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.SCISSORS,
                    },
                ], 
                'expected': ['Igor'],
            },
            {
                'combinations': [
                    {
                        'name': 'Igor',
                        'choice': Choice.SCISSORS,
                    },
                    {
                        'name': 'Artyom',
                        'choice': Choice.ROCK,
                    },
                    {
                        'name': 'Masha',
                        'choice': Choice.PAPER,
                    },
                    {
                        'name': 'Yulia',
                        'choice': Choice.PAPER,
                    },
                ], 
                'expected': [],
            },
            
        ]
        
        for situation in situations:
            expected_names = situation['expected']
            winners = situation['combinations']
            self.assertEqual(set(expected_names), set(WinnerDefiner.get_winners(winners)))
        
        
# situations = [{'comb':{}, 'exp': [...]}, {'comb':{}, 'exp': [...]}]

if __name__ == "__main__":
    unittest.main()