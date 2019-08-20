# what about when map dimension is smaller than the screen/frame size? currently the cursor moves to the edge of the frame, not the true map edge unless map is bigger than the frame
# in the above case, should restrain/resize the dimensions of the root frame to the dimensions of the map

# be able to load different size maps and still move background/cursor
# to do this: on load get screensize width/height and round down to the nearest 100pixels, freeze window size/no resizing OR on each screen resize event will have to redo grid fitting, 

# make different resolution images for portrait and in-game display

# maybe have 'summons' move independently once created, for instance the fullmoon auspice makes its 'forward movement' every turn

# make 'animations', image is updated using 'after' to rotate through series of images
# so each animation will have corresponding dictionary/atlas? of images

# constrain 'magic numbers' to size relative to screen/frame size instead of pixels except with movement/borders to avoid partial fractions

import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk,Image



# import pygame
# Witches... Theme, edit track for use as background
# background_music = "bloodMilkandSky.mp3"
# os.system("afplay " + background_music)

# set up the mixer
# freq = 44100     # audio CD quality
# bitsize = -16    # unsigned 16 bit
# channels = 1     # 1 is mono, 2 is stereo
# buffer = 1024    # number of samples (experiment to get right sound)
# pygame.mixer.init(freq, bitsize, channels, buffer)
# pygame.mixer.music.set_volume(0.7) # optional volume 0 to 1.0
# pygame.mixer.music.load('bloodMilkandSky.mp3')
# pygame.mixer.music.play(-1, 0)


# CURSOR GLOBALS
curs_pos = [0, 0]
is_object_selected = False
selected = ''

# MAP POSITION GLOBALS
map_pos = [0, 0]

# GRID GLOBALS grid[0][0] to grid[35][23]
# should constrain this dynamically by variable size of map
grid_pos = [0,0]
col = 24
row = 36
grid = [[''] * row for i in range(col)]

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.img_dict = {}
        self.choose_map()
#         self.create_map_curs()
#         self.create_units()
        
        
        

    def choose_map(self):
        self.marquee = tk.Label(root, text = 'Choose your map', font=("Helvetica", 36))
        self.marquee.pack(side = 'top')
        # CHOOSE MAPS
        maps = [m for r,d,m in os.walk('./maps')][0]
        self.map_button_list = []
        for i,map in enumerate(maps):
            b = ttk.Button(root)
            cmd = lambda indx = i : self.load_map(indx)
            photo = ImageTk.PhotoImage(Image.open('./maps/' + map).resize((300,300)))
            self.img_dict['map'+str(i)] = photo
            b.config(image = self.img_dict['map'+str(i)], command = cmd)
            b.pack(side = 'left')
            self.map_button_list.append(b)
            
    def load_map(self, map_number):
        self.marquee.destroy()
        for b in self.map_button_list:
            b.destroy()
        self.create_map_curs(map_number)
            
    def create_map_curs(self, map_number):
        # CANVAS
        self.canvas = tk.Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())  
        self.canvas.pack()
        filename = 'map_info/map' + str(map_number) + '.txt'
        with open(filename) as f:
            map_size = f.read().splitlines() 
        # MAP, gives 24X36 grid
        self.map_width = int(map_size[0])
        self.map_height = int(map_size[1])
        self.map_img = ImageTk.PhotoImage(Image.open('./maps/map'+str(map_number)+'.jpg').resize((self.map_width, self.map_height)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        print(self.canvas.bbox('map'))
        
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.choose_witch()
#         root.after(700, self.place_witch)
        
    def choose_witch(self):
        self.avatar_popup = tk.Toplevel()
#         avatar_popup.grab_set()
#         somewhere need to pair the above line with avatar_popup.grab_release()
        self.avatar_popup.title('Choose Your Witch')
        witches = [w for r,d,w in os.walk('./avatars')][0]
        self.avatar_popup.witch_widgets = []
        # for each witch, create frame pack left, create image button pack top, create info/name button pack center bottom
        for i,witch in enumerate(witches):
            f = tk.Frame(self.avatar_popup)
            f.pack(side = 'left')
            self.avatar_popup.witch_widgets.append(f)
            b = ttk.Button(f)
            cmd = lambda w = witch[:-4] : self.load_witch(w)
            photo = ImageTk.PhotoImage(Image.open('./avatars/' + witch).resize((200,200)))
            self.img_dict[witch] = photo
            b.config(image = self.img_dict[witch], command = cmd)
            b.pack(side = 'top')
            info = lambda w = witch[:-4] : self.show_avatar_info(w)
            b2 = tk.Button(f)
            whtspc_txt = witch[:-4].replace('_', ' ')
            b2.config(text = whtspc_txt + '\n' + 'info', command = info)
            b2.pack(side = 'bottom')
            self.avatar_popup.witch_widgets.append(b2)
            self.avatar_popup.witch_widgets.append(b)

    def show_avatar_info(self, witch):
        # create popup window with text for corresponding avatar
        info_popup = tk.Toplevel()
        info_popup.title(witch)
        text = open('avatar_info/' + witch + '.txt', 'r').read()
        f = tk.Frame(info_popup)
        f.pack()
        l = tk.Label(f, text = text)
        l.pack()
        close = tk.Button(info_popup, text = 'close', command = info_popup.destroy)
        close.pack()
    
    def load_witch(self, witch):
        print(witch)
        # destroy avatar_popup, destroy img_dict items, place witch at 0,0, place an opposing witch, kickoff play
        self.img_dict = {}
        self.witch_tag = witch
        self.protag_witch = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png').resize((100, 100)))
        self.canvas.create_image(0, 0, anchor='nw', image = self.protag_witch, tags = self.witch_tag)
        self.img_dict[witch] = [0,0]
        grid[0][0] = witch
        self.avatar_popup.destroy()
    
    def create_units(self):
        #
        self.wolfy = ImageTk.PhotoImage(Image.open("wolfy.png").resize((100,100)))
        c = 7
        r = 3
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.wolfy, tags = 'wolfy')
        self.img_dict['wolfy'] = [c,r]
        grid[c][r] = 'wolfy'
        #
    
    # needs to delete object from grid on pickup
    def pickup_putdown(self, event):
        global is_object_selected, selected, curs_pos, grid
        # 'pick up' unit, check what/if unit in space, remove from img_dict, put in selected
        if is_object_selected == False and current_pos() != '':
            is_object_selected = True
            unit = current_pos()
            del self.img_dict[unit]
            selected = unit
            grid[grid_pos[0]][grid_pos[1]] = ''
        # 'put down' unit, check that grid is empty, remove unit from selected, put in img_dict
        elif is_object_selected == True and current_pos() == '':
            is_object_selected = False
            unit = selected
            selected = ''
            self.img_dict[unit] = grid_pos[:]
            grid[grid_pos[0]][grid_pos[1]] = unit
    
    # map-    2400, 36000
    # screen- 1280, 800
    # cx - 11 or 1280//100 minus 1
    # mx - 12 or 2400//100 minus (cx+1)
    # cy - 6 or 800//100 minus 2 (reason for minus 2 here is for space from other vertical widgets)
    # my - 29 or 3600//100 minus (cy+1)
    # replace static values with variables described beside them
    
    # Need to constrain cursor_pos/map_pos/grid_pos to max of grid_size?
    # below works unless window gets manually resized in between movement, which allows cursor to move 'off map'
    def move_curs(self, event):
        frame_width = root.winfo_width()
        frame_height = root.winfo_height()
        if event.keysym == 'Left':
            if curs_pos[0] > 0: # leftmost possible cursor position, always zero
                self.canvas.move('curs', -100, 0)
                self.canvas.move(selected, -100, 0)
                curs_pos[0] -= 1
                grid_pos[0] -= 1
            elif map_pos[0] > 0: # leftmost possible map position, always zero
                map_pos[0] -= 1
                self.move_map('Left')
                grid_pos[0] -= 1
        elif event.keysym == 'Right':
            if curs_pos[0] < ((frame_width//100)-1): # 11 or width of ((framesize//100)-1)
                self.canvas.move('curs', 100, 0)
                self.canvas.move(selected, 100, 0)
                curs_pos[0] += 1
                grid_pos[0] += 1
            elif map_pos[0] < ((self.map_width//100)-(frame_width//100)): # 12 or rightmost position of map, width of (map_size//100) minus frame_width//100 plus 1
                self.move_map('Right')
                map_pos[0] += 1
                grid_pos[0] += 1
        elif event.keysym == 'Up':
            if curs_pos[1] > 0: # topmost, always zero
                self.canvas.move('curs', 0, -100)
                self.canvas.move(selected, 0, -100)
                curs_pos[1] -= 1
                grid_pos[1] -= 1
            elif map_pos[1] > 0: # topmost, always zero
                self.move_map('Down')
                map_pos[1] -= 1
                grid_pos[1] -= 1
        elif event.keysym == 'Down':
            if curs_pos[1] < ((frame_height//100)-1): # 6 or screenheight//100 minus 2
                self.canvas.move('curs', 0, 100)
                self.canvas.move(selected, 0, 100)
                curs_pos[1] += 1
                grid_pos[1] += 1
            elif map_pos[1] < ((self.map_height//100)-(frame_height//100)): # 29 or mapheight//100 minus (cy+1)
                self.move_map('Up')
                map_pos[1] += 1
                grid_pos[1] += 1


    def move_map(self, direction):
        if direction == 'Left':
            self.canvas.move('map', 100, 0)
            for img in self.img_dict.keys():
                self.canvas.move(img, 100, 0)
        elif direction == 'Right':
            self.canvas.move('map', -100, 0)
            for img in self.img_dict.keys():
                self.canvas.move(img, -100, 0)
        elif direction == 'Up':
            self.canvas.move('map', 0, -100)
            for img in self.img_dict.keys():
                self.canvas.move(img, 0, -100)
        elif direction == 'Down':
            self.canvas.move('map', 0, 100)
            for img in self.img_dict.keys():
                self.canvas.move(img, 0, 100)





# Helper functions
def current_pos():
    return grid[grid_pos[0]][grid_pos[1]]


root = tk.Tk()
app = App(master=root)


root.bind('<Right>', app.move_curs)
root.bind('<Left>', app.move_curs)
root.bind('<Up>', app.move_curs)
root.bind('<Down>', app.move_curs)
root.bind('<space>', app.pickup_putdown)


# set window size to screen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# root.geometry('%sx%s' % (width, height))
print('width is ', width)
print('height is ', height)

app.mainloop()