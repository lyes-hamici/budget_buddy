import customtkinter as ctk
from customtkinter import CTkLabel, CTkFrame

class TransactionFrame():
    def __init__(self):
        pass

    def create_labels(self, frame):
        '''
        Function that creates labels based on the number of account transactions.
        
        Args:
            frame: The frame in which labels will be created.
        '''
        for i in range(20):
            frame.after(500 * i, self.display_frame, frame, i)
            
    def display_frame(self, frame, i):
        '''
        Function that displays a transaction frame.

        Args:
            frame: The parent frame where the transaction frame will be displayed.
            i: Index of the transaction frame.
        '''
        frame_date = CTkFrame(master=frame, fg_color="transparent", bg_color="transparent")
        frame_date.pack(pady=15, fill=ctk.X)

        date_text = f"date {i}"
        date_label = CTkLabel(master=frame_date, text=date_text, font=('helvetica', 20))
        date_label.pack(side="top", pady=5, anchor=ctk.W, padx=5)

        frame_transaction = CTkFrame(master=frame_date, border_color="black", border_width=2)  # Creating the frame
        frame_transaction.pack(pady=15, fill=ctk.X, padx=5)  # Placing the frame within the main frame

        label_text_nom = f"Label_nom {i} -"  # Label text
        label_nom = CTkLabel(master=frame_transaction, text=label_text_nom, font=('helvetica', 14))
        label_nom.pack(pady=5,side="top",padx = 5,anchor="nw")  # Placing the label within the frame

        label_text_description = f"Label_Description {i}"  # Label text
        label_description = CTkLabel(master=frame_transaction, text=label_text_description, font=('helvetica', 14))
        label_description.pack(pady=5,side="top",padx = 5,anchor="n")  # Placing the label within the frame

        label_text_category = f"Label_Category {i}"  # Label text
        label_category = CTkLabel(master=frame_transaction, text=label_text_category, font=('helvetica', 14))
        label_category.pack(side="left", padx=5, pady=5, anchor="sw")  # Placing the label within the frame

        label_text_values = f"Label_values {i}"  # Label text
        label_values = CTkLabel(master=frame_transaction, text=label_text_values, font=('helvetica', 14))
        label_values.pack(side="right", padx=5, pady=5, anchor="se")  # Placing the label within the frame
