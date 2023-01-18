from tkinter import END, Frame, Label, Entry, Button

from .. import Utils


class MainFrame(Frame):
    info_label: Label
    IO_entry: Entry
    ok_button: Button

    def __init__(self, master=None) -> None:
        super().__init__(master)

        self.create_elements()  # Creates elements
        self.bind_elements()  # Binds the elements
        self.pack_elements()  # Places elements on the screen

        self.IO_entry.focus_set()

    def create_elements(self):
        self.info_label = Label(self, text="Введите количество итераций:")
        self.IO_entry = Entry(self)
        self.ok_button = Button(self, command=self.ok_button_click, text="Ok", width=10)

    def pack_elements(self) -> None:
        # pack() places the element at the top center by default
        self.info_label.pack()
        self.IO_entry.pack()
        self.ok_button.pack(pady=5)  # y-axis padding = 5px

    def bind_elements(self):
        self.IO_entry.bind('<Return>', lambda event=None: self.ok_button.invoke())
        # lambda is needed to create a function with the event variable as input.

    def ok_button_click(self) -> None:
        inp = int(self.IO_entry.get())  # gets input from the entry
        self.IO_entry.delete(0, END)  # clears the entry
        self.IO_entry.insert(0, str(Utils.sqrt_sum(inp)))  # puts the calculation result to the entry
