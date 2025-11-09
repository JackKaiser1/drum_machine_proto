import customtkinter

class DrumSelectFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        # Init Labels ------------------------------------------------------
        self.label1 = customtkinter.CTkButton(self, text="KICK", fg_color="orange", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label1, master), hover=None)
        self.label2 = customtkinter.CTkButton(self, text="SNARE", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label2, master), hover=None)
        self.label3 = customtkinter.CTkButton(self, text="CLAP", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label3, master), hover=None)
        self.label4 = customtkinter.CTkButton(self, text="HHAT", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label4, master), hover=None)
        self.label5 = customtkinter.CTkButton(self, text="RIM", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label5, master), hover=None)
        self.label6 = customtkinter.CTkButton(self, text="BELL", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label6, master), hover=None)
        self.label7 = customtkinter.CTkButton(self, text="CRASH", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label7, master), hover=None)
        self.label8 = customtkinter.CTkButton(self, text="OHAT", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label8, master), hover=None)
        self.label9 = customtkinter.CTkButton(self, text="MARACAS", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label9, master), hover=None)
        self.label10 = customtkinter.CTkButton(self, text="CLAV", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label10, master), hover=None)
        self.label11 = customtkinter.CTkButton(self, text="TOM L", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label11, master), hover=None)
        self.label12 = customtkinter.CTkButton(self, text="TOM M", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label12, master), hover=None)
        self.label13 = customtkinter.CTkButton(self, text="TOM H", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label13, master), hover=None)
        self.label14 = customtkinter.CTkButton(self, text="CONGA L", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label14, master), hover=None)
        self.label15 = customtkinter.CTkButton(self, text="CONGA M", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label15, master), hover=None)
        self.label16 = customtkinter.CTkButton(self, text="CONGA H", fg_color="grey", width=55, font=("Arial", 9), text_color="white", command=lambda: self.get_drum_select(self.label16, master), hover=None)

        # Position Labels -----------------------------------------------------
        self.label1.grid(row=0, column=0, padx=5.501, pady=5)
        self.label2.grid(row=0, column=1, padx=5.501, pady=5)
        self.label3.grid(row=0, column=2, padx=5.501, pady=5)
        self.label4.grid(row=0, column=3, padx=5.501, pady=5)
        self.label5.grid(row=0, column=4, padx=5.501, pady=5)
        self.label6.grid(row=0, column=5, padx=5.501, pady=5)
        self.label7.grid(row=0, column=6, padx=5.501, pady=5)
        self.label8.grid(row=0, column=7, padx=5.501, pady=5)
        self.label9.grid(row=0, column=8, padx=5.501, pady=5)
        self.label10.grid(row=0, column=9, padx=5.501, pady=5)
        self.label11.grid(row=0, column=10, padx=5.501, pady=5)
        self.label12.grid(row=0, column=11, padx=5.501, pady=5)
        self.label13.grid(row=0, column=12, padx=5.501, pady=5)
        self.label14.grid(row=0, column=13, padx=5.501, pady=5)
        self.label15.grid(row=0, column=14, padx=5.501, pady=5)
        self.label16.grid(row=0, column=15, padx=5.501, pady=5)

        self.label_list = [self.label1, self.label2, self.label3, self.label4,
                           self.label5, self.label6, self.label7, self.label8,
                           self.label9, self.label10, self.label11, self.label12,
                           self.label13, self.label14, self.label15, self.label16]


    def get_drum_select(self, label, master):
        master.cell_frame.drum_select(label, master)
        self.click_label(label)


    def click_label(self, label):
        for lab in self.label_list:
            if lab._fg_color == "orange":
                lab.configure(fg_color="grey")
        if label._fg_color == "grey":
            label.configure(fg_color="orange")
            return 