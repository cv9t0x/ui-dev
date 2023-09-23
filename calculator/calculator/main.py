from .model import CalculatorModel
from .view import CalculatorView
from .controller import CalculatorController


class Calculator:
    def __init__(self, parent, x, y):
        model = CalculatorModel()
        controller = CalculatorController(model, None)
        view = CalculatorView(parent, controller, x, y)
        controller.view = view
