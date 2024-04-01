import customtkinter as ctk
from customtkinter import CTkFrame 
from .TransactionFrame import TransactionFrame

class Home(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.transaction = TransactionFrame()
        self.fg_color = self.determine_fg_color() 
        self.bg_color = self.determine_bg_color()
        self.create_widgets()

    def determine_fg_color(self):
        if int(self.master.get_balance()) < 0:
            return "red"
        else:
            return "white"
        
    def determine_bg_color(self):
        if int(self.master.get_balance()) < self.master.get_overdraft():
            return "red"
        else:
            return "azure3"
        
    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color=self.bg_color, border_width=0, width=700)
        frame.pack(expand=False, side=ctk.TOP,pady = 50)


        frame2 = CTkFrame(master=self,fg_color="azure3", border_width=0, width=7000)
        frame2.pack(expand=False, side=ctk.TOP,pady = 50)

        label_sold = ctk.CTkLabel(master=frame, text=f'Balance : {self.master.get_balance()} €', font=('helvetica', 64, self.fg_color))#Replace self.balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        self.transaction.create_labels(frame2,self.master.get_transaction_list()[0:3])















