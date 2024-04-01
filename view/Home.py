import customtkinter as ctk
from customtkinter import CTkFrame , CTkLabel   
from .TransactionFrame import TransactionFrame

class Home(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()


    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="azure3", border_width=0, width=700)
        frame.pack(expand=False, side=ctk.TOP,pady = 10)


        frame2 = CTkFrame(master=self,fg_color="azure3", border_width=0, width=7000)
        frame2.pack(expand=False, side=ctk.LEFT,pady = 15, padx = 10 )

        label_sold = ctk.CTkLabel(master=frame, text=f'Balance : {self.master.get_balance()} €', font=('helvetica', 64))#Replace self.balance with a the output of a function for get the sold of the account
        label_sold.pack(pady=12, padx=100)

        for i in range(len(self.master.get_transaction_list()[0:3])):
            new_list = self.master.get_transaction_list()[i]
            print(new_list)
            self.display_frame(frame2, new_list)


    def display_frame(self, frame, i):
        print("test display frame", i)
        frame_date = CTkFrame(master=frame, fg_color="transparent", bg_color="transparent")
        frame_date.pack(pady=2, fill=ctk.X)

        date_text = f"Date {i[7]}"
        date_label = CTkLabel(master=frame_date, text=date_text, font=('helvetica', 15),text_color='black')
        date_label.pack(side="top", pady=2, anchor=ctk.W, padx=5)

        frame_transaction = CTkFrame(master=frame_date, border_color="black", border_width=2)
        frame_transaction.pack(pady=5, fill=ctk.X, padx=5)

        label_text_nom = f"Name {i[2]} -"
        label_nom = CTkLabel(master=frame_transaction, text=label_text_nom, font=('helvetica', 14))
        label_nom.pack(pady=5, side="top", padx=5, anchor="nw")

        label_text_description = f"Description : {i[3]}"
        label_description = CTkLabel(master=frame_transaction, text=label_text_description, font=('helvetica', 14))
        label_description.pack(pady=5, side="top", padx=5, anchor="n")

        label_text_category = f"Category : {i[5]}"
        label_category = CTkLabel(master=frame_transaction, text=label_text_category, font=('helvetica', 14))
        label_category.pack(side="left", padx=5, pady=5, anchor="sw")

        label_text_values = f"Values : {i[4]} €"
        label_values = CTkLabel(master=frame_transaction, text=label_text_values, font=('helvetica', 14))
        label_values.pack(side="right", padx=5, pady=5, anchor="se")











