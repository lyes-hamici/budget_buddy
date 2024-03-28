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
        frame.pack(expand=True, fill=ctk.Y, anchor=ctk.W)
        
        home_button = CTkButton(master=frame, text="Home",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_home_button_click)
        account_button = CTkButton(master=frame, text="Account",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_account_button_click)
        graphics_button = CTkButton(master=frame, text="Graphics",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_graphics_button_click)
        logout_button = CTkButton(master=frame, text="Logout",fg_color="white",hover_color="mediumpurple1",border_color="black",text_color="black",border_width=2,corner_radius=30, command=self.on_logout_button_click)
        
        home_button.pack(expand = True,padx = 5)
        account_button.pack(expand = True,padx = 5)
        graphics_button.pack(expand = True,padx = 5)
        logout_button.pack(expand = True,padx = 5)

    def on_home_button_click(self):
        self.master.set_value_display_page(3)

    def on_account_button_click(self):
        self.master.set_value_display_page(4)
    
    def on_graphics_button_click(self):
        self.master.set_value_display_page(5)

    def on_logout_button_click(self):
        pass