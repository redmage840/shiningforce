# psionic push, if end sqr is same as origin sqr then no vis happens (movement animation shouldnt happen anyway), should do alternate 'regular' animation, hotkeys for psionic push

# make map 'barriers / obstacles / objects other than summons/witches', terrain, impassable area, doorways to other maps...

# cancel 'end turn' populates context with only 'help buttons' (subset of context buttons), forces user to depop context with 'q' before can be populated again...

# start making magick costs for summons and a regen rate or squares on maps that regen

# undead attack animations -- make one or two more, try and load a sound when loading atk_anims, at same point show WHAT is being 
# attacked in some way, either vis or in labels or both

# show victory conditions on map start

# animate titlescreen

# place bg image on main canvas so edges of map show that, ie border

# Urgent fix help text popup from disabling all input if 'clicked out of' or closed manually with window manager, either put help text on main canvas or context menu or make a full screen 'popup' like choose map dialogue

# Instead of 'confirm_quit' labels, paste text across whole screen 

# what happens to context_menu when attempting to populate with more buttons than it can hold, would only be an issue if ever adding a bunch more spells or summons, ideally would become a scrollbox (whatever it's called), would have populate_context count the number of buttons it is creating and when the height exceeds the screenheight...

# start thinking about what map and map animation to use

import tkinter as tk
# from tkinter import ttk
from os import walk
from PIL import ImageTk,Image
from random import choice, randrange
from functools import partial
# import time

# convenience funcs
def dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

def to_hit(self, a1, a2):
    base = 5
    dif = a1 - a2
    base += dif
    chance = base * 10
    rand = randrange(1, 100)
    if rand < chance:
        return True
    else:
        return False
        
# add random element?
def damage(self, a1, a2):
    base = 5
    dif = a1 - a2
    if base + dif < 1: return 1 
    else: return base + dif

curs_pos = [0, 0]
is_object_selected = False
selected = ''
selected_vis = ''

map_pos = [0, 0]

grid_pos = [0,0]

# import pygame
# freq = 44100     # audio CD quality
# bitsize = -16    # unsigned 16 bit
# channels = 1     # 1 is mono, 2 is stereo
# buffer = 1024    # number of samples (experiment to get right sound)
# pygame.mixer.init(freq, bitsize, channels, buffer)
# pygame.mixer.music.set_volume(0.7) # optional volume 0 to 1.0
# pygame.mixer.music.load('bloodMilkandSky.mp3')
# pygame.mixer.music.play(-1, 0)

class Dummy():
    def __init__(self):
        pass

class Effect():
    def __init__(self, info, eot_func, undo, duration):
        self.eot_func = eot_func
        self.info = info
        self.undo = undo
        self.duration = duration


class Vis():
    def __init__(self, name, loc):
        self.name = name
        self.img = ImageTk.PhotoImage(Image.open('animations/' + name + '/0.png'))
        self.loc = loc
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[0] != '.']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + name + '/' + anim))
            self.anim_dict[i] = a
            
    def rotate_image(self):
        total_imgs = len(self.anim_dict.keys())-1
        if self.anim_counter == total_imgs:
            self.anim_counter = 0
        else:
            self.anim_counter += 1
        self.img = self.anim_dict[self.anim_counter]


class Sqr():
    def __init__(self, img, loc):
        self.img = img
        self.loc = loc
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('animations/move/')][0]
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
        self.timer = 1 # COUNTER FOR TIMING EOT EFFECT TEXT OBJECTS
        self.name = name
        self.img = img
        self.loc = loc
        self.owner = owner
        self.move_used = False
        if isinstance(self, Witch) or isinstance(self, Summon):
            self.base_str = self.str
            self.base_agl = self.agl
            self.base_end = self.end
            self.base_dodge = self.dodge
            self.base_psyche = self.psyche
            
            self.str_effects = []
            self.agl_effects = []
            self.end_effects = []
            self.dodge_effects = []
            self.psyche_effects = []
            
            
        # when ent moved by effect other than regular movement, must update origin also (square of origin at begin of turn)
        self.origin = []
        self.effects_dict = {}
        self.anim_dict = {}
        anims = [a for r,d,a in walk('./animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
        # randomize animation 'seed' to stagger different ent animations
        self.anim_counter = randrange(0, len(anims))
            
    def rotate_image(self):
        total_imgs = len(self.anim_dict.keys())-1
        if self.anim_counter == total_imgs:
            self.anim_counter = 0
        else:
            self.anim_counter += 1
        self.img = self.anim_dict[self.anim_counter]
            
    def init_attack_anims(self):
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('./attack_animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('attack_animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
            
    def init_normal_anims(self):
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('./animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
            
        
    def get_attr(self, attr):
        if attr == 'str':
            q = self.str_effects
            base = self.str
        elif attr == 'agl':
            q = self.agl_effects
            base = self.agl
        elif attr == 'end':
            q = self.end_effects
            base = self.end
        elif attr == 'dodge':
            q = self.dodge_effects
            base = self.dodge
        elif attr == 'psyche':
            q = self.psyche_effects
            base = self.psyche
        for func in q:
            base = func(base)
        return base
        
    def set_attr(self, attr, amount):
        if attr == 'str':
            self.str += amount
        elif attr == 'agl':
            self.agl += amount
        elif attr == 'end':
            self.end += amount
        elif attr == 'dodge':
            self.dodge += amount
        elif attr == 'psyche':
            self.psyche += amount
        elif attr == 'spirit':
            self.spirit += amount
        elif isinstance(self, Witch):
            if attr == 'magick':
                self. magick += amount
            
    def attr_check(self, attr):
        if attr == 'str':
            a = self.get_attr('str')
        elif attr == 'agl':
            a = self.get_attr('agl')
        elif attr == 'end':
            a = self.get_attr('end')
        elif attr == 'dodge':
            a = self.get_attr('dodge')
        elif attr == 'psyche':
            a = self.get_attr('psyche')
        if a <= 0:
            a = 0
        else:
            a = (a*2)*10
        rand = randrange(-1, 102)
        if a > rand:
            return True
        else:
            return False
            
#######################################################################################
        def psi_move_loop(vis, ent, x, y, endx, endy, sqr, start_sqr):
            if x % 25 == 0 and y % 25 == 0:
                app.vis_dict[vis].rotate_image()
                app.ent_dict[ent].rotate_image()
            app.canvas.delete(vis)
            app.canvas.delete(ent)
            app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = ent)
            app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = 'Psionic_Push')
            app.canvas.tag_raise(vis)
            if x > endx:
                x -= 5
                app.canvas.move(vis, -5, 0)
                app.canvas.move(ent, -5, 0)
            elif x < endx: 
                x += 5
                app.canvas.move(vis, 5, 0)
                app.canvas.move(ent, 5, 0)
            if y > endy: 
                y -= 5
                app.canvas.move(vis, 0, -5)
                app.canvas.move(ent, 0, -5)
            elif y < endy: 
                y += 5
                app.canvas.move(vis, 0, 5)
                app.canvas.move(ent, 0, 5)
            if x == endx and y == endy:
                self.finish_psionic_push(ent, sqr, start_sqr)
            else:
                root.after(50, lambda p = 'Psionic_Push', id = id, x = x, y = y, endx = endx, endy = endy, s = sqr, s2 = start_sqr : psi_move_loop(p, id, x, y, endx, endy, s, s2))
        if sqr == start_loc:
            self.finish_psionic_push(id, sqr, start_loc)
        else:
            psi_move_loop('Psionic_Push', id, x, y, endx, endy, sqr, start_loc)
######################################################################################
    # Move animation, if implementing as method for ALL ents, they may appear to move 'through' units although they technically cannot
    # may also appear to move diagonally, does this matter? does not change legality /start/end of moves, only appearance of animation getting from one square to the other
    def move(self, event = None):
        if self.move_used == True:
            return
        # depop context, unbind, bind 'a' do move, bind 'q' cancel move, get/animate sqrs, make confirm / cancel button
        app.depop_context(event = None)
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_move)
        sqrs = self.legal_moves()
        app.animate_squares(sqrs)
        b = tk.Button(app.context_menu, text = 'Confirm Move Square', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.do_move(e, s))
        b.pack(side = 'top', pady = 3)
        app.context_buttons.append(b)
        root.bind('<a>', lambda e, s = sqrs : self.do_move(e, s))
        
    def do_move(self, event, sqrs):
        global selected
        if grid_pos not in sqrs:
            return
        app.depop_context(event = None)
        # start ANIM here
        if isinstance(self, Witch):
            id = self.name
        else:
            id = self.number
        start_sqr = self.loc[:]
        end_sqr = grid_pos[:]
        selected = id
        x = start_sqr[0]*100+50-app.moved_right
        y = start_sqr[1]*100+50-app.moved_down
        endx = end_sqr[0]*100+50-app.moved_right
        endy = end_sqr[1]*100+50-app.moved_down
        
        # MOVE LOOP
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr):
            if x % 20 == 0 or y % 20 == 0:
                self.rotate_image()
            app.canvas.delete(id)
            app.canvas.create_image(x, y, image = self.img, tags = id)
            if x > endx:
                x -= 5
                app.canvas.move(id, -5, 0)
            if x < endx: 
                x += 5
                app.canvas.move(id, 5, 0)
            if y > endy: 
                y -= 5
                app.canvas.move(id, 0, -5)
            if y < endy: 
                y += 5
                app.canvas.move(id, 0, 5)
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr) # EXIT
            else: # CONTINUE LOOP
                root.after(50, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
    def finish_move(self, id, end, start):
        global selected
        selected = ''
        oldloc = start
        newloc = end
        self.loc = newloc[:]
        self.origin = newloc[:]
        app.grid[oldloc[0]][oldloc[1]] = ''
        if isinstance(self, Witch):
            app.grid[newloc[0]][newloc[1]] = self.name
            tg = self.name
        elif isinstance(self, Summon):
            app.grid[newloc[0]][newloc[1]] = self.number
            tg = self.number
        app.canvas.delete(tg)
        app.canvas.create_image(newloc[0]*100+50-app.moved_right, newloc[1]*100+50-app.moved_down, image = self.img, tags = tg)
        self.move_used = True
        self.cleanup_move()
        
    def cleanup_move(self, event = None):
        app.depop_context(event = None)
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
    

class Summon(Entity):
    def __init__(self, name, img, loc, owner, number):
        self.number = number
        super().__init__(name, img, loc, owner)
        
class Trickster(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'confuse':self.trickster_attack, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 3
        self.end = 2
        self.dodge = 4
        self.psyche = 5
        self.spirit = 10
        super().__init__(name, img, loc, owner, number)
        
        
    def trickster_attack(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        root.unbind('<a>')
        sqrs = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coord_pairs:
            if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
                sqrs.append(coord)
            elif coord[0] == self.loc[0] and abs(coord[1] - self.loc[1]) == 1:
                sqrs.append(coord)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.check_hit(e, sqrs = s))
        b = tk.Button(app.context_menu, text = 'Confirm Confuse', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.check_hit(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)

        
        
    def check_hit(self, event = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        if app.current_pos() == '':
            return
        app.depop_context(event = None)
        app.unbind_all()
        id = app.current_pos()
        my_psyche = self.get_attr('psyche')
        target_psyche = app.ent_dict[id].get_attr('psyche')
        if to_hit(my_psyche, target_psyche) == True:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Confuse Hit!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.after(1666, lambda id = id : self.do_attack(id))
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Confuse Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.after(1666, lambda e = None : self.cancel_attack(event = None))
        self.attack_used = True
        
    def do_attack(self, id):
        app.rebind_all()
        root.unbind('<q>')
        root.unbind('<a>')
        root.unbind('<space>')
        root.unbind('<z>')
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        dist = damage(my_agl, target_dodge)
        dist = dist//2 + 1
        app.depop_context(event = None)
        app.cleanup_squares()
        sqrs = self.confuse_sqrs(dist)
        if sqrs == []:
            self.attack_used = True
            self.cancel_attack(event = None)
            return
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, t = id, s = sqrs : self.confuse(e, id = t, sqrs = s))
        b = tk.Button(app.context_menu, text = 'Choose Square', font = ('chalkduster', 24), fg = 'tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, id = id, s = sqrs : self.confuse(e, id, s))
        b.pack(side = 'top')
        app.context_buttons.append(b)

    
    def confuse(self, event = None, id = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        app.grid[app.ent_dict[id].loc[0]][app.ent_dict[id].loc[1]] = ''
        app.canvas.delete(id)
        oldloc = app.ent_dict[id].loc
        app.ent_dict[id].loc = grid_pos[:]
        app.ent_dict[id].origin = grid_pos[:]
        app.grid[grid_pos[0]][grid_pos[1]] = id
        app.canvas.create_image(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+50-app.moved_down, image = app.ent_dict[id].img, tags = id)
        self.cancel_attack(event = None)
    
    def confuse_sqrs(self, dist):
        sqr_list = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coord_pairs:
            if app.grid[coord[0]][coord[1]] == '':
                if abs(coord[0] - self.loc[0]) + abs(coord[1] - self.loc[1]) <= dist:
                    sqr_list.append(coord)
        return sqr_list
    
    def cancel_attack(self, event = None):
        app.canvas.delete('text')
        app.depop_context(event = None)
        app.cleanup_squares()
        app.rebind_all()
    
    def legal_moves(self):
        move_list = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coord_pairs:
            if app.grid[coord[0]][coord[1]] == '':
                if abs(coord[0] - self.loc[0]) == 1 and abs(coord[1] - self.loc[1]) == 2:
                    move_list.append(coord)
                elif abs(coord[0] - self.loc[0]) == 2 and abs(coord[1] - self.loc[1]) == 1:
                    move_list.append(coord)
        return move_list
        

class Shadow(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.shadow_attack, 'move':self.move}
        self.attack_used = False
        self.str = 3
        self.agl = 3
        self.end = 2
        self.dodge = 4
        self.psyche = 4
        self.spirit = 8
        super().__init__(name, img, loc, owner, number)
        
        
    def shadow_attack(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        root.unbind('<a>')
        sqrs = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coord_pairs:
            if abs(coord[0] - self.loc[0]) == 1 and abs(coord[1] - self.loc[1]) == 1:
                sqrs.append(coord)
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, sqrs = sqrs : self.check_hit(e, sqrs))
        app.depop_context(event = None)
        b = tk.Button(app.context_menu, text = 'Confirm Attack', font = ('chalkduster', 24), fg='tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, s = sqrs: self.check_hit(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)

        
    def check_hit(self, event = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        if app.current_pos() == '':
            return
        app.depop_context(event = None)
        id = app.current_pos()
        app.unbind_all()
        my_str = self.get_attr('str')
        target_end = app.ent_dict[id].get_attr('end')
        if to_hit(my_str, target_end) == True:
            # VISUAL TO HIT, go ahead and show dmg here also
            my_psyche = self.get_attr('psyche')
            target_psyche = app.ent_dict[id].get_attr('psyche')
            d = damage(my_psyche, target_psyche)
            d //= 2
            if d == 0: d = 1
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Shadow Attack Hit!\n' + str(d) + ' Spirit Damage\n', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            if isinstance(app.ent_dict[id], Witch):
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = str(d) + ' Magick Damage', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('magick', -d)
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                if isinstance(app.ent_dict[id], Witch):
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                else:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda e = None, id = id : self.cancel_attack(event = e, id = id))
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Shadow Attack Missed!\n', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda e = None, id = id : self.cancel_attack(event = e, id = id))
        self.attack_used = True
    
    
    def cancel_attack(self, event = None, id = None):
        app.canvas.delete('text')
        if id:
            if app.ent_dict[id].spirit <= 0:
                app.kill(id)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.rebind_all()
    
    def legal_moves(self):
        move_list = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coord_pairs:
        # move on diag, 3 sqrs, same for both players
            if app.grid[coord[0]][coord[1]] == '':
                if abs(coord[0] - self.loc[0]) == abs(coord[1] - self.loc[1]) and abs(coord[0] - self.loc[0]) <= 3:
                    move_list.append(coord)
        return move_list

# change name to better fit generic flavor of witches
# attack all adjacent units, must attack at end of turn, damage nearby on death?
# abuse with trickster
class Plaguebearer(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.warrior_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 4
        self.end = 4
        self.dodge = 2
        self.psyche = 2
        self.spirit = 13
        super().__init__(name, img, loc, owner, number)
        
        
#     def warrior_attack(self, event = None):
#         if self.attack_used == True:
#             return
#         sqrs = []
#         coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#         if app.active_player == 'p1':
#             for coord in coord_pairs:
#                 if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
#                     sqrs.append(coord)
#                 elif abs(coord[0] - self.loc[0]) == 1 and coord[1]-1 == self.loc[1]:
#                     sqrs.append(coord)
#                 elif coord[0] == self.loc[0] and coord[1]-1 == self.loc[1]:
#                     sqrs.append(coord)
#         elif app.active_player == 'p2':
#             for coord in coord_pairs:
#                 if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
#                     sqrs.append(coord)
#                 elif abs(coord[0] - self.loc[0]) == 1 and coord[1]+1 == self.loc[1]:
#                     sqrs.append(coord)
#                 elif coord[0] == self.loc[0] and coord[1]+1 == self.loc[1]:
#                     sqrs.append(coord)
#         app.animate_squares(sqrs)
#         app.depop_context(event = None) 
#         root.bind('<a>', lambda e, s = sqrs : self.check_hit(e, s))
#         b = tk.Button(app.context_menu, text = 'Confirm Attack', font = ('chalkduster', 24), fg='tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, s = sqrs: self.check_hit(e, s))
#         b.pack(side = 'top')
#         app.context_buttons.append(b)
# #         self.placement_buttons.append(b)
#         root.unbind('<q>')
#         root.bind('<q>', self.cancel_attack)
#         
#     def check_hit(self, event, sqrs):
#         if grid_pos not in sqrs:
#             return
#         if app.current_pos() == '':
#             return
#         tar = app.current_pos()
#         app.unbind_all()
#         if self.to_hit(self.agl, app.ent_dict[tar].dodge) == True:
#             print('hit')
#             # call self.init_attack_anims() here to replace self.anim_dict with other images
#             # on exit, re init normal anims
#             self.init_attack_anims()
#             dmg = self.damage(self.str, app.ent_dict[tar].end)
#             self.success = tk.Label(app.context_menu, text = 'Attack Hit!', relief = 'raised', font = ('chalkduster', 24), fg = 'indianred', bg = 'tan2')
#             self.success.pack(side = 'top')
#             self.dmg = tk.Label(app.context_menu, text = str(dmg) + ' Spirit', relief = 'raised', font = ('chalkduster', 24), fg = 'indianred', bg = 'tan2')
#             self.dmg.pack(side = 'top')
#             root.after(1200, lambda id = tar, dmg = dmg : self.do_attack(id, dmg))
#         else:
#             self.miss = tk.Label(app.context_menu, text = 'Attack Missed!', relief = 'raised', font = ('chalkduster', 24), wraplength = 190, fg = 'indianred', bg = 'tan2')
#             self.miss.pack(side = 'top')
#             root.after(1200, lambda win = self.miss : self.cancel_attack(event = None, win = win))
#         self.attack_used = True
#         
#     def do_attack(self, id, dmg):
#         self.success.destroy()
#         self.dmg.destroy()
#         app.ent_dict[id].set_attr('spirit', -dmg)
#         if app.ent_dict[id].spirit <= 0:
#             app.kill(id)
#             print('target killed')
#         self.cancel_attack(event = None)
#         # re init normal anims 
#         self.init_normal_anims()
#     
#     def cancel_attack(self, event, win = None):
#         app.rebind_all()
#         if win:
#             win.destroy()
#         app.depop_context(event = None)
#         for b in self.placement_buttons:
#             b.destroy()
#         app.cleanup_squares()
#         self.init_normal_anims()
#     
#     def legal_moves(self):
#         loc = self.loc
#         mvlist = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#         def findall(loc, start, dist):
#             if start > dist:
#                 return
#             # need different 'front' depending on player
#             if app.active_player == 'p1':
#                 front = [c for c in coords if c[0] == loc[0] and c[1]-1 == loc[1] and app.grid[c[0]][c[1]] == '']
#             elif app.active_player == 'p2':
#                 front = [c for c in coords if c[0] == loc[0] and c[1]+1 == loc[1] and app.grid[c[0]][c[1]] == '']
#             for s in front:
#                 mvlist.append(s)
#                 findall(s, start+1, dist)
#         findall(loc, 1, 3) 
#         setlist = []
#         for l in mvlist:
#             if l not in setlist:
#                 setlist.append(l)
#         return setlist


# raise stats of units (bardsong)?
# force units to follow or attack?
# healer / magick recovery?
class Bard(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.warrior_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 4
        self.end = 4
        self.dodge = 2
        self.psyche = 2
        self.spirit = 13
        super().__init__(name, img, loc, owner, number)
        
        
#     def warrior_attack(self):
#         if self.attack_used == True:
#             return
#         sqrs = []
#         coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#         if app.active_player == 'p1':
#             for coord in coord_pairs:
#                 if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
#                     sqrs.append(coord)
#                 elif abs(coord[0] - self.loc[0]) == 1 and coord[1]-1 == self.loc[1]:
#                     sqrs.append(coord)
#                 elif coord[0] == self.loc[0] and coord[1]-1 == self.loc[1]:
#                     sqrs.append(coord)
#         elif app.active_player == 'p2':
#             for coord in coord_pairs:
#                 if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
#                     sqrs.append(coord)
#                 elif abs(coord[0] - self.loc[0]) == 1 and coord[1]+1 == self.loc[1]:
#                     sqrs.append(coord)
#                 elif coord[0] == self.loc[0] and coord[1]+1 == self.loc[1]:
#                     sqrs.append(coord)
#         app.animate_squares(sqrs)
#         app.depop_context(event = None) 
#         cmd = lambda s = sqrs: self.check_hit(s)
#         b = tk.Button(app.context_menu, text = 'Confirm Attack', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = cmd)
#         b.pack(side = 'left')
#         app.context_buttons.append(b)
#         self.placement_buttons.append(b)
#         root.unbind('<q>')
#         root.bind('<q>', self.cancel_attack)
#         
#     def check_hit(self, sqrs):
#         if grid_pos not in sqrs:
#             return
#         if app.current_pos() == '':
#             return
#         tar = app.current_pos()
#         app.unbind_all()
#         if self.to_hit(self.agl, app.ent_dict[tar].dodge) == True:
#             print('hit')
#             # call self.init_attack_anims() here to replace self.anim_dict with other images
#             # on exit, re init normal anims
#             self.init_attack_anims()
#             dmg = self.damage(self.str, app.ent_dict[tar].end)
#             self.success = tk.Label(app.context_menu, text = 'Attack Hit!', relief = 'raised', font = ('chalkduster', 24), fg = 'indianred', bg = 'tan2')
#             self.success.pack(side = 'left')
#             self.dmg = tk.Label(app.context_menu, text = str(dmg) + ' Spirit', relief = 'raised', font = ('chalkduster', 24), fg = 'indianred', bg = 'tan2')
#             self.dmg.pack(side = 'left')
#             root.after(1200, lambda id = tar, dmg = dmg : self.do_attack(id, dmg))
#         else:
#             self.miss = tk.Label(app.context_menu, text = 'Attack Missed!', relief = 'raised', font = ('chalkduster', 24), fg = 'indianred', bg = 'tan2')
#             self.miss.pack(side = 'left')
#             root.after(1200, lambda win = self.miss : self.cancel_attack(event = None, win = win))
#         self.attack_used = True
#         
#     def do_attack(self, id, dmg):
#         self.success.destroy()
#         self.dmg.destroy()
#         app.ent_dict[id].set_attr('spirit', -dmg)
#         if app.ent_dict[id].spirit <= 0:
#             app.kill(id)
#             print('target killed')
#         self.cancel_attack(event = None)
#         # re init normal anims 
#         self.init_normal_anims()
#     
#     def cancel_attack(self, event, win = None):
#         app.rebind_all()
#         if win:
#             win.destroy()
#         app.depop_context(event = None)
#         app.cleanup_squares()
#         self.init_normal_anims()
#     
#     def legal_moves(self):
#         loc = self.loc
#         mvlist = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#         def findall(loc, start, dist):
#             if start > dist:
#                 return
#             # need different 'front' depending on player
#             if app.active_player == 'p1':
#                 front = [c for c in coords if c[0] == loc[0] and c[1]-1 == loc[1] and app.grid[c[0]][c[1]] == '']
#             elif app.active_player == 'p2':
#                 front = [c for c in coords if c[0] == loc[0] and c[1]+1 == loc[1] and app.grid[c[0]][c[1]] == '']
#             for s in front:
#                 mvlist.append(s)
#                 findall(s, start+1, dist)
#         findall(loc, 1, 3) 
#         setlist = []
#         for l in mvlist:
#             if l not in setlist:
#                 setlist.append(l)
#         return setlist
        
        
class Undead(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.undead_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 2
        self.end = 4
        self.dodge = 2
        self.psyche = 2
        self.spirit = 15
        super().__init__(name, img, loc, owner, number)
        
    
    # movement is working fine, but atk_sqrs is messed up might be from legal_attacks()
    # need more visualizations before actions happen, better timing of vis
    def do_undead_ai(self, ents_list):
        # GET LIST OF ENEMY ENTS, PICK ONE OF THE CLOSEST
        enemy_ents = [x for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
        min = dist(app.ent_dict[enemy_ents[0]].loc, self.loc)
        closest = [enemy_ents[0]]
        for ent in enemy_ents:
            if dist(app.ent_dict[ent].loc, self.loc) < min:
                min = dist(app.ent_dict[ent].loc, self.loc)
                closest = [ent]
            elif dist(app.ent_dict[ent].loc, self.loc) == min:
                closest.append(ent)
        target = closest[0]
        t_loc = app.ent_dict[target].loc
        atk_sqrs = self.legal_attacks()
        # IF TARGET IS WITHIN ATTACK, ATTACK IT, EXIT THROUGH UNDEAD_ATTACK()
        if t_loc in atk_sqrs:
            self.undead_attack(ents_list, target)
        # IF TARGET IS NOT WITHIN ATTACK, MOVE TOWARDS IT
        else:
            mov_sqrs = self.legal_moves()
            # NO LEGAL MOVES AND TARGET NOT WITHIN CURRENT RANGE, EXIT FUNC
            if mov_sqrs == []:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            else:
            # AMONG LEGAL MOVES, PICK ONE THAT MINIMIZES DISTANCE BETWEEN SELF AND TARGET, MOVE SELF TO SQUARE
                best = mov_sqrs[0]
                min = dist(mov_sqrs[0], app.ent_dict[target].loc)
                for s in mov_sqrs:
                    if dist(s, app.ent_dict[target].loc) < min:
                        best = s
                        min = dist(s, app.ent_dict[target].loc)
                app.canvas.delete(self.number)
                app.grid[self.loc[0]][self.loc[1]] = ''
                self.loc = best[:]
                self.origin = best[:]
                app.grid[best[0]][best[1]] = self.number
                app.canvas.create_image(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, image = self.img, tags = self.number)
            # IF TARGET NOW WITHIN RANGE, MAKE ATTACK ON IT
            atk_sqrs = self.legal_attacks()
            if t_loc in atk_sqrs:
                self.undead_attack(ents_list, target) # EXIT THROUGH UNDEAD_ATTACK()
            else:
            # CANNOT ATTACK, EXIT FUNC
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def undead_attack(self, ents_list, id):
        self.init_attack_anims()
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
            # HIT, SHOW VIS, DO DAMAGE, EXIT
            my_str = self.get_attr('str')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_str, target_end)
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Attack Hit!\n' + str(d) + ' Spirit Damage', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
        else:
            # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
    def cleanup_attack(self, ents_list, id):
        if app.ent_dict[id].spirit <= 0:
            app.kill(id)
        self.init_normal_anims()
        try: app.canvas.delete('text')
        except: pass
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coords:
            if (bool(abs(coord[0] - self.loc[0]) == 1) ^ bool(abs(coord[1] - self.loc[1]) == 1)) and dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        sqrs = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coords:
            if app.grid[coord[0]][coord[1]] == '':
                if (bool(abs(coord[0] - self.loc[0]) == 1) ^ bool(abs(coord[1] - self.loc[1]) == 1)) and dist(coord, self.loc) == 1:
                    sqrs.append(coord)
        return sqrs
        
        
class Warrior(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.warrior_attack, 'move':self.move}
        self.attack_used = False
        self.str = 4
        self.agl = 4
        self.end = 4
        self.dodge = 2
        self.psyche = 2
        self.spirit = 13
        super().__init__(name, img, loc, owner, number)
        
        
    def warrior_attack(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        if app.active_player == 'p1':
            for coord in coord_pairs:
                if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
                    sqrs.append(coord)
                elif abs(coord[0] - self.loc[0]) == 1 and coord[1]-1 == self.loc[1]:
                    sqrs.append(coord)
                elif coord[0] == self.loc[0] and coord[1]-1 == self.loc[1]:
                    sqrs.append(coord)
        elif app.active_player == 'p2':
            for coord in coord_pairs:
                if abs(coord[0] - self.loc[0]) == 1 and coord[1] == self.loc[1]:
                    sqrs.append(coord)
                elif abs(coord[0] - self.loc[0]) == 1 and coord[1]+1 == self.loc[1]:
                    sqrs.append(coord)
                elif coord[0] == self.loc[0] and coord[1]+1 == self.loc[1]:
                    sqrs.append(coord)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.check_hit(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Attack', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.check_hit(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def check_hit(self, event = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        if app.current_pos() == '':
            return
        self.attack_used = True
        self.init_attack_anims()
        app.depop_context(event = None)
        app.unbind_all()
        id = app.current_pos()
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
            my_str = self.get_attr('str')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_str, target_end)
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Warrior Attack Hit!\n' + str(d) + ' Spirit Damage', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda id = id, d = d : self.do_attack(id, d))
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Warrior Attack Misses!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda e = None : self.cancel_attack(event = e))
        
    def do_attack(self, id, dmg):
        app.ent_dict[id].set_attr('spirit', -dmg)
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda id = id : app.kill(id))
            root.after(1666, lambda e = None : self.cancel_attack(e))
        else:
            self.cancel_attack(event = None)
    
    def cancel_attack(self, event):
        self.init_normal_anims()
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
        app.cleanup_squares()
    
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        def findall(loc, start, dist):
            if start > dist:
                return
            # need different 'front' depending on player
            if app.active_player == 'p1':
                front = [c for c in coords if c[0] == loc[0] and c[1]-1 == loc[1] and app.grid[c[0]][c[1]] == '']
            elif app.active_player == 'p2':
                front = [c for c in coords if c[0] == loc[0] and c[1]+1 == loc[1] and app.grid[c[0]][c[1]] == '']
            for s in front:
                mvlist.append(s)
                findall(s, start+1, dist)
        findall(loc, 1, 3) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist
                    
class Witch(Entity):
    def __init__(self, name, img, loc, owner):
        self.actions = {'spell':self.spell, 'summon':self.summon, 'move':self.move}
        self.spell_used = False
        self.summon_used = False
        self.spell_dict = {}
        self.summon_dict = {}
        self.summon_ids = 0
        
        if name == 'Agnes_Sampson':
            self.spell_dict['Plague'] = (self.plague, 5)
            self.spell_dict['Psionic_Push'] = (self.psionic_push, 4)
            self.spell_dict['Curse_of_Oriax'] = (self.curse_of_oriax, 5)
            self.spell_dict['Gravity'] = (self.gravity, 7)
            self.spell_dict["Beleth's_Command"] = (self.beleths_command, 8)
            self.str = 4
            self.agl = 2
            self.end = 3
            self.dodge = 3
            self.psyche = 4
            self.spirit = 75
            self.magick = 75
        elif name == 'Fakir_Ali':
            self.spell_dict['Horrid_Wilting'] = (self.horrid_wilting,4)
            self.spell_dict['Boiling_Blood'] = (self.boiling_blood, 3)
            self.spell_dict['Dark_Sun'] = (self.dark_sun, 4)
            self.spell_dict['Command_of_Osiris'] = (self.command_of_osiris, 5)
            self.spell_dict['Disintegrate'] = (self.disintegrate, 4)
            self.str = 3
            self.agl = 2
            self.end = 5
            self.dodge = 3
            self.psyche = 3
            self.spirit = 85
            self.magick = 70
        elif name == 'Morgan_LeFay':
            self.spell_dict['Enchant'] = (self.enchant, 4)
            self.spell_dict['Counterspell'] = (self.counterspell, 3)
            self.spell_dict["Nature's_Wrath"] = (self.natures_wrath, 5)
            self.spell_dict["Noden's_Command"] = (self.nodens_command, 6)
            self.spell_dict['Wild_Hunt'] = (self.wild_hunt, 7)
            self.str = 2
            self.agl = 4
            self.end = 3
            self.dodge = 4
            self.psyche = 3
            self.spirit = 70
            self.magick = 85
            
        super().__init__(name, img, loc, owner)
        
    
    def summon(self, event = None):
                # show vis in context_menu, summon used? eventually DEBUG fine for now
        if self.summon_used == True:
            return
        app.depop_context(event = None)
        root.bind('1', lambda e, cls = 'Warrior', cost = 10 : self.place_summon(e, cls, cost))
        root.bind('2', lambda e, cls = 'Trickster', cost = 8 : self.place_summon(e, cls, cost))
        root.bind('3', lambda e, cls = 'Shadow', cost = 7 : self.place_summon(e, cls, cost))
        b1 = tk.Button(app.context_menu, text = '1:Warrior •10', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Warrior', cost = 10 : self.place_summon(e, cls, cost))
        b1.pack(side = 'top', pady = 2)
        app.context_buttons.append(b1)
        b2 = tk.Button(app.context_menu, text = '2:Trickster •8', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Trickster', cost = 8 : self.place_summon(e, cls, cost))
        b2.pack(side = 'top', pady = 2)
        app.context_buttons.append(b2)
        b3 = tk.Button(app.context_menu, text = '3:Shadow •7', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Shadow', cost = 7 : self.place_summon(e, cls, cost))
        b3.pack(side = 'top', pady = 2)
        app.context_buttons.append(b3)
#         b4 = tk.Button(self.summon_popup, text = 'Bard', command = self.place_bard)
#         b4.pack()
#         b5 = tk.Button(self.summon_popup, text = 'Plaguebearer', command = self.place_plaguebearer)
#         b5.pack()
        b6 = tk.Button(app.context_menu, text = 'Cancel', font = ('chalkduster', 24), highlightbackground = 'tan3', fg='tan3', command = self.cancel_placement)
        b6.pack(side = 'top')
        app.context_buttons.append(b6)
    
    def cancel_placement(self, event = None):
        app.depop_context(event = None)
        app.cleanup_squares()
        for x in range(1,4):
            root.unbind(str(x))
        root.unbind('<q>')
        root.bind('<q>', app.depop_context)
        root.unbind('<a>')
        root.bind('<a>', app.populate_context)

    
    def place_summon(self, event, type, cost):
        if self.magick < cost:
            return
        self.set_attr('magick', -cost)
        root.unbind('<q>')
        root.unbind('<a>')
        for x in range(1,4):
            root.unbind(str(x))
        root.bind('<q>', self.cancel_placement)
        app.depop_context(event = None)
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in coords if abs(c[0]-self.loc[0]) + abs(c[1]-self.loc[1]) == 1 and app.grid[c[0]][c[1]] == '']
        app.animate_squares(sqrs)
        if type == 'Warrior':
            cls = Warrior
        elif type == 'Trickster':
            cls = Trickster
        elif type == 'Shadow':
            cls = Shadow
        elif type == 'Bard':
            cls = Bard
        elif type == 'Plaguebearer':
            cls = Plaguebearer
        cmd = lambda e = None, x = cls, y = sqrs : self.place(e, summon = x, sqrs = y)
        root.bind('<a>', lambda e, x = cls, y = sqrs: self.place(e, x, y))
        b = tk.Button(app.context_menu, text = 'Place '+type, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', wraplength = 190, command = cmd)
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    def place(self, event, summon, sqrs):
        if grid_pos not in sqrs:
            return
        root.unbind('<q>')
        root.bind('<q>', app.depop_context)
        root.unbind('<a>')
        root.bind('<a>', app.populate_context)
        if app.active_player == 'p1':
            number = 'a' + str(self.summon_ids)
            self.summon_ids += 1
        elif app.active_player == 'p2':
            number = 'b' + str(self.summon_ids)
            self.summon_ids += 1
        if summon == Warrior:
            name = 'Warrior'
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Warrior.png'))
        elif summon == Trickster:
            name = 'Trickster'
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Trickster.png'))
        elif summon == Shadow:
            name = 'Shadow'
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Shadow.png'))
        elif summon == Bard:
            name = 'Bard'
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Bard.png'))
        elif summon == Plaguebearer:
            name = 'Plaguebearer'
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Plaguebearer.png'))
        s = summon(name = name, img = img, loc = grid_pos[:], owner = app.active_player, number = number)
        app.ent_dict[number] = s
        self.summon_dict[number] = s
        app.canvas.create_image(grid_pos[0]*100+50-app.moved_right, grid_pos[1]*100+50-app.moved_down, image = img, tags = number)
        app.grid[grid_pos[0]][grid_pos[1]] = number
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.depop_context(event = None)
        self.summon_used = True
        
        
    def spell(self, event = None):
        if self.spell_used == True:
            return
        app.depop_context(event = None)
        # DEBUG need to unbind most keys here, rebind on cleanup_spell which should be always exited through whether successful cast or cancel
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_spell)
        # SPELL
        for i, name_spellcosttuple in enumerate(self.spell_dict.items()):
            name = name_spellcosttuple[0]
            name = name.replace('_', ' ')
            spell = name_spellcosttuple[1][0]
            cost = name_spellcosttuple[1][1]
            i += 1
            b1 = tk.Button(app.context_menu, wraplength = 190, text = str(i) +' : '+ name + ' •'+str(cost), font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = spell)
            b1.pack(side = 'top', pady = 2)
            if cost > self.magick:
                b1.config(state = 'disabled')
            else:
                root.bind(str(i), spell)
            app.context_buttons.append(b1)
        b2 = tk.Button(app.context_menu, text = 'Cancel', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = self.cleanup_spell)
        b2.pack(side = 'top')
        app.context_buttons.append(b2)
    
    
    def cleanup_spell(self, event = None, name = None):
        global selected, selected_vis
        root.unbind('<q>')
        root.unbind('<a>')
        for x in range(1, len(self.spell_dict.keys())+1):
            root.unbind(str(x))
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        try: 
            app.canvas.delete(name)
            del app.vis_dict[name]
        except: pass
        try: app.canvas.delete('text')
        except: pass
        selected = ''
        selected_vis = ''
        
        
        # Need to incorporate 'magick cost' and rules for regenerating/regaining magick, probably certain squares that replenish a set amount every turn, or squares that appear for a limited amount of time/turns that replenish
# AGNES SPELLS
        # Agnes' spells center around Death/Decay/Disease/Telekinetics
    def plague(self, event = None):
            # currently effects dif from description, one target, no to_hit check
            # Make attk (psyche versus end) on any summon within range 4 and all adjacent summons have attrs reduced to 1 (str, agl, end, dodge, psyche) lasting until 3 opp turns have passed
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Plague' : self.cleanup_spell(name = name))
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_plague(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Plague', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_plague(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_plague(self, event, sqr, sqrs):
        if app.current_pos() == '':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.spell_dict['Plague'][1]
        root.unbind('<q>')
        root.unbind('<a>')
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        app.vis_dict['Plague'] = Vis(name = 'Plague', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Plague'].img, tags = 'Plague')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Plague', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO PLAGUE EFFECTS
        def plague_effect(stat):
            return 1
        f = plague_effect
        app.ent_dict[id].str_effects.append(f)
        app.ent_dict[id].end_effects.append(f)
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        app.ent_dict[id].psyche_effects.append(f)
        def un(i):
            app.ent_dict[i].str_effects.remove(plague_effect)
            app.ent_dict[i].end_effects.remove(plague_effect)
            app.ent_dict[i].agl_effects.remove(plague_effect)
            app.ent_dict[i].dodge_effects.remove(plague_effect)
            app.ent_dict[i].psyche_effects.remove(plague_effect)
        p = partial(un, id)
        def nothing():
            pass
        eot = nothing
        n = 'Plague' + str(len(app.ent_dict[id].effects_dict.keys()))
        app.ent_dict[id].effects_dict['Plague'] = Effect(info = 'Plague\n Stats reduced to 1 for 3 turns', eot_func = eot, undo = p, duration = 3)
        root.after(2666, lambda  name = 'Plague' : self.cleanup_spell(name = name))
            
    # PSIONIC PUSH
    # make hotkeys, do something about lack of vis when 'not moving'
    def psionic_push(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Psionic_Push' : self.cleanup_spell(name = name))
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_psionic_push(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Psionic Push', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_psionic_push(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_psionic_push(self, event, sqr, sqrs):
        if app.current_pos() == '':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.spell_dict['Psionic_Push'][1]
        root.unbind('<q>')
        root.unbind('<a>')
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        loc = app.ent_dict[id].loc[:]
        ps = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        # make recursive for variable distance
#         def sqrs_until_obs(start, next, dist):
        ps.append(loc)
        for c in coords:
            if c[0] == (loc[0] + 1) and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                ps.append(c)
                n = [loc[0]+2, loc[1]]
                if n in coords:
                    if n[0] == (loc[0] + 2) and n[1] == loc[1] and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == (loc[0] - 1) and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                n = [loc[0]-2, loc[1]]
                ps.append(c)
                if n in coords:
                    if n[0] == (loc[0] - 2) and n[1] == loc[1] and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == loc[0] and c[1] == (loc[1] + 1) and app.grid[c[0]][c[1]] == '':
                n = [loc[0], loc[1]+2]
                ps.append(c)
                if n in coords:
                    if n[0] == loc[0] and n[1] == (loc[1] + 2) and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == loc[0] and c[1] == (loc[1] - 1) and app.grid[c[0]][c[1]] == '':
                n = [loc[0], loc[1]-2]
                ps.append(c)
                if n in coords:
                    if n[0] == loc[0] and n[1] == (loc[1] - 2) and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
        app.animate_squares(ps)
        root.bind('<a>', lambda e, id = id, s = grid_pos, sqrs = ps : self.choose_psi_square(event = e, id = id, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Square to Push', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, id = id, s = grid_pos, sqrs = ps : self.choose_psi_square(e, id, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
            
            # THIS LOOP WILL BE THE SAME FOR 'WALKING' ANIMATION... GENERALLY
    def choose_psi_square(self, event, id, sqr, sqrs):
        global selected, selected_vis
        if sqr not in sqrs:
            return
        app.unbind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        start_loc = app.ent_dict[id].loc[:]
        app.vis_dict['Psionic_Push'] = Vis(name = 'Psionic_Push', loc = start_loc)
        app.canvas.create_image(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+50-app.moved_down, image = app.vis_dict['Psionic_Push'].img, tags = 'Psionic_Push')
        app.canvas.create_text(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+95-app.moved_down, text = 'Psionic Push', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        x = start_loc[0]*100+50-app.moved_right
        y = start_loc[1]*100+50-app.moved_down
        endx = sqr[0]*100+50-app.moved_right
        endy = sqr[1]*100+50-app.moved_down
        if start_loc != sqr:
            selected = id
            selected_vis = 'Psionic_Push'
        def psi_move_loop(vis, ent, x, y, endx, endy, sqr, start_sqr):
            if x % 25 == 0 and y % 25 == 0:
                app.vis_dict[vis].rotate_image()
                app.ent_dict[ent].rotate_image()
            app.canvas.delete(vis)
            app.canvas.delete(ent)
            app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = 'Psionic_Push')
            app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = ent)
            app.canvas.tag_raise(vis)
            if x > endx:
                x -= 5
                app.canvas.move(vis, -5, 0)
                app.canvas.move(ent, -5, 0)
            elif x < endx: 
                x += 5
                app.canvas.move(vis, 5, 0)
                app.canvas.move(ent, 5, 0)
            if y > endy: 
                y -= 5
                app.canvas.move(vis, 0, -5)
                app.canvas.move(ent, 0, -5)
            elif y < endy: 
                y += 5
                app.canvas.move(vis, 0, 5)
                app.canvas.move(ent, 0, 5)
            if x == endx and y == endy:
                self.finish_psionic_push(ent, sqr, start_sqr)
            else:
                root.after(50, lambda p = 'Psionic_Push', id = id, x = x, y = y, endx = endx, endy = endy, s = sqr, s2 = start_sqr : psi_move_loop(p, id, x, y, endx, endy, s, s2))
        if sqr == start_loc:
            self.finish_psionic_push(id, sqr, start_loc)
        else:
            psi_move_loop('Psionic_Push', id, x, y, endx, endy, sqr, start_loc)
        
    def finish_psionic_push(self, tar, end_loc, start_loc):
        global selected, selected_vis
        app.ent_dict[tar].loc = end_loc[:]
        app.ent_dict[tar].origin = end_loc[:]
        app.grid[start_loc[0]][start_loc[1]] = ''
        app.grid[end_loc[0]][end_loc[1]] = tar
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        adj_sqrs = [c for c in coords if dist(c, end_loc) == 1]
        adj_ents = []
        for s in adj_sqrs:
            if app.grid[s[0]][s[1]] != '':
                adj_ents.append(app.grid[s[0]][s[1]])
        if adj_ents != []:
            # hit tar and adj_ents
            # add text objects for save / miss
            adj_ents.append(tar)
            tar_str = app.ent_dict[tar].get_attr('str')
            for ent in adj_ents:
                if app.ent_dict[ent].attr_check('agl') == False:
                    d = damage(tar_str, app.ent_dict[ent].get_attr('end'))
                    app.ent_dict[ent].set_attr('spirit', -d)
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = str(d) + ' Spirit Damage', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                    if app.ent_dict[ent].spirit <= 0:
                        app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+90-app.moved_down, text = app.ent_dict[ent].name + ' Killed...', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        root.after(666, app.kill(ent))
                # MISS
                else:
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = 'Agility Save', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(2666, lambda s = 'Psionic_Push' : self.cleanup_spell(name = s))
        else:
            self.cleanup_spell(name = 'Psionic_Push')
        
        
    # CURSE OF ORIAX
    def curse_of_oriax(self, event = None):
            # Any target is inflicted with 'curse', while cursed takes 2 spirit damage at end of every owner's turn and minus 1 to every stat (not spirit, magick, movement)
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in coords if dist(self.loc, s) <= 3]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_curse_of_oriax(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Curse of Oriax', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_curse_of_oriax(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_curse_of_oriax(self, event, sqr, sqrs):
        if app.current_pos() == '':
            return
        if sqr not in sqrs:
            return
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.spell_dict['Curse_of_Oriax'][1]
        root.unbind('<q>')
        root.unbind('<a>')
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        app.vis_dict['Curse_of_Oriax'] = Vis(name = 'Curse_of_Oriax', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Curse_of_Oriax'].img, tags = 'Curse_of_Oriax')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Curse of Oriax', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Curse_of_Oriax EFFECTS
        def curse_of_oriax_effect(stat):
            return stat - 1
        f = curse_of_oriax_effect
        app.ent_dict[id].str_effects.append(f)
        app.ent_dict[id].end_effects.append(f)
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        app.ent_dict[id].psyche_effects.append(f)
        def un(i):
            app.ent_dict[i].str_effects.remove(curse_of_oriax_effect)
            app.ent_dict[i].end_effects.remove(curse_of_oriax_effect)
            app.ent_dict[i].agl_effects.remove(curse_of_oriax_effect)
            app.ent_dict[i].dodge_effects.remove(curse_of_oriax_effect)
            app.ent_dict[i].psyche_effects.remove(curse_of_oriax_effect)
        p = partial(un, id)
        # EOT FUNC
        def take_2(tar):
            app.ent_dict[tar].set_attr('spirit', -2)
            time = self.timer*666
            killtime = time
            # for proper placement (involving moved_right/down) need to ensure that screen/map does not move during execution of EOT 
            root.after(time, lambda pos1 =app.ent_dict[tar].loc[0]*100+50-app.moved_right , pos2 =app.ent_dict[tar].loc[1]*100+75-app.moved_down, text = '2 Spirit Damage', font = ('Andale Mono', 14), fill = 'white', tags = 'text' : app.canvas.create_text(pos1, pos2, text=text, font=font, fill=fill, tags=tags))
            self.timer += 1
            time = self.timer*666
            root.after(time, lambda t = 'text' : app.canvas.delete(t))
            self.timer += 1
            if app.ent_dict[tar].spirit <= 0:
                root.after(killtime, lambda pos1 =app.ent_dict[tar].loc[0]*100+50-app.moved_right , pos2 =app.ent_dict[tar].loc[1]*100+95-app.moved_down, text = app.ent_dict[tar].name + ' Killed...', font = ('Andale Mono', 14), fill = 'white', tags = 'text' : app.canvas.create_text(pos1, pos2, text=text, font=font, fill=fill, tags=tags))
                root.after(time, lambda id = tar : app.kill(id))
                root.after(time, lambda t = 'text' : app.canvas.delete(t))
            
        eot = partial(take_2, id)
        n = 'Curse_of_Oriax' + str(len(app.ent_dict[id].effects_dict.keys()))
        app.ent_dict[id].effects_dict[n] = Effect(info = 'Curse_of_Oriax\n Stats reduced by 1 for 3 turns\n2 Spirit damage per turn', eot_func = eot, undo = p, duration = 3)
        root.after(2666, lambda  name = 'Curse_of_Oriax' : self.cleanup_spell(name = name))
        
    def gravity(self, event = None):
            # Target ent within range 4 and all ents within range 2 of target may not move until two of their owner's turns have ended, targets are only affected by normal movement, can still be moved through spell/attack effects, if moved out of affected squares then no longer restricted movement, any ent moving into affected squares is immediately halted and is affected in the same way until spell ends
        print('gravity')
        
    def beleths_command(self, event = None):
            # Caster is affect by 'command', while affected cannot be affected by other 'command' effects until spell ends (one 'command' effect at a time), any ent using an attack against caster first must 'to hit' caster's psyche versus attacker's psyche, a success results in normal attack, failure causes spirit damage to attacker (caster's psyche versus attacker's end) and no effects from the attack, lasts until caster has 3 turns end
        print('beleths_command')
        
        
# FAKIR ALI SPELLS
        # Ali's spells center around Heat/Fire/Resistance/Mummification
    def horrid_wilting(self, event = None):
            # make attack (psyche versus str) spirit damage, on any target within range 4 and all adjacent enemy units
        print('horrid_wilting')
        
    def boiling_blood(self, event = None):
            # Caster takes spirit damage (own inverted psyche versus own end) and affects one 'warrior' summon within range 3, any attacks made by the affected target do +5 spirit damage if they would otherwise do any spirit damage, target's agl is increased to 5 if it is less than 5, end is reduced to 1, either value may be later modified but this modification takes precedence over previous effects, affected ent takes 1 spirit damage at the end of every owner's turn
        print('boiling_blood')
        
    def dark_sun(self, event = None):
            # Any caster owned 'shadow' summons within range 2 get an extra attack if they have already attacked once this turn
        print('dark_sun')
        
    def command_of_osiris(self, event = None):
            # Caster is affected by 'command' effect, normal 'command' rules apply as above, Caster cannot move, can still be moved by spell/attack effects, at end of caster's turn any adjacent ents take spirit damage (caster's psyche versus ent's end), all spirit damage done to caster is reduced to 1, lasts until caster has 3 turns end
        print('command_of_osiris')
        
    def disintegrate(self, event = None):
            # Caster must make 'to hit' psyche versus psyche on target summon within range 4, affected summon has attrs (str, agl, end, dodge, psyche) reduced to 1 and cannot move until 2 of its owners turns have ended, attrs or movement cannot be affected by other spells/attack effects
        print('disintegrate')
        
        
# MORGAN SPELLS
        # Morgan's spells center around Nature/Earth/Weather/Illusion
    def enchant(self, event = None):
            # any summon within range 4 has attrs (str, agl, end, dodge, psyche) set to 5 until 3 opp turns have passed, prevents further modification while active
        print('enchant')
        
    def wild_hunt(self, event = None):
            # Creates 3 summons within range 2 of caster or up to 3 if not enough squares available, first is Boar (stats 3,3,3,2,2,4,0) movement range 2 attack any adjacent, second is wolf (2,3,2,4,2,3,0) movement range 3 attack any adjacent, third is hawk (2,4,2,4,3,2,0) movement range 4 not impeded by other units/obstacles attack any adjacent
        print('wild_hunt')
        
    def nodens_command(self, event = None):
            # Command rules apply, caster cannot move, all squares within range 2 of caster become 'water' (impassable terrain) any ents currently occupying these squares are moved to a random square 'at edge' (closest available square to edge of water squares or first unoccupied square if all 'edge' squares are occupied), at end of turn caster heals 4 spirit, lasts until caster has 3 turns end (healing happens first)
        print('nodens_command')
        
    def natures_wrath(self, event = None):
            # Choose a square within range 5, all ents within range 2 of square must 'to hit' their inverted agl versus dodge at the end of every caster's turn, those that 'hit' suffer 3 spirit damage, lasts 3 caster's turns (effect happens 'before' end turn, effects happen 3 times)
        print('natures_wrath')
        
    def counterspell(self, event = None):
            # Choose a spell effect 'in play', make 'to hit' psyche versus effect's owner's psyche, on success cancel all effects from the spell (call its cleanup function) and effect's owner takes magick damage psyche versus psyche
        print('counterspell')
        
    
    # Maybe change name, used not only for finding legal moves, but sqrs within 3 spaces of entity that are unoccupied
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        def findall(loc, start, dist):
            if start > dist:
                return
            adj = [c for c in coords if abs(c[0] - loc[0]) + abs(c[1] - loc[1]) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, dist)
        findall(loc, 1, 3) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.img_dict = {} # is this still used?
        self.ent_dict = {}
        self.sqr_dict = {}
        self.vis_dict = {}
        self.active_player = 'p1'
        self.num_players = 1
        self.moved_right = 0
        self.moved_down = 0
        self.context_buttons = []
        self.help_buttons = []
        # list to hold entity that is being animated as 'attacking'
        self.attacking = []
        self.p1_witch = ''
        self.p2_witch = ''
        self.choose_num_players()
        
        # Luminari 280
        # Herculanum 240
        # Papyrus 240
    def choose_num_players(self):
        self.title_screen = ImageTk.PhotoImage(Image.open('titleScreen2.png'))
        self.subtitle = ImageTk.PhotoImage(Image.open('subtitle.png'))
        self.game_title = tk.Label(root, image = self.title_screen, pady = 140, bg = 'black')
        self.game_title.pack(side = 'top')
        self.marquee = tk.Label(root, image = self.subtitle, bg = 'black', pady = 10)
        self.marquee.pack(side = 'top')
        self.one_player = tk.Button(root, text = '1 Player', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda num = 1 : self.num_chose(num))
        self.one_player.pack(pady = 9)
        self.two_player = tk.Button(root, text = '2 Player', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda num = 2 : self.num_chose(num))
        self.two_player.pack(pady = 9)
        
    def num_chose(self, num):
        self.num_players = num
        self.game_title.destroy()
        self.marquee.destroy()
        self.one_player.destroy()
        self.two_player.destroy()
        if self.num_players == 2:
            self.choose_map()
        else:
            map_number = 0
            self.create_map_curs_context(map_number)
        
    def choose_map(self):
        self.choosemap = tk.Label(root, text = 'Choose Map', fg = 'tan3', bg = 'black', font = ('chalkduster', 38))
        self.choosemap.pack()
        # CHOOSE MAPS
        maps = [m for r,d,m in walk('./2_player_maps')][0]
        self.map_button_list = []
        self.tmp_mapimg_dict = {}
        for i,map in enumerate(maps):
            b = tk.Button(root)
            cmd = lambda indx = i : self.map_choice_cleanup(indx)
            photo = ImageTk.PhotoImage(Image.open('./2_player_maps/' + map).resize((300,300)))
            self.tmp_mapimg_dict['map'+str(i)] = photo
            b.config(image = self.tmp_mapimg_dict['map'+str(i)], bg = 'black', highlightbackground = 'tan3', command = cmd)
            # DEBUG packing will have to be fixed here for different screen sizes
            b.pack(side = 'left', padx = 55)
            self.map_button_list.append(b)
        
    def map_choice_cleanup(self, map_number):
        self.choosemap.destroy()
        del self.tmp_mapimg_dict
        for b in self.map_button_list:
            b.destroy()
        del self.map_button_list
        self.create_map_curs_context(map_number)
        
    def create_map_curs_context(self, map_number):
        # GET MAP DIMENSIONS
        if self.num_players == 1:
            filename = '1_player_map_info/map' + str(map_number) + '.txt'
        else:
            filename = '2_player_map_info/map' + str(map_number) + '.txt'
        with open(filename) as f:
            self.map_info = f.read().splitlines()
        self.map = 'map' + str(map_number)
        self.map_width = int(self.map_info[0])
        self.map_height = int(self.map_info[1])
        # CREATE GRID FROM MAP DIMENSIONS
        col = self.map_width//100
        row = self.map_height//100
        self.grid = [[''] * row for i in range(col)]
        # CONTEXT MENU
        self.con_bg = ImageTk.PhotoImage(Image.open('texture2.png').resize(( 200, root.winfo_screenheight())))
        self.context_menu = tk.Canvas(root, bg = 'black', bd=0, highlightthickness=0, relief='raised', height = root.winfo_screenheight(), width = 200)
        self.context_menu.pack_propagate(0)
        self.context_menu.pack(side = 'left', fill = 'both', expand = 'false')
        self.context_menu.create_image(0, 0, anchor = 'nw', image = self.con_bg)
        # CANVAS
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        if self.map_width < width:
            width = self.map_width
        if self.map_height < height:
            height = self.map_height
        self.canvas = tk.Canvas(root, width = width, bg = 'black', height = height, bd=0, highlightthickness=0, relief='raised')
        self.canvas.pack()
        # MAP
        if self.num_players == 1:
            fname = '1_player_maps/'
        else:
            fname = '2_player_maps/'
        self.map_img = ImageTk.PhotoImage(Image.open(fname + 'map'+str(map_number)+'.jpg').resize((self.map_width, self.map_height)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        # CHOOSE WITCH
        self.choose_witch()
        
    def choose_witch(self, player_num = 1):
        self.avatar_popup = tk.Toplevel()
        self.avatar_popup.attributes('-topmost', 'true')
        self.avatar_popup.attributes("-fullscreen", True)
        self.avatar_popup.config(bg = 'black')
        self.avatar_popup.grab_set()
        label = tk.Label(self.avatar_popup, text = 'Choose Player ' + str(player_num) + ' Witch', font = ('chalkduster', 36), fg = 'indianred', bg = 'black')
        label.pack(side = 'top')
        if player_num == 1:
            witches = [w for r,d,w in walk('./portraits/')][0]
            witches = [w for w in witches[:] if w[0] != '.']
        elif player_num == 2:
            witches = [w for r,d,w in walk('./portraits')][0]
            witches = [w for w in witches[:] if w[0] != '.']
            p1_w_fname = self.p1_witch + '.png'
            witches.remove(p1_w_fname)
        self.avatar_popup.witch_widgets = []
        self.avatar_popup.img_dict = {}
        self.wrapped_funcs = []
        for i,witch in enumerate(witches):
            f = tk.Frame(self.avatar_popup, bg = 'black')
            f.pack(side = 'left')
            self.avatar_popup.witch_widgets.append(f)
            b = tk.Button(f)
            p = partial(self.load_witch, witch[:-4], player_num)
            cmd = lambda win = self.avatar_popup, p = p : self.release_wrapper(win, p)
            self.wrapped_funcs.append(p)
            photo = ImageTk.PhotoImage(Image.open('./portraits/' + witch))
            self.avatar_popup.img_dict[witch] = photo
            # DETERMINE HORIZONTAL PADDING BY SCREENSIZE
            # DEBUG ASSUMES 3 WITCHES, ASSUMES MINIMUM SCREEN WIDTH 900
            width = root.winfo_screenwidth()
            remainder_screen = width - (300 * len(witches))
            horz_pad = (remainder_screen//len(witches))//2
            b.config(image = self.avatar_popup.img_dict[witch],highlightbackground='tan3', font = ('chalkduster', 24), highlightthickness = 1, command = cmd)
            b.pack(side = 'top', padx = horz_pad)
            info = lambda w = witch[:-4] : self.show_avatar_info(w)
            b2 = tk.Button(f)
            whtspc_txt = witch[:-4].replace('_', ' ')
            b2.config(text = whtspc_txt, highlightbackground='tan3', highlightthickness= 1, fg = 'tan3', font = ('chalkduster', 24), command = info)
            b2.pack(side = 'bottom')
            self.avatar_popup.witch_widgets.append(b2)
            self.avatar_popup.witch_widgets.append(b)
        
    def load_witch(self, witch, player_num):
        if player_num == 1:
            self.p1_witch = witch
            loc = [1,1]
        elif player_num == 2:
            self.p2_witch = witch
            loc = [self.map_width//100-2, self.map_height//100-2]
        witch_img = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png'))
        self.ent_dict[witch] = Witch(name = witch, img = witch_img, loc = loc, owner = 'p' + str(player_num))
        self.canvas.create_image(self.ent_dict[witch].loc[0]*100+50-self.moved_right, self.ent_dict[witch].loc[1]*100+50-self.moved_down, image = self.ent_dict[witch].img, tags = witch)
        self.grid[self.ent_dict[witch].loc[0]][self.ent_dict[witch].loc[1]] = witch
        # EXIT FOR 1 PLAYER
        if self.num_players == 1:
            # DEBUG LOAD BOT ENEMIES FOR PLAYER 1 HERE
            # LOAD 1 PLAYER MAP BOT UNITS
            lst = self.map_info[2:]
            c1 = 0
            end = len(lst)
            itlst = iter(lst)
            for x in itlst:
                img = eval(x)
                ent = eval(next(itlst))
                self.ent_dict[ent.number] = ent
                self.canvas.create_image(self.ent_dict[ent.number].loc[0]*100+50, self.ent_dict[ent.number].loc[1]*100+50, image = self.ent_dict[ent.number].img)
                self.grid[self.ent_dict[ent.number].loc[0]][self.ent_dict[ent.number].loc[1]] = ent.number
                c1 += 1
                if c1 == end:
                    break
            self.start_turn()
            self.animate()
        # CHOOSE SECOND PLAYER WITCH
        elif self.num_players == 2 and self.p2_witch == '':
            self.choose_witch(player_num = 2)
        # EXIT CHOOSING IF BOTH FINISHED AND START TURN
        elif self.num_players == 2 and self.p2_witch != '':
            self.start_turn()
            self.animate()
        
            
    def start_turn(self):
        p = self.active_player
        if self.num_players == 1 and p == 'p1':
            self.rebind_all()
            self.get_focus(self.p1_witch)
        elif self.num_players == 2:
            self.rebind_all()
            w = self.p1_witch if p == 'p1' else self.p2_witch
            self.get_focus(w)
        elif self.num_players == 1 and p == 'p2':
            # DEBUG BOT STUFF HERE
            to_act = [x for x in self.ent_dict.keys() if self.ent_dict[x].owner == 'p2']
            self.get_focus(to_act[0])
            root.after(1666, lambda ents = to_act : self.do_ai_loop(ents))
        
    def do_ai_loop(self, ents):
        ent = ents[0]
        self.get_focus(ent)
        if self.ent_dict[ent].name == 'Undead':
            self.ent_dict[ent].do_undead_ai(ents)
        
        
        
    def end_turn(self):
        self.unbind_all()
        self.depop_context(event = None)
        for ent in self.ent_dict.keys():
            if self.ent_dict[ent].owner == self.active_player:
                # DO SPELL EFFECTS / UNDOS
                for ef in list(self.ent_dict[ent].effects_dict.keys()):
                    self.ent_dict[ent].effects_dict[ef].eot_func()
                    # ent is killed by an EOT func effect, break so as not to attempt to execute any more of this ent's EOT effects
                    # ent is programmatically killed by app.kill() called from EOT func on timer
                    if self.ent_dict[ent].spirit <= 0:
                        break
                    self.ent_dict[ent].effects_dict[ef].duration -= 1
                    if self.ent_dict[ent].effects_dict[ef].duration <= 0:
                        # CALL UNDO / DELETE EFFECT
                        self.ent_dict[ent].effects_dict[ef].undo()
                        del self.ent_dict[ent].effects_dict[ef]
                # RESET SPELLS / MOVEMENT / ATTACKS
                self.ent_dict[ent].move_used = False
                if isinstance(self.ent_dict[ent], Witch):
                    self.ent_dict[ent].spell_used = False
                    self.ent_dict[ent].summon_used = False
                elif isinstance(self.ent_dict[ent], Summon):
                    self.ent_dict[ent].attack_used = False
        # END OF CYCLE FOR ALL ENTS
        time = max([self.ent_dict[x].timer for x in self.ent_dict.keys()])
        time *= 1332
        for x in self.ent_dict.keys():
            self.ent_dict[x].timer = 1
        if self.active_player == 'p1':
            self.unbind_all()
            self.active_player = 'p2'
        elif self.active_player == 'p2':
            self.active_player = 'p1'
        root.after(time, self.start_turn)
        
        
        
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
        for vis in self.vis_dict.keys():
            if vis != selected_vis:
                self.vis_dict[vis].rotate_image()
                self.canvas.delete(vis)
                self.canvas.create_image(self.vis_dict[vis].loc[0]*100+50-self.moved_right, self.vis_dict[vis].loc[1]*100+50-self.moved_down, image = self.vis_dict[vis].img, tags = vis)
                app.canvas.tag_raise(vis)
        try: app.canvas.tag_raise('text')
        except: pass
        root.after(300, self.animate)
    
    def populate_context(self, event):
        e = self.current_pos()
        if e == '':
            return
        if self.context_buttons != []:
            print('app.context_buttons not empty')
            return
        self.repop_help_buttons()
        expanded_name = e.replace('_',' ')
        # if generic summon (name ends with number), show class name instead ent.name
        try:
            num = int(e[-1])
            expanded_name = self.ent_dict[e].__class__.__name__
        except:
            pass
        # DEBUG make info button into label that holds the info
        self.cntxt_info_bg = ImageTk.PhotoImage(Image.open('page.png'))
        bg = tk.Canvas(self.context_menu, width = 190, height = 250, bg = 'burlywood4', bd=0, relief='raised', highlightthickness=0)
        bg.pack(side = 'top')
        bg.create_image(0,0, image = self.cntxt_info_bg, anchor = 'nw')
        bg.create_text(15, 15, text=expanded_name + '\n' + self.get_info_text(e), anchor = 'nw', font = ('chalkduster', 18), fill = 'indianred')
        self.context_buttons.append(bg)
        if self.ent_dict[e].owner == self.active_player:
            act_dict = self.ent_dict[e].actions
            for i, act_call in enumerate(act_dict.items()):
                act = act_call[0]
                call = act_call[1]
                i += 1
                root.bind(str(i), call)
                p = partial(call, None)
                b = tk.Button(self.context_menu, text = str(i) + ' : ' + act, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = p)
                b.pack(side = 'top')
                self.context_buttons.append(b)
        
    def depop_context(self, event):
        # unbind any potential numeric keys bound to relative actions
        try:
            for x in range(1, 13):
                root.unbind(str(x))
        except: pass
        for b in self.context_buttons:
            b.destroy()
        self.context_buttons = []
    
    
    def move_curs(self, event = None, dir = None):
        if event == None:
            event = Dummy()
            event.keysym = None
        frame_width = self.canvas.winfo_width()
        frame_height = self.canvas.winfo_height()
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
    def help(self):
        self.help_popup = tk.Toplevel()
        self.help_popup.grab_set()
        self.help_popup.attributes('-topmost', 'true')
        help_text = '''
        You control witch in top left corner\n
        Arrow keys move cursor around map\n
        Cursor over an object you control and press 'a' to see action options\n
        Press 'q' to cancel the context menu for a selected object\n
        Cursor over enemy controlled object and press 'a' for available info\n
        Your witch can cast one spell AND use one summon per turn AND move once\n
        Your summons can move AND use one action per turn\n
        '''
        self.text = tk.Label(self.help_popup, text = help_text, font = ('chalkduster', 24), fg='indianred', bg = 'black')
        self.text.pack()
        self.close = tk.Button(self.help_popup, text = 'Close', font = ('chalkduster', 24), fg='tan3', command = lambda win = self.help_popup : self.destroy_release(win))
        self.close.pack()
        
    def get_info_text(self, ent):
        txt = ''
        txt += 'Str:' + str(self.ent_dict[ent].get_attr('str')) + '\n'
        txt += 'End:' + str(self.ent_dict[ent].get_attr('end')) + '\n'
        txt += 'Agl:' + str(self.ent_dict[ent].get_attr('agl')) + '\n'
        txt += 'Dodge:' + str(self.ent_dict[ent].get_attr('dodge')) + '\n'
        txt += 'Psyche:' + str(self.ent_dict[ent].get_attr('psyche')) + '\n'
        txt += 'Spirit:' + str(self.ent_dict[ent].spirit) + '\n'
        if isinstance(self.ent_dict[ent], Witch):
            txt += 'Magick:' + str(self.ent_dict[ent].magick) + '\n'
        return txt
                 
    def confirm_end(self):
        self.unbind_all()
        self.depop_context(event = None)
        l = tk.Label(self.context_menu, text = 'End Your Turn?', fg = 'indianred', bg = 'black', wraplength = 190, relief = 'raised', font = ('chalkduster', 24))
        self.context_buttons.append(l)
        b1 = tk.Button(self.context_menu, text = 'END', fg = 'indianred', highlightbackground = 'tan3', font = ('chalkduster', 24), command = self.end_turn)
        b1.pack(side = 'bottom')
        self.context_buttons.append(b1)
        b2 = tk.Button(self.context_menu, text = 'Cancel', fg = 'indianred', highlightbackground = 'tan3', font = ('chalkduster', 24), command = self.cancel_end_turn)
        b2.pack(side = 'bottom')
        self.context_buttons.append(b2)
        l.pack(side = 'bottom')
        
    def cancel_end_turn(self):
        self.rebind_all()
        self.depop_context(event = None)
        self.repop_help_buttons()
        
    def show_avatar_info(self, witch):
        self.info_popup = tk.Toplevel()
        self.info_popup.grab_set()
        self.info_popup.attributes('-topmost', 'true')
        self.info_popup.title(witch)
        text = open('avatar_info/' + witch + '.txt', 'r').read()
        f = tk.Frame(self.info_popup)
        f.pack()
        l = tk.Label(f, text = text, font = ('chalkduster', 24))
        l.pack()
        close = tk.Button(self.info_popup, text = 'close', font = ('chalkduster', 24), highlightbackground = 'tan3', command = lambda win = self.info_popup : self.destroy_release(win))
        close.pack()
    
    def animate_squares(self, sqrs):
        for i, sqr in enumerate(sqrs):
            img = ImageTk.PhotoImage(Image.open('animations/move/0.png'))
            self.sqr_dict['sqr'+str(i)] = Sqr(img, sqr)
            self.canvas.create_image(sqr[0]*100+50-self.moved_right, sqr[1]*100+50-self.moved_down, image = self.sqr_dict['sqr'+str(i)].img, tags = 'sqr'+str(i))
            
    def cleanup_squares(self):
        for s in app.sqr_dict.keys():
            app.canvas.delete(s)
        app.sqr_dict = {}
    
    def current_pos(self):
        return self.grid[grid_pos[0]][grid_pos[1]]
        
    def exit_fullscreen(self, event):
        root.attributes("-fullscreen", False)
        
    def destroy_release(self, popup):
        popup.grab_release()
        popup.destroy()
        
    def release_wrapper(self, window, partial):
        window.grab_release()
        window.destroy()
        partial()
        
    def kill(self, id):
        # DEBUG handle if killing witch
        # If witch is dead, show popup with victory/defeat
        self.canvas.delete(id)
        self.grid[self.ent_dict[id].loc[0]][self.ent_dict[id].loc[1]] = ''
        del self.ent_dict[id]
        # if id begins with 'a' belongs to protag_witch, else belongs to antag_witch
        if id[0] == 'a':
            del self.ent_dict[self.p1_witch].summon_dict[id]
        elif id[0] == 'b':
            if self.num_players == 2:
                del self.ent_dict[self.p2_witch].summon_dict[id]
            
    def unbind_all(self):
        root.unbind('<Right>')
        root.unbind('<Left>')
        root.unbind('<Up>')
        root.unbind('<Down>')
        root.unbind('<a>')
        root.unbind('<q>')
#         root.unbind('<Escape>')

    def rebind_all(self):
        root.bind('<Right>', app.move_curs)
        root.bind('<Left>', app.move_curs)
        root.bind('<Up>', app.move_curs)
        root.bind('<Down>', app.move_curs)
        root.bind('<a>', app.populate_context)
        root.bind('<q>', app.depop_context)
#         root.bind('<Escape>', app.exit_fullscreen)

    def confirm_quit(self):
        self.depop_context(event = None)
        self.unbind_all()
    # Instead of label just paste a bunch of intrusive text across the main canvas
    # centered around the grid_pos
        l = tk.Label(self.context_menu, text = 'Confirm Quit', relief = 'raised', fg = 'indianred', bg = 'black', font = ('chalkduster', 24))
        self.context_buttons.append(l)
        b1 = tk.Button(self.context_menu, text = 'QUIT', fg = 'indianred', highlightbackground = 'tan3', font = ('chalkduster', 24), command = root.destroy)
        self.context_buttons.append(b1)
        b2 = tk.Button(self.context_menu, text = 'Cancel', fg = 'indianred', highlightbackground = 'tan3', font = ('chalkduster', 24), command = self.cancel_quit)
        b2.pack(side = 'bottom')
        b1.pack(side = 'bottom')
        self.context_buttons.append(b2)
        l.pack(side = 'bottom')

    def cancel_quit(self):
        # destroy help buttons, repop help buttons, rebind all
        for b in self.context_buttons:
            b.destroy()
        self.repop_help_buttons()
        self.rebind_all()
        
    def repop_help_buttons(self):
        quit_button = tk.Button(self.context_menu, text="QUIT", font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command=self.confirm_quit)
        quit_button.pack(side = 'bottom')
        self.context_buttons.append(quit_button)
        end_turn_button = tk.Button(self.context_menu, text = 'End Turn', font = ('chalkduster', 24), highlightbackground = 'tan3', command = self.confirm_end)
        end_turn_button.pack(side = 'bottom')
        self.context_buttons.append(end_turn_button)
        help_button = tk.Button(self.context_menu, text = 'Help', font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command = self.help)
        help_button.pack(side = 'bottom')
        self.context_buttons.append(help_button)
        

root = tk.Tk()
app = App(master=root)

root.bind('<Right>', app.move_curs)
root.bind('<Left>', app.move_curs)
root.bind('<Up>', app.move_curs)
root.bind('<Down>', app.move_curs)
root.bind('<a>', app.populate_context)
root.bind('<q>', app.depop_context)
# root.bind('<Escape>', app.exit_fullscreen)

root.configure(background = 'black')

root.attributes('-transparent', True)
root.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))

app.mainloop()