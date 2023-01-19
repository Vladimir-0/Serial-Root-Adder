from customtkinter import CTkFont, CTkFrame, CTkLabel, CTkEntry, CTkButton

from Utils import sqrt_sum


class MainFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        # Config
        self.global_font = CTkFont("Roboto", 30)

        # Create elements
        self.info_label = CTkLabel(self,
                                   text="Enter the number of iterations",
                                   pady=5, font=self.global_font)
        self.IO_entry = CTkEntry(self, width=390, font=self.global_font)
        self.ok_button = CTkButton(self, text="OK", command=self.ok_button_click, font=self.global_font)

        self.bind_elements()
        self.pack_elements()

    def bind_elements(self):
        self.IO_entry.bind("<Return>", lambda event=None: self.ok_button_click())

    def pack_elements(self):
        self.info_label.pack()
        self.IO_entry.pack()
        self.ok_button.pack(pady=10)

    def ok_button_click(self):
        inp = self.IO_entry.get()
        self.IO_entry.delete(0, "end")
        self.IO_entry.insert(0, str(sqrt_sum(int(inp))))