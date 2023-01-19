from customtkinter import CTk

from MainFrame import MainFrame


class App(CTk):
    def __init__(self) -> None:
        super().__init__()

        # Configure the window
        self.wm_iconbitmap("res/calc.ico")
        self.geometry("500x170")
        self.title("Serial Root Adder")
        self.resizable(False, False)

        # Create elements
        self.main_frame = MainFrame(self)

        self.pack_elements()

    def pack_elements(self):
        self.main_frame.pack(pady=10)

    def run(self) -> None:
        self.mainloop()


if __name__ == '__main__':
    myapp = App()
    myapp.run()
