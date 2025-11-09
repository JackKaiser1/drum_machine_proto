import customtkinter
from constants import *

class ButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master):
            super().__init__(master)

            # Init buttons -------------------------------------------------
            self.pattern_button = customtkinter.CTkButton(self, text="PATTERN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
            self.group_button = customtkinter.CTkButton(self, text="GROUP", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
            self.pause_button = customtkinter.CTkButton(self, text="PAUSE", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey", command=master.pause)

            # Position buttons ----------------------------------------------
            self.pattern_button.grid(row=0, column=0, padx=20, pady=10)
            self.group_button.grid(row=1, column=0, padx=20, pady=10)
            self.pause_button.grid(row=2, column=0, padx=20, pady=10)