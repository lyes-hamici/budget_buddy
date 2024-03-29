import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton


class RegisterFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        
        self.running = True
        self.value_name = ctk.StringVar()
        self.value_firstname = ctk.StringVar()
        self.value_password = ctk.StringVar()
        self.value_mail = ctk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Create a frame with specified width, height, and corner radius
        frame = CTkFrame(master=self, width=400, height=834, corner_radius=45)
        frame.grid(row=0, column=0)

        # Retrieve the dimensions of the main window
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()

        # Calculate the coordinates to center the frame
        x = (window_width - 400) // 2.8  # The width of the frame is 400
        y = (window_height - 834)      # The height of the frame is 834

        # Position the frame centered within the main window
        frame.place(x=x, y=y)

        # Create a label for the registration
        label = CTkLabel(master=frame, text='Registration', font=('helvetica', 30))
        label.grid(row=0, column=0, padx=40, pady=20, columnspan=2)

        # Create entry fields for name, first name, password, email, and confirmation
        self.entry1 = CTkEntry(master=frame, placeholder_text="Name")
        self.entry1.grid(row=1, column=0, padx=40, pady=20)

        self.entry2 = CTkEntry(master=frame, placeholder_text="Firstname")
        self.entry2.grid(row=1, column=1, padx=40, pady=20)

        self.entry3 = CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.entry3.grid(row=2, column=0, padx=40, pady=20)

        self.entry31 = CTkEntry(master=frame, placeholder_text="Confirm Password", show="*")
        self.entry31.grid(row=2, column=1, padx=40, pady=20)

        self.entry4 = CTkEntry(master=frame, placeholder_text="Email")
        self.entry4.grid(row=3, column=0, padx=40, pady=20)

        self.entry41 = CTkEntry(master=frame, placeholder_text="Confirm Email")
        self.entry41.grid(row=3, column=1, padx=40, pady=20)

        # Create buttons for validation and going back
        validation_button = CTkButton(master=frame, text="Click to validate", command=self.on_click_validation)
        validation_button.grid(row=4, column=0, padx=40, pady=20)

        quit_button = CTkButton(master=frame, text="Go back", command=self.on_go_back)
        quit_button.grid(row=4, column=1, padx=40, pady=20)


        
    # to this point new methods

    def on_click_validation(self):
        self.master.set_value_display_page(1)
        self.master.set_value_asking_for_creation(True)
    
    def on_go_back(self):
        self.master.set_value_display_page(1)
