# fix/organize imports later, just double importing now
# also doesnt work, refers to 'app' but only for summon placement, seems to work for witch movement

import tkinter as tk
from tkinter import ttk
# make sure import os works same for win/mac/linux
import os
from PIL import ImageTk,Image
from random import choice

root = tk.Tk()

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
        # DEBUG, protags are referred to as .name, summons are disambiguated by .number
        # this is fine here, but displays summon 'number', maybe should hide completely
        info_label = tk.Label(self.info_popup, text = self.name +'\n'+ self.__class__.__name__)
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

class Summon(Entity):
    def __init__(self, name, img, loc, owner, number):
        self.number = number
        # ADD MOVEMENT / ACTIONS
        super().__init__(name, img, loc, owner)
        
class Warrior(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.attack}
        super().__init__(name, img, loc, owner, number)
        
    def attack(self):
        # after button press, highlight legal sqrs, cursor over sqr, 'confirm target' button which only
        # has effect when over legal target/sqr, 'confirm target' legal press should destroy buttons, destroy
        # sqrs, set self.has_acted? to True, plus actual effects of attack
        print('attack')
    
    def legal_moves(self, width, height, grid):
        move_list = []
        total_move = 3
        coord_pairs = [[x,y] for x in range(width//100) for y in range(height//100)]
        for coord in coord_pairs:
            if grid[coord[0]][coord[1]] == '':
                if app.active_player == 'p1':
                    if self.loc[0] == coord[0] and self.loc[1] < coord[1] < self.loc[1]+4:
                        move_list.append(coord)
                elif app.active_player == 'p2':
                    if self.loc[0] == coord[0] and self.loc[1] < coord[1] < self.loc[1]-4:
                        move_list.append(coord)
        return move_list
                    
class Witch(Entity):
    def __init__(self, name, img, loc, owner):
        self.actions = {'spell':self.spell, 'summon':self.summon}
        self.spell_used = False
        self.summon_used = False
        self.spell_dict = {}
        self.summon_dict = {}
        self.placement_buttons = []
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
        b2 = tk.Button(self.spell_popup, text = 'Cancel', command = self.spell_popup.destroy)
        b2.pack()
    
    def summon(self):
        # if summon_used == False, create summon popup, upon summon set self.summon_used = True
        if self.summon_used == True:
            return
        print('summon')
        self.summon_popup = tk.Toplevel()
        b1 = tk.Button(self.summon_popup, text = 'Warrior', command = self.place_warrior)
        b1.pack()
#         b2 = tk.Button(self.summon_popup, text = 'Trickster', command = self.place_trickster)
#         b2.pack()
#         b3 = tk.Button(self.summon_popup, text = 'Shadow', command = self.place_shadow)
#         b3.pack()
#         b4 = tk.Button(self.summon_popup, text = 'Bard', command = self.place_bard)
#         b4.pack()
#         b5 = tk.Button(self.summon_popup, text = 'Plaguebearer', command = self.place_plaguebearer)
#         b5.pack()
        b6 = tk.Button(self.summon_popup, text = 'Cancel', command = self.summon_popup.destroy)
        b6.pack()
    
    def cancel_placement(self, event):
        for b in self.placement_buttons:
            b.destroy()
        for s in app.sqr_dict.keys():
            app.canvas.delete(s)
        app.sqr_dict = {}
        root.bind('<q>', app.depopulate_context)

    
    def place_warrior(self):
        self.summon_popup.destroy()
        sqrs = self.legal_moves(root.map_width, root.map_height, root.parent.grid)
        app.animate_squares(sqrs)
        cmd = lambda x = Warrior, y = sqrs : self.place(x, y)
        b = tk.Button(app.context_menu, text = 'Place Warrior', command = cmd)
        b.pack(side = 'left')
        app.context_buttons.append(b)
        self.placement_buttons.append(b)
        root.unbind('<q>')
        root.bind('<q>', self.cancel_placement)
        
        
    def place(self, summon, sqrs):
        if grid_pos not in sqrs:
            return
        number = 'a' + str(len(self.summon_dict.keys()))
        if summon == Warrior:
            name = 'warrior'
            img = ImageTk.PhotoImage(Image.open('warrior.png'))
        s = summon(name = name, img = img, loc = grid_pos[:], owner = app.active_player, number = number)
        app.ent_dict[number] = s
        app.canvas.create_image(grid_pos[0]*100+50-app.moved_right, grid_pos[1]*100+50-app.moved_down, image = img, tags = number)
        app.grid[grid_pos[0]][grid_pos[1]] = number
        # DELETE SQUARES
        for s in app.sqr_dict.keys():
            app.canvas.delete(s)
        app.sqr_dict = {}
        for b in app.context_buttons:
            b.destroy()
        app.context_buttons = []
        self.summon_used = True
        root.unbind('<q>')
        root.bind('<q>', app.depopulate_context)

#         print('debug line 201 app.ent_dict keys ', app.ent_dict.keys())
#         print('debug next line inst.summon_dict keys ', self.summon_dict.keys())
#         print('next line inst.summon_dict items ', self.summon_dict.items())
#         print('next line app.ent_dict items ', app.ent_dict.items())
        
        
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
    
    # Maybe change name, used not only for finding legal moves, but sqrs within 3 spaces of entity that are unoccupied
    def legal_moves(self, width, height, grid):
        move_list = []
        total_move = 3
        coord_pairs = [[x,y] for x in range(width//100) for y in range(height//100)]
        for coord in coord_pairs:
            if abs(coord[0] - self.loc[0]) + abs(coord[1] - self.loc[1]) <= total_move:
                if grid[coord[0]][coord[1]] == '':
                    move_list.append(coord)
        return move_list
