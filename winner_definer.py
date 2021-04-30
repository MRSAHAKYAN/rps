import enum
from functools import total_ordering


@total_ordering
class Choice(enum.Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    
    @property
    def beats(self):
        return list(Choice)[self.value - 1]  # [2] => [1]
       
    def __gt__(self, other): 
        # Choice.SCISSORS.beats => Choice.PAPER
        if self.__class__ is other.__class__:
            return self.beats == other
            
        return NotImplemented 
    
    # def __gt__(self, other): 
    #     #? rock > scissors
    #     #? paper > rock
    #     #? scissors > paper
    #     if self.__class__ is other.__class__:
    #         # import ipdb; ipdb.set_trace()
    #         rock_win = (self.value == Choice.ROCK.value and other.value == Choice.SCISSORS.value)
    #         paper_win = (self.value == Choice.PAPER.value and other.value == Choice.ROCK.value)
    #         scissors_win = (self.value == Choice.SCISSORS.value and other.value == Choice.PAPER.value) 
    #         win = rock_win and paper_win and scissors_win
    #         return win
    #     return NotImplemented
      

class WinnerDefiner:
    @staticmethod
    def get_winners(results):
        # set([б б б б]) => {б} > 2
        # set([к к н н]) => {к н}
        choices = {result['choice'] for result in results}
        # choices = {Choice.ROCK, Choice.PAPER}
        
        #! Пусто, потому что изначально мы считаем, что результат сравнения - ничья
        winners = []
        if len(choices) == 2:
            strongest_choice = max(choices)
            winners = [result['name'] for result in results if result['choice'] == strongest_choice]
        return winners 
            # mas = [5, 2, 6, 3, 8, 34, 89, 2]
            # max(mas) => 5 > 2 > 6 > 3.... > - __gt__

            # choice1 > choice2
            # choice1.__gt__(choice2)
            # set([1, 2, 3, 4, 4, 4, 4]) => list({1, 2, 3, 4}) => [1, 2, 3, 4]
            #         Игра началась 
            # 1) люди выбрали жесты и показывают
            # 2) если только два жеста, то выявить победа, иначе ничья
