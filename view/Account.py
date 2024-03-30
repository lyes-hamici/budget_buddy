import customtkinter as ctk
from customtkinter import CTkFrame , CTkScrollableFrame
from .TransactionFrame import TransactionFrame

class Account(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.running = True
        self.account_balance = 0
        self.transaction = TransactionFrame()
        self.create_widgets()

    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1",  width=700,corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP,fill = ctk.X)


        frame2 = CTkScrollableFrame(master=self,fg_color="white",  width=7000,corner_radius=0)
        frame2.pack(expand=True, side=ctk.TOP,fill = 'both')

        label_sold = ctk.CTkLabel(master=frame, text=f'Available balance : {self.master.get_balance()} €', font=('helvetica', 30))#Replace self.account_balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        self.transaction.create_labels(frame2,self.master.get_transaction_list())
