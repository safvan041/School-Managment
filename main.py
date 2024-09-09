from tkinter import Tk
from home_page import HomePage

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("School Management System")
        self.geometry('800x600')
        self.home_page = HomePage(self)
        self.home_page.pack(fill='both', expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
