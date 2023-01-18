from tkinter import Tk

from . import MainFrame


class App(Tk):
    def __init__(self) -> None:
        super().__init__()

        # Configures the window
        self.wm_iconbitmap("res/calc.ico")
        self.wm_title("Serial Root Adder")
        self.wm_minsize(300, 80)
        self.wm_resizable(False, False)

        self.main_frame = MainFrame(self)
        self.main_frame.pack()

    def run(self) -> None:
        self.mainloop()


if __name__ == '__main__':
    myapp = App()
    myapp.run()
