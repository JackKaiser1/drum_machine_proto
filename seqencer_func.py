from sound_class import drum, sample
from sound import kick, snare, hihat, rim
from sound_map import cell_list

# def click_cell(button, drum):
#     beat = int(button._text)
#     if button._fg_color == "grey" or button._fg_color == "darkgrey": 
#         drum.beat_list.append(beat)
#         button.configure(fg_color="orange")
#     elif beat in [5,6,7,8,13,14,15,16]:
#         drum.beat_list.remove(beat)
#         button.configure(fg_color="darkgrey")
#     else:
#         drum.beat_list.remove(beat)
#         button.configure(fg_color="grey")
#     print(drum.beat_list)


# def drum_select(drum):
#     if drum == "kick":
#         drum_sound.drum_obj = kick
#     elif drum == "snare":
#         drum_sound.drum_obj = snare
#     elif drum == "hihat":
#         drum_sound.drum_obj = hihat
#     elif drum == "rim":
#         drum_sound.drum_obj = rim
    
#     for cell in cell_list:
#         cell_num = int(cell._text)
#         beat_list = drum_sound.drum_obj.beat_list
#         if cell_num in beat_list:
#             cell.configure(fg_color="orange")
#         elif cell._fg_color == "orange":
#             if cell_num in [5,6,7,8,13,14,15,16]:
#                 cell.configure(fg_color="darkgrey")
#             else:
#                 cell.configure(fg_color="grey")

# drum_sound = drum(kick)

# cell_list = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10, cell_11, cell_12, cell_13, cell_14, cell_15, cell_16]