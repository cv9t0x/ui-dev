from calculator.main import Calculator


class App:
    def __init__(self, root):
        self.root = root
        calculator = Calculator(self.root, 0, 0)
