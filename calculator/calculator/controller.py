import math


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def buttonClicked(self, label):
        if label == "%":
            self.calculatePercent()
        elif label == "С" or label == "CE":
            self.clear()
        elif label == "\u00D7":
            self.backspace()
        elif label == "1/x":
            self.calculateReciprocal()
        elif label == "x^2":
            self.calculateSquare()
        elif label == "√x":
            self.calculateSqrt()
        elif label == "=":
            self.calculate()
        elif label == "+/-":
            self.toggleSign()
        elif label == ".":
            self.addDecimalPoint()
        else:
            self.appendToExpression(label)

    def calculatePercent(self):
        try:
            expression = self.model.expression
            if "%" in expression:
                expression = expression.replace("%", "")
            self.model.expression = str(eval(expression) / 100.0)
            self.view.updateEntry(self.model.expression)
        except Exception:
            self.view.updateEntry("Error")

    def clear(self):
        self.model.expression = ""
        self.view.updateEntry(self.model.expression)

    def backspace(self):
        self.model.expression = self.model.expression[:-1]
        self.view.updateEntry(self.model.expression)

    def calculateReciprocal(self):
        try:
            self.model.expression = str(1 / float(self.model.expression))
            self.view.updateEntry(self.model.expression)
        except Exception:
            self.view.updateEntry("Error")

    def calculateSquare(self):
        try:
            self.model.expression = str(float(self.model.expression) ** 2)
            self.view.updateEntry(self.model.expression)
        except Exception:
            self.view.updateEntry("Error")

    def calculateSqrt(self):
        try:
            self.model.expression = str(
                math.sqrt(float(self.model.expression)))
            self.view.updateEntry(self.model.expression)
        except Exception:
            self.view.updateEntry("Error")

    def calculate(self):
        try:
            self.model.expression = str(eval(self.model.expression))
            self.view.updateEntry(self.model.expression)
        except Exception:
            self.view.updateEntry("Error")

    def toggleSign(self):
        if self.model.expression:
            if self.model.expression[0] == "-":
                self.model.expression = self.model.expression[1:]
            else:
                self.model.expression = "-" + self.model.expression
            self.view.updateEntry(self.model.expression)

    def addDecimalPoint(self):
        if "." not in self.model.expression:
            self.model.expression += "."
            self.view.updateEntry(self.model.expression)

    def appendToExpression(self, label):
        self.model.expression += label
        self.view.updateEntry(self.model.expression)
