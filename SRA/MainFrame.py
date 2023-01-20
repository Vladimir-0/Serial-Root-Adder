from customtkinter import CTk, CTkFont, CTkFrame, CTkLabel, CTkEntry, CTkButton

from Utils import sqrt_sum


class MainFrame(CTkFrame):
    def __init__(self, master: CTk, elements_font: CTkFont = None) -> None:
        super().__init__(master, fg_color="transparent")

        # Config
        self._elements_font = elements_font

        # Create elements
        self._info_label = CTkLabel(self,
                                    text="Enter the amount of iterations",
                                    font=self._elements_font)
        self._IO_entry = CTkEntry(self, width=390, font=self._elements_font)
        self._ok_button = CTkButton(self, text="OK", command=self._ok_button_click, font=self._elements_font)

        self._bind_elements()
        self._pack_elements()

    def _bind_elements(self) -> None:
        """
        Bind the keyboard keys to the elements.
        """
        self._IO_entry.bind("<Return>", lambda event=None: self._ok_button_click())
        # <Return> is Enter on the keyboard
        # lambda generates a function with an event variable as input to avoid an error

    def _pack_elements(self) -> None:
        """
        Display all frame elements.
        """
        self._info_label.pack()
        self._IO_entry.pack()
        self._ok_button.pack(pady=10)  # y-axis padding = 10px

    def _ok_button_click(self) -> None:
        """
        Put calculation results into the entry.
        """
        inp = self._IO_entry.get()  # get input text
        self._IO_entry.delete(0, "end")  # delete all characters
        self._IO_entry.insert(0, str(sqrt_sum(int(inp))))  # enters the calculation result
