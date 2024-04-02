from collections.abc import Iterable
from typing import Any, Tuple
import customtkinter as ctk
from customtkinter import CTkFrame, CTkButton

class Dashboard(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        frame = CTkFrame(master=self, fg_color="azure3", corner_radius=0)
        frame.pack(expand=True, fill="y", side=ctk.RIGHT)
        
        home_button = CTkButton(master=frame, text="Home",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_home_button_click,width=100)
        account_button = CTkButton(master=frame, text="Account",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_account_button_click,width=100)
        graphics_button = CTkButton(master=frame, text="Graphics",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_graphics_button_click,width=100)
        logout_button = CTkButton(master=frame, text="Logout",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_logout_button_click,width=100)
        transaction_button = CTkButton(master=frame, text="Transaction",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_transaction_button_click,width=100)
        
        
        home_button.pack(padx = 80,pady = 30)
        account_button.pack(padx = 80,pady = 30)
        graphics_button.pack(padx = 80,pady = 30)
        transaction_button.pack(padx = 80,pady = 30)
        logout_button.pack(expand = True,padx = 80,pady = 10,anchor = "s")

    def on_home_button_click(self):
        self.master.set_value_display_page(3)

    def on_account_button_click(self):
        self.master.set_value_display_page(4)
    
    def on_graphics_button_click(self):
        self.master.set_value_display_page(5)


    def on_transaction_button_click(self):
        self.master.set_value_display_page(6)

    def on_logout_button_click(self):
        print("logout button clicked")
        self.master.set_logout_request(True)