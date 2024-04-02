import customtkinter as ctk
from customtkinter import CTkFrame , CTkButton , CTkEntry , CTkLabel

class SearchPage(CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        self.running = True
        self.create_widgets()



    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="mediumpurple1", width=700, corner_radius=0)
        frame.pack(expand=False, side=ctk.TOP, fill=ctk.X)

        frame2 = CTkFrame(master=self, fg_color="white", width=700, corner_radius=0)
        frame2.pack(expand=True, side=ctk.TOP, fill='both')

        # Left side - Entry widgets
        label_category = CTkLabel(master=frame2, text=f'Choose a category : ', text_color='black')
        
        combobox_category = ctk.CTkComboBox(master=frame2, values=["Food", "Health", "Leisure", "Transport", "Lodging", "Tax", "Daily expenses", "Salary", "Other"],
                                            command="""combobox_callback""")
        combobox_category.set("None")

        entry_date = CTkEntry(master=frame2, fg_color="white", width=20,placeholder_text="Date",placeholder_text_color="black",text_color="black")
        
        # Button widget
        search_button = CTkButton(master=frame2, text="Search", command=self.on_search_button_click)

        label_category.pack(pady=10, padx=10, fill = ctk.X)
        combobox_category.pack(pady=10, padx=10, fill = ctk.X)
        entry_date.pack(pady=10, padx=10,fill = ctk.X)
        search_button.pack(pady=10, padx=50)

        # Getter methods for entry widgets
        self.entry_category = combobox_category
        self.entry_date = entry_date

    # Getter methods to retrieve the content of each entry
    def get_entry_category_text(self):
        return self.entry_category.get()
    
    def get_entry_date_text(self):
        return self.entry_date.get()

    def on_search_button_click(self):
        # Implement the search functionality here
        self.master.set_search_category(self.get_entry_category_text())
        self.master.set_search_date(self.get_entry_date_text())
        self.master.set_search_request(True)
        