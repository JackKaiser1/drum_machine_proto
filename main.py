import customtkinter
from constants import *

root = customtkinter.CTk()

root.geometry("1205x600")
root.title("Drum Machine")

def record_button():
    print("record mode is on!")

def click_cell(button):
    if button._fg_color == "orange": 
        button.configure(fg_color="grey")
    else:
        button.configure(fg_color="orange")


button_frame = customtkinter.CTkFrame(root)
button_frame.grid(row=1, column=0, padx=5, pady=10)

slider_frame = customtkinter.CTkFrame(root)
slider_frame.grid(row=1, column=1, padx=5, pady=10) 

cell_frame = customtkinter.CTkFrame(root)
cell_frame.grid(row=2, column=1, padx=0, pady=10)

root.grid_rowconfigure(0, weight=0)




bpm_button = customtkinter.CTkButton(root, text="BPM", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
shift_button = customtkinter.CTkButton(button_frame, text="SHIFT", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
group_button = customtkinter.CTkButton(button_frame, text="GROUP", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
pattern_button = customtkinter.CTkButton(button_frame, text="PATTERN", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey")
rec_button = customtkinter.CTkButton(root, text="REC", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, fg_color="grey", hover_color="darkgrey") 
presets_button = customtkinter.CTkButton(root, text="Presets", height=50, width=200, fg_color="grey", hover_color="darkgrey")




cell_1 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_1), hover=None, fg_color="grey")
cell_2 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_2), hover=None, fg_color="grey")
cell_3 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_3), hover=None, fg_color="grey")
cell_4 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_4), hover=None, fg_color="grey")

cell_5 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_5), hover=None, fg_color="grey")
cell_6 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_6), hover=None, fg_color="grey")
cell_7 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_7), hover=None, fg_color="grey")
cell_8 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_8), hover=None, fg_color="grey")

cell_9 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_9), hover=None, fg_color="grey")
cell_10 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_10), hover=None, fg_color="grey")
cell_11 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_11), hover=None, fg_color="grey")
cell_12 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_12), hover=None, fg_color="grey")

cell_13 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_13), hover=None, fg_color="grey")
cell_14 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_14), hover=None, fg_color="grey")
cell_15 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_15), hover=None, fg_color="grey")
cell_16 = customtkinter.CTkButton(cell_frame, text="", height=55, width=55, command=lambda: click_cell(cell_16), hover=None, fg_color="grey")




slider_1 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_2 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_3 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_4 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_5 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_6 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_7 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_8 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_9 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_10 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_11 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_12 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_13 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_14 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_15 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")
slider_16 = customtkinter.CTkSlider(slider_frame, height=300, from_=0, to=100, orientation="vertical")

slider_1.grid(row=4, column=1, padx=25)
slider_2.grid(row=4, column=2, padx=25)
slider_3.grid(row=4, column=3, padx=25)
slider_4.grid(row=4, column=4, padx=25)
slider_5.grid(row=4, column=5, padx=25)
slider_6.grid(row=4, column=6, padx=25)
slider_7.grid(row=4, column=7, padx=25)
slider_8.grid(row=4, column=8, padx=25)
slider_9.grid(row=4, column=9, padx=25)
slider_10.grid(row=4, column=10, padx=25)
slider_11.grid(row=4, column=11, padx=25)
slider_12.grid(row=4, column=12, padx=25)
slider_13.grid(row=4, column=13, padx=25)
slider_14.grid(row=4, column=14, padx=25)
slider_15.grid(row=4, column=15, padx=25)
slider_16.grid(row=4, column=16, padx=25)


bpm_button.grid(row=0, column=0, padx=20, pady=10)
shift_button.grid(row=1, column=0, padx=20, pady=10)
group_button.grid(row=2, column=0, padx=20, pady=10)
pattern_button.grid(row=3, column=0, padx=20, pady=10)
rec_button.grid(row=2, column=0, padx=10, pady=40)
presets_button.grid(row=0, column=1)

cell_1.grid(row=5, column=1, pady=5, padx=5.5)
cell_2.grid(row=5, column=2, pady=5, padx=5.5)
cell_3.grid(row=5, column=3, pady=5, padx=5.5)
cell_4.grid(row=5, column=4, pady=5, padx=5.5)
cell_5.grid(row=5, column=5, pady=5, padx=5.5)
cell_6.grid(row=5, column=6, pady=5, padx=5.5)
cell_7.grid(row=5, column=7, pady=5, padx=5.5)
cell_8.grid(row=5, column=8, pady=5, padx=5.5)
cell_9.grid(row=5, column=9, pady=5, padx=5.5)
cell_10.grid(row=5, column=10, pady=5, padx=5.5)
cell_11.grid(row=5, column=11, pady=5, padx=5.5)
cell_12.grid(row=5, column=12, pady=5, padx=5.5)
cell_13.grid(row=5, column=13, pady=5, padx=5.5)
cell_14.grid(row=5, column=14, pady=5, padx=5.5)
cell_15.grid(row=5, column=15, pady=5, padx=5.5)
cell_16.grid(row=5, column=16, pady=5, padx=5.5)


# root.grid_columnconfigure(0, weight=1)


root.mainloop()
