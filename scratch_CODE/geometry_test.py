# problem was packing the main canvas in a frame, and having context_menu canvas packed first not in the same frame
# got rid of frame and just made both canvas children of root, borders could be cleaned up though
# error happens with just this stuff
# bottom of canvas 'cutoff'
# doesnt seem to happen with context menu removed

# minimal geometry to get full screen working correctly
import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk,Image
from random import choice

# CURSOR GLOBALS
curs_pos = [0, 0]
# Used to determine if an object has been selected by the cursor
is_object_selected = False
selected = ''

# MAP POSITION GLOBAL
map_pos = [0, 0]

# GRID POSITION GLOBAL
grid_pos = [0,0]

# do i need subclass here? ie super? root and app?
class App(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.choose_map()
        
    def choose_map(self):
        self.marquee = tk.Label(root, text = 'Choose your map', fg = 'tan3', bg = 'black', font=("chalkduster", 36))
        self.marquee.pack(side = 'top')
        # CHOOSE MAPS
        maps = [m for r,d,m in os.walk('./maps')][0]
        self.map_button_list = []
        self.tmp_mapimg_dict = {}
        for i,map in enumerate(maps):
            cmd = lambda indx = i : self.load_map(indx)
            photo = ImageTk.PhotoImage(Image.open('./maps/' + map).resize((300,300)))
            self.tmp_mapimg_dict['map'+str(i)] = photo
            b = tk.Button(root, image = self.tmp_mapimg_dict['map'+str(i)], bg = 'black', highlightbackground = 'tan4', command = cmd)
            b.pack(side = 'left')
            self.map_button_list.append(b)
            
    # really this just is an 'intermediate' function that doesnt load_map, it deletes vars from the last function
    def load_map(self, map_number):
        self.marquee.destroy()
        del self.tmp_mapimg_dict
        for b in self.map_button_list:
            b.destroy()
        del self.map_button_list
        self.create_map_curs_context(map_number)

# All frames/canvas created here
# Should be able to take any 'map number' and load it, even new maps dropped in later
# OR 'maps/areas loaded programmatically / in-game
    def create_map_curs_context(self, map_number):
        # GET MAP DIMENSIONS
        filename = 'map_info/map' + str(map_number) + '.txt'
        with open(filename) as f:
            map_size = f.read().splitlines()
        self.map = 'map' + str(map_number)
        self.map_width = int(map_size[0])
        self.map_height = int(map_size[1])
        # CREATE GRID FROM MAP DIMENSIONS
        col = self.map_width//100
        row = self.map_height//100
        self.grid = [[''] * row for i in range(col)]
        
        
        # CONTEXT MENU
        self.con_bg = ImageTk.PhotoImage(Image.open('scroll.png').resize((root.winfo_screenwidth(), 50)))
        self.context_menu = tk.Canvas(root, bg = 'black', bd=0, highlightthickness=0, relief='ridge', width = root.winfo_screenwidth(), height = 50)
        
#         self.context_menu.pack_propagate(0)
        
        self.context_menu.pack(side = 'top', fill = 'both', expand = 'false')
        
        self.context_menu.create_image(0, 0, anchor = 'nw', image = self.con_bg)
#         QUIT should have 'are you sure' popup
        self.quit = tk.Button(self.context_menu, text="QUIT", font = ('chalkduster', 24), fg="tan4", highlightbackground = 'tan3', command=self.master.destroy)
        self.quit.pack(side = 'right')
#         HELP
#         self.help_b = tk.Button(self.context_menu, text = 'Help', font = ('chalkduster', 24), fg="tan4", highlightbackground = 'tan3', command = self.help)
#         self.help_b.pack(side = 'right')
        # CANVAS
        
#         self.canvas_frame = tk.Frame(root)
#         self.canvas_frame.pack()

        # DEBUG THIS SHOULD NOT BE
        # setting inner frame/canvas to screenheight, when adding 'context menu' height, total is greater than screen
        # maybe subtract height of context menu
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        if self.map_width < width:
            width = self.map_width
        if self.map_height < height:
            height = self.map_height
        self.canvas = tk.Canvas(root, width = width, bg = 'black', height = height, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        # MAP
        self.map_img = ImageTk.PhotoImage(Image.open('./maps/map'+str(map_number)+'.jpg').resize((self.map_width, self.map_height)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        





#     def move_curs(self, event = None, dir = None):
#         if event == None:
#             event = Dummy()
#             event.keysym = None
#         frame_width = root.winfo_width()
#         frame_height = root.winfo_height()
#         if event.keysym == 'Left' or dir == 'Left':
#             if curs_pos[0] > 0: # leftmost possible cursor position, always zero
#                 self.canvas.move('curs', -100, 0)
#                 self.canvas.move(selected, -100, 0)
#                 curs_pos[0] -= 1
#                 grid_pos[0] -= 1
#             elif map_pos[0] > 0: # leftmost possible map position, always zero
#                 map_pos[0] -= 1
#                 self.move_map('Left')
#                 grid_pos[0] -= 1
#         elif event.keysym == 'Right' or dir == 'Right':
#             if grid_pos[0] == ((self.map_width//100) - 1):
#                 return
#             if curs_pos[0] < ((frame_width//100)-1):
#                 self.canvas.move('curs', 100, 0)
#                 self.canvas.move(selected, 100, 0)
#                 curs_pos[0] += 1
#                 grid_pos[0] += 1
#             elif map_pos[0] < ((self.map_width//100)-(frame_width//100)):
#                 self.move_map('Right')
#                 map_pos[0] += 1
#                 grid_pos[0] += 1
#         elif event.keysym == 'Up' or dir == 'Up':
#             if curs_pos[1] > 0: # topmost, always zero
#                 self.canvas.move('curs', 0, -100)
#                 self.canvas.move(selected, 0, -100)
#                 curs_pos[1] -= 1
#                 grid_pos[1] -= 1
#             elif map_pos[1] > 0: # topmost, always zero
#                 self.move_map('Down')
#                 map_pos[1] -= 1
#                 grid_pos[1] -= 1
#         elif event.keysym == 'Down' or dir == 'Down':
#             if grid_pos[1] == ((self.map_height//100)-1):
#                 return
#             if curs_pos[1] < ((frame_height//100)-1):
#                 self.canvas.move('curs', 0, 100)
#                 self.canvas.move(selected, 0, 100)
#                 curs_pos[1] += 1
#                 grid_pos[1] += 1
#             elif map_pos[1] < ((self.map_height//100)-(frame_height//100)):
#                 self.move_map('Up')
#                 map_pos[1] += 1
#                 grid_pos[1] += 1

#     def move_map(self, direction):
#         tmp = self.ent_dict.keys()
#         ents = [x for x in tmp if x != selected]
#         if direction == 'Left':
#             self.canvas.move('map', 100, 0)
#             self.moved_right -= 100
#             for ent in ents:
#                 self.canvas.move(ent, 100, 0)
#             for sqr in self.sqr_dict.keys():
#                 self.canvas.move(sqr, 100, 0)
#         elif direction == 'Right':
#             self.canvas.move('map', -100, 0)
#             self.moved_right += 100
#             for ent in ents:
#                 self.canvas.move(ent, -100, 0)
#             for sqr in self.sqr_dict.keys():
#                 self.canvas.move(sqr, -100, 0)
#         elif direction == 'Up':
#             self.canvas.move('map', 0, -100)
#             self.moved_down += 100
#             for ent in ents:
#                 self.canvas.move(ent, 0, -100)
#             for sqr in self.sqr_dict.keys():
#                 self.canvas.move(sqr, 0, -100)
#         elif direction == 'Down':
#             self.canvas.move('map', 0, 100)
#             self.moved_down -= 100
#             for ent in ents:
#                 self.canvas.move(ent, 0, 100)
#             for sqr in self.sqr_dict.keys():
#                 self.canvas.move(sqr, 0, 100)


root = tk.Tk()
# root.attributes('-transparent', True)
# root.attributes("-fullscreen", True)

# root.config(menu="")

# root.wm_attributes('-type', 'splash')


app = App(root)


# root.bind('<Right>', app.move_curs)
# root.bind('<Left>', app.move_curs)
# root.bind('<Up>', app.move_curs)
# root.bind('<Down>', app.move_curs)

# menubar = Menu(root)
# root.config(menu=menubar)
# 
# submenu = Menu(menubar)
# menubar.add_cascade(label="Submenu", menu=submenu)
# submenu.add_command(label="Option 1")
# submenu.add_command(label="Option 2")
# submenu.add_command(label="Option 3")
# 
# def remove_func():
#     emptyMenu = Menu(root)
#     root.config(menu=emptyMenu)
# 
# remove_button = Button(root, text="Remove", command=remove_func)
# remove_button.pack()

app.mainloop()