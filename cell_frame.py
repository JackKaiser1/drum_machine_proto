import customtkinter
from sound_map import sample_map

class CellFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.i = -1
        self.previous_color = None

        # Init cells -------------------------------------------------
        self.cell_1 = customtkinter.CTkButton(self, text="1", height=55, width=55, command=lambda: self.click_cell(self.cell_1, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_2 = customtkinter.CTkButton(self, text="2", height=55, width=55, command=lambda: self.click_cell(self.cell_2, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_3 = customtkinter.CTkButton(self, text="3", height=55, width=55, command=lambda: self.click_cell(self.cell_3, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_4 = customtkinter.CTkButton(self, text="4", height=55, width=55, command=lambda: self.click_cell(self.cell_4, master.drum_sound.drum_obj), hover=None, fg_color="grey")

        self.cell_5 = customtkinter.CTkButton(self, text="5", height=55, width=55, command=lambda: self.click_cell(self.cell_5, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_6 = customtkinter.CTkButton(self, text="6", height=55, width=55, command=lambda: self.click_cell(self.cell_6, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_7 = customtkinter.CTkButton(self, text="7", height=55, width=55, command=lambda: self.click_cell(self.cell_7, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_8 = customtkinter.CTkButton(self, text="8", height=55, width=55, command=lambda: self.click_cell(self.cell_8, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")

        self.cell_9 = customtkinter.CTkButton(self, text="9", height=55, width=55, command=lambda: self.click_cell(self.cell_9, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_10 = customtkinter.CTkButton(self, text="10", height=55, width=55, command=lambda: self.click_cell(self.cell_10, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_11 = customtkinter.CTkButton(self, text="11", height=55, width=55, command=lambda: self.click_cell(self.cell_11, master.drum_sound.drum_obj), hover=None, fg_color="grey")
        self.cell_12 = customtkinter.CTkButton(self, text="12", height=55, width=55, command=lambda: self.click_cell(self.cell_12, master.drum_sound.drum_obj), hover=None, fg_color="grey")

        self.cell_13 = customtkinter.CTkButton(self, text="13", height=55, width=55, command=lambda: self.click_cell(self.cell_13, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_14 = customtkinter.CTkButton(self, text="14", height=55, width=55, command=lambda: self.click_cell(self.cell_14, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_15 = customtkinter.CTkButton(self, text="15", height=55, width=55, command=lambda: self.click_cell(self.cell_15, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")
        self.cell_16 = customtkinter.CTkButton(self, text="16", height=55, width=55, command=lambda: self.click_cell(self.cell_16, master.drum_sound.drum_obj), hover=None, fg_color="darkgrey")

        # Position cells ----------------------------------------------
        self.cell_1.grid(row=0, column=1, pady=5, padx=5.5)
        self.cell_2.grid(row=0, column=2, pady=5, padx=5.5)
        self.cell_3.grid(row=0, column=3, pady=5, padx=5.5)
        self.cell_4.grid(row=0, column=4, pady=5, padx=5.5)
        self.cell_5.grid(row=0, column=5, pady=5, padx=5.5)
        self.cell_6.grid(row=0, column=6, pady=5, padx=5.5)
        self.cell_7.grid(row=0, column=7, pady=5, padx=5.5)
        self.cell_8.grid(row=0, column=8, pady=5, padx=5.5)
        self.cell_9.grid(row=0, column=9, pady=5, padx=5.5)
        self.cell_10.grid(row=0, column=10, pady=5, padx=5.5)
        self.cell_11.grid(row=0, column=11, pady=5, padx=5.5)
        self.cell_12.grid(row=0, column=12, pady=5, padx=5.5)
        self.cell_13.grid(row=0, column=13, pady=5, padx=5.5)
        self.cell_14.grid(row=0, column=14, pady=5, padx=5.5)
        self.cell_15.grid(row=0, column=15, pady=5, padx=5.5)
        self.cell_16.grid(row=0, column=16, pady=5, padx=5.5)

        # Cell list --------------------------------------------------
        self.cell_list = [self.cell_1, self.cell_2, self.cell_3, self.cell_4, 
                          self.cell_5, self.cell_6, self.cell_7, self.cell_8, 
                          self.cell_9, self.cell_10, self.cell_11, self.cell_12, 
                          self.cell_13, self.cell_14, self.cell_15, self.cell_16]
        
    def click_cell(self, button, drum):
        beat = int(button._text)
        beat_list = drum.beat_list 
        active = button._fg_color == "chocolate1"

        if not active:
            if button._fg_color == "grey": 
                beat_list.append(beat)
                button.configure(fg_color="orange")
            elif button._fg_color == "darkgrey":
                beat_list.append(beat)
                button.configure(fg_color="dark orange")
            elif beat in [5,6,7,8,13,14,15,16] and button._fg_color == "dark orange":
                beat_list.remove(beat)
                button.configure(fg_color="darkgrey")
            else:
                beat_list.remove(beat)
                button.configure(fg_color="grey")
            print(beat_list)


    def drum_select(self, label, master):
        drum_name = label._text
        if drum_name in sample_map.keys():
            master.drum_sound.drum_obj = sample_map[drum_name]
        
        for cell in self.cell_list:
            cell_num = int(cell._text)
            beat_list = master.drum_sound.drum_obj.beat_list

            if cell_num in beat_list:
                if cell._fg_color == "grey":
                    cell.configure(fg_color="orange")
                elif cell._fg_color == "darkgrey":
                    cell.configure(fg_color="dark orange")
                    
            elif cell._fg_color == "orange":
                cell.configure(fg_color="grey")
            elif cell._fg_color == "dark orange":
                cell.configure(fg_color="darkgrey")

    def display_beat(self):
        cell_list = self.cell_list

        if self.previous_color is not None:
            cell_list[self.i].configure(fg_color=self.previous_color)
        self.i += 1
        if self.i == 16:
            self.i = 0

        self.previous_color = cell_list[self.i]._fg_color
        cell_list[self.i].configure(fg_color="chocolate1")

        return cell_list[self.i]
