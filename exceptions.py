class DuplicateStepException(Exception):
    def __init__(self, name):
        self.name = name
        self.message = 'Вы уже сделали ход!'
        super().__init__(self.message)