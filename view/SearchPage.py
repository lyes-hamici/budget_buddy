import customtkinter as ctk
from customtkinter import CTkFrame , CTkButton , CTkEntry , CTkLabel, CTkScrollableFrame
import time

class SearchPage(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.running = True
        self.create_widgets()



    def create_widgets(self):

        self.frame2 = CTkScrollableFrame(master=self, fg_color="white", width=700, corner_radius=0)
        self.frame2.pack(expand=True, side=ctk.TOP, fill='both')

        # Left side - Entry widgets
        label_category = CTkLabel(master=self.frame2, text=f'Choose a category : ', text_color='black')
        
        combobox_category = ctk.CTkComboBox(master=self.frame2, values=["Food", "Health", "Leisure", "Transport", "Lodging", "Tax", "Daily expenses", "Salary", "Other"],
                                            command="""combobox_callback""")
        combobox_category.set("Category")
        
        combobox_type = ctk.CTkComboBox(master=self.frame2, values=["Expense", "Income"], command="""combobox_callback""")
        combobox_type.set("Type")

        entry_date = CTkEntry(master=self.frame2, fg_color="white", width=20,placeholder_text="Date",placeholder_text_color="black",text_color="black")
        
        # Button widget
        search_button = CTkButton(master=self.frame2, text="Search", command=self.on_search_button_click)

        label_category.pack(pady=10, padx=10, fill = ctk.X)
        combobox_category.pack(pady=10, padx=10, fill = ctk.X)
        combobox_type.pack(pady=10, padx=10, fill = ctk.X)
        entry_date.pack(pady=10, padx=10,fill = ctk.X)
        search_button.pack(pady=10, padx=50)
        


        # Getter methods for entry widgets
        self.entry_category = combobox_category
        self.entry_date = entry_date
        self.entry_type = combobox_type
        
        for i in range(len(self.master.get_research_list())):
            new_list = self.master.get_research_list()[i]
            self.display_frame(self.frame2, new_list)
    


    def display_frame(self, frame, i):
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



    
    # Getter methods to retrieve the content of each entry
    def get_entry_category_text(self):
        return self.entry_category.get()
    
    def get_entry_date_text(self):
        return self.entry_date.get()
    
    def get_entry_type(self):
        return self.entry_type.get()

    def on_search_button_click(self):
        self.master.set_search_category(self.get_entry_category_text())
        self.master.set_search_date(self.get_entry_date_text())
        self.master.set_search_type(self.get_entry_type())
        self.master.set_search_request(True)
        
        