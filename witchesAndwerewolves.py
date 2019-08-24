# FINISH PICKUP after squares

# on curs_pickup, if ent.owner == active_player show movement(if any) and legal actions(if any)
# if not active_player owned, show info

# ent.mov should be a 'type', types return legal move squares given a starting square given a populated grid

# maybe use update_idletasks() to force 'redraw' while blocking/prevent race conditions

# speed up responsiveness by only animating 'on-screen' entities
# only call rotate_image() of 'on-screen' entities
# how to determine what is 'on-screen'?

# img.thumbnail() instead of .resize() will preserve aspect ratio, still takes two int tuple of MAX dimensions

# maybe use .resizable() to make sure window sizes according to screen size and then is not further resizable

# make different resolution images for portrait and in-game display

# maybe have 'summons' move independently once created, for instance the fullmoon auspice makes its 'forward movement' every turn

import tkinter as tk
from tkinter import ttk
# make sure import os works same for win/mac/linux
import os
from PIL import ImageTk,Image
from random import choice

# make sure works on win/mac/linux
# import pygame
# Witches... Theme, edit track for use as background
# set up the mixer
# freq = 44100     # audio CD quality
# bitsize = -16    # unsigned 16 bit
# channels = 1     # 1 is mono, 2 is stereo
# buffer = 1024    # number of samples (experiment to get right sound)
# pygame.mixer.init(freq, bitsize, channels, buffer)
# pygame.mixer.music.set_volume(0.7) # optional volume 0 to 1.0
# pygame.mixer.music.load('bloodMilkandSky.mp3')
# pygame.mixer.music.play(-1, 0)


# CURSOR GLOBALS, for determining where cursor is relative to edge of SCREEN/rootframe (not necessarily map)?
curs_pos = [0, 0]
# Used to determine if an object has been selected by the cursor
is_object_selected = False
selected = ''

# MAP POSITION GLOBALS, can i get rid of this and just use grid_pos????????
map_pos = [0, 0]

# GRID POSITION GLOBAL
grid_pos = [0,0]

class Dummy():
    def __init__(self):
        pass

class Sqr():
    def __init__(self, img, loc):
        self.img = img
        self.loc = loc
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in os.walk('animations/move/')][0]
        anims = [a for a in anims[:] if a[0] != '.']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/move/' + anim))
            self.anim_dict[i] = a
            
    def rotate_image(self):
        total_imgs = len(self.anim_dict.keys())-1
        if self.anim_counter == total_imgs:
            self.anim_counter = 0
        else:
            self.anim_counter += 1
        self.img = self.anim_dict[self.anim_counter]

class Entity():
    def __init__(self, name, img, loc, mov, owner):
        self.name = name
        self.img = img
        self.loc = loc
        # mov is one of witch, full, half, new, wax, wane
        self.mov = mov
        self.owner = owner
        
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in os.walk('./animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
            
    def legal_moves(self, width, height, grid):
        move_list = []
        # return list of tups (legal grid coords can move to)
        # move types witch, fullmoon, halfmoon, newmoon, waxing, waning
        if self.mov == 'witch':
            total_move = 3
            coord_pairs = [[x,y] for x in range(width//100) for y in range(height//100)]
            # for every coord pair in grid,
            # if abs(grid_pos[0]-ent.loc[0]) + abs(grid_pos[1]-ent.loc[1]) <= total_move(3),
            # if grid_pos is empty,
            # then add grid coord to legal moves list
            for coord in coord_pairs:
                if abs(coord[0] - self.loc[0]) + abs(coord[1] - self.loc[1]) <= total_move:
                    if grid[coord[0]][coord[1]] == '':
                        move_list.append(coord)
            return move_list
            
        elif self.mov == 'full':
            pass
        elif self.mov == 'half':
            pass
        elif self.mov == 'new':
            pass
        elif self.mov == 'wax':
            pass
        elif self.mov == 'wane':
            pass
    
    def rotate_image(self):
        total_imgs = len(self.anim_dict.keys())-1
        if self.anim_counter == total_imgs:
            self.anim_counter = 0
        else:
            self.anim_counter += 1
        self.img = self.anim_dict[self.anim_counter]

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.img_dict = {}
        self.ent_dict = {}
        self.sqr_dict = {}
        self.active_player = 'p1'
        self.opponent = 'computer'
        self.moved_right = 0
        self.moved_down = 0
        
        self.choose_map()
        
    def choose_map(self):
        self.marquee = tk.Label(root, text = 'Choose your map', font=("Helvetica", 36))
        self.marquee.pack(side = 'top')
        # CHOOSE MAPS
        maps = [m for r,d,m in os.walk('./maps')][0]
        self.map_button_list = []
        self.tmp_mapimg_dict = {}
        for i,map in enumerate(maps):
            b = ttk.Button(root)
            cmd = lambda indx = i : self.load_map(indx)
            photo = ImageTk.PhotoImage(Image.open('./maps/' + map).resize((300,300)))
            # should use temp img_dict tied to this popup, currently is not a popup !!!!!!!!!
            # or just destroy the unused img_dict entries
            self.tmp_mapimg_dict['map'+str(i)] = photo
            b.config(image = self.tmp_mapimg_dict['map'+str(i)], command = cmd)
            b.pack(side = 'left')
            self.map_button_list.append(b)
            
    def load_map(self, map_number):
        self.marquee.destroy()
        del self.tmp_mapimg_dict
        for b in self.map_button_list:
            b.destroy()
        del self.map_button_list
        self.create_map_curs(map_number)
            
    def create_map_curs(self, map_number):
        # Get map dimensions
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
        # CANVAS
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        if self.map_width < width:
            width = self.map_width
        if self.map_height < height:
            height = self.map_height
        self.canvas = tk.Canvas(root, width = width, height = height)  
        self.canvas.pack()
        # MAP
        self.map_img = ImageTk.PhotoImage(Image.open('./maps/map'+str(map_number)+'.jpg').resize((self.map_width, self.map_height)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.choose_witch()
        
    def choose_witch(self):
        self.avatar_popup = tk.Toplevel()
#         avatar_popup.grab_set()
#         somewhere need to pair the above line with avatar_popup.grab_release()
        self.avatar_popup.title('Choose Your Witch')
        witches = [w for r,d,w in os.walk('./avatars')][0]
        witches = [w for w in witches[:] if w[0] != '.']
        self.avatar_popup.witch_widgets = []
        self.avatar_popup.img_dict = {}
        for i,witch in enumerate(witches):
            f = tk.Frame(self.avatar_popup)
            f.pack(side = 'left')
            self.avatar_popup.witch_widgets.append(f)
            b = ttk.Button(f)
            cmd = lambda w = witch[:-4] : self.load_witch(w)
            # Make higher resolution images for here, upsampling and losing image quality !!!!!!!!!!
            photo = ImageTk.PhotoImage(Image.open('./avatars/' + witch).resize((200,200)))
            self.avatar_popup.img_dict[witch] = photo
            b.config(image = self.avatar_popup.img_dict[witch], command = cmd)
            b.pack(side = 'top')
            info = lambda w = witch[:-4] : self.show_avatar_info(w)
            b2 = tk.Button(f)
            whtspc_txt = witch[:-4].replace('_', ' ')
            b2.config(text = whtspc_txt + '\n' + 'info', command = info)
            b2.pack(side = 'bottom')
            self.avatar_popup.witch_widgets.append(b2)
            self.avatar_popup.witch_widgets.append(b)

    def show_avatar_info(self, witch):
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
        self.protag_witch = witch
        protag_witch_img = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png'))
        self.ent_dict[witch] = Entity(name = witch, img = protag_witch_img, loc = [1, 1], mov = 'witch', owner = 'p1')
        self.canvas.create_image(self.ent_dict[witch].loc[0], self.ent_dict[witch].loc[1], image = self.ent_dict[witch].img, tags = witch)
        self.grid[self.ent_dict[witch].loc[0]][self.ent_dict[witch].loc[1]] = witch
        self.avatar_popup.destroy()
        self.place_antag()
    
    def place_antag(self):
        remain_witches = [w for r,d,w in os.walk('./avatars')][0]
        remain_witches = [w for w in remain_witches[:] if w[0] != '.']
        remain_witches = [w[:-4] for w in remain_witches[:]] 
        remain_witches.remove(self.protag_witch)
        self.antag_witch = choice(remain_witches)
        antag_witch_img = ImageTk.PhotoImage(Image.open('avatars/' + self.antag_witch +'.png'))
        self.ent_dict[self.antag_witch] = Entity(name = self.antag_witch, img = antag_witch_img, loc = [self.map_width//100-1, self.map_height//100-1], mov = 'witch', owner = 'p2')
        self.canvas.create_image(self.ent_dict[self.antag_witch].loc[0], self.ent_dict[self.antag_witch].loc[1], image = self.ent_dict[self.antag_witch].img, tags = self.antag_witch)
        self.grid[(self.map_width//100)-1][(self.map_height//100)-1] = self.antag_witch
        # ANIMATE / START_ACTION
        self.animate()
        self.start_action()
        
        
        # Should now call 'FIRST TURN'
        # 1 player at first, but keep in mind 2nd player action
        # make struct of actions-taken/takeable
        # allow for move/summon/spell/summon-action in any order
        # each entity tracks 'if moved' per turn, reset end of round
        # on cursor over, if owned by 'active-player', pickup shows potential move-squares, 'i' shows 'info'
        # 'z' brings up context menu for 'selected', on 'place'-->are you sure place here?, prevent misclick likelihood,
        # on each turn switch 'focus' bring cursor to avatar,
    
    def start_action(self):
        p = self.active_player
        print('start action')
        # Focus on protag
        w = self.protag_witch if p == 'p1' else self.antag_witch
        self.get_focus(w)
        # 
        
            
        
    def get_focus(self, w):
        while grid_pos[0] < self.ent_dict[w].loc[0]:
            self.move_curs(dir = 'Right')
        while grid_pos[0] > self.ent_dict[w].loc[0]:
            self.move_curs(dir = 'Left')
        while grid_pos[1] < self.ent_dict[w].loc[1]:
            self.move_curs(dir = 'Down')
        while grid_pos[1] > self.ent_dict[w].loc[1]:
            self.move_curs(dir = 'Up')
        
    def animate(self):
        for ent in self.ent_dict.keys():
            if ent != selected:
                self.ent_dict[ent].rotate_image()
                self.canvas.delete(ent)
                self.canvas.create_image(self.ent_dict[ent].loc[0]*100+50-self.moved_right, self.ent_dict[ent].loc[1]*100+50-self.moved_down, image = self.ent_dict[ent].img, tags = ent)
        for sqr in self.sqr_dict.keys():
            self.sqr_dict[sqr].rotate_image()
            self.canvas.delete(sqr)
            self.canvas.create_image(self.sqr_dict[sqr].loc[0]*100+50-self.moved_right, self.sqr_dict[sqr].loc[1]*100+50-self.moved_down, image = self.sqr_dict[sqr].img, tags = sqr)
        root.after(1000, self.animate)
    
    def pickup_putdown(self, event):
        global is_object_selected, selected, curs_pos
        # PICK UP
        if is_object_selected == False and self.current_pos() != '':
            is_object_selected = True
            unit = self.current_pos()
            # check if owned
            if self.ent_dict[unit].owner == self.active_player:
                # show mov (if any), avail actions (if any)
                sqrs = self.ent_dict[unit].legal_moves(self.map_width, self.map_height, self.grid)
                # show 'highlight image' over legal sqrs
                for i, sqr in enumerate(sqrs):
                    img = ImageTk.PhotoImage(Image.open('animations/move/0.png'))
                    self.sqr_dict['sqr'+str(i)] = Sqr(img, sqr)
                    # sqr location needs to be modified by moved_up/down
                    self.canvas.create_image(sqr[0]*100+50-self.moved_right, sqr[1]*100+50-self.moved_down, image = self.sqr_dict['sqr'+str(i)].img, tags = 'sqr'+str(i))
                    
            # Only change loc/move if able (owned by active_player
            self.ent_dict[unit].loc = [None, None]
            selected = unit
            self.grid[grid_pos[0]][grid_pos[1]] = ''
        # PUT DOWN
        elif is_object_selected == True and self.current_pos() == '':
            # erase old sqrs
            for sqr in self.sqr_dict.keys():
                self.canvas.delete(sqr)
            self.sqr_dict = {}
            is_object_selected = False
            unit = selected
            selected = ''
            self.ent_dict[unit].loc = grid_pos[:]
            self.grid[grid_pos[0]][grid_pos[1]] = unit
    
    def move_curs(self, event = None, dir = None):
        if event == None:
            event = Dummy()
            event.keysym = None
        frame_width = root.winfo_width()
        frame_height = root.winfo_height()
        if event.keysym == 'Left' or dir == 'Left':
            if curs_pos[0] > 0: # leftmost possible cursor position, always zero
                self.canvas.move('curs', -100, 0)
                self.canvas.move(selected, -100, 0)
                curs_pos[0] -= 1
                grid_pos[0] -= 1
            elif map_pos[0] > 0: # leftmost possible map position, always zero
                map_pos[0] -= 1
                self.move_map('Left')
                grid_pos[0] -= 1
        elif event.keysym == 'Right' or dir == 'Right':
            if grid_pos[0] == ((self.map_width//100) - 1):
                return
            if curs_pos[0] < ((frame_width//100)-1):
                self.canvas.move('curs', 100, 0)
                self.canvas.move(selected, 100, 0)
                curs_pos[0] += 1
                grid_pos[0] += 1
            elif map_pos[0] < ((self.map_width//100)-(frame_width//100)):
                self.move_map('Right')
                map_pos[0] += 1
                grid_pos[0] += 1
        elif event.keysym == 'Up' or dir == 'Up':
            if curs_pos[1] > 0: # topmost, always zero
                self.canvas.move('curs', 0, -100)
                self.canvas.move(selected, 0, -100)
                curs_pos[1] -= 1
                grid_pos[1] -= 1
            elif map_pos[1] > 0: # topmost, always zero
                self.move_map('Down')
                map_pos[1] -= 1
                grid_pos[1] -= 1
        elif event.keysym == 'Down' or dir == 'Down':
            if grid_pos[1] == ((self.map_height//100)-1):
                return
            if curs_pos[1] < ((frame_height//100)-1):
                self.canvas.move('curs', 0, 100)
                self.canvas.move(selected, 0, 100)
                curs_pos[1] += 1
                grid_pos[1] += 1
            elif map_pos[1] < ((self.map_height//100)-(frame_height//100)):
                self.move_map('Up')
                map_pos[1] += 1
                grid_pos[1] += 1


    def move_map(self, direction):
        tmp = self.ent_dict.keys()
        ents = [x for x in tmp if x != selected]
        if direction == 'Left':
            self.canvas.move('map', 100, 0)
            self.moved_right -= 100
            for ent in ents:
                self.canvas.move(ent, 100, 0)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 100, 0)
        elif direction == 'Right':
            self.canvas.move('map', -100, 0)
            self.moved_right += 100
            for ent in ents:
                self.canvas.move(ent, -100, 0)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, -100, 0)
        elif direction == 'Up':
            self.canvas.move('map', 0, -100)
            self.moved_down += 100
            for ent in ents:
                self.canvas.move(ent, 0, -100)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 0, -100)
        elif direction == 'Down':
            self.canvas.move('map', 0, 100)
            self.moved_down -= 100
            for ent in ents:
                self.canvas.move(ent, 0, 100)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 0, 100)

    # Helper functions
    def current_pos(self):
        return self.grid[grid_pos[0]][grid_pos[1]]

root = tk.Tk()
app = App(master=root)


root.bind('<Right>', app.move_curs)
root.bind('<Left>', app.move_curs)
root.bind('<Up>', app.move_curs)
root.bind('<Down>', app.move_curs)
root.bind('<space>', app.pickup_putdown)

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry('%sx%s' % (width, height))

app.mainloop()