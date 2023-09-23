from tkinter import Tk
from app import App


def main():
    root = Tk()
    app = App(root)

    root.resizable(0, 0)
    root.title("Calculator")
    root.mainloop()


if __name__ == "__main__":
    main()
