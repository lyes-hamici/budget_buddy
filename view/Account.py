import customtkinter as ctk
from customtkinter import CTkFrame , CTkScrollableFrame
from .TransactionFrame import TransactionFrame

class Account(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.transaction = TransactionFrame()
        self.create_widgets()

    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1",  width=700,corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP,fill = ctk.X)

        frame2 = CTkFrame(master=self, fg_color="azure3",  width=700,corner_radius=0)
        frame2.pack(expand=False, side=ctk.TOP,fill = ctk.X)

        button1 = ctk.CTkButton(master=frame2, text="1")
        button1.pack(side='left',padx=30, pady=5)

        button2 = ctk.CTkButton(master=frame2, text="2")
        button2.pack(side='left',padx=30, pady=5)


        button3 = ctk.CTkButton(master=frame2, text="3")
        button3.pack(side='left',padx=30, pady=5)

        button4 = ctk.CTkButton(master=frame2, text="4")
        button4.pack(side='left',padx=30, pady=5)

        button5 = ctk.CTkButton(master=frame2, text="4")
        button5.pack(side='left',padx=30, pady=5)

        frame3 = CTkScrollableFrame(master=self,fg_color="white",  width=7000,corner_radius=0)
        frame3.pack(expand=True, side=ctk.TOP,fill = 'both')

        label_sold = ctk.CTkLabel(master=frame, text=f'Available balance : {self.master.get_balance()} €', font=('helvetica', 30))#Replace self.account_balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        self.transaction.create_labels(frame3,self.master.get_transaction_list())
