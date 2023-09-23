from tkinter import END, NORMAL, Button, Frame, Text, DISABLED


class CalculatorView:
    def __init__(self, parent, controller, x, y):
        self.parent = parent
        self.controller = controller
        self.container = Frame(self.parent, padx=8, pady=8)
        self.container.grid(row=x, column=y)
        self.createWidgets()

    def createWidgets(self):
        self.createEntry()
        self.createButtons()

    def createEntry(self):
        self.entry = Text(self.container, font=("Arial", 24),
                          width=0, height=1, padx=8, pady=8, state=DISABLED)
        self.entry.grid(row=0, column=0, columnspan=5, pady=8, sticky="we")

    def createButtons(self):
        buttons = [
            "%", "CE", "С", "\u00D7",
            "1/x", "x^2", "√x", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "+/-", "0", ".", "="
        ]
        gridRows, gridColumns = 4, 4
        grid = [(label, idx // gridRows + 1, idx % gridColumns)
                for idx, label in enumerate(buttons)]

        for label, x, y in grid:
            self.createButton(label, x, y)

    def createButton(self, label, x, y):
        button = Button(self.container, text=label, font=("Arial", 18), width=4,
                        height=1, command=lambda: self.controller.buttonClicked(label))
        button.grid(row=x, column=y, padx=2, pady=2)

    def updateEntry(self, text):
        self.entry.config(state=NORMAL)
        self.entry.delete('1.0', END)
        self.entry.insert('1.0', text)
        self.entry.config(state=DISABLED)
