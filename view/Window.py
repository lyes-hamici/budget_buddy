import tkinter as tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter MVC")
        self.geometry("1280x720")
        self.resizable(False, False)
   
    
if __name__ == "__main__":
    app = Window()
    app.mainloop()