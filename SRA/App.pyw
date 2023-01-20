from customtkinter import CTk, CTkFont

from MainFrame import MainFrame


class App(CTk):
    def __init__(self) -> None:
        super().__init__()

        # Config
        self._global_font = CTkFont("Roboto", 30)

        # Configure the window
        self.wm_iconbitmap("res/calc.ico")
        self.geometry("450x170")
        self.title("Serial Root Adder")
        self.resizable(False, False)

        # Create elements
        self._main_frame = MainFrame(self, self._global_font)

        self._pack_elements()

    def _pack_elements(self) -> None:
        """
        Display all window elements.
        """
        self._main_frame.pack(pady=10)  # y-axis padding = 10px

    def run(self) -> None:
        """
        Run the application.
        """
        self.mainloop()


if __name__ == '__main__':
    App().run()
