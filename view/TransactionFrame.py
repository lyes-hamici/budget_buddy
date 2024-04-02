import customtkinter as ctk
from customtkinter import CTkLabel, CTkFrame, CTkEntry

class TransactionFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)

    def create_labels(self, frame, transaction_list):
        '''
        Function that creates labels based on the number of account transactions.
        
        Args:
            frame: The frame in which labels will be created.
        '''
        for i in range(len(transaction_list)):
            new_list = transaction_list[i]
            print(new_list)
            # print(transaction_list[str(i)])
            frame.after(200 * i, self.display_frame,frame, new_list)
            
    def display_frame(self, frame, i):
        print("test display frame", i)
        frame_date = CTkFrame(master=frame, fg_color="transparent", bg_color="transparent")
        frame_date.pack(pady=2, fill=ctk.X)


        if i[0] == self.master.get_to_modify():
            date_text = f"Date : {i[7]} - To modify"
            date_input = CTkEntry(master=frame_date, placeholder_text= date_text, font=('helvetica', 15),text_color='black', width=10*len(date_text))
            date_input.pack(side="top", pady=2, anchor=ctk.W, padx=5, expand=True)

            frame_transaction = CTkFrame(master=frame_date, border_color="black", border_width=2)
            frame_transaction.pack(pady=5, fill=ctk.X, padx=5)

            button1 = ctk.CTkButton(master=frame_transaction, text="Back", command=self.back_modif)
            button1.pack(side="right", anchor="ne", padx=5, pady=5)

            button2 = ctk.CTkButton(master=frame_transaction, text="Validate", command=self.validate_modif)
            button2.pack(side="right", anchor="ne", padx=5, pady=5)

            input_text_nom = f"Name {i[2]} - To modify"
            input_nom = CTkEntry(master=frame_transaction, placeholder_text= input_text_nom, font=('helvetica', 14), width=10*len(input_text_nom))
            input_nom.pack(pady=5, side="top", padx=5, anchor="nw")

            input_text_description = f"Description : {i[3]} - To modify"
            input_description = CTkEntry(master=frame_transaction, placeholder_text= input_text_description, font=('helvetica', 14), width=10*len(input_text_description))
            input_description.pack(pady=5, side="top", padx=5, anchor="n")

            input_text_category = f"Category : {i[5]} - To modify"
            input_category = CTkEntry(master=frame_transaction, placeholder_text= input_text_category, font=('helvetica', 14), width=10*len(input_text_category))
            input_category.pack(side="left", padx=5, pady=5, anchor="sw")

            input_text_values = f"Values : {i[4]} € - To modify"
            input_values = CTkEntry(master=frame_transaction, placeholder_text= input_text_values, font=('helvetica', 14), width=10*len(input_text_values))
            input_values.pack(side="right", padx=5, pady=5, anchor="se")

            self.input_nom = input_nom
            self.input_description = input_description
            self.input_category = input_category
            self.input_values = input_values
            self.input_date = date_input



        else:

            date_text = f"Date {i[7]}"
            date_label = CTkLabel(master=frame_date, text=date_text, font=('helvetica', 15),text_color='black')
            date_label.pack(side="top", pady=2, anchor=ctk.W, padx=5)

            frame_transaction = CTkFrame(master=frame_date, border_color="black", border_width=2)
            frame_transaction.pack(pady=5, fill=ctk.X, padx=5)

            # Ajout des boutons
            button1 = ctk.CTkButton(master=frame_transaction, text="Remove", command=lambda: self.on_remove_transaction_button_click(i[0]))
            button1.pack(side="right", anchor="ne", padx=5, pady=5)

            button2 = ctk.CTkButton(master=frame_transaction, text="Modify", command=lambda: self.on_modify_transaction_button_click(i[0], i[2], i[3], i[5], i[4], i[7]))
            button2.pack(side="right", anchor="ne", padx=5, pady=5)

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

    
    def on_remove_transaction_button_click(self, id_transaction):
        '''
        Function that removes a transaction from the account.
        
        Args:
            id_transaction: The id of the transaction to remove.
        '''
        self.master.set_id_transaction(id_transaction)

    def on_modify_transaction_button_click(self, id_transaction, name, description, category, value, date):
        '''
        Function that modifies a transaction from the account.
        
        Args:
            id_transaction: The id of the transaction to modify.
        '''
        self.master.set_to_modify(id_transaction)
        self.store_transaction_data(name, description, category, value, date)

    def validate_modif(self):
        '''
        Function that validates the modification of a transaction.
        '''
        self.master.store_transaction_data(self.input_nom.get(), 
                                           self.input_description.get(), 
                                           self.input_category.get(), 
                                           self.input_values.get(), 
                                           self.input_date.get()
                                           )
        self.master.set_validate_modification(True)
        print("validate_modif button clicked")

    def back_modif(self):
        '''
        Function that goes back to the transaction list.
        '''
        self.master.set_validate_modification(False)
    
    def store_transaction_data(self,  name, description, category, value, date):
        '''
        Function that stores the transaction data.
        '''
        self.master.store_transaction_data( name, description, category, value, date)