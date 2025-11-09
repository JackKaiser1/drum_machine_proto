import customtkinter

class SliderFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


        # Init sliders -------------------------------------------------
        self.slider_1 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_2 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_3 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_4 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_5 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_6 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_7 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_8 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_9 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_10 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_11 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_12 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_13 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_14 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_15 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")
        self.slider_16 = customtkinter.CTkSlider(self, height=300, from_=0, to=100, orientation="vertical")


        # Position sliders ----------------------------------------------
        self.slider_1.grid(row=4, column=1, padx=25)
        self.slider_2.grid(row=4, column=2, padx=25)
        self.slider_3.grid(row=4, column=3, padx=25)
        self.slider_4.grid(row=4, column=4, padx=25)
        self.slider_5.grid(row=4, column=5, padx=25)
        self.slider_6.grid(row=4, column=6, padx=25)
        self.slider_7.grid(row=4, column=7, padx=25)
        self.slider_8.grid(row=4, column=8, padx=25)
        self.slider_9.grid(row=4, column=9, padx=25)
        self.slider_10.grid(row=4, column=10, padx=25)
        self.slider_11.grid(row=4, column=11, padx=25)
        self.slider_12.grid(row=4, column=12, padx=25)
        self.slider_13.grid(row=4, column=13, padx=25)
        self.slider_14.grid(row=4, column=14, padx=25)
        self.slider_15.grid(row=4, column=15, padx=25)
        self.slider_16.grid(row=4, column=16, padx=25)        
