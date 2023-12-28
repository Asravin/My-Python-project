class ResultHandler:
    def __init__(self) -> None:
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Результат: {}'.format(self.sequence, result))
    
