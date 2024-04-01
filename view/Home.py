import customtkinter as ctk
from customtkinter import CTkFrame 
from .TransactionFrame import TransactionFrame

class Home(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.transaction = TransactionFrame()   
        self.create_widgets()


    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="azure3", border_width=0, width=700)
        frame.pack(expand=False, side=ctk.TOP,pady = 50)


        frame2 = CTkFrame(master=self,fg_color="azure3", border_width=0, width=7000)
        frame2.pack(expand=False, side=ctk.TOP,pady = 50)

        label_sold = ctk.CTkLabel(master=frame, text=f'Balance : {self.master.get_balance()} €', font=('helvetica', 64))#Replace self.balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        self.transaction.create_labels(frame2,self.master.get_transaction_list()[0:3])















