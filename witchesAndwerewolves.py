# put 'instructions', bound keys in context menu, maybe use same key for all 'cancels' ie cancel move/context buttons

# bind different key for 'actions', separate from 'movement/pickup_putdown'
# actions include summon, spell, summon-actions(attack or special)
# should 'place barrier' be separate action or result of spell?

# start thinking about what map and map animation to use

# maybe take photo for portrait background instead of scroll texture

# splash screen?

# speed up responsiveness by only animating 'on-screen' entities
# only call rotate_image() of 'on-screen' entities
# how to determine what is 'on-screen'?

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


# CURSOR GLOBALS
curs_pos = [0, 0]
# Used to determine if an object has been selected by the cursor
is_object_selected = False
selected = ''

# MAP POSITION GLOBAL
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
    def __init__(self, name, img, loc, owner):
        self.name = name
        self.img = img
        self.loc = loc
        self.owner = owner
        self.has_moved = False
        self.origin = []
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in os.walk('./animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
            
    def info(self):
        self.info_popup = tk.Toplevel()
        info_label = tk.Label(self.info_popup, text = self.name +'/n'+ self.__class__.__name__)
        info_label.pack()
        close = tk.Button(self.info_popup, text = 'close', command = self.info_popup.destroy)
        close.pack()
    
    def rotate_image(self):
        total_imgs = len(self.anim_dict.keys())-1
        if self.anim_counter == total_imgs:
            self.anim_counter = 0
        else:
            self.anim_counter += 1
        self.img = self.anim_dict[self.anim_counter]

class Witch(Entity):
    def __init__(self, name, img, loc, owner):
        self.actions = {'spell':self.spell, 'summon':self.summon}
        self.spell_used = False
        self.summon_used = False
        self.spell_dict = {}
        if name == 'Agnes_Sampson':
            self.spell_dict['horrid wilting'] = self.horrid_wilting
        elif name == 'Fakir_Ali':
            self.spell_dict['plague'] = self.plague
        elif name == 'Morgan_LeFay':
            self.spell_dict['enchant'] = self.enchant
            
        super().__init__(name, img, loc, owner)
        
    def spell(self):
        # if spell_used == False, create spell popup, upon cast set self.spell_used = True
        if self.spell_used == True:
            return
        print('spell cast')
        # spell Toplevel
        self.spell_popup = tk.Toplevel()
        for name, spell in self.spell_dict.items():
            b1 = tk.Button(self.spell_popup, text = name, command = self.spell_dict[name])
            b1.pack()
    
    def summon(self):
        # if summon_used == False, create summon popup, upon summon set self.summon_used = True
        if self.summon_used == True:
            return
        print('summon')
        self.summon_used = True
        
    def enchant(self):
        print('enchant')
        self.spell_used = True
        self.spell_popup.destroy()
        
    def plague(self):
        print('plague')
        self.spell_used = True
        self.spell_popup.destroy()
        
    def horrid_wilting(self):
        print('wilt')
        self.spell_used = True
        self.spell_popup.destroy()
    
    def legal_moves(self, width, height, grid):
        if self.has_moved == True:
            return []
        move_list = []
        total_move = 3
        coord_pairs = [[x,y] for x in range(width//100) for y in range(height//100)]
        for coord in coord_pairs:
            if abs(coord[0] - self.loc[0]) + abs(coord[1] - self.loc[1]) <= total_move:
                if grid[coord[0]][coord[1]] == '':
                    move_list.append(coord)
        return move_list

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
        self.marquee = tk.Label(root, text = 'Choose your map', fg = 'tan3', bg = 'black', font=("chalkduster", 36))
        self.marquee.pack(side = 'top')
        # CHOOSE MAPS
        maps = [m for r,d,m in os.walk('./maps')][0]
        self.map_button_list = []
        self.tmp_mapimg_dict = {}
        for i,map in enumerate(maps):
            b = tk.Button(root)
            cmd = lambda indx = i : self.load_map(indx)
            photo = ImageTk.PhotoImage(Image.open('./maps/' + map).resize((300,300)))
            self.tmp_mapimg_dict['map'+str(i)] = photo
            b.config(image = self.tmp_mapimg_dict['map'+str(i)], bg = 'black', highlightbackground = 'tan4', command = cmd)
            b.pack(side = 'left')
            self.map_button_list.append(b)
            
    def load_map(self, map_number):
        self.marquee.destroy()
        del self.tmp_mapimg_dict
        for b in self.map_button_list:
            b.destroy()
        del self.map_button_list
        self.create_map_curs_context(map_number)
            
    def create_map_curs_context(self, map_number):
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
        # CONTEXT MENU
        self.con_bg = ImageTk.PhotoImage(Image.open('scroll.png').resize((root.winfo_screenwidth(), 50)))
        self.context_menu = tk.Canvas(root, bg = 'black', bd=0, highlightthickness=0, relief='ridge', width = root.winfo_screenwidth(), height = 50)
        self.context_menu.pack_propagate(0)
        self.context_menu.pack(side = 'top', fill = 'both', expand = 'false')
        self.context_menu.create_image(0, 0, anchor = 'nw', image = self.con_bg)
        # quit should have 'are you sure' popup
        self.quit = tk.Button(self.context_menu, text="QUIT", font = ('chalkduster', 24), fg="tan4", highlightbackground = 'tan3',
                              command=self.master.destroy)
        bw = self.context_menu.create_window(root.winfo_screenwidth(), 0, anchor='ne', window=self.quit)
        # CANVAS
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        if self.map_width < width:
            width = self.map_width
        if self.map_height < height:
            height = self.map_height
        self.canvas = tk.Canvas(self.canvas_frame, width = width, bg = 'black', height = height, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        # MAP
        self.map_img = ImageTk.PhotoImage(Image.open('./maps/map'+str(map_number)+'.jpg').resize((self.map_width, self.map_height)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')

        
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        self.choose_witch()
        
    def choose_witch(self):
        self.avatar_popup = tk.Toplevel()
#         avatar_popup.grab_set()
#         somewhere need to pair the above line with avatar_popup.grab_release()
        self.avatar_popup.title('Choose Your Witch')
        witches = [w for r,d,w in os.walk('./portraits/')][0]
        witches = [w for w in witches[:] if w[0] != '.']
        self.avatar_popup.witch_widgets = []
        self.avatar_popup.img_dict = {}
        for i,witch in enumerate(witches):
            f = tk.Frame(self.avatar_popup, bg = 'black')
            f.pack(side = 'left')
            self.avatar_popup.witch_widgets.append(f)
            b = tk.Button(f)
            cmd = lambda w = witch[:-4] : self.load_witch(w)
            photo = ImageTk.PhotoImage(Image.open('./portraits/' + witch))
            self.avatar_popup.img_dict[witch] = photo
            b.config(image = self.avatar_popup.img_dict[witch],highlightbackground='tan3', highlightthickness = 1, command = cmd)
            b.pack(side = 'top')
            info = lambda w = witch[:-4] : self.show_avatar_info(w)
            b2 = tk.Button(f)
            whtspc_txt = witch[:-4].replace('_', ' ')
            b2.config(text = whtspc_txt, highlightbackground='tan3', highlightthickness= 1, fg = 'tan3', font = ('chalkduster', 24), command = info)
            b2.pack(side = 'bottom')
            self.avatar_popup.witch_widgets.append(b2)
            self.avatar_popup.witch_widgets.append(b)

    def show_avatar_info(self, witch):
        info_popup = tk.Toplevel()
        info_popup.title(witch)
        text = open('avatar_info/' + witch + '.txt', 'r').read()
        f = tk.Frame(info_popup)
        f.pack()
        l = tk.Label(f, text = text, font = ('chalkduster', 24))
        l.pack()
        close = tk.Button(info_popup, text = 'close', font = ('chalkduster', 24), command = info_popup.destroy)
        close.pack()
    
    def load_witch(self, witch):
        self.protag_witch = witch
        protag_witch_img = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png'))
        self.ent_dict[witch] = Witch(name = witch, img = protag_witch_img, loc = [1, 1], owner = 'p1')
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
        self.ent_dict[self.antag_witch] = Witch(name = self.antag_witch, img = antag_witch_img, loc = [self.map_width//100-1, self.map_height//100-1], owner = 'p2')
        self.canvas.create_image(self.ent_dict[self.antag_witch].loc[0], self.ent_dict[self.antag_witch].loc[1], image = self.ent_dict[self.antag_witch].img, tags = self.antag_witch)
        self.grid[(self.map_width//100)-1][(self.map_height//100)-1] = self.antag_witch
        # ANIMATE / START_ACTION
        self.animate()
        self.start_action()
        
        
    
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
        root.after(500, self.animate)
    
    def populate_context(self, event):
        # should show name of ent that populated
        e = self.current_pos()
        if e == '':
            return
        if self.context_menu.pack_slaves() != []:
            return
        act_dict = self.ent_dict[e].actions
        b = tk.Button(self.context_menu, text = e, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = self.ent_dict[e].info)
        b.pack(side = 'left')
        # remove buttons after used
        for act, call in act_dict.items():
            b = tk.Button(self.context_menu, text = act, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = call)
            b.pack(side = 'left') 
        
    def depopulate_context(self, event):
        for b in self.context_menu.pack_slaves():
            b.destroy()
        print('depop')
    
    def cancel_pickup(self, event):
        global is_object_selected, selected
        if is_object_selected == True:
            for sqr in self.sqr_dict.keys():
                self.canvas.delete(sqr)
            self.sqr_dict = {}
            self.grid[self.ent_dict[selected].origin[0]][self.ent_dict[selected].origin[1]] = selected
            # return selected entity to sqr of origin
            self.canvas.delete(selected)
            self.canvas.create_image(self.ent_dict[selected].origin[0]*100+50-self.moved_right, self.ent_dict[selected].origin[1]*100+50-self.moved_down, image = self.ent_dict[selected].img, tags = selected)
            self.ent_dict[selected].loc = self.ent_dict[selected].origin[:]
            w = selected
            is_object_selected = False
            selected = ''
            self.get_focus(w)
    
    def pickup_putdown(self, event):
        global is_object_selected, selected, curs_pos
        # PICK UP
        if is_object_selected == False and self.current_pos() != '':
            unit = self.current_pos()
            if self.ent_dict[unit].owner == self.active_player and self.ent_dict[unit].has_moved == False:
                is_object_selected = True
                # SQUARES / MOVEMENT
                sqrs = self.ent_dict[unit].legal_moves(self.map_width, self.map_height, self.grid)
                for i, sqr in enumerate(sqrs):
                    img = ImageTk.PhotoImage(Image.open('animations/move/0.png'))
                    self.sqr_dict['sqr'+str(i)] = Sqr(img, sqr)
                    self.canvas.create_image(sqr[0]*100+50-self.moved_right, sqr[1]*100+50-self.moved_down, image = self.sqr_dict['sqr'+str(i)].img, tags = 'sqr'+str(i))
                self.ent_dict[unit].origin = self.ent_dict[unit].loc[:]
                self.ent_dict[unit].loc = [None, None]
                selected = unit
                # REMOVE UNIT FROM GRID
                self.grid[grid_pos[0]][grid_pos[1]] = ''
            # ELSE SHOW INFO
            elif self.ent_dict[unit].owner != self.active_player:
                print('not yours')
        # PUT DOWN
        elif is_object_selected == True and self.current_pos() == '':
            # Restrict movement, if grid_pos is within highlighted sqrs
            sqrs = [self.sqr_dict[s].loc for s in self.sqr_dict.keys()]
            if grid_pos not in sqrs:
                return
            self.ent_dict[selected].has_moved = True
            # erase old sqrs
            for sqr in self.sqr_dict.keys():
                self.canvas.delete(sqr)
            self.sqr_dict = {}
            is_object_selected = False
            unit = selected
            selected = ''
            self.ent_dict[unit].loc = grid_pos[:]
            self.ent_dict[unit].origin = grid_pos[:]
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
root.bind('<z>', app.cancel_pickup)
root.bind('<a>', app.populate_context)
root.bind('<q>', app.depopulate_context)

root.configure(background = 'black')

# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry('%sx%s' % (width, height))

app.mainloop()