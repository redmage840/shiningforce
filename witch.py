# preload all images!

# library, sometimes 2 revenants generated on first turn instead of 1?

# add delay to get_focus / focus_sqr

# unbinding ints 1-4 during summon?

# troll ai still hangs? only sometimes when path is impeded? movement of 9 may influence?

# button to cycle through units, requires adding to 'all hotkeys' that get disabled and enabled during context switches

# make 'click on sqr to move cursor to, maybe 'select unit' (bring up context menu)

# consider limit 1 bard, how does that change certain levels that rely on healing? kensai, dragon. Possibly increase heal amount by ~2 and limit one bard at a time (as opposed to ever)

# confusing - app.effects_counter is used to get unique numbers. Whenever one is needed for an arbitrary purpose, the current value is taken and then app.effects_counter is incremented. The name comes from the fact that Effect instances grab the current value to refer to uniquely refer to the instance AND THEN the init method of the Effect increments app.effects_counter. Elsewhere it is incremented manually.

# remake levels with proper shadows

# make each elemental unique

# only warrior attack has delayed text before kill

# allow click on unit along with press 'a'
#   - click on 100X100 pixel sqr?
# make right click equiv to 'q'
#  - is contextual probably, search each bind of 'q'
# spells right-click for info
#   # bind button when spells populated, each button has rclick function
# on left click, move cursor to sqr?
#   # will be 100x100 sqr pixel areas, relative to screen grid not total grid
# generic death anim placeholder
#   # 'x' animation or cursor(like?) picture, blinking/fading
# randomness to ai 'attack patterns' on some levels, ents 'group up', 'hang back', 'hold position', 'route around'
# force player to approach warlock, fight through interim undead

# BALANCED MEANS YOU SHOULD BE ABLE TO SPEND A LIFETIME EXPLORING ALL THE POSSIBLE STRATEGIES (think chess)

# blood milk sky

# new summon type gained at ritual circle, limit one, does not count towards other summon limit, choose one of few types, demon

# fuse trap (and maybe darkness/poison sting) allows for endless kiting of slow moving enemies (orcs and slower)
# fuse trap probably op in above situations and also not very useful against much faster enemies (dragons, teleporters...)
# mesmerize too good against barbarian (sub-boss of level), newly acquired abilities should be useful on same level, just balance probably by raising psyche of barbarian

# prob change vengeance to something else, not an interesting spell, either op or useless

# barbarian too slow / easy to separate from sorceress, make sorceress able to teleport barbarian from anywhere/further?

# is pain/entomb too good?

# fix sorc teleport barbarian, do not teleport if endloc is further from goal

# one fuse trap at a time?, effects instead of dmg?

# library level, cant move 'all the way down', seems to happen on dragon level also?
# revenant attack, taking focus on target?
# ghost attack better

# death triggers allot 3333 during ai/computer turn, user-controlled ents (either 1player mode killing own units OR 2player mode killing opponent user ents) may currently interrupt the visual resolution (logical not affected) of death triggers by moving beyond edge of map (quickly pressing arrow keys many times during trigger resolution) or calling some effect/spell that takes focus/focus squares on ent that is beyond edge of visible map
# Can potentially fix above by unbind_all() / rebind_all() during death trigger

# potential visual problems when familiar death triggers happen at same time as other death triggers (contagion), due to taking focus in familiar death as soon as called, otherwise all calls to kill() allot 3333 for death trigger resolution

# scrye, hatred, sound effect inaudible

# make all summons use 'regular' movement types that get range based on some attribute so they can be easily altered (+/-N)

# abilities for shadow/warrior buffs

# make plaguebearer a plagued wolf, healable

# more buff/defensive spells

# psi push impact sound

# save during level, write all ents and map number, write globals like curs_pos, write all map_triggers still in effect, write app.attrs like vis_dict effects_counter global_effects_dict, on load call create_map_curs() with protag object, empty and repopulate map_triggers, replace app.attrs

# spells that buff friendly for agnes, one more cantrip for each, debuff cantrip for ali

# kensai cut sound effect, barbarian attack anim and sounds, dragon sounds, orc attack anim, 

# can run bfs() only once by making 'goals' 'dist from ANY enemy_ent'

# warlock_move, pathfinding through walls (completely empty grid) is what causes move to be prematurely shortened due to path through wall that is then ended upon first contact with wall
# fix by finding sqr within legal moves that minimizes distance of attack range
# this approach would only be invalidated by a series of 'block' that is longer than warlock move (does not exist on level)

# entomb handle 'all sqrs occupied' edge case, may not be possible to even reach this state with current levels...?

# update help menu, begin game help screen, spell/attr/action descriptions

# minotaur regen? minotaur kill trigger? kill both undead knight trigger?

# teleport or psi pushing on to sqr with trigger (sparkle), pressing button before cleanup of spell happens will cause spell cleanup to destroy text object if button clicked quickly, no logical problems only visual destroying of text object early

# when dragon 'flies' make bottom portion 'large'

# in 'do_save' if a player saves and then hits cmd/ctrl+q or otherwise exits manually, the object/save may not be pickled properly resulting in zero byte file. This is because programmatic logic 'stays' in 'do_save' until 'next_area' button hit, resulting in not closing the file opened/created during pickling. Using 'with' already to auto-close file, but probably existing vars block out automatic close. To solve this, call some other function from 'do_save' (probably a dummy/empty/close-dialog), probably do not call next_area so as to skip on-screen text

# revenant pathfinding, move along regular grid when egrid path results in all paths end in block
# warlock pathfinding, is searching empty grid? removing 'block'?

# menu options to adjust music, sound effects volume

# make sure ownership checks also work  for 2player mode

# bug with bfs-pathfinding - if there is no 'goal' square (sqr within moving Ents attack range of target) then no path will be returned by bfs, ie if Enemy Ent has attack range of 1 and all squares within range 1 of target are occupied, then no path exists, this will be solved by egrid removing friendly ents UNLESS ent is set to target a specific ent blockaded by its own friendly ents OR if a map contains a square surrounded by 'block' on all squares within range of the pathfinding ent, CURRENTLY no square exists like this on any maps (0-122/22) and only Minotaur pathfinds for specific ents, minotaur mostly handles blockades by removing ALL ents on egrid (except for target)

# get_focus and focus_square calls in conjunction with other 'afters' most likely potential causes for race conditions

# widen teleport vis

# make sure to_hit range has a min/max of 10 or 5 percent

# both need some damaging cantrip when runs out of magick and summons

# stagger text objects when created simultaneously, esp horrid wilting
# dark sun, bottom of anim 'blinks' text object

# level 41, should be able to occupy spawn square to prevent spawns?

# add death of protag scenes

# 2 player mode needs some sort of terrain objective, reasons to engage or hold areas, when and where

# what to do about deaths, need some kind of visual cue

# make popups into fullscreen toplevels

# victory condition happens too fast, need to freeze screen and show 'confirm' or 'notice'

# death anims, at least delay before something like contagion

# would it be possible to 'pause' in the middle of a move_loop or to keep text object on screen

# make walking/movement animations

# magick regen rate or squares on maps that regen?, maybe for some levels, include in intent/design

# show victory conditions on map start

# animate titlescreen

# Instead of 'confirm_quit' labels, paste text across whole screen 

import tkinter as tk
# from tkinter import ttk
from os import walk
from PIL import ImageTk,Image
from random import choice, randrange
from functools import partial
# from pickle import dump, load
from copy import deepcopy
# filehandler = open(filename, 'r') 
# object = pickle.load(filehandler)


# convenience funcs
def dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

# CHANGE TO 'GOAL IS LIST OF GOALS'
# start is coord like [2,3], goal is list of coords like [[2,4],[4,5]...], grid is list of lists where each list is a 'row'
# 'row' holds strings ('', 'EntityID', or 'block')
# returns path from start to goal (list of coords)
def bfs(start, goal, grid):
#     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
    path = []
    q = [[start]]
    visited = [start]
    while q:
        path = q[0]
        q = q[1:]
        last = path[-1]
        if last in goal:
            return path
        adj = [c for c in app.coords if dist(c, last) == 1 and grid[c[0]][c[1]] == '']
        for s in adj:
            if s not in visited:
                q.append(path + [s])
                visited.append(s)

def to_hit(a1, a2):
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
def damage(a1, a2):
    base = 5
    dif = a1 - a2
    if base + dif < 1: return 1 
    else: return base + dif

# GLOBALS
curs_pos = [0, 0]
is_object_selected = False
selected = []
selected_vis = ''

map_pos = [0, 0]

grid_pos = [0,0]


# change to only import what is neededmm
# import pygame
from pygame import mixer
freq = 44100     # audio CD quality
bitsize = -16    # unsigned 16 bit
channels = 1     # 1 is mono, 2 is stereo
buffer = 1024    # number of samples (experiment to get right sound)
# use this just for intro screen, ideally make it loop smoothly (no lull in sound)
mixer.init(freq, bitsize, channels, buffer)
background_music = mixer.Channel(0) # argument must be int
sound_effects = mixer.Channel(1)
# background_music.music.set_volume(0.7) # optional volume 0 to 1.0
# background_music.music.load('Ove Melaa - Dead, Buried and Cold.ogg')
# background_music.music.play(-1, 0)

class Dummy():
    def __init__(self):
        pass

class Effect():
    def __init__(self, name, info, eot_func, undo, duration, sot_func = None):
        self.name = name
        if sot_func == None:
            def nothing():
                return None
            self.sot_func = nothing
        else:
            self.sot_func = sot_func
        self.eot_func = eot_func
        self.info = info
        self.undo = undo
        self.duration = duration
        app.effects_counter += 1


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
    def __init__(self, name, img, loc, owner, type = 'normal'):
#         self.timer = 1 # COUNTER FOR TIMING EOT EFFECT TEXT OBJECTS
        self.name = name
        self.img = img
        self.loc = loc
        self.owner = owner
        self.move_used = False
        self.type = type
        self.immovable = False
        if isinstance(self, Witch):
            self.tags = self.name
        elif self.type == 'large':
            self.tags = ('large', self.number)
        elif isinstance(self, Summon):
            self.tags = self.number
            
        if isinstance(self, Witch) or isinstance(self, Summon):
            self.base_str = self.str
            self.base_agl = self.agl
            self.base_end = self.end
            self.base_dodge = self.dodge
            self.base_psyche = self.psyche
            self.base_spirit = self.spirit
            if isinstance(self, Witch):
                self.base_magick = self.magick
            
            self.str_effects = []
            self.agl_effects = []
            self.end_effects = []
            self.dodge_effects = []
            self.psyche_effects = []
        # when ent moved by effect other than regular movement, must update origin also (square of origin at begin of turn)
#         self.origin = []
        self.effects_dict = {}
        self.anim_dict = {}
        anims = [a for r,d,a in walk('./animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/' + self.name + '/' + anim))
            self.anim_dict[i] = a
        # randomize animation 'seed' to stagger different ent animations
        self.anim_counter = randrange(0, len(anims))
            
    def death_trigger(self):
        return None
            
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
            
    def init_cast_anims(self):
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('./casting_animations/' + self.name + '/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('casting_animations/' + self.name + '/' + anim))
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
            if self.spirit > self.base_spirit:
                self.spirit = self.base_spirit
        elif isinstance(self, Witch) or isinstance(self, Trickster):
            if attr == 'magick':
                self. magick += amount
                if self.magick > self.base_magick:
                    self.magick = self.base_magick
            
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
            a *= 10
        rand = randrange(-1, 102)
        if a > rand:
            return True # pass
        else:
            return False # fail
            
    # Move for user controlled Ents that cannot move through obstacles
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
        app.unbind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        if isinstance(self, Witch) or isinstance(self, Bard) or isinstance(self, Warrior) or isinstance(self, Plaguebearer):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Familiar_Imp):
            effect1 = mixer.Sound('Sound_Effects/familiar_imp_move.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Familiar_Homonculus):
            effect1 = mixer.Sound('Sound_Effects/familiar_homonculus_move.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        # start ANIM here
        if isinstance(self, Witch):
            id = self.name
        else:
            id = self.number
        start_sqr = self.loc[:]
        end_sqr = grid_pos[:]
        selected = [id]
        # get path and move_loop over each sqr until path consumed
        path = bfs(start_sqr, [end_sqr], app.grid) # end_sqr must be in list
        begin = path[0]
        end = path[1]
        x = begin[0]*100+50-app.moved_right
        y = begin[1]*100+50-app.moved_down
        endx = end[0]*100+50-app.moved_right
        endy = end[1]*100+50-app.moved_down
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path):
            if x % 20 == 0 or y % 20 == 0:
                self.rotate_image()
                app.canvas.delete(id)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
            if x > endx:
                x -= 10
                app.canvas.move(id, -10, 0)
            if x < endx: 
                x += 10
                app.canvas.move(id, 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(id, 0, -10)
            if y < endy: 
                y += 10
                app.canvas.move(id, 0, 10)
            try: app.canvas.tag_lower((self.tags), 'large')
            except: pass
            app.canvas.tag_lower((app.ent_dict[id].tags), 'maptop')
            app.canvas.tag_raise('cursor')
            if x == end_sqr[0]*100+50-app.moved_right and y == end_sqr[1]*100+50-app.moved_down: # END WHOLE MOVE
                self.finish_move(id, end_sqr, start_sqr)
            elif x == endx and y == endy: # END PORTION OF PATH
                path = path[1:]
                begin = path[0]
                end = path[1]
                x = begin[0]*100+50-app.moved_right
                y = begin[1]*100+50-app.moved_down
                endx = end[0]*100+50-app.moved_right
                endy = end[1]*100+50-app.moved_down
                move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, ex = endx, ey = endy, s = start_sqr, s2 = end_sqr, p = path : move_loop(id, x, y, ex, ey, s, s2, p))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
        
    # used by trickster, shadow, ...
    def teleport_move(self, event = None):
        if self.move_used == True:
            return
        # depop context, unbind, bind 'a' do move, bind 'q' cancel move, get/animate sqrs, make confirm / cancel button
        app.depop_context(event = None)
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_move)
        sqrs = self.legal_moves()
        app.animate_squares(sqrs)
        if isinstance(self, Shadow):
            text = 'Confirm Shadow Move'
        else:
            text = 'Confirm Teleport Square'
        b = tk.Button(app.context_menu, text = text, wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.do_teleport(e, s))
        b.pack(side = 'top', pady = 3)
        app.context_buttons.append(b)
        root.bind('<a>', lambda e, s = sqrs : self.do_teleport(e, s))
        
    def do_teleport(self, event, sqrs):
#         global selected
        endloc = grid_pos[:]
        if endloc not in sqrs:
            return
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        self.move_used = True
        oldloc = self.loc[:]
        if isinstance(self, Shadow):
            effect1 = mixer.Sound('Sound_Effects/shadow_move.ogg')
            effect1.set_volume(.3)
            sound_effects.play(effect1, 0)
            app.vis_dict['Shadow_Move'] = Vis(name = 'Shadow_Move', loc = oldloc[:])
            vis = app.vis_dict['Shadow_Move']
        else:
            effect1 = mixer.Sound('Sound_Effects/teleport_move.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc[:])
            vis = app.vis_dict['Teleport']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(1999, lambda endloc = endloc : self.finish_teleport(endloc))
        
    def finish_teleport(self, endloc):
        app.grid[self.loc[0]][self.loc[1]] = ''
        app.canvas.delete(self.number)
        self.loc = endloc[:]
#         app.ent_dict[id].origin = newloc[:]
        app.grid[endloc[0]][endloc[1]] = self.number
        app.canvas.delete('Teleport')
        if isinstance(self, Shadow):
            del app.vis_dict['Shadow_Move']
            app.vis_dict['Shadow_Move'] = Vis(name = 'Shadow_Move', loc = endloc[:])
            vis = app.vis_dict['Shadow_Move']
        else:
            effect1 = mixer.Sound('Sound_Effects/teleport_move.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            del app.vis_dict['Teleport']
            app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = endloc[:])
            vis = app.vis_dict['Teleport']
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(1999, lambda endloc = endloc : self.cleanup_teleport(endloc))
        
    def cleanup_teleport(self, endloc):
        try: 
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        try: 
            del app.vis_dict['Shadow_Move']
            app.canvas.delete('Shadow_Move')
        except: pass
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        try: app.canvas.tag_lower(self.tags, 'large')
        except: pass
        app.canvas.tag_lower(self.tags, 'maptop')
        app.depop_context(event = None)
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
            
            
    def finish_move(self, id, end, start):
        sound_effects.stop()
        global selected
        selected = []
        oldloc = start
        newloc = end
        self.loc = newloc[:]
        self.origin = newloc[:]
        app.grid[oldloc[0]][oldloc[1]] = ''
        if isinstance(self, Witch):
            app.grid[newloc[0]][newloc[1]] = self.name
        elif isinstance(self, Summon):
            app.grid[newloc[0]][newloc[1]] = self.number
        self.move_used = True
        self.cleanup_move()
        
    def cleanup_move(self, event = None):
        app.depop_context(event = None)
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
    

class Summon(Entity):
    def __init__(self, name, img, loc, owner, number, type = 'normal'):
        self.number = number
        super().__init__(name, img, loc, owner, type = type)
        
    # only called by computer controlled Entities, takes the list of all entities to act that is consumed by each entity as it uses its turn, and the location being moved to
    def ai_move(self, ents_list, endloc):
        global selected
        if isinstance(self, Tortured_Soul):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Kensai):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Undead):
            effect1 = mixer.Sound('Sound_Effects/undead_move.ogg')
            effect1.set_volume(2)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Undead_Knight):
            effect1 = mixer.Sound('Sound_Effects/undead_knight_move.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Troll):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Orc_Axeman):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        elif isinstance(self, Barbarian):
            effect1 = mixer.Sound('Sound_Effects/footsteps.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, -1)
        selected = [self.number]
        id = self.number
        start_sqr = self.loc[:]
        end_sqr = endloc[:] # redundant naming of vars
        path = bfs(start_sqr, [end_sqr], app.grid) # end_sqr must be put in list
        begin = path[0]
        end = path[1]
        x = begin[0]*100+50-app.moved_right
        y = begin[1]*100+50-app.moved_down
        endx = end[0]*100+50-app.moved_right
        endy = end[1]*100+50-app.moved_down
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path):
            if x % 20 == 0 or y % 20 == 0:
                self.rotate_image()
                app.canvas.delete(id)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
            if x > endx:
                x -= 10
                app.canvas.move(id, -10, 0)
            if x < endx: 
                x += 10
                app.canvas.move(id, 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(id, 0, -10)
            if y < endy: 
                y += 10
                app.canvas.move(id, 0, 10)
            try: app.canvas.tag_lower((self.tags), 'large')
            except: pass
            app.canvas.tag_lower((self.tags), 'maptop')
            app.canvas.tag_raise('cursor')
            if x == end_sqr[0]*100+50-app.moved_right and y == end_sqr[1]*100+50-app.moved_down: # END WHOLE MOVE
                self.ai_finish_move(end_sqr, start_sqr, ents_list)
            elif x == endx and y == endy: # END PORTION OF PATH
                path = path[1:]
                begin = path[0]
                end = path[1]
                x = begin[0]*100+50-app.moved_right
                y = begin[1]*100+50-app.moved_down
                endx = end[0]*100+50-app.moved_right
                endy = end[1]*100+50-app.moved_down
                move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, ex = endx, ey = endy, s = start_sqr, s2 = end_sqr, p = path : move_loop(id, x, y, ex, ey, s, s2, p))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
        
    def ai_finish_move(self, end_sqr, start_sqr, ents_list):
        global selected
        sound_effects.stop()
        selected = []
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        # MAKE ATTACK ON ANY ENEMY ENT WITHIN RANGE
        atk_sqrs = self.legal_attacks()
        ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
        enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
        if isinstance(self, Kensai):
            enemy_ents = [e for e in enemy_ents if app.grid[e[0]][e[1]] not in self.attacked_ids]
        if enemy_ents != []:
            any = enemy_ents[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda t = id : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
class Tomb(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {}
        self.attack_used = False
        self.str = 1
        self.agl = 1
        self.end = 5
        self.dodge = 1
        self.psyche = 5
        self.spirit = 20
        self.move_type = 'immobile'
        super().__init__(name, img, loc, owner, number)
        
        
class Trickster(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Pyrotechnics':self.pyrotechnics, 'Simulacrum':self.simulacrum,'Gate':self.gate,'Teleport':self.teleport_move}
        self.attack_used = False
        self.str = 2
        self.agl = 4
        self.end = 2
        self.dodge = 5
        self.psyche = 5
        self.spirit = 13
        self.move_type = 'teleport'
        super().__init__(name, img, loc, owner, number)
        
    def pyrotechnics(self, event):
        if self.attack_used == True:
            return
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_pyrotechnics)
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 3]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_pyrotechnics(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Pyrotechnics', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_pyrotechnics(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_pyrotechnics(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        effect1 = mixer.Sound('Sound_Effects/pyrotechnics.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        id = app.current_pos()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.attack_used = True
        app.vis_dict['Pyrotechnics'] = Vis(name = 'Pyrotechnics', loc = sqr[:])
        vis = app.vis_dict['Pyrotechnics']
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = vis.img, tags = 'Pyrotechnics')
        app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = 'Pyrotechnics\n2 Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 13), tags = 'text')
        app.ent_dict[id].set_attr('spirit', -2)
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+95, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 13), tags = 'text')
        root.after(1666, lambda e = None, id = id : self.cleanup_pyrotechnics(event = e, id = id))
        
    def cleanup_pyrotechnics(self, event = None, id = None):
        try: 
            del app.vis_dict['Pyrotechnics']
            app.canvas.delete('Pyrotechnics')
        except: pass
        app.unbind_all()
        app.rebind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        if id:
            if app.ent_dict[id].spirit <= 0:
                app.kill(id)
        app.canvas.delete('text')
        
        
    def simulacrum(self, event):
        if self.attack_used == True:# or self.magick < 3:
            return
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_simulacrum)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_simulacrum(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Simulacrum', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_simulacrum(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_simulacrum(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        # PREVENT STACKING OF SIMULACRUM
        if 'Simulacrum' in app.ent_dict[id].effects_dict.keys():
            return
#         self.set_attr('magick', -3)
        effect1 = mixer.Sound('Sound_Effects/simulacrum.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.attack_used = True
        # DO SIMULACRUM EFFECTS
        def simulacrum_effect(stat):
            stat += 3
            return stat
        f = simulacrum_effect
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        def un(i):
            app.ent_dict[i].agl_effects.remove(simulacrum_effect)
            app.ent_dict[i].dodge_effects.remove(simulacrum_effect)
            return None
        p = partial(un, id)
        def nothing():
            return None
        eot = nothing
        n = 'Simulacrum' + str(app.effects_counter)
        app.ent_dict[id].effects_dict['Simulacrum'] = Effect(name = 'Simulacrum', info = 'Simulacrum\nAgl, Dodge incr by 3 for 3 turns', eot_func = eot, undo = p, duration = 3)
        # DO SIMULACRUM VISUALS
        start_loc = app.ent_dict[id].loc[:]
        app.vis_dict['Simulacrum'] = Vis(name = 'Simulacrum', loc = start_loc[:])
        app.canvas.create_image(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+50-app.moved_down, image = app.ent_dict[id].img, tags = 'left')
        app.canvas.create_image(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+50-app.moved_down, image = app.ent_dict[id].img, tags = 'right')
        app.canvas.create_image(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+50-app.moved_down, image = app.vis_dict['Simulacrum'].img, tags = ('Simulacrum','right'))
        app.canvas.create_image(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+50-app.moved_down, image = app.vis_dict['Simulacrum'].img, tags = ('Simulacrum','left'))
        app.canvas.create_text(start_loc[0]*100+50-app.moved_right, start_loc[1]*100+95-app.moved_down, text = 'Simulacrum', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        x = start_loc[0]*100+50-app.moved_right
        y = start_loc[1]*100+50-app.moved_down
        end_left = start_loc[0]*100-app.moved_right # minus 50 from center
        end_right = start_loc[0]*100+100-app.moved_right # plus 50 from center
        selected_vis = 'Simulacrum'
        def simulacrum_loop_left(vis, x, y, end_left, tar):
            if x % 5 == 0: # this just gets new image (flickers simulacrum opacity)
                app.vis_dict[vis].rotate_image()
                app.canvas.delete('left') # this deletes both vis left and right
                app.canvas.create_image(x, y, image = app.ent_dict[tar].img, tags = 'left')
                app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = ('Simulacrum','left'))
            app.canvas.tag_raise(vis)
            if x > end_left:
                x -= 10
                app.canvas.move('left',-10,0)
            if x == end_left:
                pass
            else:
                root.after(100, lambda vis = 'Simulacrum', x = x, y = y, end_left = end_left, tar = tar : simulacrum_loop_left(vis, x, y, end_left, tar))
        def simulacrum_loop_right(vis, x, y, end_right, tar):
            if x % 5 == 0: # this just gets new image (flickers simulacrum opacity)
                app.vis_dict[vis].rotate_image()
                app.canvas.delete('right') # this deletes both vis left and right
                app.canvas.create_image(x, y, image = app.ent_dict[tar].img, tags = 'right')
                app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = ('Simulacrum','right'))
            app.canvas.tag_raise(vis)
            if x < end_right:
                x += 10
                app.canvas.move('right',10,0)
            if x == end_right:
                root.after(666, self.cleanup_simulacrum)
            else:
                root.after(100, lambda vis = 'Simulacrum', x = x, y = y, end_right = end_right, tar = tar : simulacrum_loop_right(vis, x, y, end_right, tar))
        simulacrum_loop_left('Simulacrum', x, y, end_left, id)
        simulacrum_loop_right('Simulacrum', x, y, end_right, id)
        
        
    def cleanup_simulacrum(self, event = None):
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        app.canvas.delete('left')
        app.canvas.delete('right')
        try: 
            del app.vis_dict['Simulacrum']
            app.canvas.delete('Simulacrum')
        except: pass
        app.canvas.delete('text')
        
        
    def gate(self, event = None):
        if self.attack_used == True:# or self.magick < 3:
            return
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_gate)
        root.unbind('<a>')
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in app.coords:
            if dist(c, self.loc) <= 2:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.choose_target(e, sqrs = s))
        b = tk.Button(app.context_menu, text = 'Choose Target', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.choose_target(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    def choose_target(self, event = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        id = app.current_pos()
        if app.ent_dict[id].type == 'large':
            return
        if app.ent_dict[id].immovable == True:
            return
        app.depop_context(event = None)
        app.unbind_all()
        app.rebind_all()
        root.unbind('<q>')
        root.unbind('<a>')
        root.bind('<q>', self.cleanup_gate)
#         self.set_attr('magick', -3)
#         my_psyche = self.get_attr('psyche')
#         target_psyche = app.ent_dict[id].get_attr('psyche')
        distance = 5 #damage(my_psyche, target_psyche)
        app.cleanup_squares()
        sqrs = self.doorway_squares(distance)
        if sqrs == []:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+60-app.moved_down, text = 'No Available Area', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(999, self.cleanup_gate)
        else:
            app.animate_squares(sqrs)
            root.bind('<a>', lambda e, id = id, sqrs = sqrs : self.do_gate(e, id = id, sqrs = sqrs))
            b = tk.Button(app.context_menu, text = 'Choose Location', font = ('chalkduster', 24), fg = 'tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, id = id, s = sqrs : self.do_gate(e, id, s))
            b.pack(side = 'top')
            app.context_buttons.append(b)

    
    #Put VIS IN HERE
    def do_gate(self, event = None, id = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        self.attack_used = True
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        effect1 = mixer.Sound('Sound_Effects/gate.ogg')
        effect1.set_volume(.7)
        sound_effects.play(effect1, 0)
        oldloc = app.ent_dict[id].loc[:]
        newloc = grid_pos[:]
        app.vis_dict['Gate'] = Vis(name = 'Gate', loc = oldloc[:])
        vis = app.vis_dict['Gate']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Gateway')
        root.after(1666, lambda newloc = newloc, id = id : self.finish_gate(newloc, id))
        
    def finish_gate(self, newloc, id):
        app.grid[app.ent_dict[id].loc[0]][app.ent_dict[id].loc[1]] = ''
        app.canvas.delete(id)
        app.ent_dict[id].loc = newloc[:]
        app.ent_dict[id].origin = newloc[:]
        app.grid[newloc[0]][newloc[1]] = id
        try: 
            del app.vis_dict['Gate']
            app.canvas.delete('Gate')
        except: pass
        app.vis_dict['Gate'] = Vis(name = 'Gate', loc = newloc[:])
        vis = app.vis_dict['Gate']
        root.after(1666, lambda id = id, newloc = newloc : self.place_entity(id, newloc))
        
    def place_entity(self, id, newloc):
        del app.vis_dict['Gate']
        app.canvas.delete('Gate')
        app.canvas.create_image(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+50-app.moved_down, image = app.ent_dict[id].img, tags = app.ent_dict[id].tags)
        try: app.canvas.tag_lower((app.ent_dict[id].tags), 'large')
        except: pass
        app.canvas.tag_lower((app.ent_dict[id].tags), 'maptop')
        root.after(666, self.cleanup_gate)
    
    def doorway_squares(self, distance):
        sqr_list = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in coord_pairs:
            if dist(c, self.loc) <= distance: 
                if app.grid[c[0]][c[1]] == '':
                    sqr_list.append(c)
        return sqr_list
    
    def cleanup_gate(self, event = None):
        try:
            del app.vis_dict['Gate']
            app.canvas.delete('Gate')
        except: pass
        app.canvas.delete('text')
        app.depop_context(event = None)
        app.cleanup_squares()
        app.rebind_all()
    
    def legal_moves(self):
        move_list = []
        for c in app.coords:
            if app.grid[c[0]][c[1]] == '':
                if dist(c, self.loc) <= 4:
                    move_list.append(c)
        return move_list
        

class Shadow(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Attack':self.shadow_attack, 'Shadow Move':self.teleport_move}
        self.attack_used = False
        self.str = 3
        self.agl = 3
        self.end = 3
        self.dodge = 6
        self.psyche = 4
        self.spirit = 14
        self.move_type = 'teleport'
        super().__init__(name, img, loc, owner, number)
        
        
    def shadow_attack(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        root.unbind('<a>')
        sqrs = []
        for coord in app.coords:
            if 1 < dist(coord, self.loc) <= 4:
                sqrs.append(coord)
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, sqr = grid_pos, sqrs = sqrs : self.check_hit(e, sqr, sqrs))
        app.depop_context(event = None)
        b = tk.Button(app.context_menu, text = 'Confirm Attack', font = ('chalkduster', 24), fg='tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, sqr = grid_pos, sqrs = sqrs: self.check_hit(event = e, sqr = sqr, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def check_hit(self, event = None, sqr = None, sqrs = None):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        effect1 = mixer.Sound('Sound_Effects/shadow_attack.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.unbind_all()
        my_psyche = self.get_attr('psyche')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        app.vis_dict['Shadow_Attack'] = Vis(name = 'Shadow_Attack', loc = sqr[:])
        vis = app.vis_dict['Shadow_Attack']
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = vis.img, tags = 'Shadow_Attack')
        if to_hit(my_psyche, target_dodge) == True:
            # VISUAL TO HIT
            my_psyche = self.get_attr('psyche')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_psyche, target_end)
            app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+75, text = 'Shadow Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
#             if isinstance(app.ent_dict[id], Witch):
#                 app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+75, text = str(d) + ' Magick', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
#                 app.ent_dict[id].set_attr('magick', -d)
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+100, text = app.ent_dict[id].name.replace('_', ' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2333, lambda e = None, id = id : self.cancel_attack(event = e, id = id))
        else:
            app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+50, text = 'Shadow Attack Missed!\n', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2333, lambda e = None, id = id : self.cancel_attack(event = e, id = id))
        self.attack_used = True
    
    
    def cancel_attack(self, event = None, id = None):
        app.canvas.delete('text')
        try:
            del app.vis_dict['Shadow_Attack']
            app.canvas.delete('Shadow_Attack')
        except: pass
        if id:
            if app.ent_dict[id].spirit <= 0:
                app.kill(id)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.rebind_all()
    
    def legal_moves(self):
        move_list = []
        for c in app.coords:
            if app.grid[c[0]][c[1]] == '':
                if dist(self.loc, c) <= 4:
                    move_list.append(c)
        return move_list


# contagion adjacent ents on death
class Plaguebearer(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'pox':self.pox, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 2
        self.end = 6
        self.dodge = 2
        self.psyche = 5
        self.spirit = 15
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
#     Override superclass set_attr(self, attr, amount) to check for own death, if no death call superclass set_attr
#     def set_attr(self, attr, amount):
    def death_trigger(self):
        effect1 = mixer.Sound('Sound_Effects/contagion.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        # app.kill is handled by killer effect/attack, just do contagion
#         if attr == 'spirit' and self.spirit + amount < 1: # amount is passed int 'negative' for subtracting attrs
            # DO CONTAGION
            # get Ents within AOE
#         coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in app.coords if dist(self.loc, c) == 1]
        ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        for e in ents:
            # cannot stack contagion
            ef_names = [v.name for k,v in app.ent_dict[e].effects_dict.items() if v.name == 'Contagion']
            if 'Contagion' in ef_names:
                continue
            else:
                # create Effect, needs name, info, eot_func, undo, duration
                n = 'Contagion' + str(app.effects_counter)
                info = 'Contagion\n-2 Str -2 End for 3 turns'
                def contagion_effect(stat):
                    stat -= 3
                    if stat < 1:
                        return 1
                    else:
                        return stat
                f = contagion_effect
                app.ent_dict[e].str_effects.append(f)
                app.ent_dict[e].end_effects.append(f)
                app.ent_dict[e].agl_effects.append(f)
                app.ent_dict[e].dodge_effects.append(f)
                def un(id, func):# change to get name of effect, remove by name
#                         name = 'contagion_effect'
                    app.ent_dict[id].str_effects.remove(func)
                    app.ent_dict[id].end_effects.remove(func)
                    app.ent_dict[id].agl_effects.remove(func)
                    app.ent_dict[id].dodge_effects.remove(func)
                    return None
                p = partial(un, e, f)
                def nothing():
                    return None
                eot = nothing
                d = 3
                app.ent_dict[e].effects_dict[n] = Effect(name = 'Contagion', info = info, eot_func = eot , undo = p, duration = 3)
                # DO DAMAGE AND VIS
                n2 = 'Contagion' + str(app.effects_counter) # not an effect, just need unique int
                app.effects_counter += 1 # that is why this is incr manually here, no Effect init
                app.vis_dict[n2] = Vis(name = 'Contagion', loc = app.ent_dict[e].loc[:])
                rand_start_anim = randrange(1,7)
                for i in range(rand_start_anim):
                    app.vis_dict[n2].rotate_image()
                app.canvas.create_text(app.ent_dict[e].loc[0]*100-app.moved_right+50, app.ent_dict[e].loc[1]*100-app.moved_down+90, text = 'CONTAGION', justify = 'center', fill = 'green2', font = ('Andale Mono', 16), tags = ('contagion_text'))# CALLED DURING A SET_ATTR, SO NEED A DIFFERENT TEXT TAG TO AVOID CLEANUP OF UNRELATED TEXT OBJECTS ON CANVAS
                app.canvas.create_image(app.ent_dict[e].loc[0]*100+50-app.moved_right, app.ent_dict[e].loc[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = n2)
                
        root.after(3333, self.cleanup_contagion)
        return 'Not None'
#             super(Plaguebearer, self).set_attr(attr, amount)
#         else:
#             super(Plaguebearer, self).set_attr(attr, amount)
        
    def cleanup_contagion(self):
        try:
            keys = [k for k,v in app.vis_dict.items() if v.name == 'Contagion']
            for k in keys:
                del app.vis_dict[k]
            app.canvas.delete('Contagion')
        except: pass
        app.canvas.delete('contagion_text')
        
    # give all adj units pox Effect if they have no pox effects, causes 2 spirit damage EOT, if affected ent's movement is blocked by obstacles it's movement is reduced by 1 to a minimum of 1, lasts 4 turns
    def pox(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_pox)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in app.coords if dist(self.loc, c) == 1]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.do_pox(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Pox', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.do_pox(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    # make pox vis regardless of existing ents
    def do_pox(self, event = None, sqrs = None):
        effect1 = mixer.Sound('Sound_Effects/pox.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        self.attack_used = True
#         self.init_attack_anims()
        app.cleanup_squares()
        app.depop_context(event = None)
        app.unbind_all()
        ents = []
        for s in sqrs:
            n2 = 'Pox' + str(app.effects_counter) # not an effect, just need unique int
            app.effects_counter += 1 # that is why this is incr manually here, no Effect init
            app.vis_dict[n2] = Vis(name = 'Pox', loc = s)
            rand_start_anim = randrange(1,7)
            for i in range(rand_start_anim):
                app.vis_dict[n2].rotate_image()
#             app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Pox')
            ent = app.grid[s[0]][s[1]]
            if ent != '' and ent != 'block' and isinstance(app.ent_dict[ent].__class__, Plaguebearer) == False:
                #GIVE POX EFFECT if doesn't exist
                ef_names = [v.name for k,v in app.ent_dict[ent].effects_dict.items()]
                if 'Pox' not in ef_names:
#                     n2 = 'Pox' + str(app.effects_counter) # not an effect, just need unique int
#                     app.effects_counter += 1 # that is why this is incr manually here, no Effect init
#                     app.vis_dict[n2] = Vis(name = 'Pox', loc = s)
#                     rand_start_anim = randrange(1,7)
#                     for i in range(rand_start_anim):
#                         app.vis_dict[n2].rotate_image()
#                     app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Pox')
                    n = 'Pox'+str(app.effects_counter)
                    # needs name, info, eot_func, undo, duration
                    def take_3(tar):
                        app.get_focus(tar)
                        app.ent_dict[tar].set_attr('spirit', -3)
                        app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+60-app.moved_down, text = '3 Spirit\nPox', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        if app.ent_dict[tar].spirit <= 0:
                            app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        return 'Not None'
                    # EOT
                    eot = partial(take_3, ent)
                    # UNDO
                    def un():
                        return None
                    u = un
                    # POX VIS
                    app.ent_dict[ent].effects_dict[n] = Effect(name = 'Pox', info = 'Pox\n2 Spirit damage EOT\n-1 to Entities with normal movement', eot_func = eot , undo = u, duration = 4)
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100-app.moved_right+50, app.ent_dict[ent].loc[1]*100-app.moved_down+90, text = 'Pox', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                
        root.after(2999, self.finish_pox)
        
    def finish_pox(self, event = None):
#         self.init_normal_anims()
        try:
            keys = [k for k in app.vis_dict.keys() if k[:3] == 'Pox']
            for k in keys:
                del app.vis_dict[k]
            app.canvas.delete('Pox')
        except: pass
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
        app.cleanup_squares()
    
    
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 2)
        return [list(x) for x in set(tuple(x) for x in mvlist)]



class Bard(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Unholy Chant':self.unholy_chant, 'Discord' : self.discord, 'Moonlight' : self.moonlight, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 3
        self.end = 3
        self.dodge = 5
        self.psyche = 5
        self.spirit = 15
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
        
    def moonlight(self, event = None):
        if self.attack_used == True:
            return
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_moonlight)
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 2]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_moonlight(event = e, s = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Moonlight', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_moonlight(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_moonlight(self, event, s, sqrs):
        global selected_vis
        id = app.grid[s[0]][s[1]]
        if id == '' or id == 'block':
            return
        if s not in sqrs:
            return
        if not isinstance(app.ent_dict[id], Trickster) and not isinstance(app.ent_dict[id], Warrior) and not isinstance(app.ent_dict[id], Bard) and not isinstance(app.ent_dict[id], Shadow):
             return
        effect1 = mixer.Sound('Sound_Effects/moonlight.ogg')
        effect1.set_volume(.2)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
#         self.init_cast_anims()
        app.ent_dict[id].set_attr('spirit', 3)
        self.attack_used = True
        app.vis_dict['Moonlight'] = Vis(name = 'Moonlight', loc = s)
        app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+70-app.moved_down, image = app.vis_dict['Moonlight'].img, tags = 'Moonlight')
        app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+65-app.moved_down, text = 'Moonlight\n+3 Spirit', font = ('Andale Mono', 16), fill = 'azure', tags = 'text')
        selected_vis = 'Moonlight'
        # needs to be moved upwards at the same rate, when rotating image also move up one tick
        def moonlight_loop(starty, endy, x):
            if starty > endy:
                app.vis_dict['Moonlight'].rotate_image()
                app.canvas.delete('Moonlight')
                app.canvas.create_image(x, starty, image = app.vis_dict['Moonlight'].img, tags = 'Moonlight')
                starty -= 10
                app.canvas.move('Moonlight', 0, -10)
                app.canvas.tag_raise('Moonlight')
            if starty == endy:
                root.after(333, self.cleanup_moonlight)
            else:
                root.after(166, lambda sy = starty, ey = endy, x = x : moonlight_loop(sy, ey, x))
        locy = s[1]*100+70-app.moved_down
        locx = s[0]*100+50-app.moved_right
        moonlight_loop(locy, locy-120, locx)
        
    def cleanup_moonlight(self, event = None):
        global selected, selected_vis
#         self.init_normal_anims()
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        try: 
            del app.vis_dict['Moonlight']
            app.canvas.delete('Moonlight')
        except: pass
        try: app.canvas.delete('text')
        except: pass
        selected = []
        selected_vis = ''
        
    # change to effect that gives +1 to all stats for 1 turn, non-stackable
    def unholy_chant(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_unholy_chant)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in app.coords if dist(self.loc, c) <= 2]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.do_unholy_chant(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Unholy Chant', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs : self.do_unholy_chant(event = e, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    def do_unholy_chant(self, event = None, sqrs = None):
        self.attack_used = True
#         self.init_attack_anims()
        effect1 = mixer.Sound('Sound_Effects/unholy_chant.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.unbind_all()
        ents = []
        for s in sqrs:
            ent = app.grid[s[0]][s[1]]
            if ent != '' and ent != 'block':
                if app.ent_dict[ent].owner == app.active_player:
                    ef_names = [v.name for k,v in app.ent_dict[ent].effects_dict.items()]
                    if 'Unholy_Chant' not in ef_names:
                        n2 = 'Unholy_Chant' + str(app.effects_counter) # not an effect, just need unique int
                        app.effects_counter += 1 # that is why this is incr manually here, no Effect init
                        app.vis_dict[n2] = Vis(name = 'Unholy_Chant', loc = s)
                        app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Unholy_Chant')
                        app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+70-app.moved_down, text = 'Unholy\nChant', justify = 'center', font = ('Andale Mono', 14), fill = 'ivory3', tags = 'text')
                        app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+90-app.moved_down, text = '+1 All Stats', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
                        def unholy_chant_effect(stat):
                            stat += 1
                            return stat
                        f = unholy_chant_effect
                        app.ent_dict[ent].str_effects.append(f)
                        app.ent_dict[ent].end_effects.append(f)
                        app.ent_dict[ent].agl_effects.append(f)
                        app.ent_dict[ent].dodge_effects.append(f)
                        app.ent_dict[ent].psyche_effects.append(f)
                        
                        n = 'Unholy_Chant' + str(app.effects_counter)
                        def un(i, func):
                            app.ent_dict[i].str_effects.remove(func)
                            app.ent_dict[i].end_effects.remove(func)
                            app.ent_dict[i].agl_effects.remove(func)
                            app.ent_dict[i].dodge_effects.remove(func)
                            app.ent_dict[i].psyche_effects.remove(func)
                            return None
                        p = partial(un, ent, f)
                        # EOT FUNC
                        def nothing():
                            return None
                        n = 'Unholy_Chant' + str(app.effects_counter)
                        app.ent_dict[ent].effects_dict[n] = Effect(name = 'Unholy_Chant', info = 'Unholy_Chant\n Stats increased by 1 for 1 turn', eot_func = nothing, undo = p, duration = 1)
        root.after(3666, self.finish_unholy_chant)
        
    def finish_unholy_chant(self, event = None):
#         self.init_normal_anims()
        try:
            keys = [k for k in app.vis_dict.keys() if k[:12] == 'Unholy_Chant']
            for k in keys:
                del app.vis_dict[k]
            app.canvas.delete('Unholy_Chant')
        except: pass
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
    
    # minor attack, psyche based
    def discord(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_discord)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in app.coords if dist(self.loc, c) <= 3]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, sqr = grid_pos, sqrs = sqrs : self.do_discord(event = e, sqr = sqr, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Confirm Discord Target', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqr = grid_pos, sqrs = sqrs : self.do_discord(event = e, sqr = sqr, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    # make discord vis
    def do_discord(self, event, sqr, sqrs):
        target = app.grid[sqr[0]][sqr[1]]
        if target == '' or target == 'block':
            return
        if app.ent_dict[target].loc not in sqrs:
            return
        effect1 = mixer.Sound('Sound_Effects/discord.ogg')
        effect1.set_volume(.5)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        app.vis_dict['Discord'] = Vis(name = 'Discord', loc = sqr[:])
        vis = app.vis_dict['Discord']
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = vis.img, tags = 'Discord')
        id = target
        my_psyche = self.get_attr('psyche')
        tar_psyche = app.ent_dict[id].get_attr('psyche')
        if to_hit(my_psyche, tar_psyche) == True:
            d = damage(my_psyche, tar_psyche)
            d = d//2
            if d == 0: d = 1
            d += 1
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Discord Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+90, text = app.ent_dict[id].name.replace('_',' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(1666, lambda id = id : app.kill(id))
            root.after(1666, lambda e = None : self.finish_discord(event = e))
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Discord Missed!\n', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda e = None : self.finish_discord(event = e))
        self.attack_used = True
        
    def finish_discord(self, event):
        try: 
            del app.vis_dict['Discord']
            app.canvas.delete('Discord')
        except: pass
        app.unbind_all()
        app.rebind_all()
        app.depop_context(event = None)
        app.canvas.delete('text')
        app.cleanup_squares()
        
    
    
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 5) 
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class White_Dragon_Top(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = True):
#         self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 9
        self.agl = 8
        self.end = 9
        self.dodge = 5
        self.psyche = 8
        self.spirit = 157
        self.waiting = waiting
        super().__init__(name, img, loc, owner, number, type = 'large')
    # 'tall' ent, bigger than 100 pixels height, needs to be split into 2 images so the 'top' image is 'large' (raised above 'maptop', bottom part of ent is hidden behind 'maptop'
class White_Dragon(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 9
        self.agl = 8
        self.end = 9
        self.dodge = 5
        self.psyche = 8
        self.spirit = 157
        self.waiting = waiting
        self.retreated_once = False
        self.move_type = 'flying'
        super().__init__(name, img, loc, owner, number, type = 'large_bottom')
        self.immovable = True
        # create top half
        img = ImageTk.PhotoImage(Image.open('animations/White_Dragon_Top/0.png'))
        app.ent_dict[self.number+'top'] = White_Dragon_Top(name = 'White_Dragon_Top', img = img, loc = [self.loc[0],self.loc[1]-1], owner = 'p2', number = self.number+'top')
        
    def large_undo(self):
        app.canvas.delete(self.number+'top')
        del app.ent_dict[self.number+'top']
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  White_Dragon AI
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        # if spirit low, fly to random spot can occupy, set waiting, summon orcs?
        elif self.spirit < 88 and self.retreated_once == False:
#             coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
            empty_locs = [c for c in app.coords if app.grid[c[0]][c[1]] == '' and dist(c, self.loc) >= 12]
            endloc = choice(empty_locs)
            # create orcs
            orc_sqrs = [[15,1],[16,1],[17,1],[18,1],[15,2],[16,2],[17,2],[18,2],[15,3],[16,3],[17,3],[18,3],[15,4],[16,4],[17,4],[18,4]]
            for s in orc_sqrs[:]:
                if app.grid[s[0]][s[1]] != '':
                    orc_sqrs.remove(s)
            if endloc in orc_sqrs[:]:
                orc_sqrs.remove(endloc)
            loc1 = choice(orc_sqrs)
            orc_sqrs.remove(loc1)
            loc2 = choice(orc_sqrs)
            orc_sqrs.remove(loc2)
            loc3 = choice(orc_sqrs)
            orc_sqrs.remove(loc3)
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Orc_axeman.png'))
            app.ent_dict['b2'] = Orc_Axeman(name = 'Orc_Axeman', img = img, loc = loc1[:], owner = 'p2', number = 'b2')
            app.ent_dict['b3'] = Orc_Axeman(name = 'Orc_Axeman', img = img, loc = loc2[:], owner = 'p2', number = 'b3')
            app.ent_dict['b4'] = Orc_Axeman(name = 'Orc_Axeman', img = img, loc = loc3[:], owner = 'p2', number = 'b4')
            app.grid[loc1[0]][loc1[1]] = 'b2'
            app.grid[loc2[0]][loc2[1]] = 'b3'
            app.grid[loc3[0]][loc3[1]] = 'b4'
            self.waiting = True
            self.retreated_once = True
#             root.after(1333, lambda el = ents_list, endloc = endloc : self.white_dragon_move(el, endloc))
            self.white_dragon_move(ents_list, endloc, go_to_sleep = True)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if 0 < dist(c, el) <= 3 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.white_dragon_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if 0 < dist(c, el) <= 3 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.white_dragon_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
            
    def white_dragon_move(self, ents_list, endloc, go_to_sleep = None):
        global selected
        # FIND SQUARE FURTHEST ALONG PATH THAT IS WITHIN MOVE RANGE
        id = self.number
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = endloc[0]*100+50-app.moved_right
        endy = endloc[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = endloc[:]
        selected = [self.number,self.number+'top']
        # MOVE LOOP
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr):
            if x % 25 == 0 or y % 25 == 0:
                self.rotate_image()
                app.ent_dict[id+'top'].rotate_image()
                app.canvas.delete(id)
                app.canvas.delete(id+'top')
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
                app.canvas.create_image(x, y-100, image = app.ent_dict[id+'top'].img, tags = (id+'top','large'))
            if x > endx:
                x -= 10
                app.canvas.move(id, -10, 0)
                app.canvas.move(id+'top', -10, 0)
            if x < endx: 
                x += 10
                app.canvas.move(id, 10, 0)
                app.canvas.move(id+'top', 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(id, 0, -10)
                app.canvas.move(id+'top', 0, -10)
            if y < endy: 
                y += 10
                app.canvas.move(id, 0, 10)
                app.canvas.move(id+'top', 0, 10)
            app.canvas.tag_raise('cursor')
            try: app.canvas.tag_lower((self.tags), 'large')
            except: pass
            app.canvas.tag_lower((self.tags), 'maptop')
            if x == endx and y == endy:
                if go_to_sleep == True:
                    def awaken_dragon():
        #                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                        sqrs = [s for s in app.coords if dist(s, app.ent_dict['b1'].loc) <= 9]
                        ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
                        for ent in ents:
                            if app.ent_dict[ent].owner == 'p1':
                                app.ent_dict['b1'].waiting = False
                                app.map_triggers.remove(awaken_dragon)
                                break
                    root.after(1666, lambda f = awaken_dragon : app.map_triggers.append(awaken_dragon))
                self.finish_move(id, end_sqr, start_sqr, ents_list) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
            
    # change to attack any within range, not ncsrly original target
    # DONE MOVING, ATTEMPT ATTACK AND EXIT
    def finish_move(self, id, end_sqr, start_sqr, ents_list):
        global selected
        selected = []
        self.loc = end_sqr[:]
        app.ent_dict[id+'top'].loc = [end_sqr[0],end_sqr[1]-1]
#         self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        # MAKE ATTACK ON ANY ENEMY ENT WITHIN RANGE
        atk_sqrs = self.legal_attacks()
        ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
        enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
        if enemy_ents != []:
            any = enemy_ents[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda t = id : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.finish_attack(ents_list)
        else:
            app.get_focus(id)
            # get adj ents
            adj_coords = [c for c in app.coords if dist(app.ent_dict[id].loc, c) == 1]
            ents = [app.grid[s[0]][s[1]] for s in adj_coords if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
            if 'b1' in ents:
                ents.remove('b1')
            ents.append(id)
            for id in ents:
                n = 'Iceblast' + str(app.effects_counter) # not an effect, just need unique int
                app.effects_counter += 1 # that is why this is incr manually here, no Effect init
                loc = app.ent_dict[id].loc[:]
                app.vis_dict[n] = Vis(name = 'Iceblast', loc = loc)
                def cleanup_vis(name):
                    del app.vis_dict[name]
                    app.canvas.delete(name)
                root.after(3666, lambda n = n : cleanup_vis(n))
                app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict[n].img, tags = n)
                app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down-30, text = 'Iceblast', justify ='center', font = ('Andale Mono', 14), fill = 'black', tags = 'text')
        
    #         app.ent_dict[self.number+'top'].init_attack_anims()
                my_agl = self.get_attr('agl')
                target_dodge = app.ent_dict[id].get_attr('dodge')
                if to_hit(my_agl, target_dodge) == True:
                    # HIT, SHOW VIS, DO DAMAGE, EXIT
                    my_str = self.get_attr('str')
                    target_end = app.ent_dict[id].get_attr('end')
                    d = damage(my_str, target_end)
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Hit!\n' + str(d) + '\nSpirit', justify = 'center', fill = 'black', font = ('Andale Mono', 13), tags = 'text')
                    app.ent_dict[id].set_attr('spirit', -d)
                    if app.ent_dict[id].spirit <= 0:
                        app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+78, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'black', font = ('Andale Mono', 13), tags = 'text')
#                     root.after(3666, lambda i = id : self.cleanup_attack(i)) # EXIT THROUGH CLEANUP_ATTACK()
                else:
                    # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Miss!', justify = 'center', fill = 'black', font = ('Andale Mono', 13), tags = 'text')
#                     root.after(3666, lambda i = id : self.cleanup_attack(i))
#             root.after(3999, lambda el = ents_list: self.finish_attack(el))
            root.after(3999, lambda el = ents_list, ids = ents: self.cleanup_attack(el, ids))
        
    # change to loop over list of ids
    def cleanup_attack(self, el, ids):
        if ids != []:
            id = ids[0]
            ids = ids[1:]
            if app.ent_dict[id].spirit <= 0:
                if app.kill(id) == None:
                    self.cleanup_attack(el, ids)
                else:
                    root.after(3333, lambda el = el, ids = ids : self.cleanup_attack(el, ids))
            else:
                self.cleanup_attack(el, ids)
    #         app.ent_dict[self.number+'top'].init_normal_anims()
        else:
            root.after(1999, lambda el = el: self.finish_attack(el))

        
    def finish_attack(self, ents_list):
        app.canvas.delete('text')
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) <= 3:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        for c in app.coords:
            if app.grid[c[0]][c[1]] == '' and dist(loc, c) <= 9:
                mvlist.append(c)
        return mvlist
        
        
class Tortured_Soul(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 7
        self.agl = 6
        self.end = 7
        self.dodge = 4
        self.psyche = 2
        self.spirit = 25
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  TORTURED SOUL AI
    def do_ai(self, ents_list):
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) <= 3 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) <= 3 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
            
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/tortured_soul_agony.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            # make range atk vis
            visloc = app.ent_dict[id].loc[:]
            app.vis_dict['Tortured_Soul_Agony'] = Vis(name = 'Tortured_Soul_Agony', loc = visloc)
            app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Tortured_Soul_Agony'].img, tags = 'Tortured_Soul_Agony')
            app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+95-app.moved_down, text = 'Agony', font = ('Andale Mono', 16), fill = 'orangered4', tags = 'text')
        
            my_agl = self.get_attr('agl')
            target_dodge = app.ent_dict[id].get_attr('dodge')
            if to_hit(my_agl, target_dodge) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_psyche = app.ent_dict[id].get_attr('psyche')
                d = damage(my_str, target_psyche)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Tortured Soul Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Tortured Soul Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(3666, lambda  el = ents_list, id = id : self.cleanup_attack(el, id))
        
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
            del app.vis_dict['Tortured_Soul_Agony']
            app.canvas.delete('Tortured_Soul_Agony')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) <= 3:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 6)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class Ghost(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 9
        self.end = 8
        self.dodge = 9
        self.psyche = 7
        self.spirit = 75
        self.waiting = waiting
        self.move_type = 'ethereal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  GHOST AI
    # 'do not move' just attack within range
    def do_ai(self, ents_list):
        if self.waiting == True: # DO NOT MOVE TOWARDS OR ATTACK UNTIL TRIGGER
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else:# GO TO NEXT ENT
                ents_list = ents_list[1:]
                if ents_list == []:
                    root.after(666, app.end_turn)
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    
            
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            effect1 = mixer.Sound('Sound_Effects/ghost_attack.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
    #         self.init_attack_anims()
            # make range atk vis
    #         visloc = app.ent_dict[id].loc[:]
    #         app.vis_dict['Revenant_Terror'] = Vis(name = 'Revenant_Terror', loc = visloc)
    #         app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Revenant_Terror'].img, tags = 'Revenant_Terror')
    #         app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+105-app.moved_down, text = 'Terror', font = ('Andale Mono', 16), fill = 'gray77', tags = 'text')
            my_psyche = self.get_attr('psyche')
            target_psyche = app.ent_dict[id].get_attr('psyche')
            if to_hit(my_psyche, target_psyche) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                d = damage(my_psyche, target_psyche)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Ghost Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Ghost Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')

            root.after(3666, lambda  el = ents_list, id = id : self.cleanup_attack(el, id))
        
        
        
    def cleanup_attack(self, ents_list, id):
#         self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Tortured_Soul_Agony']
#             app.canvas.delete('Tortured_Soul_Agony')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) <= 3:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
        
        
class Revenant(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 4
        self.end = 5
        self.dodge = 4
        self.psyche = 7
        self.spirit = 29
        self.waiting = waiting
        self.move_type = 'ethereal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  REVENANT AI
    def do_ai(self, ents_list):
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                # Need paths 'through' objects
                # cannot end move in 'block' or Ent
                    goals = [c for c in app.coords if dist(c, el) <= 2 and app.grid[c[0]][c[1]] == '']
                    egrid = [[''] * (app.map_height//100) for i in range(app.map_width//100)]
                    path = bfs(self.loc[:], goals, egrid)
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.revenant_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                # for revenant, will always be paths, this section unused
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) <= 3 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.revenant_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    def revenant_move(self, ents_list, endloc):
        global selected
        effect1 = mixer.Sound('Sound_Effects/revenant_move.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        # FIND SQUARE FURTHEST ALONG PATH THAT IS WITHIN MOVE RANGE
        id = self.number
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = endloc[0]*100+50-app.moved_right
        endy = endloc[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = endloc[:]
        selected = [self.number]
        # MOVE LOOP
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr):
            if x % 25 == 0 or y % 25 == 0:
                self.rotate_image()
                app.canvas.delete(id)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
                app.canvas.tag_lower((self.tags), 'maptop')
                try: app.canvas.tag_lower((self.tags), 'large')
                except: pass
            if x > endx:
                x -= 10
                app.canvas.move(id, -10, 0)
            if x < endx: 
                x += 10
                app.canvas.move(id, 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(id, 0, -10)
            if y < endy: 
                y += 10
                app.canvas.move(id, 0, 10)
#             try: app.canvas.tag_raise('large', (self.tags))
#             except: pass
#             app.canvas.tag_raise('maptop')
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr, ents_list) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
            
    # change to attack any within range, not ncsrly original target
    # DONE MOVING, ATTEMPT ATTACK AND EXIT
    def finish_move(self, id, end_sqr, start_sqr, ents_list):
        global selected
        selected = []
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        # MAKE ATTACK ON ANY ENEMY ENT WITHIN RANGE
        atk_sqrs = self.legal_attacks()
        ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
        enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
        if enemy_ents != []:
            any = enemy_ents[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda t = id : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/revenant_terror.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            # make range atk vis
            visloc = app.ent_dict[id].loc[:]
            app.vis_dict['Revenant_Terror'] = Vis(name = 'Revenant_Terror', loc = visloc)
            app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Revenant_Terror'].img, tags = 'Revenant_Terror')
            app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+105-app.moved_down, text = 'Terror', font = ('Andale Mono', 16), fill = 'gray77', tags = 'text')
        
            my_psyche = self.get_attr('psyche')
            target_psyche = app.ent_dict[id].get_attr('psyche')
            if to_hit(my_psyche, target_psyche) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                d = damage(my_psyche, target_psyche)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Revenant Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Revenant Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')

            root.after(3666, lambda  el = ents_list, id = id : self.cleanup_attack(el, id))
            
            
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
            del app.vis_dict['Revenant_Terror']
            app.canvas.delete('Revenant_Terror')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) <= 2:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in app.coords:
            if dist(loc, c) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist
        
        
        
        # make cut attack against numerous ents
class Kensai(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 8
        self.end = 5
        self.dodge = 9
        self.psyche = 8
        self.spirit = 59
        self.times_attacked = 0
        self.attacked_ids = []
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def get_attr(self, attr):
        if attr == 'str':
            return self.base_str
        elif attr == 'end':
            return self.base_end
        elif attr == 'agl':
            return self.base_agl
        elif attr == 'dodge':
            return self.base_dodge
        elif attr == 'psyche':
            return self.base_psyche
        
    
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  KENSAI AI
    def do_ai(self, ents_list):
        if self.waiting == True: # WAITING, PASSIVE, PASS PRIORITY
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            print(atk_sqrs)
            atk_sqrs = [x for x in atk_sqrs if app.grid[x[0]][x[1]] not in self.attacked_ids]
            print('atk_sqrs ', atk_sqrs)
            print('attacked_ids ', self.attacked_ids)
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1' and x not in self.attacked_ids]
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            self.init_attack_anims()
    #         effect1 = mixer.Sound('Sound_Effects/kensai_cut.ogg')
    #         effect1.set_volume(1)
    #         sound_effects.play(effect1, 0)
            visloc = app.ent_dict[id].loc[:]
            app.vis_dict['Kensai_Cut'] = Vis(name = 'Kensai_Cut', loc = visloc)
            app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Kensai_Cut'].img, tags = 'Kensai_Cut')
            app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+95-app.moved_down, text = 'Cut', font = ('Andale Mono', 13), fill = 'white', tags = 'text')

            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Kensai Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Kensai Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            del app.vis_dict['Kensai_Cut']
            app.canvas.delete('Kensai_Cut')
        except: pass
        try: app.canvas.delete('text')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                self.continue_cleanup(ents_list, id)
            else:
                root.after(3333, lambda el = ents_list, id = id : self.continue_cleanup(el, id))
        else:
                self.continue_cleanup(ents_list, id)
                
    def continue_cleanup(self, ents_list, id):
        self.attacked_ids.append(id)
        if self.times_attacked < 4:
            near_sqrs = [s for s in app.coords if dist(s, self.loc) <= 3]
            near_ents = [app.grid[s[0]][s[1]] for s in near_sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
            pot_targets = [e for e in near_ents if app.ent_dict[e].owner == 'p1' and e not in self.attacked_ids]
            if pot_targets != []:
                id = choice(pot_targets)
                self.times_attacked += 1
                self.do_ai(ents_list)
            else:
                self.end_attack(ents_list)
        else:
            self.end_attack(ents_list)
                
    def end_attack(self, ents_list):
#         self.times_attacked = 0
#         self.attacked_ids = []
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 3)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class Undead(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 5
        self.agl = 3
        self.end = 4
        self.dodge = 2
        self.psyche = 2
        self.spirit = 9
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  UNDEAD AI
    # instead of calling bfs on each potential target, can i walk grid with bfs until any enemy is found?
    def do_ai(self, ents_list):
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/Undead_attack.ogg')
            sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name.replace('_',' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: app.canvas.delete('text')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 3)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
class Undead_Knight(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 10
        self.agl = 8
        self.end = 6
        self.dodge = 8
        self.psyche = 6
        self.spirit = 86
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  Undead Knight AI
    # instead of calling bfs on each potential target, can i walk grid with bfs until any enemy is found?
    def do_ai(self, ents_list):
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/undead_knight_attack.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Knight Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Undead Knight Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Tortured_Soul_Agony']
#             app.canvas.delete('Tortured_Soul_Agony')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 3)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
class Troll(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 9
        self.agl = 6
        self.end = 8
        self.dodge = 5
        self.psyche = 2
        self.spirit = 35
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  TROLL AI
    # instead of calling bfs on each potential target, can i walk grid with bfs until any enemy is found?
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            # TROLL REGEN
            if self.spirit < 35:
                app.canvas.create_text(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, text='Regen 2 Spirit', font= ('Andale Mono', 14), fill = 'white', tags = 'text')
                root.after(999, lambda t = 'text' : app.canvas.delete('text'))
                self.spirit += 2
                if self.spirit > 35:
                    self.spirit = 35
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
                # change to calling bfs once
                goals = [c for c in app.coords for s in enemy_ent_locs if dist(c, s) == 1 and app.grid[c[0]][c[1]] == '']
                path = bfs(self.loc[:], goals, app.grid[:])
                if path:
#                     apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in path[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
                    goals = [c for c in app.coords for s in enemy_ent_locs if dist(c, s) == 1 and egrid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, egrid[:])
                    if path:
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in path[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/troll_attack.ogg')
            effect1.set_volume(.8)
            sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Troll Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Troll Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Tortured_Soul_Agony']
#             app.canvas.delete('Tortured_Soul_Agony')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 9)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class Warlock(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 5
        self.agl = 7
        self.end = 7
        self.dodge = 5
        self.psyche = 11
        self.spirit = 89
        self.waiting = waiting
        self.move_type = 'teleport'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  WARLOCK AI
    # change to 'move away after attack' if able to attack from start location
    # randomly cast spells, teleport away, summon undead
    
    # make casting anims
    def do_ai(self, ents_list):
        p = partial(self.__class__.legal_moves, self) #   PUT BACK CLASS METHOD MOVEMENT
        self.legal_moves = p
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            # Summon Undead
            root.after(1333, lambda el = ents_list : self.warlock_summon(el))
            
    def warlock_summon(self, ents_list):
        # give visual cue, timing, alternate turns?
        effect1 = mixer.Sound('Sound_Effects/warlock_summon.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.effects_counter += 3 # skip existing ent ids
        uniq_num = app.effects_counter
        app.effects_counter += 1
        # get random empty location
        coords = [c for c in app.coords if dist(c, self.loc) <= 6]
        empty = [c for c in coords if app.grid[c[0]][c[1]] == '']
        if empty != []:
            undead_loc = choice(empty)
            app.focus_square(undead_loc)
            app.vis_dict['Summon_Undead'] = Vis(name = 'Summon_Undead', loc = undead_loc[:])
            app.canvas.create_image(undead_loc[0]*100+50-app.moved_right, undead_loc[1]*100+50-app.moved_down, image = app.vis_dict['Summon_Undead'].img, tags = 'Summon_Undead')
            def cleanup_vis(name):
                del app.vis_dict[name]
                app.canvas.delete(name)
            root.after(2333, lambda name = 'Summon_Undead' : cleanup_vis(name))
            app.canvas.create_text(undead_loc[0]*100+50-app.moved_right, undead_loc[1]*100+90-app.moved_down, text = 'Summon Undead', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Undead.png'))
            app.ent_dict['b'+str(uniq_num)] = Undead(name = 'Undead', img = img, loc = undead_loc[:], owner = 'p2', number = 'b'+str(uniq_num))
            app.grid[undead_loc[0]][undead_loc[1]] = 'b'+str(uniq_num)
            app.canvas.create_image(undead_loc[0]*100+50-app.moved_right, undead_loc[1]*100+50-app.moved_down, image = img, tags = 'b'+str(uniq_num))
            root.after(2333, lambda t = 'text' : app.canvas.delete(t))
        root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
        # End Summon Undead, ATTEMPT ATTACK
            
    def continue_ai(self, ents_list):
        atk_sqrs = self.legal_attacks()
        atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
        if atk_sqrs != []:
            any = atk_sqrs[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda id = id : app.get_focus(id))
            root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
        else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
            # among legal sqrs, move to sqr within dist of attack or that minimizes dist
            leg_sqrs = self.legal_moves()
            if leg_sqrs != []:
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                # first try to move to sqr at edge of attack range
                goals = [c for c in app.coords for e in enemy_ent_locs if dist(c, e) <= 3 and app.grid[c[0]][c[1]] == '']
                target_sqrs = []
                for sqr in leg_sqrs:
                    if sqr in goals:
                        target_sqrs.append(sqr)
                if target_sqrs != []: # move to sqr within target_sqrs that is furthest from enemy_ent_loc
                    furthest_sqrs = [s for s in target_sqrs for x in enemy_ent_locs if dist(s, x) == max([dist(j, y) for j in target_sqrs for y in enemy_ent_locs])]
                    loc = choice(furthest_sqrs)
                    root.after(666, lambda sqr = loc : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = loc : self.warlock_move(el, loc))
                else: # move to sqr within leg_sqrs that minimizes dist
                    closest_sqrs = [s for s in leg_sqrs for x in enemy_ent_locs if dist(s, x) == min([dist(j, y) for j in leg_sqrs for y in enemy_ent_locs])]
                    loc = choice(closest_sqrs)
                    root.after(666, lambda sqr = loc : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = loc : self.warlock_move(el, loc))
            else: # continue ai_loop
                ents_list = ents_list[1:]
                if ents_list == []:
                    root.after(666, app.end_turn)
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
            
    # change to 'teleport move'
    def warlock_move(self, ents_list, endloc):
        global selected
        self.move_used = True
        oldloc = self.loc[:]
        
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.finish_move(ents_list, endloc))
        
    def finish_move(self, ents_list, endloc):
        app.grid[self.loc[0]][self.loc[1]] = ''
        app.canvas.delete(self.number)
        self.loc = endloc[:]
#         app.ent_dict[id].origin = newloc[:]
        app.grid[endloc[0]][endloc[1]] = self.number
        try: 
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = endloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.cleanup_teleport(ents_list, endloc))
        
    def cleanup_teleport(self, ents_list, endloc):
        del app.vis_dict['Teleport']
        app.canvas.delete('Teleport')
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        try: app.canvas.tag_lower(self.tags, 'large')
        except: pass
        app.canvas.tag_lower(self.tags, 'maptop')
        root.after(666, lambda ents_list = ents_list : self.finish_turn(ents_list))
        
        
    def finish_turn(self, ents_list):
        if self.attack_used == False:
            atk_sqrs = self.legal_attacks()
            ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
            enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
            if enemy_ents != []:
                any = enemy_ents[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda t = id : app.get_focus(t))
                root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
            else: # END TURN
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            self.attack_used = True
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/warlock_duress.ogg')
            effect1.set_volume(.7)
            sound_effects.play(effect1, 0)
            # make range atk vis
            visloc = app.ent_dict[id].loc[:]
            app.vis_dict['Duress'] = Vis(name = 'Duress', loc = visloc)
            app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Duress'].img, tags = 'Duress')
            app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+10-app.moved_down, text = 'Duress', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
            my_psyche = self.get_attr('psyche')
            target_psyche = app.ent_dict[id].get_attr('psyche')
            if to_hit(my_psyche, target_psyche) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                d = damage(my_psyche, target_psyche)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Warlock Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Warlock Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')

            root.after(3666, lambda  el = ents_list, id = id : self.cleanup_attack(el, id))
        
        
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            del app.vis_dict['Duress']
            app.canvas.delete('Duress')
        except: pass
        try: app.canvas.delete('text')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                self.finish_cleanup(ents_list, id)
            else:
                root.after(3333, lambda el = ents_list, id = id : self.finish_cleanup(el, id))
        else:
            self.finish_cleanup(ents_list, id)
        
    def finish_cleanup(self, ents_list, id):
        # if havent moved, attempt random move
        if self.move_used == False:
            # move to random square at least 9 away
            empty_sqrs = [s for s in app.coords if app.grid[s[0]][s[1]] == '' and dist(self.loc, s) > 9]
            if empty_sqrs != []:
                s =  choice(empty_sqrs)
                effect1 = mixer.Sound('Sound_Effects/warlock_teleport_away.ogg')
                effect1.set_volume(1)
                sound_effects.play(effect1, 0)
                self.warlock_move(ents_list, s)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) <= 3:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        for c in app.coords:
            if dist(loc, c) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist
        
        
        '''
elemental mages
sparkles 5,5 and 34,5
orb 20,17

fire mage 18,19
spawn 3 elementals if no elementals exist
elementals do small damage to large area, 2 to each ents
killing a set of elementals temporarily 'grounds' fire mage (recharges before resummon)
otherwise fire mage is ungroundable and teleports to between 5-7 away from player ents and casts 'fire wall' (damages all in a line across whole axis)

earth mage 22,19
4 elementals that always attempt to move adjacent to mage
when all elementals are adjacent mage takes no damage
for each elemental that is adjacent, attrs increased
mage casts earthquake (moves non-elementals away from mage and damages them)
mage is 'grounded' (unmoveable)
when elemental is killed (if), after casting earthquake resummon 1 elemental

air mage 18,15
casts cyclone (moves ent to random sqr, dmgs)
mage teleports around, 'grounded'
3 elementals that fly (movement type) and attack like warlock (teleport away after attack)

water mage 22,15
        '''
        
class Earth_Mage(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 3
        self.agl = 3
        self.end = 4
        self.dodge = 2
        self.psyche = 5
        self.spirit = 79
        self.waiting = waiting
        self.move_type = 'teleport'
        self.summons_used = False
        super().__init__(name, img, loc, owner, number)
        # add effects that alter attrs based on alive elementals
        def elementals(stat):
            alive = [k for k,v in app.ent_dict.items() if v.name == 'Earth_Elemental']
            bonus = len(alive)
            stat += bonus
            return stat
        self.str_effects.append(elementals)
        self.agl_effects.append(elementals)
        self.end_effects.append(elementals)
        self.dodge_effects.append(elementals)
        self.psyche_effects.append(elementals)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
    
    # make casting anims
    def do_ai(self, ents_list):
        if self.waiting == True:
            self.pass_priority(ents_list)
        else:
            # summon elementals once
            if self.summons_used == False:
                self.summons_used = True
                app.effects_counter += 1 # skip existing ent ids, increment 'just in case'
                num1 = app.effects_counter
                app.effects_counter += 1
                num2 = app.effects_counter
                app.effects_counter += 1
                num3 = app.effects_counter
                app.effects_counter += 1
                nums = [num1, num2, num3]
                # get random empty locations
                coords = [c for c in app.coords if dist(c, self.loc) <= 7]
                empty = [c for c in coords if app.grid[c[0]][c[1]] == '']
                if len(empty) >= 3:
                    f_loc1 = choice(empty)
                    empty.remove(f_loc1)
                    f_loc2 = choice(empty)
                    empty.remove(f_loc2)
                    f_loc3 = choice(empty)
                    empty.remove(f_loc3)
                    f_locs = [f_loc1[:], f_loc2[:], f_loc3[:]]
                    def summon_loop(loc, num):
                        app.focus_square(loc)
                        app.vis_dict['Summon_Undead'] = Vis(name = 'Summon_Undead', loc = loc[:])
                        app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict['Summon_Undead'].img, tags = 'Summon_Undead')
                        def cleanup_vis(name):
                            del app.vis_dict[name]
                            app.canvas.delete(name)
                        root.after(2333, lambda name = 'Summon_Undead' : cleanup_vis(name))
                        app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+90-app.moved_down, text = 'Summon Earth Elemental', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        img = ImageTk.PhotoImage(Image.open('summon_imgs/Earth_Elemental.png'))
                        app.ent_dict['b'+str(num)] = Earth_Elemental(name = 'Earth_Elemental', img = img, loc = loc[:], owner = 'p2', number = 'b'+str(num))
                        app.grid[loc[0]][loc[1]] = 'b'+str(num)
                        app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = img, tags = 'b'+str(num))
                        root.after(2333, lambda t = 'text' : app.canvas.delete(t))
                        if f_locs == []:
                            app.get_focus(self.number)
                            root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
                        else:
                            loc = f_locs.pop()
                            num = nums.pop()
                            root.after(2333, lambda l = loc, n = num : summon_loop(l, n))
                    loc = f_locs.pop()
                    num = nums.pop()
                    summon_loop(loc, num)
                else:
                    app.get_focus(self.number)
                    root.after(1333, lambda el = ents_list : self.continue_ai(el))
            else:
                app.get_focus(self.number)
                root.after(1333, lambda el = ents_list : self.continue_ai(el))
            
            
    # teleport near enemy ents, cast earthquake
    def continue_ai(self, ents_list):
        # get empty sqrs within 6 of any enemy
        ent_locs = [v.loc[:] for k,v in app.ent_dict.items() if v.owner == 'p1']
        locs = [s for s in app.coords for c in ent_locs if dist(s, c) <= 6 and app.grid[s[0]][s[1]] == '']
        if locs != []:
            loc = choice(locs)
            app.focus_square(loc)
            root.after(1333, lambda el = ents_list, loc = loc : self.earth_mage_move(el, loc))
        else:
            root.after(1333, lambda el = ents_list : self.do_attack(el)) # ATTACK
            
            
    def earth_mage_move(self, ents_list, endloc):
        global selected
        self.move_used = True
        oldloc = self.loc[:]
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.finish_move(ents_list, endloc))
        
    def finish_move(self, ents_list, endloc):
        app.grid[self.loc[0]][self.loc[1]] = ''
        app.canvas.delete(self.number)
        self.loc = endloc[:]
        app.grid[endloc[0]][endloc[1]] = self.number
        try: 
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = endloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.cleanup_teleport(ents_list, endloc))
        
    def cleanup_teleport(self, ents_list, endloc):
        del app.vis_dict['Teleport']
        app.canvas.delete('Teleport')
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        try: app.canvas.tag_lower(self.tags, 'large')
        except: pass
        app.canvas.tag_lower(self.tags, 'maptop')
        root.after(666, lambda ents_list = ents_list : self.finish_turn(ents_list))
        
        
    def finish_turn(self, ents_list):
        if self.attack_used == False:
            root.after(1333, lambda el = ents_list : self.do_attack(el)) # EXIT THROUGH ATTACK
        else:# CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    # earthquake, dmg near ents (non-flying) and move them to a sqr not within close range
    def do_attack(self, ents_list):
        if self.attack_used == True:
            self.cleanup_attack(ents_list)
        else:
            self.attack_used = True
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/earthquake.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            sqrs = []
            for c in app.coords:
                if dist(c, self.loc) <= 3:
                    sqrs.append(c)
            app.canvas.create_text(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+85-app.moved_down, text = 'Earthquake', font = ('Andale Mono', 16), fill = 'goldenrod1', tags = 'text')
            app.vis_dict['Earthquake'] = Vis(name = 'Earthquake', loc = self.loc[:])
            app.canvas.create_image(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, image = app.vis_dict['Earthquake'].img, tags = 'Earthquake')
            # get all ents in vicinity
            ents = [k for k,v in app.ent_dict.items() if v.owner != self.owner and v.loc in sqrs and v.move_type != 'flying']
            if ents != []:
                t1,t2,t3 = [],[],[]
                for e in ents:
                    if dist(app.ent_dict[e].loc, self.loc) == 3:
                        t1.append(e)
                    elif dist(app.ent_dict[e].loc, self.loc) == 2:
                        t2.append(e)
                    elif dist(app.ent_dict[e].loc, self.loc) == 1:
                        t3.append(e)
                ents = t1[:] + t2[:] + t3[:]
                # check for dmg and create text object
                # move ents away from mage
                # must do earthquake_loop on each tier, timed
                def earthquake_loop(ents):
                    global selected
                    app.canvas.delete('text')
                    id = ents[0]
                    ents = ents[1:]
                    app.get_focus(id)
                    my_psyche = self.get_attr('psyche')
                    target_agl = app.ent_dict[id].get_attr('agl')
                    d = damage(my_psyche, target_agl)
                    app.ent_dict[id].set_attr('spirit', -d)
                    loc = app.ent_dict[id].loc[:]
                    app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = str(d)+' Spirit', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                    if app.ent_dict[id].spirit <= 0:
                        app.canvas.create_text(loc[0]*100-app.moved_right+50, loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name.replace('_',' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                        result = root.after(1666, lambda id = id : app.kill(id))
                        if ents == []:
                            root.after(4666, lambda el = ents_list : self.cleanup_attack(el))
                        else:
                            root.after(4666, lambda e = ents : earthquake_loop(e))
                    else: # ENT NOT KILLED, INSERT PSI PUSH
                        start_loc = app.ent_dict[id].loc[:]
                        # LEFT
                        if start_loc[0] < self.loc[0] and abs(start_loc[1] - self.loc[1]) <= 1:
                            if [start_loc[0]-1,start_loc[1]] in app.coords and app.grid[start_loc[0]-1][start_loc[1]] == '':
                                if [start_loc[0]-2,start_loc[1]] in app.coords and app.grid[start_loc[0]-2][start_loc[1]] == '':
                                    dest = [start_loc[0]-2,start_loc[1]]
                                else:
                                    dest = [start_loc[0]-1,start_loc[1]]
                            else:
                                dest = start_loc[:]
                        # RIGHT
                        elif start_loc[0] > self.loc[0] and abs(start_loc[1] - self.loc[1]) <= 1:
                            if [start_loc[0]+1,start_loc[1]] in app.coords and app.grid[start_loc[0]+1][start_loc[1]] == '':
                                if [start_loc[0]+2,start_loc[1]] in app.coords and app.grid[start_loc[0]+2][start_loc[1]] == '':
                                    dest = [start_loc[0]+2,start_loc[1]]
                                else:
                                    dest = [start_loc[0]+1,start_loc[1]]
                            else:
                                dest = start_loc[:]
                        # UP
                        elif abs(start_loc[0] - self.loc[0]) <= 1 and start_loc[1] < self.loc[1]:
                            if [start_loc[0],start_loc[1]-1] in app.coords and app.grid[start_loc[0]][start_loc[1]-1] == '':
                                if [start_loc[0],start_loc[1]-2] in app.coords and app.grid[start_loc[0]][start_loc[1]-2] == '':
                                    dest = [start_loc[0],start_loc[1]-2]
                                else:
                                    dest = [start_loc[0],start_loc[1]-1]
                            else:
                                dest = start_loc[:]
                        # DOWN
                        elif abs(start_loc[0] - self.loc[0]) <= 1 and start_loc[1] > self.loc[1]:
                            if [start_loc[0],start_loc[1]+1] in app.coords and app.grid[start_loc[0]][start_loc[1]+1] == '':
                                if [start_loc[0],start_loc[1]+2] in app.coords and app.grid[start_loc[0]][start_loc[1]+2] == '':
                                    dest = [start_loc[0],start_loc[1]+2]
                                else:
                                    dest = [start_loc[0],start_loc[1]+1]
                            else:
                                dest = start_loc[:]
                        # end destination logic
                        x = start_loc[0]*100+50-app.moved_right
                        y = start_loc[1]*100+50-app.moved_down
                        endx = dest[0]*100+50-app.moved_right
                        endy = dest[1]*100+50-app.moved_down
                        if start_loc != dest: # do move then go to next eq loop, else go to next eq loop
                            selected = [id]
                            def finish_psionic_push(tar, end_loc, start_loc):
                                global selected
                                selected = []
                                app.ent_dict[tar].loc = end_loc[:]
                                app.grid[start_loc[0]][start_loc[1]] = ''
                                app.grid[end_loc[0]][end_loc[1]] = tar
                                if ents == []:
                                    root.after(3666, lambda el = ents_list : self.cleanup_attack(el))
                                else:
                                    root.after(3666, lambda e = ents : earthquake_loop(e))
                                
                            def psi_move_loop(ent, x, y, endx, endy, sqr, start_sqr):
                                if x % 25 == 0 and y % 25 == 0:
                                    app.ent_dict[ent].rotate_image()
                                    app.canvas.delete(ent)
                                    app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
                                if x > endx:
                                    x -= 10
                                    app.canvas.move(ent, -10, 0)
                                elif x < endx: 
                                    x += 10
                                    app.canvas.move(ent, 10, 0)
                                if y > endy: 
                                    y -= 10
                                    app.canvas.move(ent, 0, -10)
                                elif y < endy: 
                                    y += 10
                                    app.canvas.move(ent, 0, 10)
                                try: app.canvas.tag_lower(app.ent_dict[ent].tags, 'large')
                                except: pass
                                app.canvas.tag_lower(app.ent_dict[ent].tags, 'maptop')
                                if x == endx and y == endy:
                                    root.after(666, lambda e = ent, s = sqr, ss = start_sqr : finish_psionic_push(e, s, ss))
                                else:
                                    root.after(50, lambda id = id, x = x, y = y, endx = endx, endy = endy, s = sqr, s2 = start_sqr : psi_move_loop(id, x, y, endx, endy, s, s2))
                            psi_move_loop(id, x, y, endx, endy, dest, start_loc)
                            
                        elif ents == []:
                            root.after(3666, lambda el = ents_list : self.cleanup_attack(el))
                        else:
                            root.after(3666, lambda e = ents : earthquake_loop(e))
                # first call of eq loop, called if affected ents exist
                root.after(1999, lambda ents = ents : earthquake_loop(ents))
            else: # no affected ents, exit
                root.after(3333, lambda el = ents_list : self.cleanup_attack(el))
            
            
    def cleanup_attack(self, ents_list):
#         self.init_normal_anims()
        names = [k for k,v in app.vis_dict.items() if v.name == 'Earthquake']
        for n in names:
            del app.vis_dict[n]
        try:
            del app.vis_dict['Earthquake']
            app.canvas.delete('Earthquake')
        except: pass
        try: app.canvas.delete('text')
        except: pass
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
#     def legal_attacks(self):
#         sqrs = []
#         for coord in app.coords:
#             if dist(coord, self.loc) <= 3:
#                 if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
#                     sqrs.append(coord)
#         return sqrs
        
    # not used for movement, kept for purposes of monkey-patching
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        for c in app.coords:
            if dist(loc, c) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist
        
        
class Earth_Elemental(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 6
        self.agl = 4
        self.end = 6
        self.dodge = 4
        self.psyche = 3
        self.spirit = 29
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    # EARTH ELEMENTAL AI
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
#             effect1 = mixer.Sound('Sound_Effects/earth_elemental_attack.ogg')
#             effect1.set_volume(1)
#             sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+70, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Earth Elemental Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+90, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Earth Elemental Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
            
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['']
#             app.canvas.delete('')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 4)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
# casts firewall after teleporting randomly within a dist, resummons fire elementals if they all die
# This unit regains its normal movement (teleport) at the begin of every do_ai() (like Warlock)
class Fire_Mage(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 5
        self.agl = 6
        self.end = 6
        self.dodge = 5
        self.psyche = 9
        self.spirit = 79
        self.waiting = waiting
        self.move_type = 'teleport'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
    
    # make casting anims
    def do_ai(self, ents_list):
        p = partial(self.__class__.legal_moves, self) #   PUT BACK CLASS METHOD MOVEMENT
        self.legal_moves = p
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            # Summon Elementals
            root.after(1333, lambda el = ents_list : self.elemental_summon(el))
            
    def elemental_summon(self, ents_list):
#         effect1 = mixer.Sound('Sound_Effects/warlock_summon.ogg')
#         effect1.set_volume(1)
#         sound_effects.play(effect1, 0)
        f_elems = [v.name for k,v in app.ent_dict.items() if v.name == 'Fire_Elemental']
        if f_elems == []:
            app.effects_counter += 1 # skip existing ent ids
            num1 = app.effects_counter
            app.effects_counter += 1
            num2 = app.effects_counter
            app.effects_counter += 1
            num3 = app.effects_counter
            app.effects_counter += 1
            nums = [num1, num2, num3]
            # get random empty location
            coords = [c for c in app.coords if dist(c, self.loc) <= 7]
            empty = [c for c in coords if app.grid[c[0]][c[1]] == '']
            if len(empty) >= 3:
                f_loc1 = choice(empty)
                empty.remove(f_loc1)
                f_loc2 = choice(empty)
                empty.remove(f_loc2)
                f_loc3 = choice(empty)
                empty.remove(f_loc3)
                f_locs = [f_loc1[:], f_loc2[:], f_loc3[:]]
                def summon_loop(loc, num):
                    app.focus_square(loc)
                    app.vis_dict['Summon_Undead'] = Vis(name = 'Summon_Undead', loc = loc[:])
                    app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict['Summon_Undead'].img, tags = 'Summon_Undead')
                    def cleanup_vis(name):
                        del app.vis_dict[name]
                        app.canvas.delete(name)
                    root.after(2333, lambda name = 'Summon_Undead' : cleanup_vis(name))
                    app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+90-app.moved_down, text = 'Summon Fire Elemental', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Fire_Elemental.png'))
                    app.ent_dict['b'+str(num)] = Fire_Elemental(name = 'Fire_Elemental', img = img, loc = loc[:], owner = 'p2', number = 'b'+str(num))
                    app.grid[loc[0]][loc[1]] = 'b'+str(num)
                    app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = img, tags = 'b'+str(num))
                    root.after(2333, lambda t = 'text' : app.canvas.delete(t))
                    if f_locs == []:
                        app.get_focus(self.number)
                        root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
                    else:
                        loc = f_locs.pop()
                        num = nums.pop()
                        root.after(2333, lambda l = loc, n = num : summon_loop(l, n))
                loc = f_locs.pop()
                num = nums.pop()
                summon_loop(loc, num)
            else:
                app.get_focus(self.number)
                root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
        else:
            app.get_focus(self.number)
            root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
        # End Summon Elemental, ATTEMPT ATTACK
            
    # teleport to random sqr within 6 of an enemy ent, do firewall
    def continue_ai(self, ents_list):
        # get empty sqrs within 6 of any enemy
        ent_locs = [v.loc[:] for k,v in app.ent_dict.items() if v.owner == 'p1']
        locs = [s for s in app.coords for c in ent_locs if dist(s, c) <= 6 and app.grid[s[0]][s[1]] == '']
        if locs != []:
            loc = choice(locs)
            app.focus_square(loc)
            root.after(1333, lambda el = ents_list, loc = loc : self.fire_mage_move(el, loc))
        else:
            root.after(1333, lambda el = ents_list : self.do_attack(el)) # ATTACK
            
            
    def fire_mage_move(self, ents_list, endloc):
        global selected
        self.move_used = True
        oldloc = self.loc[:]
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.finish_move(ents_list, endloc))
        
    def finish_move(self, ents_list, endloc):
        app.grid[self.loc[0]][self.loc[1]] = ''
        app.canvas.delete(self.number)
        self.loc = endloc[:]
        app.grid[endloc[0]][endloc[1]] = self.number
        try: 
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = endloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.cleanup_teleport(ents_list, endloc))
        
    def cleanup_teleport(self, ents_list, endloc):
        del app.vis_dict['Teleport']
        app.canvas.delete('Teleport')
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        try: app.canvas.tag_lower(self.tags, 'large')
        except: pass
        app.canvas.tag_lower(self.tags, 'maptop')
        root.after(666, lambda ents_list = ents_list : self.finish_turn(ents_list))
        
        
    def finish_turn(self, ents_list):
        if self.attack_used == False:
            root.after(1333, lambda el = ents_list : self.do_attack(el)) # EXIT THROUGH ATTACK
        else:# CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list):
        if self.attack_used == True:
            self.cleanup_attack(ents_list)
        else:
            self.attack_used = True
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/firewall.ogg')
            effect1.set_volume(.7)
            sound_effects.play(effect1, 0)
            sqrs = []
            for c in app.coords:
                if c[0] == self.loc[0] and abs(c[1] - self.loc[1]) <= 6:
                    sqrs.append(c)
                elif abs(c[0] - self.loc[0]) <= 5 and c[1] == self.loc[1]:
                    sqrs.append(c)
            sqrs.remove(self.loc)
            app.canvas.create_text(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+85-app.moved_down, text = 'Firewall', font = ('Andale Mono', 16), fill = 'yellow', tags = 'text')
            for s in sqrs:
                u_name = 'Firewall' + str(app.effects_counter)
                app.effects_counter += 1
                app.vis_dict[u_name] = Vis(name = 'Firewall', loc = s[:])
                app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[u_name].img, tags = 'Firewall')
            # get all ents in paths
            ents = [k for k,v in app.ent_dict.items() if v.name != 'Fire_Elemental' and v.loc in sqrs]
            if ents != []:
                # check for dmg and create text object
                def firewall_loop(ents):
                    app.canvas.delete('text')
                    id = ents[0]
                    ents = ents[1:]
                    app.get_focus(id)
                    my_psyche = self.get_attr('psyche')
                    target_end = app.ent_dict[id].get_attr('end')
                    d = damage(my_psyche, target_end)
                    app.ent_dict[id].set_attr('spirit', -d)
                    loc = app.ent_dict[id].loc[:]
                    app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = str(d)+' Spirit', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                    if app.ent_dict[id].spirit <= 0:
                        app.canvas.create_text(loc[0]*100-app.moved_right+50, loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name.replace('_',' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                        result = root.after(1333, lambda id = id : app.kill(id))
                        if ents == []:
                            root.after(4666, lambda el = ents_list : self.cleanup_attack(el))
                        else:
                            root.after(4666, lambda e = ents : firewall_loop(e))
                    else:
                        if ents == []:
                            root.after(2666, lambda el = ents_list : self.cleanup_attack(el))
                        else:
                            root.after(2666, lambda e = ents : firewall_loop(e))
                root.after(1666, lambda e = ents : firewall_loop(e))
            else: # cleanup vis / cont ai_loop
                root.after(2999, lambda el = ents_list : self.cleanup_attack(el))
            
            
            
    def cleanup_attack(self, ents_list):
#         self.init_normal_anims()
        names = [k for k,v in app.vis_dict.items() if v.name == 'Firewall']
        for n in names:
            del app.vis_dict[n]
        try:
            del app.vis_dict['Firewall']
            app.canvas.delete('Firewall')
        except: pass
        try: app.canvas.delete('text')
        except: pass
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    # this unit has no need of legal_attacks(), left here in case of overwrite
    def legal_attacks(self):
        pass
    # this unit has no need of legal_moves(), left here in case of overwrite
    def legal_moves(self):
        pass
        
        
class Sorceress(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 5
        self.agl = 6
        self.end = 6
        self.dodge = 6
        self.psyche = 7
        self.spirit = 59
        self.waiting = waiting
        self.move_type = 'teleport'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    # attempt to teleport barbarian, take away summon undead, do not teleport away instead teleport towards barbarian
    #  SORCERESS AI
    def do_ai(self, ents_list):
        if self.waiting == True: # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            self.teleport_barbarian(ents_list)
#             root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
            # Summon Undead
#             root.after(1333, lambda el = ents_list : self.warlock_summon(el))
    # b2
    def teleport_barbarian(self, ents_list):
        # if b2 within 5 sqrs teleport it to the nearest enemy ent
        sqrs = [s for s in app.coords if dist(s, self.loc) <= 5]
        ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        if 'b2' in ents:
            # find nearest enemy ent
            enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
            loc = enemy_ent_locs[0] # will always exist
            min_dist = dist(self.loc, loc)
            enemy_ent_locs = enemy_ent_locs[1:]
            if enemy_ent_locs != []:
                for s in enemy_ent_locs:
                    if dist(s, self.loc) < min_dist:
                        min_dist = dist(s, self.loc)
                        loc = s
            # find the closest empty sqr that is within teleport range
            empty_sqrs = [s for s in app.coords if app.grid[s[0]][s[1]] == '' and dist(s, self.loc) < 4]
            closest_sqr = empty_sqrs[0] # should always exist
            if closest_sqr != []:
                min_dist = dist(closest_sqr, loc)
                for s in empty_sqrs:
                    if dist(s, loc) < min_dist:
                        closest_sqr = s
                        min_dist = dist(s, loc)
                # teleport b2 to closest_sqr
                oldloc = app.ent_dict['b2'].loc[:]
                app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc)
                vis = app.vis_dict['Teleport']
                app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
                root.after(2333, lambda ents_list = ents_list, oldloc = oldloc, newloc = closest_sqr : self.cleanup_bar_teleport(ents_list, oldloc, newloc))
            else:
                self.continue_ai(ents_list)
        else:
            self.continue_ai(ents_list)
        
    def cleanup_bar_teleport(self, ents_list, oldloc, newloc):
        del app.vis_dict['Teleport']
        app.canvas.delete('Teleport')
        app.grid[oldloc[0]][oldloc[1]] = ''
        app.grid[newloc[0]][newloc[1]] = 'b2'
        app.ent_dict['b2'].loc = newloc[:]
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = newloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(newloc[0]*100+50-app.moved_right, newloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        app.canvas.create_image(newloc[0]*100+50-app.moved_right, newloc[1]*100+50-app.moved_down, image = app.ent_dict['b2'].img, tags = app.ent_dict['b2'].tags)
        root.after(2333, lambda ents_list = ents_list : self.continue_ai(ents_list))
        
            
    def continue_ai(self, ents_list):
        try:
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        atk_sqrs = self.legal_attacks()
        atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
        if atk_sqrs != []:
            any = atk_sqrs[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda id = id : app.get_focus(id))
            root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
        else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
            # among legal sqrs, move to sqr within dist of attack or that minimizes dist
            leg_sqrs = self.legal_moves()
            if leg_sqrs != []:
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                # first try to move to sqr at edge of attack range
                goals = [c for c in app.coords for e in enemy_ent_locs if dist(c, e) <= 3 and app.grid[c[0]][c[1]] == '']
                target_sqrs = []
                for sqr in leg_sqrs:
                    if sqr in goals:
                        target_sqrs.append(sqr)
                if target_sqrs != []: # move to sqr within target_sqrs that is furthest from enemy_ent_loc
                    furthest_sqrs = [s for s in target_sqrs for x in enemy_ent_locs if dist(s, x) == max([dist(j, y) for j in target_sqrs for y in enemy_ent_locs])]
                    loc = choice(furthest_sqrs)
                    root.after(666, lambda sqr = loc : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = loc : self.sorceress_move(el, loc))
                else: # move to sqr within leg_sqrs that minimizes dist
                    closest_sqrs = [s for s in leg_sqrs for x in enemy_ent_locs if dist(s, x) == min([dist(j, y) for j in leg_sqrs for y in enemy_ent_locs])]
                    loc = choice(closest_sqrs)
                    root.after(666, lambda sqr = loc : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = loc : self.sorceress_move(el, loc))
            else: # continue ai_loop
                ents_list = ents_list[1:]
                if ents_list == []:
                    root.after(666, app.end_turn)
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
#         atk_sqrs = self.legal_attacks()
#         atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
#         if atk_sqrs != []:
#             any = atk_sqrs[0]
#             id = app.grid[any[0]][any[1]]
#             root.after(666, lambda id = id : app.get_focus(id))
#             root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
#         else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
#             enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
#             paths = []
# #             coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#             for el in enemy_ent_locs:
#             # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
#             # Need paths 'through' objects
#             # cannot end move in 'block' or Ent
#                 goals = [c for c in app.coords if dist(c, el) <= 4 and app.grid[c[0]][c[1]] == '']
#                 # this can cause 'path-shortening', finds path which is then obstructed on real grid resulting in 'short move'
#                 egrid = [[''] * (app.map_height//100) for i in range(app.map_width//100)]
#                 path = bfs(self.loc[:], goals, egrid)
#                 if path:
#                     paths.append(path)
#             smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
#             if smallpaths != []: # IF ANY PATHS EXIST AT ALL
#                 apath = smallpaths[0]
#                 # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
#                 moves = self.legal_moves()
#                 endloc = None
#                 for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
#                     if sqr in moves:
#                         endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
#                         break
#                 if endloc != None:
#                     root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
#                     root.after(1333, lambda el = ents_list, endloc = endloc : self.sorceress_move(el, endloc))
#                 else:
#                     ents_list = ents_list[1:]
#                     if ents_list == []:
#                         root.after(666, app.end_turn)
#                     else:
#                         root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    # change to 'teleport move'
    def sorceress_move(self, ents_list, endloc):
        global selected
        self.move_used = True
        oldloc = self.loc[:]
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = oldloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.finish_move(ents_list, endloc))
        
    def finish_move(self, ents_list, endloc):
        app.grid[self.loc[0]][self.loc[1]] = ''
        app.canvas.delete(self.number)
        self.loc = endloc[:]
#         app.ent_dict[id].origin = newloc[:]
        app.grid[endloc[0]][endloc[1]] = self.number
        try: 
            del app.vis_dict['Teleport']
            app.canvas.delete('Teleport')
        except: pass
        app.vis_dict['Teleport'] = Vis(name = 'Teleport', loc = endloc[:])
        vis = app.vis_dict['Teleport']
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Teleport')
        root.after(2999, lambda ents_list = ents_list, endloc = endloc : self.cleanup_teleport(ents_list, endloc))
        
    def cleanup_teleport(self, ents_list, endloc):
        del app.vis_dict['Teleport']
        app.canvas.delete('Teleport')
        app.canvas.create_image(endloc[0]*100+50-app.moved_right, endloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        try: app.canvas.tag_lower(self.tags, 'large')
        except: pass
        app.canvas.tag_lower(self.tags, 'maptop')
        root.after(666, lambda ents_list = ents_list : self.finish_turn(ents_list))
        
        
    def finish_turn(self, ents_list):
        if self.attack_used == False:
            atk_sqrs = self.legal_attacks()
            ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
            enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
            if enemy_ents != []:
                any = enemy_ents[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda t = id : app.get_focus(t))
                root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
            else: # END TURN
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    # change to fireblast
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
            self.attack_used = True
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/immolate.ogg')
            effect1.set_volume(.7)
            sound_effects.play(effect1, 0)
            # make range atk vis
            visloc = app.ent_dict[id].loc[:]
            app.vis_dict['Fireblast'] = Vis(name = 'Fireblast', loc = visloc)
            app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Fireblast'].img, tags = 'Fireblast')
            app.canvas.create_text(visloc[0]*100+50-app.moved_right, visloc[1]*100+10-app.moved_down, text = 'Fireblast', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
            my_psyche = self.get_attr('psyche')
            target_psyche = app.ent_dict[id].get_attr('psyche')
            if to_hit(my_psyche, target_psyche) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                d = damage(my_psyche, target_psyche)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Sorceress Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+100, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+80, text = 'Sorceress Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 12), tags = 'text')

            root.after(3666, lambda  el = ents_list, id = id : self.cleanup_attack(el, id))
        
        
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
            del app.vis_dict['Fireblast']
            app.canvas.delete('Fireblast')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) <= 3:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in app.coords:
            if dist(loc, c) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist
        
        
class Orc_Axeman(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 6
        self.agl = 5
        self.end = 6
        self.dodge = 7
        self.psyche = 3
        self.spirit = 29
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  ORC AXEMAN AI
    # instead of calling bfs on each potential target, can i walk grid with bfs until any enemy is found?
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/orc_axeman_attack.ogg')
            effect1.set_volume(.5)
            sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Orc Axeman Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Orc Axeman Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
            
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Fireblast']
#             app.canvas.delete('Fireblast')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 4)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class Fire_Elemental(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 5
        self.agl = 4
        self.end = 3
        self.dodge = 4
        self.psyche = 4
        self.spirit = 19
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    # FIRE ELEMENTAL AI
    # change attack to sirocco, small damage to all in area?
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
            effect1 = mixer.Sound('Sound_Effects/fire_elemental_attack.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+70, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Fire Elemental Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+90, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Fire Elemental Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
            
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Fireblast']
#             app.canvas.delete('Fireblast')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 4)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
        
class Barbarian(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 10
        self.agl = 8
        self.end = 8
        self.dodge = 5
        self.psyche = 3
        self.spirit = 79
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  BARBARIAN AI
    # instead of calling bfs on each potential target, can i walk grid with bfs until any enemy is found?
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    endloc = None
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    if endloc != None:
                        root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                        root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.ai_move(el, endloc))
                        else:
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else:
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            app.get_focus(id)
    #         self.init_attack_anims()
    #         effect1 = mixer.Sound('Sound_Effects/orc_axeman_attack.ogg')
    #         effect1.set_volume(1)
    #         sound_effects.play(effect1, 0)
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Barbarian Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Barbarian Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
        
            
    def cleanup_attack(self, ents_list, id):
        self.init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Fireblast']
#             app.canvas.delete('Fireblast')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 2) 
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
    # if no ent within immediate move/attack range, only move toward witch
class Minotaur_Top(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = True):
#         self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 11
        self.agl = 11
        self.end = 11
        self.dodge = 5
        self.psyche = 9
        self.spirit = 163
        self.waiting = waiting
        super().__init__(name, img, loc, owner, number, type = 'large')
    # 'tall' ent, bigger than 100 pixels height, needs to be split into 2 images so the 'top' image is 'large' (raised above 'maptop', bottom part of ent is hidden behind 'maptop'
class Minotaur(Summon):
    def __init__(self, name, img, loc, owner, number, waiting = False):
        self.actions = {'attack':self.do_attack}
        self.attack_used = False
        self.str = 11
        self.agl = 11
        self.end = 11
        self.dodge = 5
        self.psyche = 9
        self.spirit = 163
        self.waiting = waiting
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number, type = 'large_bottom')
        self.immovable = True
        # create top half
        img = ImageTk.PhotoImage(Image.open('animations/Minotaur_Top/0.png'))
        app.ent_dict[self.number+'top'] = Minotaur_Top(name = 'Minotaur_Top', img = img, loc = [self.loc[0],self.loc[1]], owner = 'p2', number = self.number+'top')
        
    def large_undo(self):
        app.canvas.delete(self.number+'top')
        del app.ent_dict[self.number+'top']
        
    def pass_priority(self, ents_list):
        ents_list = ents_list[1:]
        if ents_list == []:
            app.end_turn()
        else:
            app.do_ai_loop(ents_list)
        
    #  Minotaur AI
    def do_ai(self, ents_list):
        if self.waiting == True: # PASSIVE / WAITING
            self.pass_priority(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.do_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
#                 coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                for el in enemy_ent_locs:
                # FIND PATH TO SQR WITHIN RANGE OF THIS ENT
                    goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                    path = bfs(self.loc[:], goals, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)] # THE SHORTEST PATHS AMONG PATHS
                if smallpaths != []: # IF ANY PATHS EXIST AT ALL
                    apath = smallpaths[0]
                    if len(apath) > 5: # NOT WITHIN IMMEDIATE MOVE/ATTACK RANGE, MOVE TOWARDS WITCH
                        root.after(1333, lambda e = ents_list : self.move_to_witch(e))
                    else:
                        moves = self.legal_moves()
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc : self.minotaur_move(el, endloc))
                        else: #####
                            print('exit here')
                            ents_list = ents_list[1:]
                            if ents_list == []:
                                root.after(666, app.end_turn)
                            else:
                                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                            
                # CHANGE TO BEST EFFORT MOVE TOWARDS WITCH EGRID
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
                    # NOW FIND PATH AND PASS TO MOVE
#                     coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
                    for el in enemy_ent_locs:
                        goals = [c for c in app.coords if dist(c, el) == 1 and app.grid[c[0]][c[1]] == '']
                        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        if len(apath) > 5: # NOT WITHIN IMMEDIATE MOVE/ATTACK RANGE, MOVE TOWARDS WITCH
                            root.after(1333, lambda e = ents_list : self.move_to_witch(e))
                        else:
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                            moves = self.legal_moves()
                            endloc = None
                            for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                                if sqr in moves:
                                    endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                    break
                            if endloc != None:
                                # here need to 'trim path' to prevent moving to square 'through' friendly ents
                                root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                                root.after(1333, lambda el = ents_list, endloc = endloc : self.minotaur_move(el, endloc))
                            else:# POSSIBLE TO BE BLOCKED BY FRIENDLY UNIT, ATTEMPT ATTACK ON ANY HERE
                                atk_sqrs = self.legal_attacks()
                                ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
                                if ents_near != []:
                                    any = ents_near[0]
                                    id = app.grid[any[0]][any[1]]
                                    root.after(666, lambda t = id : app.get_focus(t))
                                    root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT 
                                else:
                                    ents_list = ents_list[1:]
                                    if ents_list == []:
                                        root.after(666, app.end_turn)
                                    else:
                                        root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                    else: # SHOULD NOT GET HERE ON LABYRINTH LEVEL, GETTING HERE MEANS THAT NO PATH EXISTS TO ANY PLAYER ENT EVEN AFTER REMOVING FRIENDLY ENTS
                        print('got to blocked minotaur AI area')
                        ents_list = ents_list[1:]
                        if ents_list == []:
                            root.after(666, app.end_turn)
                        else:
                            root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
                                
    # should be improved by first attempting path to witch on regular grid (not egrid)
    # make best effort to move towards witch (move to closest square on potentially blocked paths)
    # assumes that no Ents were within immediate attack/move-attack range
    def move_to_witch(self, ents_list):
        egrid = deepcopy(app.grid)
        # change to remove all non-witch ents
        nonwitch_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].name != app.p1_witch]
        for eloc in nonwitch_ent_locs:
            egrid[eloc[0]][eloc[1]] = '' # EGRID NOW EMPTIED OF FRIENDLY ENTS
        # NOW FIND PATH AND PASS TO MOVE
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        goals = [c for c in app.coords if dist(c, app.ent_dict[app.p1_witch].loc) == 1 and app.grid[c[0]][c[1]] == '']
        path = bfs(self.loc[:], goals, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
        if path: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
            # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
            moves = self.legal_moves()
            endloc = None
            for sqr in path[::-1]: # START WITH SQRS CLOSEST TO TARGET
                if sqr in moves:
                    endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                    break
            if endloc != None:
                # here need to 'trim path' to prevent moving to square 'through' friendly ents
                root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                root.after(1333, lambda el = ents_list, endloc = endloc : self.minotaur_move(el, endloc))
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    root.after(666, app.end_turn)
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                root.after(666, app.end_turn)
            else:
                root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            
    def minotaur_move(self, ents_list, endloc):
        global selected
        effect1 = mixer.Sound('Sound_Effects/minotaur_move.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, -1)
        selected = [self.number, self.number+'top']
        id = self.number
        start_sqr = self.loc[:]
        end_sqr = endloc[:] # redundant naming of vars
        path = bfs(start_sqr, [end_sqr], app.grid) # end_sqr must be put in list
        begin = path[0]
        end = path[1]
        x = begin[0]*100+50-app.moved_right
        y = begin[1]*100+50-app.moved_down
        endx = end[0]*100+50-app.moved_right
        endy = end[1]*100+50-app.moved_down
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path):
            if x % 20 == 0 or y % 20 == 0:
                app.ent_dict[id+'top'].rotate_image()
                app.canvas.delete(id)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
                app.canvas.delete(id+'top')
                app.canvas.create_image(x, y, image = app.ent_dict[id+'top'].img, tags = (id+'top','large'))
            if x > endx:
                x -= 10
                app.canvas.move(id, -10, 0)
                app.canvas.move(id+'top', -10, 0)
            if x < endx: 
                x += 10
                app.canvas.move(id, 10, 0)
                app.canvas.move(id+'top', 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(id, 0, -10)
                app.canvas.move(id+'top', 0, -10)
            if y < endy: 
                y += 10
                app.canvas.move(id, 0, 10)
                app.canvas.move(id+'top', 0, 10)
            try: app.canvas.tag_lower((self.tags), 'large')
            except: pass
            app.canvas.tag_lower((self.tags), 'maptop')
            app.canvas.tag_raise('cursor')
            if x == end_sqr[0]*100+50-app.moved_right and y == end_sqr[1]*100+50-app.moved_down: # END WHOLE MOVE
                self.finish_move(end_sqr, start_sqr, ents_list)
            elif x == endx and y == endy: # END PORTION OF PATH
                path = path[1:]
                begin = path[0]
                end = path[1]
                x = begin[0]*100+50-app.moved_right
                y = begin[1]*100+50-app.moved_down
                endx = end[0]*100+50-app.moved_right
                endy = end[1]*100+50-app.moved_down
                move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, ex = endx, ey = endy, s = start_sqr, s2 = end_sqr, p = path : move_loop(id, x, y, ex, ey, s, s2, p))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr, path)
        
    def finish_move(self, end_sqr, start_sqr, ents_list):
        global selected
        sound_effects.stop()
        selected = []
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        app.ent_dict[self.number+'top'].loc = [end_sqr[0],end_sqr[1]]
        # MAKE ATTACK ON ANY ENEMY ENT WITHIN RANGE
        atk_sqrs = self.legal_attacks()
        ents_near = [e for e in atk_sqrs if app.grid[e[0]][e[1]] != '' and app.grid[e[0]][e[1]] != 'block']
#         enemy_ents = [e for e in ents_near if app.ent_dict[app.grid[e[0]][e[1]]].owner == 'p1']
        if ents_near != []:
            any = ents_near[0]
            id = app.grid[any[0]][any[1]]
            root.after(666, lambda t = id : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = id : self.do_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def do_attack(self, ents_list, id):
        if self.attack_used == True:
            self.cleanup_attack(ents_list, id)
        else:
            effect1 = mixer.Sound('Sound_Effects/minotaur_attack.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, -1)
            app.get_focus(id)
            app.ent_dict[self.number+'top'].init_attack_anims()
            my_agl = self.get_attr('agl')
            target_agl = app.ent_dict[id].get_attr('agl')
            if to_hit(my_agl, target_agl) == True:
                # HIT, SHOW VIS, DO DAMAGE, EXIT
                my_str = self.get_attr('str')
                target_end = app.ent_dict[id].get_attr('end')
                d = damage(my_str, target_end)
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Minotaur Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                app.ent_dict[id].set_attr('spirit', -d)
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
            else:
                # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Minotaur Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id))
        
            
    def cleanup_attack(self, ents_list, id):
#         self.init_normal_anims()
        app.ent_dict[self.number+'top'].init_normal_anims()
        try: 
            app.canvas.delete('text')
#             del app.vis_dict['Fireblast']
#             app.canvas.delete('Fireblast')
        except: pass
        if app.ent_dict[id].spirit <= 0:
            if app.kill(id) == None:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    app.do_ai_loop(ents_list)
            else:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(3333, lambda el = ents_list : app.do_ai_loop(el))
        else:
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                app.do_ai_loop(ents_list)
        
        
    def legal_attacks(self):
        sqrs = []
        for coord in app.coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 5)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
        
class Warrior(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.warrior_attack, 'leap':self.leap, 'guard':self.guard, 'move':self.move}
        self.attack_used = False
        self.str = 5
        self.agl = 5
        self.end = 6
        self.dodge = 2
        self.psyche = 2
        self.spirit = 15
        self.move_type = 'charge'
        super().__init__(name, img, loc, owner, number)
        
    def init_leap_anims(self):
        self.anim_dict = {}
        self.anim_counter = 0
        anims = [a for r,d,a in walk('./animations/Leap/')][0]
        anims = [a for a in anims[:] if a[-3:] == 'png']
        for i, anim in enumerate(anims):
            a = ImageTk.PhotoImage(Image.open('animations/Leap/' + anim))
            self.anim_dict[i] = a
        
    def guard(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 3 and c != self.loc:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, sqrs = sqrs, sqr = grid_pos : self.do_guard(event = e, sqrs = sqrs, sqr = sqr)) 
        b = tk.Button(app.context_menu, text = 'Confirm Guard', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs, sqr = grid_pos : self.do_guard(event = e, sqrs = sqrs, sqr = sqr))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_guard(self, event = None, sqrs = None, sqr = None):
        if sqr not in sqrs:
            return
        self.attack_used = True
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if app.ent_dict[id].owner != self.owner:
            return
#         effect1 = mixer.Sound('Sound_Effects/guard.ogg')
#         effect1.set_volume(1)
#         sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        def guard_effect():
            pass
        f = guard_effect
        def guard_set_attr(attr = None, amount = None, obj = None, redir_obj = None):# REPLACE OBJ set_attr with -2 (2 more subtracted)
            if attr == 'str':
                obj.str += amount
            elif attr == 'agl':
                obj.agl += amount
            elif attr == 'end':
                obj.end += amount
            elif attr == 'dodge':
                obj.dodge += amount
            elif attr == 'psyche':
                obj.psyche += amount
            elif attr == 'spirit':
                app.canvas.create_text(obj.loc[0]*100-app.moved_right+50, obj.loc[1]*100-app.moved_down+95, text = 'Guard Redirect', justify = 'center', fill = 'white', font = ('Andale Mono', 13), tags = 'text')
                redir_obj.spirit += amount
                if redir_obj.spirit > obj.base_spirit:
                    redir_obj.spirit = obj.base_spirit
                if redir_obj.spirit <= 0:
                    p = partial(obj.__class__.set_attr, obj, attr, d) #   PUT BACK CLASS METHOD set_attr
                    obj.set_attr = p
                    app.focus_square(redir_obj.loc)
                    app.canvas.create_text(redir_obj.loc[0]*100-app.moved_right+50, redir_obj.loc[1]*100-app.moved_down+95, text = 'Guard Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 13), tags = 'text')
                    root.after(1999, lambda e = self.id : app.kill(e))
            elif isinstance(obj, Witch) or isinstance(obj, Trickster):
                if attr == 'magick':
                    obj. magick += amount
                    if obj.magick > obj.base_magick:
                        obj.magick = obj.base_magick
        p = partial(guard_set_attr, obj = app.ent_dict[id], redir_obj = app.ent_dict[self.number])
        app.ent_dict[id].set_attr = p
        def un(i):
            p = partial(app.ent_dict[i].__class__.set_attr, app.ent_dict[i], attr, d) #   PUT BACK CLASS METHOD set_attr
            app.ent_dict[i].set_attr = p
            return None
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Guard' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Guard', info = 'Guard, redir dmg', eot_func = eot, undo = p, duration = 3)
        root.after(2666, lambda e = None: self.cancel_attack(e))





        
    def leap(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 3 and app.grid[c[0]][c[1]] == '':
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, sqrs = sqrs, sqr = grid_pos : self.do_leap(event = e, sqrs = sqrs, sqr = sqr)) 
        b = tk.Button(app.context_menu, text = 'Confirm Leap', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs, sqr = grid_pos : self.do_leap(event = e, sqrs = sqrs, sqr = sqr))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_leap(self, event = None, sqrs = None, sqr = None):
        global selected
        if sqr not in sqrs:
            return
        self.attack_used = True
        self.init_leap_anims()
#         effect1 = mixer.Sound('Sound_Effects/leap.ogg')
#         effect1.set_volume(1)
#         sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = sqr[0]*100+50-app.moved_right
        endy = sqr[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = sqr[:]
        selected = [self.number]
        total_distance = abs(x - endx) + abs(y - endy)
        tic = total_distance/6
        # need to call rotate_image every tic
        def move_loop(x, y, endx, endy, start_sqr, end_sqr, acm, tic):
            if acm > tic:
                acm = 0
                self.rotate_image()
                app.canvas.delete(self.number)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
            if x > endx:
                acm += 10
                x -= 10
                app.canvas.move(self.number, -10, 0)
            if x < endx:
                acm += 10
                x += 10
                app.canvas.move(self.number, 10, 0)
            if y > endy:
                acm += 10
                y -= 10
                app.canvas.move(self.number, 0, -10)
            if y < endy:
                acm += 10
                y += 10
                app.canvas.move(self.number, 0, 10)
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_leap(end_sqr, start_sqr) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr, acm = acm, tic = tic : move_loop(x, y, e, e2, s, s2, acm, tic))
        move_loop(x, y, endx, endy, start_sqr, end_sqr, tic+1, tic)
            
            
    def finish_leap(self, end_sqr, start_sqr):
        global selected
        selected = []
        self.loc = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        self.init_normal_anims()
        app.rebind_all()
#         app.canvas.delete('text')
#         try: 
#             del app.vis_dict['Warrior_Slash']
#             app.canvas.delete('Warrior_Slash')
#         except: pass
        app.depop_context(event = None)
        app.cleanup_squares()
        
        
    def warrior_attack(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) == 1:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, sqrs = sqrs, sqr = grid_pos : self.check_hit(event = e, sqrs = sqrs, sqr = sqr)) 
        b = tk.Button(app.context_menu, text = 'Confirm Attack', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs, sqr = grid_pos : self.check_hit(event = e, sqrs = sqrs, sqr = sqr))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def check_hit(self, event = None, sqrs = None, sqr = None):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        self.attack_used = True
        self.init_attack_anims()
        effect1 = mixer.Sound('Sound_Effects/warrior_attack.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        app.vis_dict['Warrior_Slash'] = Vis(name = 'Warrior_Slash', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Warrior_Slash'].img, tags = 'Warrior_Slash')
        my_agl = self.get_attr('agl')
        target_agl = app.ent_dict[id].get_attr('agl')
        if to_hit(my_agl, target_agl) == True:
            my_str = self.get_attr('str')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_str, target_end)
            app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+50, text = 'Warrior Attack Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda id = id, d = d : self.do_attack(id, d))
        else:
            app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+50, text = 'Warrior Attack Misses!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda e = None : self.cancel_attack(event = e))
        
    def do_attack(self, id, dmg):
        app.ent_dict[id].set_attr('spirit', -dmg)
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name.replace('_', ' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(1666, lambda id = id : app.kill(id))
            root.after(1666, lambda e = None : self.cancel_attack(e))
        else:
            self.cancel_attack(event = None)
    
    def cancel_attack(self, event):
        self.init_normal_anims()
        app.rebind_all()
        app.canvas.delete('text')
        try: 
            del app.vis_dict['Warrior_Slash']
            app.canvas.delete('Warrior_Slash')
        except: pass
        app.depop_context(event = None)
        app.cleanup_squares()
    
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        # need to stop movement when obstructed
        coords.remove(loc)
        for c in coords:
            if loc[0]-1 == c[0] and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
                n = [c[0]-1, c[1]]
                if n in coords:
                    if  app.grid[n[0]][n[1]] == '':
                        mvlist.append(n)
                        n = [n[0]-1, n[1]]
                        if n in coords:
                            if  app.grid[n[0]][n[1]] == '':
                                mvlist.append(n)
                        
            elif loc[0]+1 == c[0] and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
                n = [c[0]+1, c[1]]
                if n in coords:
                    if  app.grid[n[0]][n[1]] == '':
                        mvlist.append(n)
                        n = [n[0]+1, n[1]]
                        if n in coords:
                            if  app.grid[n[0]][n[1]] == '':
                                mvlist.append(n)
                        
            elif c[0] == loc[0] and loc[1]-1 == c[1] and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
                n = [c[0], c[1]-1]
                if n in coords:
                    if  app.grid[n[0]][n[1]] == '':
                        mvlist.append(n)
                        n = [n[0], n[1]-1]
                        if n in coords:
                            if  app.grid[n[0]][n[1]] == '':
                                mvlist.append(n)
                        
            elif c[0] == loc[0] and loc[1]+1 == c[1] and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
                n = [c[0], c[1]+1]
                if n in coords:
                    if  app.grid[n[0]][n[1]] == '':
                        mvlist.append(n)
                        n = [n[0], n[1]+1]
                        if n in coords:
                            if  app.grid[n[0]][n[1]] == '':
                                mvlist.append(n)
        return mvlist
                    
                    
    # confuse, target must make psyche check before attack
    # fuse trap, set global effect on sqr, when effect ends all ents within range 2 take 5 dmg 
class Familiar_Homonculus(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Mesmerize':self.mesmerize, 'Fuse Trap':self.fuse_trap, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 5
        self.end = 5
        self.dodge = 6
        self.psyche = 5
        self.spirit = 11
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
                    
                    
    def fuse_trap(self, event = None):
        if self.attack_used == True:
            return
        app.depop_context(event = None)
        root.unbind('<q>')
        root.unbind('<a>')
        root.bind('<q>', self.cleanup_fuse_trap)
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 5]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_fuse_trap(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Square For Fuse Trap', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_fuse_trap(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    # place in unoccupied sqr?
    def do_fuse_trap(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        if app.grid[sqr[0]][sqr[1]] != '':
            return
        # not working, allowing multiple
        visuals = [v.name for k,v in app.vis_dict.items() if v.loc == sqr]
        if 'Fuse_Trap' in visuals:
            return
        effect1 = mixer.Sound('Sound_Effects/fuse_trap.ogg')
        effect1.set_volume(.07)
        sound_effects.play(effect1, 0)
        self.attack_used = True
        app.unbind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        uniq_name = 'Fuse_Trap' + str(app.effects_counter)
        app.effects_counter += 1
        app.vis_dict[uniq_name] = Vis(name = 'Fuse_Trap', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = uniq_name)
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Fuse Trap', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Fuse trap EFFECTS
        def fuse_trap_effect():
            return None
        # on undo, dmg within range 2
        def un(sqrs, name):
            app.focus_square(app.vis_dict[name].loc)
            effect1 = mixer.Sound('Sound_Effects/fuse_explosion.ogg')
            effect1.set_volume(1)
            sound_effects.play(effect1, 0)
            ents = [k for k,v in app.ent_dict.items() if v.loc in sqrs]
            for sqr in sqrs:
                uniq_name = 'Fuse_Explosion' + str(app.effects_counter)
                app.effects_counter += 1
                app.vis_dict[uniq_name] = Vis(name = 'Fuse_Explosion', loc = sqr[:])
                app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = uniq_name)
                def clean_explosion(u_name):
                    del app.vis_dict[u_name]
                    app.canvas.delete(u_name)
                    app.canvas.delete('text')
                root.after(2666, lambda n = uniq_name : clean_explosion(n))
            for id in ents:
                sqr = app.ent_dict[id].loc[:]
                app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Fuse Trap\n5 Spirit', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                app.ent_dict[id].set_attr('spirit', -5)
                # add kill
                if app.ent_dict[id].spirit <= 0:
                    app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+95-app.moved_down, text = app.ent_dict[id].name.replace('_', ' ') + ' Killed...', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                    root.after(2666, lambda id = id : app.kill(id))
            try: 
                del app.vis_dict[name]
                app.canvas.delete(name)
            except: pass
            return 'Not None'
            
        def nothing():
            return None
        eot = nothing
        sqrs_area = [s for s in app.coords if dist(s, sqr) <= 2]
        p = partial(un, sqrs_area, uniq_name)
        app.global_effects_dict[uniq_name] = Effect(name = 'Fuse_Trap', info = 'dmgs all within range 2 when duration ends', eot_func = eot, undo = p, duration = 3)
        root.after(1666, self.cleanup_fuse_trap)
                    
    def cleanup_fuse_trap(self, event = None):
        app.depop_context(event = None)
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.canvas.delete('text')
                    
    def mesmerize(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_mesmerize)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 3:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_mesmerize(event = e, sqr = s, sqrs = sqrs)) 
        b = tk.Button(app.context_menu, text = 'Confirm Mesmerize', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_mesmerize(event = e, sqr = s, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    # add mesmerize fail text
    def do_mesmerize(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        effs = [k for k in app.ent_dict[id].effects_dict.keys()]
        if 'Mesmerize' in effs:
            return
        effect1 = mixer.Sound('Sound_Effects/mesmerize.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.attack_used = True
        # add confuse effect, at start of turn unit makes psyche check, on fail unit gets attack_used set to True and takes 5 dmg
#         def mesmerize_effect():
#             pass
        def un():
            return None
        def nothing():
            return None
        eot = nothing
        # SOT FUNC
        def mesmerized(tar):
            app.get_focus(tar)
            # make psyche check
            if app.ent_dict[tar].attr_check('psyche') == False:
                app.ent_dict[tar].attack_used = True
                app.ent_dict[tar].set_attr('spirit', -5)
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+70-app.moved_down, text = '5 Spirit, mesmerized', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                if app.ent_dict[tar].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            else:
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+70-app.moved_down, text = 'Mesmerize Save', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            return 'Not None'
            
        sot = partial(mesmerized, id)
        app.ent_dict[id].effects_dict['Mesmerize'] = Effect(sot_func = sot, name = 'Mesmerize', info = 'Mesmerize\nMay attack self', eot_func = eot, undo = un, duration = 4)
        
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Mesmerize', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
        app.vis_dict['Mesmerize'] = Vis(name = 'Mesmerize', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Mesmerize'].img, tags = 'Mesmerize')
        root.after(2999, self.cancel_mesmerize)
        
        
    def cancel_mesmerize(self, event = None):
        app.unbind_all()
        app.rebind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        app.canvas.delete('text')
        try: 
            del app.vis_dict['Mesmerize']
            app.canvas.delete('Mesmerize')
        except: pass
                    
                    
    def death_trigger(self):
        if self.owner == 'p1':
            witch = app.p1_witch
        else:
            witch = app.p2_witch
        loc = app.ent_dict[witch].loc[:]
        app.ent_dict[witch].set_attr('spirit', -3)
        app.get_focus(witch)
        app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = '3 Spirit, Familiar Death', font = ('Andale Mono', 14), fill = 'white', tags = 'familiar_death')
        root.after(2333, lambda t = 'familiar_death' : app.canvas.delete(t))
        if app.ent_dict[witch].spirit <= 0:
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+95-app.moved_down, text = app.ent_dict[witch].name.replace('_', ' ')+' Killed...', font = ('Andale Mono', 14), fill = 'white', tags = 'self_death')
            root.after(1666, lambda id = app.ent_dict[witch].name : app.kill(id))

    def legal_moves(self):
        loc = self.loc
        mvlist = []
        for c in app.coords:
            if dist(c, loc) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist



class Cenobite(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Strength Through Wounding':self.strength_through_wounding, 'Flesh Hooks': self.flesh_hooks, 'Hellfire': self.hellfire, 'Move': self.move}
        self.attack_used = False
        self.str = 6
        self.agl = 6
        self.end = 6
        self.dodge = 6
        self.psyche = 6
        self.spirit = 16
        self.move_type = 'normal'
        super().__init__(name, img, loc, owner, number)
        
    def strength_through_wounding(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_strength_through_wounding)
        sqrs = [c for c in app.coords if dist(self.loc, c) <= 3]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.do_strength_through_wounding(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Strength Through Wounding', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs : self.do_strength_through_wounding(event = e, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_strength_through_wounding(self, event = None, sqrs = None):
        self.attack_used = True
        effect1 = mixer.Sound('Sound_Effects/strength_through_wounding.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.unbind_all()
        ents = []
        for s in sqrs:
            ent = app.grid[s[0]][s[1]]
            if ent != '' and ent != 'block':
            # deal 2 to this ent
                app.ent_dict[ent].set_attr('spirit', -2)
                app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+70-app.moved_down, text = '2 spirit', justify = 'center', font = ('Andale Mono', 13), fill = 'ivory3', tags = 'text')
                if app.ent_dict[ent].spirit <= 0:
                    app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+90-app.moved_down, text = app.ent_dict[ent].name + ' Killed...', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
                    root.after(3666, lambda e = ent : app.kill(e))
                # give stat bonus if friendly
                elif app.ent_dict[ent].owner == app.active_player:
                    ef_names = [v.name for k,v in app.ent_dict[ent].effects_dict.items()]
                    if 'Strength_Through_Wounding' not in ef_names:
                        n2 = 'Strength_Through_Wounding' + str(app.effects_counter) # not an effect, just need unique int
                        app.effects_counter += 1 # that is why this is incr manually here, no Effect init
                        app.vis_dict[n2] = Vis(name = 'Strength_Through_Wounding', loc = s)
                        app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Strength_Through_Wounding')
                        app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+90-app.moved_down, text = '+2 End, Psy', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
                        def strength_through_wounding_effect(stat):
                            stat += 2
                            return stat
                        f = strength_through_wounding_effect
                        app.ent_dict[ent].end_effects.append(f)
                        app.ent_dict[ent].psyche_effects.append(f)
                        n = 'Strength_Through_Wounding' + str(app.effects_counter)
                        def un(i, func):
                            app.ent_dict[i].end_effects.remove(func)
                            app.ent_dict[i].psyche_effects.remove(func)
                            return None
                        p = partial(un, ent, f)
                        # EOT FUNC
                        def nothing():
                            return None
                        n = 'Strength_Through_Wounding' + str(app.effects_counter)
                        app.ent_dict[ent].effects_dict[n] = Effect(name = 'Strength_Through_Wounding', info = 'STW, +2 end, psy', eot_func = nothing, undo = p, duration = 3)
        root.after(3666, self.finish_strength_through_wounding)
        
    def finish_strength_through_wounding(self, event = None):
#         self.init_normal_anims()
        try:
            ks = list(app.vis_dict.keys())
            for k in ks:
                if k.startswith('Strength_Through_Wounding') == True:
                    del app.vis_dict[k]
            app.canvas.delete('Strength_Through_Wounding')
        except: pass
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
        
    # add ranged attack to a unit, unit gains: attack each enemy unit within range3 with to-hit check of own agl versus dodge, dmg is 12//num_targets min1, unit then deals 2 to self, lasts 3 turns
    def flesh_hooks(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_flesh_hooks)
        sqrs = [c for c in app.coords if dist(self.loc, c) <= 3 and c != self.loc]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_flesh_hooks(event = e, sqr = s, sqrs = sqrs)) 
        b = tk.Button(app.context_menu, text = 'Bestow Flesh Hooks', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_flesh_hooks(event = e, sqr = s, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_flesh_hooks(self, event = None, sqr = None, sqrs = None):
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if app.ent_dict[id].owner != self.owner:
            return
        self.attack_used = True
#         self.init_attack_anims()
        effect1 = mixer.Sound('Sound_Effects/flesh_hooks.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.cleanup_squares()
        app.unbind_all()
        app.vis_dict['Flesh_Hooks'] = Vis(name = 'Flesh_Hooks', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Flesh_Hooks'].img, tags = 'Flesh_Hooks')
        app.canvas.create_text(sqr[0]*100-app.moved_right+50, sqr[1]*100-app.moved_down+90, text = 'Flesh Hooks', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
        # add action to ent, needs to focus on each hit, lessen damage(divide by targets probably?)
        def hook_attack(event = None, obj = None):
            if obj.attack_used == True:
                return
            root.unbind('<a>')
            root.unbind('<q>')
            root.bind('<q>', lambda e, obj = obj : cancel_attack(obj = obj))
            sqrs = []
            for c in app.coords:
                if 1 <= dist(obj.loc, c) <= 3:
                    sqrs.append(c)
            app.animate_squares(sqrs)
            app.depop_context(event = None)
            root.bind('<a>', lambda e, sqrs = sqrs, sqr = grid_pos, obj = obj : check_hit(event = e, sqrs = sqrs, sqr = sqr, obj = obj)) 
            b = tk.Button(app.context_menu, text = 'Confirm Hook Attack', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs, sqr = grid_pos, obj = obj : check_hit(event = e, sqrs = sqrs, sqr = sqr, obj = obj))
            b.pack(side = 'top')
            app.context_buttons.append(b)
            # INNER-INNER FUNCS, context must be passed to obj receiving this action
            def check_hit(event = None, sqrs = None, sqr = None, obj = None):
                if sqr not in sqrs:
                    return
                id = app.grid[sqr[0]][sqr[1]]
                if id == '' or id == 'block':
                    return
                obj.attack_used = True
#                 obj.init_attack_anims()
                effect1 = mixer.Sound('Sound_Effects/hook_attack.ogg')
                effect1.set_volume(1)
                sound_effects.play(effect1, 0)
                app.depop_context(event = None)
                app.unbind_all()
                app.cleanup_squares()
                visloc = app.ent_dict[id].loc[:]
                app.vis_dict['Hook_Attack'] = Vis(name = 'Hook_Attack', loc = visloc)
                app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Hook_Attack'].img, tags = 'Hook_Attack')
                my_psyche = obj.get_attr('psyche')
                target_dodge = app.ent_dict[id].get_attr('dodge')
                if to_hit(my_psyche, target_dodge) == True:
                    my_end = obj.get_attr('end')
                    target_end = app.ent_dict[id].get_attr('end')
                    d = damage(my_end, target_end)
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = 'Hit!\n' + str(d) + ' Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                    app.ent_dict[id].set_attr('spirit', -d)
                    if app.ent_dict[id].spirit <= 0:
                        app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+90, text = app.ent_dict[id].name+' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                        root.after(2666, lambda id = id : app.kill(id))
                    root.after(2666, lambda e = None, obj = obj : cancel_attack(event = e, obj = obj))
                else:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+90, text = 'Hook Attack Misses!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                    root.after(2666, lambda e = None, obj = obj : cancel_attack(event = e, obj = obj))
            # INNER INNER FUNC
            def cancel_attack(event = None, obj = None):
                obj.init_normal_anims() # to init attack anims, provide them for each possible unit that can gain hook_attack
                app.rebind_all()
                app.canvas.delete('text')
                try:
                    del app.vis_dict['Hook_Attack']
                    app.canvas.delete('Hook_Attack')
                except: pass
                app.depop_context(event = None)
                app.cleanup_squares()
            # END INNER-INNER FUNCS
        # ADD ACTION TO TARGET
        p = partial(hook_attack, obj = app.ent_dict[id])
        app.ent_dict[id].actions['Hook Attack'] = p
        def hook_effect():
            pass
        f = hook_effect
        def un(i):
            del app.ent_dict[i].actions['Hook Attack']
            return None
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Hook_Attack' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Hook_Attack', info = 'Added Hook Attack', eot_func = eot, undo = p, duration = 3)
        root.after(2666, self.finish_flesh_hooks)
        
    def finish_flesh_hooks(self, event = None):
#         self.init_normal_anims()
        try:
            del app.vis_dict['Flesh_Hooks']
            app.canvas.delete('Flesh_Hooks')
        except: pass
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
        
    # damage and possible burn to target
    # vis, self 'glows', target flames
    def hellfire(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_hellfire)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 2:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.check_hit(event = e, sqr = s, sqrs = sqrs)) 
        b = tk.Button(app.context_menu, text = 'Confirm Hellfire', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos[:], sqrs = sqrs : self.check_hit(event = e, sqr = s, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def check_hit(self, event = None, sqr = None, sqrs = None):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        self.attack_used = True
#         self.init_attack_anims()
#         effect1 = mixer.Sound('Sound_Effects/hellfire.ogg')
#         effect1.set_volume(1)
#         sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        visloc = app.ent_dict[id].loc[:]
        app.vis_dict['Hellfire'] = Vis(name = 'Hellfire', loc = visloc)
        app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Hellfire'].img, tags = 'Hellfire')
        my_psyche = self.get_attr('psyche')
        target_psyche = app.ent_dict[id].get_attr('psyche')
        if to_hit(my_psyche, target_psyche) == True:
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_psyche, target_end)
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+75-app.moved_down, text = 'Hit! '+str(d)+' spirit', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+90-app.moved_down, text = app.ent_dict[id].name.replace('_',' ')+' Killed...', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                root.after(2999, lambda id = id: app.kill(id))
            else:
            # save to avoid burn
                if 1 == 1:
#                 if app.ent_dict[id].attr_check('end') == False:
                    app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+95-app.moved_down, text = 'Burned', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                # burn effect, every time burned ent takes spirit dmg it takes that much dmg plus 2
                # need to overwrite ent.set_attr
                    def burn_effect():
                        pass
                    f = burn_effect
                    def burned_set_attr(attr = None, amount = None, obj = None):# REPLACE OBJ set_attr with -2 (2 more subtracted)
                        if attr == 'str':
                            obj.str += amount
                        elif attr == 'agl':
                            obj.agl += amount
                        elif attr == 'end':
                            obj.end += amount
                        elif attr == 'dodge':
                            obj.dodge += amount
                        elif attr == 'psyche':
                            obj.psyche += amount
                        elif attr == 'spirit':
                            if amount < 0: # only add 2 dmg when taking dmg, not when healing
                                obj.spirit += amount-2
                            else:
                                obj.spirit += amount
                            if obj.spirit > obj.base_spirit:
                                obj.spirit = obj.base_spirit
                            app.canvas.create_text(obj.loc[0]*100+50-app.moved_right, obj.loc[1]*100+55-app.moved_down, text = '2 spirit burn', justify ='center', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
                        elif isinstance(obj, Witch) or isinstance(obj, Trickster):
                            if attr == 'magick':
                                obj. magick += amount
                                if obj.magick > obj.base_magick:
                                    obj.magick = obj.base_magick
                    p = partial(burned_set_attr, obj = app.ent_dict[id])
                    app.ent_dict[id].set_attr = p
                    def un(i):
                        p = partial(app.ent_dict[i].__class__.set_attr, app.ent_dict[i]) # PUT BACK CLASS METHOD MOVEMENT
                        app.ent_dict[i].set_attr = p
                        return None
                    p = partial(un, id)
                    # EOT FUNC
                    def nothing():
                        return None
                    eot = nothing
                    n = 'Burn' + str(app.effects_counter)
                    app.ent_dict[id].effects_dict[n] = Effect(name = 'Burn', info = 'Burn, 2 more dmg', eot_func = eot, undo = p, duration = 3)
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+75-app.moved_down, text = 'Missed', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
        root.after(2666, lambda e = None : self.cancel_hellfire(event = e))
        
    def cancel_hellfire(self, event):
        self.init_normal_anims()
        app.rebind_all()
        app.canvas.delete('text')
        try: 
            del app.vis_dict['Hellfire']
            app.canvas.delete('Hellfire')
        except: pass
        app.depop_context(event = None)
        app.cleanup_squares()
        
        
        
        
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 4) 
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
    # ensure only one at a time, on death witch loses spirit, flight for movement (not blocked by obstacles)
    # casts poison sting, darkness, 
    # darkness, global effect that affects sqrs within distance 3, any movement originating in one of these sqrs is reduced to distance 2, only affects ents that use 'normal' movement (non-teleport)
    # poison sting, agl versus dodge to hit check, on success target gets 'poison' effect, -1 str 2 dmg for 3 turns, stackable, range 2
class Familiar_Imp(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Poison Sting':self.poison_sting, 'Darkness':self.darkness, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 6
        self.end = 3
        self.dodge = 7
        self.psyche = 6
        self.spirit = 9
        self.move_type = 'flying'
        super().__init__(name, img, loc, owner, number)
        
        
    def darkness(self, event = None):
        g_effects = [v.name for k,v in app.global_effects_dict.items()]
        if 'Darkness' in g_effects:
            return
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 3:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_darkness(event = e, sqr = s, sqrs = sqrs)) 
        b = tk.Button(app.context_menu, text = 'Confirm Darkness', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_darkness(event = e, sqr = s, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_darkness(self, event = None, sqr = None, sqrs = None):
        if sqr not in sqrs:
            return
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        effect1 = mixer.Sound('Sound_Effects/darkness.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        self.attack_used = True
        app.canvas.create_text(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+75-app.moved_down, text = 'Darkness', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # create vis on every sqr within distance 3 from sqr
        affected_sqrs = []
        for c in app.coords:
            if dist(sqr, c) <= 2:
                affected_sqrs.append(c)
        darkness_group = 'Darkness' + str(app.effects_counter)
        app.effects_counter += 1
        uniq_names = []
        for s in affected_sqrs:
            num = app.effects_counter
            app.effects_counter += 1
            uniq_name = 'Darkness' + str(num)
            uniq_names.append(uniq_name)
            app.vis_dict[uniq_name] = Vis(name = 'Darkness', loc = s)
            rand_num = randrange(1,6)
            for x in range(rand_num):
                app.vis_dict[uniq_name].rotate_image()
            app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = uniq_name)
            
        def darkness_effect(sqrs):
            # find all ents with locs in sqrs
            ents = [k for k,v in app.ent_dict.items() if v.loc in sqrs]
            # blind effect
            for id in ents:
                effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
                if 'Blind' in effs:
                    continue
                else:
                    def blind_effect(): # EOT effect (nothing)
                        pass
                    # SOT effect (at begin of turn, if ent is within affected sqrs)
                    def blind(i):# REPLACE CLASS MOVEMENT WITH MOVE dist 2 if movement type == normal
                        mvlist = []
                        for c in app.coords:
                            if dist(c, app.ent_dict[i].loc) <= 2:
                                mvlist.append(c)
                        return mvlist
                    if app.ent_dict[id].move_type == 'normal':
                        blind_p = partial(blind, id)
                        app.ent_dict[id].legal_moves = blind_p
                    def un(i):
                        p = partial(app.ent_dict[i].__class__.legal_moves, app.ent_dict[i]) # PUT BACK CLASS MOVES
                        app.ent_dict[i].legal_moves = p
                    p = partial(un, id)
                    # EOT FUNC
                    def nothing():
                        return None
                    eot = nothing
                    n = 'Blind' + str(app.effects_counter)
                    app.ent_dict[id].effects_dict[n] = Effect(name = 'Blind', info = 'Blind\nNormal movement reduced to 2', eot_func = eot, undo = p, duration = 1)
            return None
        def un(uniq_names):
            for name in uniq_names:
                del app.vis_dict[name]
                app.canvas.delete(name)
            return None
        eot_p = partial(darkness_effect, affected_sqrs)
        p = partial(un, uniq_names)
        app.global_effects_dict[darkness_group] = Effect(name = 'Darkness', info = 'darkness limits movement', eot_func = eot_p, undo = p, duration = 6)
        root.after(1666, self.cleanup_darkness)
            
    def cleanup_darkness(self, event = None):
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        try: app.canvas.delete('text')
        except: pass
        
    def death_trigger(self):
        if self.owner == 'p1':
            witch = app.p1_witch
        else:
            witch = app.p2_witch
        loc = app.ent_dict[witch].loc[:]
        app.ent_dict[witch].set_attr('spirit', -3)
        app.get_focus(witch)
        app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = '3 Spirit, Familiar Death', font = ('Andale Mono', 14), fill = 'white', tags = 'familiar_death')
        root.after(2333, lambda t = 'familiar_death' : app.canvas.delete(t))
        if app.ent_dict[witch].spirit <= 0:
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+95-app.moved_down, text = app.ent_dict[witch].name.replace('_', ' ')+' Killed...', font = ('Andale Mono', 14), tags = 'self_death')
            root.after(1666, lambda id = app.ent_dict[witch].name : app.kill(id))
        
    def poison_sting(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cancel_attack)
        sqrs = []
        for c in app.coords:
            if dist(self.loc, c) <= 3:
                sqrs.append(c)
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.check_hit(event = e, sqr = s, sqrs = sqrs)) 
        b = tk.Button(app.context_menu, text = 'Confirm Poison Sting', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos[:], sqrs = sqrs : self.check_hit(event = e, sqr = s, sqrs = sqrs))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    # add directional vis
    # create dart object on origin sqr, rotate image based on slope and direction of line from origin to target?
    def check_hit(self, event = None, sqr = None, sqrs = None):
        if sqr not in sqrs:
            return
        if app.grid[sqr[0]][sqr[1]] == '' or app.grid[sqr[0]][sqr[1]] == 'block':
            return
        self.attack_used = True
#         self.init_attack_anims()
        effect1 = mixer.Sound('Sound_Effects/poison_sting.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        id = app.grid[sqr[0]][sqr[1]]
        visloc = app.ent_dict[id].loc[:]
        app.vis_dict['Poison_Sting'] = Vis(name = 'Poison_Sting', loc = visloc)
        app.canvas.create_image(visloc[0]*100+50-app.moved_right, visloc[1]*100+50-app.moved_down, image = app.vis_dict['Poison_Sting'].img, tags = 'Poison_Sting')
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+75-app.moved_down, text = 'Poison Sting Hit', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            # poison str effect
            def poison_sting_effect(stat):
                stat -= 1
                if stat < 1:
                    return 1
                else:
                    return stat
            f = poison_sting_effect
            app.ent_dict[id].str_effects.append(f)
            def un(i):
                app.ent_dict[i].str_effects.remove(poison_sting_effect)
                return None
            p = partial(un, id)
            # EOT FUNC
            def take_2(tar):
                app.get_focus(tar)
                app.ent_dict[tar].set_attr('spirit', -2)
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+50-app.moved_down, text = '2 Spirit\nPoison', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                if app.ent_dict[tar].spirit <= 0:
                    app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                return 'Not None'
            eot = partial(take_2, id)
            n = 'Poison_Sting' + str(app.effects_counter)
            app.ent_dict[id].effects_dict[n] = Effect(name = 'Poison_Sting', info = 'Poison Sting\n Str reduced by 1 for 3 turns\n2 Spirit damage per turn', eot_func = eot, undo = p, duration = 5)
        else:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+75-app.moved_down, text = 'Poison Sting Missed', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        root.after(2666, lambda e = None : self.cancel_attack(event = e))
        
    def cancel_attack(self, event):
        self.init_normal_anims()
        app.rebind_all()
        app.canvas.delete('text')
        try: 
            del app.vis_dict['Poison_Sting']
            app.canvas.delete('Poison_Sting')
        except: pass
        app.depop_context(event = None)
        app.cleanup_squares()
    
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        for c in app.coords:
            if dist(c, loc) <= 5 and app.grid[c[0]][c[1]] == '':
                mvlist.append(c)
        return mvlist
                    
class Witch(Entity):
    def __init__(self, name, img, loc, owner):
        self.actions = {'spell':self.spell, 'summon':self.summon, 'move':self.move}
#         self.spell_used = False
        self.summon_cap = 6
        self.summon_count = 0
        self.cantrip_used = False
        self.arcane_used = False
        self.summon_used = False
        self.arcane_dict = {}
        self.cantrip_dict = {}
#         self.summon_dict = {}
        self.summon_ids = 0
        self.move_type = 'normal'
        
        if name == 'Agnes_Sampson':
            self.cantrip_dict['Psionic_Push'] = (self.psionic_push)
            self.cantrip_dict['Scrye'] = (self.scrye)
            self.cantrip_dict['Energize'] = (self.energize)
            self.arcane_dict['Plague'] = (self.plague, 6)
            self.arcane_dict['Pestilence'] = (self.pestilence, 6)
            self.arcane_dict['Curse_of_Oriax'] = (self.curse_of_oriax, 3)
            self.arcane_dict['Gravity'] = (self.gravity, 5)
            self.arcane_dict["Beleth's_Command"] = (self.beleths_command, 6)
            self.str = 4
            self.agl = 3
            self.end = 4
            self.dodge = 4
            self.psyche = 6
            self.spirit = 40
            self.magick = 75
        elif name == 'Fakir_Ali':
            self.cantrip_dict['Boiling_Blood'] = (self.boiling_blood)
            self.cantrip_dict['Dark_Sun'] = (self.dark_sun)
            self.cantrip_dict['Meditate'] = (self.meditate)
            self.arcane_dict['Horrid_Wilting'] = (self.horrid_wilting,5)
            self.arcane_dict['Disintegrate'] = (self.disintegrate, 4)
            self.arcane_dict['Mummify'] = (self.mummify, 5)
            self.arcane_dict['Immolate'] = (self.immolate, 9)
            self.arcane_dict['Command_of_Osiris'] = (self.command_of_osiris, 5)
            self.str = 3
            self.agl = 4
            self.end = 6
            self.dodge = 3
            self.psyche = 5
            self.spirit = 50
            self.magick = 70
        elif name == 'Morgan_LeFay':
            self.spell_dict['Enchant'] = (self.enchant, 4)
            self.spell_dict['Counterspell'] = (self.counterspell, 3)
            self.spell_dict["Nature's_Wrath"] = (self.natures_wrath, 5)
            self.spell_dict["Noden's_Command"] = (self.nodens_command, 6)
            self.spell_dict['Wild_Hunt'] = (self.wild_hunt, 7)
            self.str = 2
            self.agl = 5
            self.end = 3
            self.dodge = 6
            self.psyche = 5
            self.spirit = 35
            self.magick = 85
            
        super().__init__(name, img, loc, owner, type = 'normal')
        
    def reset_transient_vars(self):
#         self.summon_dict = {}
        self.summon_ids = 0
#         self.spell_used = False
        self.cantrip_used = False
        self.arcane_used = False
        self.summon_used = False
        self.spirit = self.base_spirit
        self.magick = self.base_magick
        self.str_effects = []
        self.agl_effects = []
        self.end_effects = []
        self.dodge_effects = []
        self.psyche_effects = []
        self.move_used = False
        self.effects_dict = {}
        self.summon_count = 0
    
    def summon(self, event = None):
                # show vis in context_menu, summon used? eventually DEBUG fine for now
        if self.summon_used == True:
            return
        app.depop_context(event = None)
        root.bind('1', lambda e, cls = 'Warrior' : self.place_summon(e, cls))
        root.bind('2', lambda e, cls = 'Trickster' : self.place_summon(e, cls))
        root.bind('3', lambda e, cls = 'Shadow' : self.place_summon(e, cls))
        root.bind('4', lambda e, cls = 'Bard': self.place_summon(e, cls))
        root.bind('5', lambda e, cls = 'Plaguebearer' : self.place_summon(e, cls))
        b1 = tk.Button(app.context_menu, text = '1:Warrior', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Warrior' : self.place_summon(e, cls))
        b1.pack(side = 'top', pady = 2)
        app.context_buttons.append(b1)
        b2 = tk.Button(app.context_menu, text = '2:Trickster', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Trickster' : self.place_summon(e, cls))
        b2.pack(side = 'top', pady = 2)
        app.context_buttons.append(b2)
        b3 = tk.Button(app.context_menu, text = '3:Shadow', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Shadow' : self.place_summon(e, cls))
        b3.pack(side = 'top', pady = 2)
        app.context_buttons.append(b3)
        b4 = tk.Button(app.context_menu, text = '4:Bard', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Bard' : self.place_summon(e, cls))
        b4.pack(side = 'top', pady = 2)
        app.context_buttons.append(b4)
        b5 = tk.Button(app.context_menu, text = '5:Plaguebearer', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Plaguebearer' : self.place_summon(e, cls))
        b5.pack(side = 'top', pady = 2)
        app.context_buttons.append(b5)
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

    
    def place_summon(self, event, type):
        if self.summon_count >= self.summon_cap:
            return
        root.unbind('<q>')
        root.unbind('<a>')
        for x in range(1,4):
            root.unbind(str(x))
        root.bind('<q>', self.cancel_placement)
        app.depop_context(event = None)
        sqrs = [c for c in app.coords if dist(c, self.loc) == 1 and app.grid[c[0]][c[1]] == '']
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
        cmd = lambda e = None, x = cls, y = sqrs, s = grid_pos : self.place(e, summon = x, sqrs = y, sqr = s)
        root.bind('<a>', lambda e, x = cls, y = sqrs, s = grid_pos : self.place(e, x, y, s))
        b = tk.Button(app.context_menu, text = 'Place '+type, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', wraplength = 190, command = cmd)
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    def place(self, event, summon, sqrs, sqr):
        if sqr not in sqrs:
            return
        app.unbind_all()
        root.unbind('<q>')
        root.bind('<q>', app.depop_context)
        root.unbind('<a>')
        root.bind('<a>', app.populate_context)
        # SOUND
        effect1 = mixer.Sound('Sound_Effects/summon.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        # place visual summon
        app.vis_dict['Summon'] = Vis(name = 'Summon', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Summon'].img, tags = 'Summon')
        if app.active_player == 'p1':
            number = 'a' + str(self.summon_ids)
            self.summon_ids += 1
            self.summon_count += 1
        elif app.active_player == 'p2':
            number = 'b' + str(self.summon_ids)
            self.summon_ids += 1
            self.summon_count += 1
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
        s = summon(name = name, img = img, loc = sqr[:], owner = app.active_player, number = number)
        app.cleanup_squares()
        app.depop_context(event = None)
        # separate here to finish summon vis, place ent after a sec or two
        root.after(1999, lambda s = s, sqr = sqr, id = number : self.finish_place(s, sqr, id))
        
    def finish_place(self, summon, sqr, id):
        app.ent_dict[id] = summon
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = summon.img, tags = summon.tags)
        app.grid[sqr[0]][sqr[1]] = id
        app.unbind_all()
        app.rebind_all()
        self.summon_used = True
        app.canvas.delete('Summon')
        del app.vis_dict['Summon']
        
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 3)
        return [list(x) for x in set(tuple(x) for x in mvlist)]
        
    def spell(self, event = None):
#         if self.spell_used == True:
#             return
        app.depop_context(event = None)
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_spell)
        b1 = tk.Button(app.context_menu, wraplength = 190, text = 'Cantrip', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = self.cantrip)
        b1.pack(side = 'top', pady = 2)
        app.context_buttons.append(b1)
        root.bind(str(1), self.cantrip)
        b2 = tk.Button(app.context_menu, wraplength = 190, text = 'Arcane', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = self.arcane)
        b2.pack(side = 'top', pady = 2)
        app.context_buttons.append(b2)
        root.bind(str(2), self.arcane)
        
    def cantrip(self, event = None):
        if self.cantrip_used == True:
            return
#         app.unbind_all()
        app.depop_context(event = None)
        root.unbind('<q>')
        root.unbind('<a>')
        root.bind('<q>', self.cleanup_spell)
        for i, item in enumerate(self.cantrip_dict.items()):
            name = item[0]
            name = name.replace('_', ' ')
            spell = item[1]
            i += 1
            b1 = tk.Button(app.context_menu, wraplength = 190, text = str(i) +' : '+ name + ' •', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = spell)
            b1.pack(side = 'top', pady = 2)
            root.bind(str(i), spell)
            app.context_buttons.append(b1)
        b2 = tk.Button(app.context_menu, text = 'Cancel', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = self.cleanup_spell)
        b2.pack(side = 'top')
        app.context_buttons.append(b2)
        
    def arcane(self, event = None):
        if self.arcane_used == True:
            return
        app.depop_context(event = None)
        root.unbind('<q>')
        root.unbind('<a>')
        root.bind('<q>', self.cleanup_spell)
        for i, name_spellcosttuple in enumerate(self.arcane_dict.items()):
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
        self.init_normal_anims()
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        try: 
            del app.vis_dict[name]
            app.canvas.delete(name)
        except: pass
        try: app.canvas.delete('text')
        except: pass
        selected = []
        selected_vis = ''
        
        
        # SPELLS
        # available to all through powerups
    # drain_life cantrip, deal 2 to any enemy target, heal 2 spirit?
    # exchange positions of friendly summon and enemy summon, or any two summons?
    # cantrip boost stats of a summon for multiple turns, non-stacking?
    
    def summon_cenobite(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Summon_Cenobite' : self.cleanup_spell(name = name))
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 3 and app.grid[s[0]][s[1]] == '']
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_summon_cenobite(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Location', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_summon_cenobite(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_summon_cenobite(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        if app.grid[sqr[0]][sqr[1]] != '':
            return
        my_ent_names = [v.name for k,v in app.ent_dict.items() if v.owner == self.owner]
        if 'Cenobite' in my_ent_names:
            return
        self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/summon_cenobite.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Summon'] = Vis(name = 'Summon', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Summon'].img, tags = 'Summon')
        root.after(1666, lambda s = sqr : self.finish_summon_cenobite(s))
        root.after(2666, self.cleanup_summon_cenobite)
        root.after(2999, lambda name = 'Summon_Cenobite' : self.cleanup_spell(name = name))
        
    def finish_summon_cenobite(self, sqr):
        num = self.summon_ids
        self.summon_ids += 1
        if self.owner == 'p1':
            prefix = 'a'
        else:
            prefix = 'b'
        id = prefix + str(num)
        img = ImageTk.PhotoImage(Image.open('summon_imgs/Cenobite.png'))
        app.ent_dict[id] = Cenobite(name = 'Cenobite', img = img, loc = sqr[:], owner = self.owner, number = id)
        app.grid[sqr[0]][sqr[1]] = id
        
    def cleanup_summon_cenobite(self):
        del app.vis_dict['Summon']
        app.canvas.delete('Summon')
        
# Agnes' spells center around Death/Decay/Disease/Telekinetics/Cosmology
    # target summon may move again this turn
    def energize(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Energize' : self.cleanup_spell(name = name))
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_energize(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Energize', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_energize(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_energize(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if not isinstance(app.ent_dict[id], Summon):
            return
        self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/energize.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.cantrip_used = True
        app.ent_dict[id].move_used = False
        app.vis_dict['Energize'] = Vis(name = 'Energize', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Energize'].img, tags = 'Energize')
        root.after(2999, lambda  name = 'Energize' : self.cleanup_spell(name = name))
    
    # target summon gets +2 agl, +2 psyche for one turn
    def scrye(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Scrye' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 2]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_scrye(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Scrye', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_scrye(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_scrye(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if isinstance(app.ent_dict[id], Witch):
            return
        self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/scrye.ogg')
        effect1.set_volume(.08)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.cantrip_used = True
        app.vis_dict['Scrye'] = Vis(name = 'Scrye', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Scrye'].img, tags = 'Scrye')
        
        def scrye_effect(stat):
            stat += 2
            return stat
        f = scrye_effect
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].psyche_effects.append(f)
        def un(i):
            app.ent_dict[i].agl_effects.remove(scrye_effect)
            app.ent_dict[i].psyche_effects.remove(scrye_effect)
            return None
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Scrye' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Scrye', info = '+2 Agl, +2 Psyche, 1 turn', eot_func = eot, undo = p, duration = 1)
        root.after(2999, lambda  name = 'Scrye' : self.cleanup_spell(name = name))

    def foul_familiar(self, event = None):
        names = [v.name for k,v in app.ent_dict.items() if v.owner == self.owner]
        if 'Familiar_Imp' in names or 'Familiar_Homonculus' in names or 'Familiar_Pseudodragon' in names:
            return
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Foul_Familiar' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 2]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_foul_familiar(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Location', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_foul_familiar(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
    
    def do_foul_familiar(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        loc = app.grid[sqr[0]][sqr[1]]
        if loc != '':
            return
#         self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/foul_familiar.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.cantrip_used = True
        app.vis_dict['Foul_Familiar'] = Vis(name = 'Foul_Familiar', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Foul_Familiar'].img, tags = 'Foul_Familiar')
        # summon familiar based on witch
        num = self.summon_ids
        self.summon_ids += 1
        if self.owner == 'p1':
            prefix = 'a'
        else:
            prefix = 'b'
        id = prefix + str(num)
        if self.name == 'Agnes_Sampson':
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Familiar_Imp.png'))
            app.ent_dict[id] = Familiar_Imp(name = 'Familiar_Imp', img = img, loc = sqr[:], owner = self.owner, number = id)
            app.grid[sqr[0]][sqr[1]] = id
        elif self.name == 'Fakir_Ali':
            img = ImageTk.PhotoImage(Image.open('summon_imgs/Familiar_Homonculus.png'))
            app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = img, tags = id)
            app.ent_dict[id] = Familiar_Homonculus(name = 'Familiar_Homonculus', img = img, loc = sqr[:], owner = self.owner, number = id)
            app.grid[sqr[0]][sqr[1]] = id
        
        root.after(666, lambda  name = 'Foul_Familiar' : self.cleanup_spell(name = name))
    
    # create 'tomb' in current location, tomb is summon entity with no movement or attacks that doesnt count towards summon cap, teleport self to new location, only 1 tomb can exist at a time
    def entomb(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Entomb' : self.cleanup_spell(name = name))
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 7]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_entomb(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Location', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_entomb(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_entomb(self, event, sqr, sqrs):
        global selected
        names = [v.name for k,v in app.ent_dict.items() if v.name == 'Tomb' and v.owner == self.owner]
        if names != []:
            return
        if sqr not in sqrs:
            return
        loc = app.grid[sqr[0]][sqr[1]]
        if loc != '':
            return
#         self.init_cast_anims()
#         effect1 = mixer.Sound('Sound_Effects/entomb.ogg')
#         effect1.set_volume(.08)
#         sound_effects.play(effect1, 0)
        self.magick -= self.arcane_dict['Entomb'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        selected = [self.tags]
        app.canvas.delete(self.tags)
        oldloc = self.loc[:]
        # ENTOMB VIS
        app.vis_dict['Entomb'] = Vis(name = 'Entomb', loc = oldloc[:])
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = app.vis_dict['Entomb'].img, tags = 'Entomb')
        # CREATE TOMB ENTITY
        if self.owner == 'p1':
            prefix = 'a'
        else:
            prefix = 'b'
        id = prefix + str(self.summon_ids)
        self.summon_ids += 1
        img = ImageTk.PhotoImage(Image.open('summon_imgs/Tomb.png'))
        app.ent_dict[id] = Tomb(name = 'Tomb', img = img, loc = oldloc[:], owner = self.owner, number = id)
        app.grid[oldloc[0]][oldloc[1]] = id
        newloc = sqr[:]
#         app.vis_dict['Entomb'] = Vis(name = 'Entomb', loc = oldloc)
#         app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = app.vis_dict['Entomb'].img, tags = 'Entomb')
        app.canvas.create_text(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+75-app.moved_down, text = 'Entomb', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        root.after(2666, lambda loc = newloc : self.finish_entomb(loc))
        
    def finish_entomb(self, loc):
        del app.vis_dict['Entomb']
        app.canvas.delete('Entomb')
        app.vis_dict['Entomb'] = Vis(name = 'Entomb', loc = loc[:])
        app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict['Entomb'].img, tags = 'Entomb')
        selected = []
        self.loc = loc[:]
        app.grid[loc[0]][loc[1]] = self.tags
        root.after(1333, lambda x = loc[0]*100+50-app.moved_right, y = loc[1]*100+50-app.moved_down, i = self.img, t = self.tags : app.canvas.create_image(x, y, image = i, tags = t))
#         app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
        root.after(2999, lambda  name = 'Entomb' : self.cleanup_spell(name = name))
        

    # deal damage equal to spirit lost
    def vengeance(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Vengeance' : self.cleanup_spell(name = name))
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_vengeance(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Vengeance', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_vengeance(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
    
    def do_vengeance(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
#         self.init_cast_anims()

        effect1 = mixer.Sound('Sound_Effects/vengeance.ogg')
        effect1.set_volume(.08)
        sound_effects.play(effect1, 0)

        self.magick -= self.arcane_dict['Vengeance'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        d = self.base_spirit - self.spirit
        app.ent_dict[id].set_attr('spirit', -d)
        app.vis_dict['Vengeance'] = Vis(name = 'Vengeance', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Vengeance'].img, tags = 'Vengeance')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Vengeance\n'+str(d)+' Spirit', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+100-app.moved_down, text = app.ent_dict[id].name.replace('_',' ')+' Killed...', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(2999, lambda id = id: app.kill(id))
        root.after(2999, lambda  name = 'Vengeance' : self.cleanup_spell(name = name))
      
    # lose 3 spirit, all summons within range 2 may act again?
    def hatred(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Hatred' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        root.bind('<a>', self.do_hatred)
        b = tk.Button(app.context_menu, text = 'Confirm Hatred', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = self.do_hatred)
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_hatred(self, event = None):
#         self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/hatred.ogg')
        effect1.set_volume(.07)
        sound_effects.play(effect1, 0)
        self.magick -= self.arcane_dict['Hatred'][1]
        app.unbind_all()
        app.depop_context(event = None)
        self.arcane_used = True
        ents = [k for k,v in app.ent_dict.items() if v.owner == 'p1']
        for id in ents:
            sqr = app.ent_dict[id].loc[:]
            uniq_name = 'Hatred'+str(app.effects_counter)
            app.effects_counter += 1
            app.ent_dict[id].attack_used = False
            def clean_hatred(name):
                del app.vis_dict[name]
                app.canvas.delete(name)
            root.after(3666, lambda name = uniq_name : clean_hatred(name))
            app.vis_dict[uniq_name] = Vis(name = 'Hatred', loc = sqr)
            app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = 'Hatred')
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Hatred', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')

        root.after(3666, lambda  name = 'Hatred' : self.cleanup_spell(name = name))
        
        
    # target gets -2 psyche for 4 turns (does not stack), takes psyche versus end damage on cast
    def torment(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Torment' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_torment(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Torment', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_torment(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
    
    def do_torment(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
#         self.init_cast_anims()
        
        effect1 = mixer.Sound('Sound_Effects/torment.ogg')
        effect1.set_volume(.07)
        sound_effects.play(effect1, 0)
        
        self.magick -= self.arcane_dict['Torment'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        my_psyche = self.get_attr('psyche')
        tar_end = app.ent_dict[id].get_attr('end')
        d = damage(my_psyche, tar_end)
        app.ent_dict[id].set_attr('spirit', -d)
        app.vis_dict['Torment'] = Vis(name = 'Torment', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Torment'].img, tags = 'Torment')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Torment\n'+str(d)+' Spirit', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+100-app.moved_down, text = app.ent_dict[id].name.replace('_',' ')+' Killed...', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(3666, lambda id = id: app.kill(id))
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Torment' not in effs:
            def torment_effect(stat):
                stat -= 2
                if stat < 1:
                    return 1
                else:
                    return stat
            f = torment_effect
            app.ent_dict[id].psyche_effects.append(f)
            def un(i):
                app.ent_dict[i].psyche_effects.remove(torment_effect)
                return None
            p = partial(un, id)
            # EOT FUNC
            def nothing():
                return None
            eot = nothing
            n = 'Torment' + str(app.effects_counter)
            app.ent_dict[id].effects_dict[n] = Effect(name = 'Torment', info = 'Torment, -2 psyche 4 turns', eot_func = eot, undo = p, duration = 4)
        root.after(3666, lambda  name = 'Torment' : self.cleanup_spell(name = name))



    # destroy a summon you own to deal dmg to adj ents
    def pain(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Pain' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_pain(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Pain', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_pain(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_pain(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if app.ent_dict[id].owner != 'p1' or not isinstance(app.ent_dict[id], Summon):
            return
            
        effect1 = mixer.Sound('Sound_Effects/pain.ogg')
        effect1.set_volume(.07)
        sound_effects.play(effect1, 0)
            
        app.kill(id)
#         self.init_cast_anims()
        self.magick -= self.arcane_dict['Pain'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Pain'] = Vis(name = 'Pain', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Pain'].img, tags = 'Pain')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Pain', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        root.after(1777, lambda  name = 'Pain' : self.cleanup_spell(name = name))
        
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        adj_sqrs = [s for s in app.coords if dist(sqr, s) == 1 and app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        adj_ents = [app.grid[s[0]][s[1]] for s in adj_sqrs] #if app.ent_dict[app.grid[s[0]][s[1]]].owner != self.owner] 
        all_targets = adj_ents
        for id in all_targets:
            n = 'Pain' + str(app.effects_counter) # not an effect, just need unique int
            app.effects_counter += 1 # that is why this is incr manually here, no Effect init
            loc = app.ent_dict[id].loc[:]
            app.vis_dict[n] = Vis(name = 'Pain_Explode', loc = loc)
            def cleanup_vis(name):
                del app.vis_dict[name]
                app.canvas.delete(name)
            root.after(3666, lambda n = n : cleanup_vis(n))
            rand_start_anim = randrange(1,7)
            for i in range(rand_start_anim):
                app.vis_dict[n].rotate_image()
            app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict[n].img, tags = n)
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down-30, text = 'Pain', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            # Damage
            my_psyche = self.get_attr('psyche')
            tar_agl = app.ent_dict[id].get_attr('agl')
            d = damage(my_psyche, tar_agl)
            d += 9
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = str(d)+' Spirit', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+100-app.moved_down, text = app.ent_dict[id].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                root.after(3666, lambda id = id : app.kill(id))
#         root.after(3666, lambda  name = 'Pain' : self.cleanup_spell(name = name))

        
        
        
    def plague(self, event = None):
            # currently effects dif from description, one target, no to_hit check
            # attrs reduced to by 3 to a minimum of 1 (str, agl, end, dodge, psyche) lasting until 3 opp turns have passed
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Plague' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_plague(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Plague', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_plague(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_plague(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        # PLAGUE CANNOT BE STACKED WITH OTHER PLAGUES
        if 'Plague' in app.ent_dict[id].effects_dict.keys():
            return
        self.init_cast_anims()
        
        effect1 = mixer.Sound('Sound_Effects/plague.ogg')
        effect1.set_volume(2)
        sound_effects.play(effect1, 0)
        
        self.magick -= self.arcane_dict['Plague'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Plague'] = Vis(name = 'Plague', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Plague'].img, tags = 'Plague')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Plague', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO PLAGUE EFFECTS
        def plague_effect(stat):
            stat -= 2
            if stat < 1:
                return 1
            else:
                return stat
        f = plague_effect
        app.ent_dict[id].str_effects.append(f)
        app.ent_dict[id].end_effects.append(f)
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        def un(i):
            app.ent_dict[i].str_effects.remove(plague_effect)
            app.ent_dict[i].end_effects.remove(plague_effect)
            app.ent_dict[i].agl_effects.remove(plague_effect)
            app.ent_dict[i].dodge_effects.remove(plague_effect)
            return None
        p = partial(un, id)
        def nothing():
            return None
        eot = nothing
        n = 'Plague' + str(app.effects_counter)
        app.ent_dict[id].effects_dict['Plague'] = Effect(name = 'Plague', info = 'Plague\n Stats reduced by 2 for 3 turns', eot_func = eot, undo = p, duration = 3)
        root.after(3666, lambda  name = 'Plague' : self.cleanup_spell(name = name))
            
    # PSIONIC PUSH
    def psionic_push(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Psionic_Push' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_psionic_push(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Psionic Push', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_psionic_push(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_psionic_push(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        # cannot target large
        if app.ent_dict[id].type == 'large' or app.ent_dict[id].immovable == True:
            return
        app.depop_context(event = None)
        app.cleanup_squares()
        loc = app.ent_dict[id].loc[:]
        ps = []
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        # make recursive for variable distance
#         def sqrs_until_obs(start, next, dist):
        ps.append(loc)
        for c in app.coords:
            if c[0] == (loc[0] + 1) and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                ps.append(c)
                n = [loc[0]+2, loc[1]]
                if n in app.coords:
                    if n[0] == (loc[0] + 2) and n[1] == loc[1] and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == (loc[0] - 1) and c[1] == loc[1] and app.grid[c[0]][c[1]] == '':
                n = [loc[0]-2, loc[1]]
                ps.append(c)
                if n in app.coords:
                    if n[0] == (loc[0] - 2) and n[1] == loc[1] and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == loc[0] and c[1] == (loc[1] + 1) and app.grid[c[0]][c[1]] == '':
                n = [loc[0], loc[1]+2]
                ps.append(c)
                if n in app.coords:
                    if n[0] == loc[0] and n[1] == (loc[1] + 2) and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
            elif c[0] == loc[0] and c[1] == (loc[1] - 1) and app.grid[c[0]][c[1]] == '':
                n = [loc[0], loc[1]-2]
                ps.append(c)
                if n in app.coords:
                    if n[0] == loc[0] and n[1] == (loc[1] - 2) and app.grid[n[0]][n[1]] == '':
                        ps.append(n)
        app.animate_squares(ps)
        root.bind('<a>', lambda e, id = id, s = grid_pos, sqrs = ps : self.choose_psi_square(event = e, id = id, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Square to Push', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, id = id, s = grid_pos, sqrs = ps : self.choose_psi_square(e, id, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
            
    def choose_psi_square(self, event, id, sqr, sqrs):
        global selected, selected_vis
        if sqr not in sqrs:
            return
        self.cantrip_used = True
        self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/psionic_push.ogg')
        effect1.set_volume(.3)
        sound_effects.play(effect1, 0)
#         self.magick -= self.cantrip_dict['Psionic_Push'][1]
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
            selected = [id]
            selected_vis = 'Psionic_Push'
        def psi_move_loop(vis, ent, x, y, endx, endy, sqr, start_sqr):
            if x % 25 == 0 and y % 25 == 0:
                app.vis_dict[vis].rotate_image()
                app.ent_dict[ent].rotate_image()
                app.canvas.delete(vis)
                app.canvas.delete(ent)
                app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = 'Psionic_Push')
                app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
            if x > endx:
                x -= 10
                app.canvas.move(vis, -10, 0)
                app.canvas.move(ent, -10, 0)
            elif x < endx: 
                x += 10
                app.canvas.move(vis, 10, 0)
                app.canvas.move(ent, 10, 0)
            if y > endy: 
                y -= 10
                app.canvas.move(vis, 0, -10)
                app.canvas.move(ent, 0, -10)
            elif y < endy: 
                y += 10
                app.canvas.move(vis, 0, 10)
                app.canvas.move(ent, 0, 10)
            app.canvas.tag_raise(vis)
            try: app.canvas.tag_lower(app.ent_dict[ent].tags, 'large')
            except: pass
            app.canvas.tag_lower(app.ent_dict[ent].tags, 'maptop')
            if x == endx and y == endy:
                root.after(666, lambda e = ent, s = sqr, ss = start_sqr : self.finish_psionic_push(e, s, ss))
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
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        adj_sqrs = [c for c in app.coords if dist(c, end_loc) == 1]
        adj_ents = []
        for s in adj_sqrs:
            if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block':
                adj_ents.append(app.grid[s[0]][s[1]])
        if adj_ents != []:
            # hit tar and adj_ents
            adj_ents.append(tar)
            tar_str = app.ent_dict[tar].get_attr('str')
            for ent in adj_ents:
                if app.ent_dict[ent].attr_check('agl') == False:
                    d = damage(tar_str, app.ent_dict[ent].get_attr('end'))
                    app.ent_dict[ent].set_attr('spirit', -d)
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = str(d) + ' Spirit', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                    if app.ent_dict[ent].spirit <= 0:
                        app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+100-app.moved_down, text = app.ent_dict[ent].name + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        root.after(1333, app.kill(ent))
                # MISS
                else:
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = 'Agility\nSave',justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(2666, lambda s = 'Psionic_Push' : self.cleanup_spell(name = s))
        else:
            root.after(2666, lambda s = 'Psionic_Push' : self.cleanup_spell(name = s))
        
        
    def pestilence(self, event = None):
        # AOE damage in straight line
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 3]
        for s in sqrs[:]:
            if abs(s[0]-self.loc[0]) == 1 and abs(s[1]-self.loc[1]) == 1:
                sqrs.remove(s)
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_pestilence(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Pestilence', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_pestilence(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_pestilence(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        if app.grid[sqr[0]][sqr[1]] == '' or app.grid[sqr[0]][sqr[1]] == 'block':
            return
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        
        effect1 = mixer.Sound('Sound_Effects/pestilence.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        
        self.arcane_used = True
        self.magick -= self.arcane_dict['Pestilence'][1]
        self.init_cast_anims()
        # get ent and all adj ents
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        target = app.grid[sqr[0]][sqr[1]]
        all_targets = [target]
        all_squares = []
        # get direction and sign
        if abs(sqr[0]-self.loc[0]) > abs(sqr[1]-self.loc[1]):# direction is left/right
            if sqr[0] > self.loc[0]:# sign is pos
                # get ents in this direction
                for c in app.coords:
                    if sqr[0] < c[0] <= sqr[0]+4 and c[1] == sqr[1]:
                        all_squares.append(c)
            else:#sign is neg
                for c in app.coords:
                    if sqr[0] > c[0] >= sqr[0]-4 and c[1] == sqr[1]:
                        all_squares.append(c)
        else:#direction is up/down
            if sqr[1] > self.loc[1]:# sign is pos
                # get ents in this direction
                for c in app.coords:
                    if sqr[1] < c[1] <= sqr[1]+4 and c[0] == sqr[0]:
                        all_squares.append(c)
            else:#sign is neg
                for c in app.coords:
                    if sqr[1] > c[1] >= sqr[1]-4 and c[0] == sqr[0]:
                        all_squares.append(c)
        all_targets += [app.grid[s[0]][s[1]] for s in all_squares if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        
        # Change to 'rolling vis' start first, delay, start next
        for id in all_targets:
            n = 'Pestilence' + str(app.effects_counter) # not an effect, just need unique int
            app.effects_counter += 1 # that is why this is incr manually here, no Effect init
            loc = app.ent_dict[id].loc[:]
            app.vis_dict[n] = Vis(name = 'Pestilence', loc = loc)
            def cleanup_vis(name):
                del app.vis_dict[name]
                app.canvas.delete(name)
            root.after(3666, lambda n = n : cleanup_vis(n))
            rand_start_anim = randrange(1,7)
            for i in range(rand_start_anim):
                app.vis_dict[n].rotate_image()
            app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict[n].img, tags = n)
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down-20, text = 'Pestilence', justify ='center', font = ('Andale Mono', 14), fill = 'gray75', tags = 'text')
            # DAMAGE
            my_psyche = self.get_attr('psyche')
            tar_psyche = app.ent_dict[id].get_attr('psyche')
            # HACK
            #d = damage(my_psyche, tar_psyche)
            d = 666
            #
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+65-app.moved_down, text = str(d)+'\nSpirit', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+100-app.moved_down, text = app.ent_dict[id].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                root.after(3666, lambda id = id : app.kill(id))
        root.after(3666, lambda  name = 'Pestilence' : self.cleanup_spell(name = name))
    
    
    
        
    # CURSE OF ORIAX
    def curse_of_oriax(self, event = None):
            # Any target is inflicted with 'curse', while cursed takes 2 spirit damage at end of every owner's turn and minus 1 to every stat (not spirit, magick, movement)
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 3]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_curse_of_oriax(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Curse of Oriax', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_curse_of_oriax(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_curse_of_oriax(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        id = app.current_pos()
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Curse_of_Oriax' in effs:
            return
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.arcane_dict['Curse_of_Oriax'][1]
        
        effect1 = mixer.Sound('Sound_Effects/curse_of_oriax.ogg')
        effect1.set_volume(.9)
        sound_effects.play(effect1, 0)
        
        self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Curse_of_Oriax'] = Vis(name = 'Curse_of_Oriax', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Curse_of_Oriax'].img, tags = 'Curse_of_Oriax')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+100-app.moved_down, text = 'Curse\nof\nOriax', justify = 'center', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
        # DO Curse_of_Oriax EFFECTS
        def curse_of_oriax_effect(stat):
            stat -= 1
            if stat < 1:
                return 1
            else:
                return stat
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
            return None
        p = partial(un, id)
        # EOT FUNC
        def take_2(tar):
            app.get_focus(tar)
            app.ent_dict[tar].set_attr('spirit', -2)
            app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+50-app.moved_down, text = '2 Spirit\nCurse', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            if app.ent_dict[tar].spirit <= 0:
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            return 'Not None'
            
        eot = partial(take_2, id)
        n = 'Curse_of_Oriax' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Curse_of_Oriax', info = 'Curse_of_Oriax\n Stats reduced by 1 for 3 turns\n2 Spirit damage per turn', eot_func = eot, undo = p, duration = 3)
        root.after(3666, lambda  name = 'Curse_of_Oriax' : self.cleanup_spell(name = name))
        
    def gravity(self, event = None):
        # consider 'being moved' through means other than movement ends effect
        # an effect that overwrites the ent.legal_moves() method to return []
        # undo removes the overwrite
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_gravity(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Gravity', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_gravity(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_gravity(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Gravity' in effs:
            return
        self.magick -= self.arcane_dict['Gravity'][1]
        
        effect1 = mixer.Sound('Sound_Effects/gravity.ogg')
        effect1.set_volume(.9)
        sound_effects.play(effect1, 0)
        
        self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Gravity'] = Vis(name = 'Gravity', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Gravity'].img, tags = 'Gravity')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Gravity', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO gravity EFFECTS
        def gravity_effect(stat):
            stat -= 1
            if stat < 1:
                return 1
            else:
                return stat
        f = gravity_effect
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        def gravity():# REPLACE CLASS MOVEMENT WITH NOTHING
            return []
        app.ent_dict[id].legal_moves = gravity
        def un(i):
            app.ent_dict[i].agl_effects.remove(gravity_effect)
            app.ent_dict[i].dodge_effects.remove(gravity_effect)
            p = partial(app.ent_dict[i].__class__.legal_moves, app.ent_dict[i]) #   PUT BACK CLASS METHOD MOVEMENT
            app.ent_dict[i].legal_moves = p
            return None
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Gravity' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Gravity', info = 'Gravity\nCannot move and agl and dodge reduced by 1 for 2 turns', eot_func = eot, undo = p, duration = 2)
        root.after(3666, lambda  name = 'Gravity' : self.cleanup_spell(name = name))
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # self cannot move (lasts 2 turns, cannot use if moved this turn), adj ents take 9 spirit, self gets +3 psyche, +3 end (2 turns) 
    def beleths_command(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
        root.bind('<a>', self.do_beleths_command)
        b = tk.Button(app.context_menu, text = "Confirm Beleth's Command", wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = self.do_beleths_command)
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_beleths_command(self, event = None):
        if self.move_used == True:
            return
        id = self.name
        sqr = self.loc[:]
        self.magick -= self.arcane_dict["Beleth's_Command"][1]
        # SOUND
        effect1 = mixer.Sound('Sound_Effects/beleths_command.ogg')
        effect1.set_volume(.7)
        sound_effects.play(effect1, 0)
        self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict["Beleth's_Command"] = Vis(name = "Beleth's_Command", loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict["Beleth's_Command"].img, tags = "Beleth's_Command")
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = "Beleth's_Command", justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # BURN AT STAKE LOOP
        selected_vis = "Beleth's_Command"
        x = sqr[0]*100+50-app.moved_right
        y = sqr[1]*100+50-app.moved_down
        def beleths_loop(timeout):
            if timeout > 0:
                app.vis_dict["Beleth's_Command"].rotate_image()
                app.canvas.delete("Beleth's_Command")
                app.canvas.create_image(x, y, image = app.vis_dict["Beleth's_Command"].img, tags = "Beleth's_Command")
                app.canvas.tag_lower("Beleth's_Command", self.tags)
                timeout -= 1
                root.after(99, lambda t = timeout : beleths_loop(t))
        beleths_loop(36)
        # Adj ents take 9 spirit
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(sqr, s) == 1]
        ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        for e in ents:
            s = app.ent_dict[e].loc[:]
            app.ent_dict[e].set_attr('spirit', -9)
            name = app.ent_dict[e].name
            uniq_name = 'Immolate'+str(app.effects_counter)
            app.effects_counter += 1
            app.vis_dict[uniq_name] = Vis(name = 'Immolate', loc = s) # using Immolate animations
            app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = "Beleth's_Command")
            app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+80-app.moved_down, text = "9 Spirit", justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            if app.ent_dict[e].spirit <= 0:
                app.canvas.create_text(s[0]*100+50-app.moved_right, s[1]*100+95-app.moved_down, text = name+' Killed...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                root.after(2666, lambda id = e : app.kill(id))
            def clean_beleths_command(n):
                del app.vis_dict[n]
                app.canvas.delete(n)
            root.after(3666, lambda n = uniq_name : clean_beleths_command(n))
        # DO Beleth's Command EFFECTS
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if "Beleth's_Command" not in effs:
            def beleths_command_effect(stat):
                stat += 2
                return stat
            f = beleths_command_effect
            app.ent_dict[id].end_effects.append(f)
            app.ent_dict[id].psyche_effects.append(f)
            def beleth():# REPLACE CLASS MOVEMENT WITH NOTHING
                return []
            app.ent_dict[id].legal_moves = beleth
            def un(i):
                app.ent_dict[i].end_effects.remove(beleths_command_effect)
                app.ent_dict[i].psyche_effects.remove(beleths_command_effect)
                p = partial(app.ent_dict[i].__class__.legal_moves, app.ent_dict[i]) #   PUT BACK CLASS METHOD MOVEMENT
                app.ent_dict[i].legal_moves = p
                return None
            p = partial(un, id)
            # EOT FUNC
            def nothing():
                return None
            eot = nothing
            app.ent_dict[id].effects_dict["Beleth's_Command"] = Effect(name = "Beleth's_Command", info = 'Cannot move, +3 psyche and end', eot_func = eot, undo = p, duration = 2)
        root.after(3666, lambda  name = "Beleth's_Command" : self.cleanup_spell(name = name))
        
        
# FAKIR ALI SPELLS
        # Ali's spells center around Heat/Fire/Resistance/Mummification
    def meditate(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Meditate' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
#         sqrs = [s for s in coords if dist(self.loc, s) <= 4]
#         app.animate_squares(sqrs)
        root.bind('<a>', self.do_meditate)
        b = tk.Button(app.context_menu, text = 'Confirm Meditate', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None : self.do_meditate(e))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_meditate(self, event):
#         self.init_cast_anims()
        effect1 = mixer.Sound('Sound_Effects/meditate.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.unbind_all()
        app.depop_context(event = None)
        self.cantrip_used = True
        id = self.name
        sqr = self.loc[:]
        app.vis_dict['Meditate'] = Vis(name = 'Meditate', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Meditate'].img, tags = 'Meditate')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Meditate', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Meditate EFFECTS
        def meditate_effect(stat):
            stat += 2
            return stat
        f = meditate_effect
        app.ent_dict[id].psyche_effects.append(f)
############################################
        def meditate_move():# REPLACE CLASS MOVEMENT
            loc = self.loc
            mvlist = []
            def findall(loc, start, distance):
                if start > distance:
                    return
                adj = [c for c in app.coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
                for s in adj:
                    mvlist.append(s)
                    findall(s, start+1, distance)
            findall(loc, 1, 5)
            return [list(x) for x in set(tuple(x) for x in mvlist)]
#####################################
        app.ent_dict[id].legal_moves = meditate_move
        def un(i):
            app.ent_dict[i].psyche_effects.remove(meditate_effect)
            p = partial(app.ent_dict[i].__class__.legal_moves, app.ent_dict[i]) #   PUT BACK CLASS METHOD MOVEMENT
            app.ent_dict[i].legal_moves = p
            return None
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Meditate' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Meditate', info = 'Meditate\n+2 Psyche\n+2 Move', eot_func = eot, undo = p, duration = 1)
        root.after(3666, lambda  name = 'Meditate' : self.cleanup_spell(name = name))
        
        
        
    def horrid_wilting(self, event = None):
        # make attack (psyche versus str) spirit damage, on any target within range 4 and all adjacent enemy units
        app.depop_context(event = None)
        root.bind('<q>', lambda name = 'Horrid_Wilting' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_horrid_wilting(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Horrid Wilting', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_horrid_wilting(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_horrid_wilting(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        if app.grid[sqr[0]][sqr[1]] == '' or app.grid[sqr[0]][sqr[1]] == 'block':
            return
        effect1 = mixer.Sound('Sound_Effects/horrid_wilting.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        self.arcane_used = True
        self.magick -= self.arcane_dict['Horrid_Wilting'][1]
        # get ent and all adj ents
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        adj_sqrs = [s for s in app.coords if dist(sqr, s) == 1 and app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        adj_ents = [app.grid[s[0]][s[1]] for s in adj_sqrs] #if app.ent_dict[app.grid[s[0]][s[1]]].owner != self.owner] 
        all_targets = adj_ents + [app.grid[sqr[0]][sqr[1]]]
        for id in all_targets:
            n = 'Horrid_Wilting' + str(app.effects_counter) # not an effect, just need unique int
            app.effects_counter += 1 # that is why this is incr manually here, no Effect init
            loc = app.ent_dict[id].loc[:]
            app.vis_dict[n] = Vis(name = 'Horrid_Wilting', loc = loc)
            def cleanup_vis(name):
                del app.vis_dict[name]
                app.canvas.delete(name)
            root.after(3666, lambda n = n : cleanup_vis(n))
            rand_start_anim = randrange(1,7)
            for i in range(rand_start_anim):
                app.vis_dict[n].rotate_image()
            app.canvas.create_image(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down, image = app.vis_dict[n].img, tags = n)
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+50-app.moved_down-30, text = 'Horrid Wilting', justify ='center', font = ('Andale Mono', 13), fill = 'wheat2', tags = 'text')
            # DAMAGE
            my_psyche = self.get_attr('psyche')
            tar_end = app.ent_dict[id].get_attr('end')
            d = damage(my_psyche, tar_end)
            app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+75-app.moved_down, text = str(d)+' Spirit', justify ='center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(loc[0]*100+50-app.moved_right, loc[1]*100+100-app.moved_down, text = app.ent_dict[id].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
                root.after(3666, lambda id = id : app.kill(id))
        root.after(3666, lambda  name = 'Horrid_Wilting' : self.cleanup_spell(name = name))
        
        
    def boiling_blood(self, event = None):
        ##
        app.depop_context(event = None)
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', lambda name = 'Boiling_Blood' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) == 1]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_boiling_blood(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Boiling Blood', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_boiling_blood(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_boiling_blood(self, event, sqr, sqrs):
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if id == '' or id == 'block':
            return
        if not isinstance(app.ent_dict[id], Warrior):
            return
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Boiling_Blood' in effs:
            return
        effect1 = mixer.Sound('Sound_Effects/boiling_blood.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        self.cantrip_used = True
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        app.vis_dict['Boiling_Blood'] = Vis(name = 'Boiling_Blood', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Boiling_Blood'].img, tags = 'Boiling_Blood')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Boiling\nBlood', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Boiling_Blood EFFECTS
        def boiling_blood_str_effect(stat):
            stat += 5
            return stat
        def boiling_blood_end_effect(stat):
            return 1
        app.ent_dict[id].str_effects.append(boiling_blood_str_effect)
        app.ent_dict[id].end_effects.append(boiling_blood_end_effect)
        def un(i):
            app.ent_dict[i].str_effects.remove(boiling_blood_str_effect)
            app.ent_dict[i].end_effects.remove(boiling_blood_end_effect)
            return None
        p = partial(un, id)
        # EOT FUNC
        def take_1(tar):
            app.get_focus(tar)
            app.ent_dict[tar].set_attr('spirit', -1)
            app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+50-app.moved_down, text = '1 Spirit\nBoiling Blood', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            if app.ent_dict[tar].spirit <= 0:
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            return 'Not None'
            
        eot = partial(take_1, id)
        n = 'Boiling_Blood' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Boiling_Blood', info = 'Boiling_Blood\n+5 Str, End reduced to 1\n1 Spirit damage per turn', eot_func = eot, undo = p, duration = 4)
        root.after(3666, lambda  name = 'Boiling_Blood' : self.cleanup_spell(name = name))
        
    
        
    def dark_sun(self, event = None):
        # Any one 'shadow' summon within range 2 gets an extra attack if they have already attacked once this turn
        app.depop_context(event = None)
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', lambda name = 'Dark_Sun' : self.cleanup_spell(name = name))
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 2]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_dark_sun(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Dark Sun', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_dark_sun(e, s, sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_dark_sun(self, event, sqr, sqrs):
        global selected_vis
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        if not isinstance(app.ent_dict[id], Shadow):
            return
        effect1 = mixer.Sound('Sound_Effects/dark_sun.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        self.cantrip_used = True
        app.depop_context(event = None)
        app.unbind_all()
        app.cleanup_squares()
        app.ent_dict[id].attack_used = False
        app.vis_dict['Dark_Sun'] = Vis(name = 'Dark_Sun', loc = sqr[:]) #[sqr[0],sqr[1]-1])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Dark_Sun'].img, tags = 'Dark_Sun')
        app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+50-app.moved_down+40, text = 'Dark Sun', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        selected_vis = 'Dark_Sun'
        def dark_sun_loop(starty, endy, x):
            if starty > endy:
                app.vis_dict['Dark_Sun'].rotate_image()
                app.canvas.delete('Dark_Sun')
                app.canvas.create_image(x, starty, image = app.vis_dict['Dark_Sun'].img, tags = 'Dark_Sun')
                starty -= 10
                app.canvas.move('Dark_Sun', 0, -10)
                app.canvas.tag_raise('Dark_Sun')
            if starty == endy:
                root.after(1333, lambda  name = 'Dark_Sun' : self.cleanup_spell(name = name))
            else:
                root.after(299, lambda sy = starty, ey = endy, x = x : dark_sun_loop(sy, ey, x))
                
        locy = sqr[1]*100+70-app.moved_down
        locx = sqr[0]*100+50-app.moved_right
        dark_sun_loop(locy, locy-90, locx)
        
        
    def mummify(self, event = None):
        # +9 to endurance and target cannot move any target 3 turns
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 3]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_mummify(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Mummify', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_mummify(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_mummify(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Mummify' in effs:
            return
        effect1 = mixer.Sound('Sound_Effects/mummify.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        self.magick -= self.arcane_dict['Mummify'][1]
#         self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Mummify'] = Vis(name = 'Mummify', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Mummify'].img, tags = 'Mummify')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+95-app.moved_down, text = 'Mummify', justify = 'center', font = ('Andale Mono', 14), fill = 'darkgoldenrod', tags = 'text')
        # DO Mummify EFFECTS
        def mummify_effect(stat):
            stat += 9
            return stat
        f = mummify_effect
        app.ent_dict[id].end_effects.append(f)
        def un(i):
            for ef in app.ent_dict[i].end_effects[:]:
                    if ef.__name__ == 'mummify_effect':
                        app.ent_dict[i].end_effects.remove(ef)
            p = partial(app.ent_dict[i].__class__.legal_moves, app.ent_dict[i]) #   PUT BACK CLASS METHOD MOVEMENT
            app.ent_dict[i].legal_moves = p
            return None
        def mummifier():# REPLACE CLASS MOVEMENT WITH NOTHING
            return []
        app.ent_dict[id].legal_moves = mummifier
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Mummify' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Mummify', info = 'Mummify\n+9 End and cannot move', eot_func = eot, undo = p, duration = 3)
        root.after(3666, lambda  name = 'Mummify' : self.cleanup_spell(name = name))
        
        
        
    def immolate(self, event = None):
        # high psyche damage one target
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 2]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_immolate(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Immolate', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_immolate(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_immolate(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        effect1 = mixer.Sound('Sound_Effects/immolate.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
        id = app.grid[sqr[0]][sqr[1]]
        self.magick -= self.arcane_dict['Immolate'][1]
#         self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Immolate'] = Vis(name = 'Immolate', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Immolate'].img, tags = 'Immolate')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+25-app.moved_down, text = 'Immolate', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        my_psyche = self.get_attr('psyche')
        tar_psyche = app.ent_dict[id].get_attr('psyche')
        d = damage(my_psyche, tar_psyche)
        d += 5
        app.ent_dict[id].set_attr('spirit', -d)
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+80-app.moved_down, text = str(d)+' Spirit', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
        if app.ent_dict[id].spirit <= 0:
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+95-app.moved_down, text = app.ent_dict[id].name.replace('_', ' ')+' Killed...', justify = 'center', font = ('Andale Mono', 13), fill = 'white', tags = 'text')
            root.after(3111, lambda id = id : app.kill(id))
                
        root.after(3111, lambda  name = 'Immolate' : self.cleanup_spell(name = name))
        
        
    def disintegrate(self, event = None):
        # target gets -1 to all stats every turn (cumulative) and takes 1 spirit per turn
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, s = grid_pos, sqrs = sqrs : self.do_disintegrate(event = e, sqr = s, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Choose Target For Disintegrate', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, s = grid_pos, sqrs = sqrs : self.do_disintegrate(e, s, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_disintegrate(self, event, sqr, sqrs):
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        id = app.grid[sqr[0]][sqr[1]]
        effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
        if 'Disintegrate' in effs:
            return
        self.magick -= self.arcane_dict['Disintegrate'][1]
        effect1 = mixer.Sound('Sound_Effects/disintegrate.ogg')
        effect1.set_volume(1)
        sound_effects.play(effect1, 0)
#         self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        app.vis_dict['Disintegrate'] = Vis(name = 'Disintegrate', loc = sqr[:])
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Disintegrate'].img, tags = 'Disintegrate')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Disintegrate', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Disintegrate EFFECTS
        def disintegrate_effect(stat):
            stat -= 1
            if stat < 1:
                return 1
            else:
                return stat
        f = disintegrate_effect
        app.ent_dict[id].str_effects.append(f)
        app.ent_dict[id].end_effects.append(f)
        app.ent_dict[id].agl_effects.append(f)
        app.ent_dict[id].dodge_effects.append(f)
        app.ent_dict[id].psyche_effects.append(f)
        def un(i):
            for ef in app.ent_dict[i].str_effects[:]:
                    if ef.__name__ == 'disintegrate_effect':
                        app.ent_dict[i].str_effects.remove(ef)
            for ef in app.ent_dict[i].end_effects[:]:
                    if ef.__name__ == 'disintegrate_effect':
                        app.ent_dict[i].end_effects.remove(ef)
            for ef in app.ent_dict[i].agl_effects[:]:
                    if ef.__name__ == 'disintegrate_effect':
                        app.ent_dict[i].agl_effects.remove(ef)
            for ef in app.ent_dict[i].dodge_effects[:]:
                    if ef.__name__ == 'disintegrate_effect':
                        app.ent_dict[i].dodge_effects.remove(ef)
            for ef in app.ent_dict[i].psyche_effects[:]:
                    if ef.__name__ == 'disintegrate_effect':
                        app.ent_dict[i].psyche_effects.remove(ef)
            return None
                
        p = partial(un, id)
        # EOT FUNC
        def disint(tar):
            def disintegrate_effect(stat):
                stat -= 1
                if stat < 1:
                    return 1
                else:
                    return stat
            f = disintegrate_effect
            app.ent_dict[tar].str_effects.append(f)
            app.ent_dict[tar].end_effects.append(f)
            app.ent_dict[tar].agl_effects.append(f)
            app.ent_dict[tar].dodge_effects.append(f)
            app.ent_dict[tar].psyche_effects.append(f)
            
            app.get_focus(tar)
            app.ent_dict[tar].set_attr('spirit', -1)
            app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+50-app.moved_down, text = '1 Spirit\nDisintegrate', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            if app.ent_dict[tar].spirit <= 0:
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name.replace('_',' ') + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            return 'Not None'
            
        eot = partial(disint, id)
        n = 'Disintegrate' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Disintegrate', info = 'Disintegrate\n Stats reduced by 1 every turn for 3 turns\n1 Spirit damage per turn', eot_func = eot, undo = p, duration = 3)
        root.after(3111, lambda  name = 'Disintegrate' : self.cleanup_spell(name = name))
        
        
        
    # all friendly ents within range 3 get +1 all attrs and heals 1 spirit, all enemy ents get -1 all attrs and loses 1 spirit, lasts 3 turns, does not stack
    def command_of_osiris(self, event = None):
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_spell)
#         coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in app.coords if dist(self.loc, s) <= 4]
        app.animate_squares(sqrs)
        root.bind('<a>', lambda e, sqrs = sqrs : self.do_command_of_osiris(event = e, sqrs = sqrs))
        b = tk.Button(app.context_menu, text = 'Confirm Command of Osiris', wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = lambda e = None, sqrs = sqrs : self.do_command_of_osiris(e, sqrs = sqrs))
        b.pack(side = 'top', pady = 2)
        app.context_buttons.append(b)
        
    def do_command_of_osiris(self, event, sqrs):
        self.magick -= self.arcane_dict['Disintegrate'][1]
#         self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.arcane_used = True
        ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
        friendly_ents = [e for e in ents if app.ent_dict[e].owner == self.owner]
        enemy_ents = [e for e in ents if app.ent_dict[e].owner != self.owner]
        # SUN VIS
        app.vis_dict['Osiris_Sun'] = Vis(name = 'Osiris_Sun', loc = [self.loc[0],self.loc[1]-4])
        app.canvas.create_image(self.loc[0]*100+50-app.moved_right, (self.loc[1]-4)*100+50-app.moved_down, image = app.vis_dict['Osiris_Sun'].img, tags = 'Command_of_Osiris')
        app.canvas.create_text(self.loc[0]*100+50-app.moved_right, (self.loc[1]-3)*100+95-app.moved_down, text = 'Command of Osiris', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        def cleanup_sun():
            del app.vis_dict['Osiris_Sun']
            app.canvas.delete('Osiris_Sun')
        root.after(3666, cleanup_sun)
        # FRIENDLY ENTS
        for id in friendly_ents:
            effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
            if 'Command_of_Osiris' in effs:
                continue
            sqr = app.ent_dict[id].loc[:]
            uniq_name = 'Command_of_Osiris' + str(app.effects_counter)
            app.effects_counter += 1
            app.vis_dict[uniq_name] = Vis(name = 'Command_of_Osiris', loc = sqr)
            app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = 'Command_of_Osiris')
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = '+1 Stats\n+1 Spirit', justify = 'center', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
            # CLEANUP UNIQUE VIS
            def cleanup_osiris(n):
                del app.vis_dict[n]
                app.canvas.delete(n)
            root.after(3666, lambda n = uniq_name : cleanup_osiris(n))
            # SPIRIT
            if app.ent_dict[id].spirit < app.ent_dict[id].base_spirit:
                app.ent_dict[id].set_attr('spirit', 1)
            # DO Command of Osiris EFFECTS
            def osiris_effect(stat):
                stat += 1
                return stat
            f = osiris_effect
            app.ent_dict[id].str_effects.append(f)
            app.ent_dict[id].end_effects.append(f)
            app.ent_dict[id].agl_effects.append(f)
            app.ent_dict[id].dodge_effects.append(f)
            app.ent_dict[id].psyche_effects.append(f)
            def un(i):
                for ef in app.ent_dict[i].str_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].str_effects.remove(ef)
                for ef in app.ent_dict[i].end_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].end_effects.remove(ef)
                for ef in app.ent_dict[i].agl_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].agl_effects.remove(ef)
                for ef in app.ent_dict[i].dodge_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].dodge_effects.remove(ef)
                for ef in app.ent_dict[i].psyche_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].psyche_effects.remove(ef)
                return None
            p = partial(un, id)
            # EOT FUNC
            def nothing():
                return None
            eot = nothing
            n = 'Command_of_Osiris' + str(app.effects_counter)
            app.ent_dict[id].effects_dict[n] = Effect(name = 'Command_of_Osiris', info = '+1 attrs, spirit friendly ents, -1 attrs, spirit enemy ents', eot_func = eot, undo = p, duration = 3)
        #  ENEMY ENTS
        for id in enemy_ents:
            effs = [v.name for k,v in app.ent_dict[id].effects_dict.items()]
            if 'Command_of_Osiris' in effs:
                continue
            sqr = app.ent_dict[id].loc[:]
            uniq_name = 'Command_of_Osiris' + str(app.effects_counter)
            app.effects_counter += 1
            app.vis_dict[uniq_name] = Vis(name = 'Command_of_Osiris', loc = sqr)
            app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict[uniq_name].img, tags = 'Command_of_Osiris')
            app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = '-1 Stats\n-1 Spirit', justify = 'center', font = ('Andale Mono', 12), fill = 'white', tags = 'text')
            # CLEANUP UNIQUE VIS
            def cleanup_osiris(n):
                del app.vis_dict[n]
                app.canvas.delete(n)
            root.after(3666, lambda n = uniq_name : cleanup_osiris(n))
            # SPIRIT
            app.ent_dict[id].set_attr('spirit', -1)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+100-app.moved_down, text = app.ent_dict[id].name+' Killed...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                root.after(2666, lambda id = id : app.kill(id))
            # DO Command of Osiris EFFECTS
            def osiris_effect(stat):
                stat -= 1
                if stat < 1:
                    return 1
                else:
                    return stat
            f = osiris_effect
            app.ent_dict[id].str_effects.append(f)
            app.ent_dict[id].end_effects.append(f)
            app.ent_dict[id].agl_effects.append(f)
            app.ent_dict[id].dodge_effects.append(f)
            app.ent_dict[id].psyche_effects.append(f)
            def un(i):
                for ef in app.ent_dict[i].str_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].str_effects.remove(ef)
                for ef in app.ent_dict[i].end_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].end_effects.remove(ef)
                for ef in app.ent_dict[i].agl_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].agl_effects.remove(ef)
                for ef in app.ent_dict[i].dodge_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].dodge_effects.remove(ef)
                for ef in app.ent_dict[i].psyche_effects[:]:
                        if ef.__name__ == 'osiris_effect':
                            app.ent_dict[i].psyche_effects.remove(ef)
                return None
            p = partial(un, id)
            # EOT FUNC
            def nothing():
                return None
            eot = nothing
            n = 'Command_of_Osiris' + str(app.effects_counter)
            app.ent_dict[id].effects_dict[n] = Effect(name = 'Command_of_Osiris', info = '+1 attrs, spirit friendly ents, -1 attrs, spirit enemy ents', eot_func = eot, undo = p, duration = 3)
            
            
        root.after(3666, lambda  name = 'Command_of_Osiris' : self.cleanup_spell(name = name))
        print('command_of_osiris')
        
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
        
    
    
class VerticalScrolledFrame(tk.Frame): 
    '''
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    '''
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, relief = 'raised', troughcolor = 'black', highlightbackground = 'black', width = 13)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, bg = 'black',
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)
        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window = interior, anchor = 'nw')
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.ent_dict = {}
        self.sqr_dict = {}
        self.vis_dict = {}
        self.image_holder = []
        self.global_effects_dict = {}
        self.active_player = 'p1'
        self.num_players = 1
        self.moved_right = 0
        self.moved_down = 0
        self.context_buttons = []
        self.help_buttons = []
        # list to hold entity that is being animated as 'attacking'
        self.attacking = []
        self.effects_counter = 0 # used for uniquely naming Effects with the same prefix/name
        self.p1_witch = ''
        self.p2_witch = ''
        self.two_player_map_num = 0
        self.turn_counter = 0
        self.choose_num_players()
        
        # Luminari 280
        # Herculanum 240
        # Papyrus 240
    def choose_num_players(self):
#         background_music.music.load('Ove Melaa - Dead, Buried and Cold.ogg')
        sound1 = mixer.Sound('Music/Ove Melaa - Dead, Buried and Cold.ogg')
        background_music.play(sound1, -1)
        sound1.set_volume(0.6)
        self.title_screen = ImageTk.PhotoImage(Image.open('titleScreen8.png').resize((root.winfo_screenwidth(),root.winfo_screenheight())))
        self.game_title = tk.Canvas(root, width = root.winfo_screenwidth(), bg = 'black', highlightthickness = 0, height = root.winfo_screenheight())
        self.game_title.create_image(0,0, image =self.title_screen, anchor = 'nw')
        self.game_title.pack(side = 'top')
        
        self.one_player = tk.Button(root, text = '1 Player', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda num = 1 : self.num_chose(num))
        self.game_title.create_window(root.winfo_screenwidth()/2, root.winfo_screenheight()-120, anchor='s', window = self.one_player)
        
        self.two_player = tk.Button(root, text = '2 Player', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda num = 2 : self.num_chose(num))
        self.game_title.create_window(root.winfo_screenwidth()/2, root.winfo_screenheight()-70, anchor='s', window = self.two_player)
        
        self.load_button = tk.Button(root, text = 'Load Game', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = self.try_load)
        self.game_title.create_window(root.winfo_screenwidth()/2, root.winfo_screenheight()-20, anchor='s', window = self.load_button)
        
    def try_load(self):
        saves = [s for r,d,s in walk('save_games/')][0]
        saves = [s for s in saves[:] if s[0] != '.']
        # create a button for each save and a cancel button
        self.scroll_frame = VerticalScrolledFrame(root)
        self.game_title.create_window(root.winfo_screenwidth()/2 + root.winfo_screenwidth()/8, root.winfo_screenheight()-220, anchor = 'nw', window = self.scroll_frame)
        self.game_title.saves_buttons = []
        for s in saves:
            # expand filename into readable
            with open('save_games/'+s, 'r') as f:
#                 obj = load(f)
                name = f.readline().strip('\n')
                if name == 'Agnes_Sampson':
                    img = ImageTk.PhotoImage(Image.open('avatars/Agnes_Sampson.png'))
                    obj = Witch(name = 'Agnes_Sampson', img = img, loc = [0,0], owner = 'p1')
                elif name == 'Fakir_Ali':
                    img = ImageTk.PhotoImage(Image.open('avatars/Fakir_Ali.png'))
                    obj = Witch(name = 'Fakir_Ali', img = img, loc = [0,0], owner = 'p1')
                cantrips = eval(f.readline().strip('\n'))
                arcane = eval(f.readline().strip('\n'))
                sum_cap = int(f.readline().strip('\n'))
                b_str = int(f.readline().strip('\n'))
                b_agl = int(f.readline().strip('\n'))
                b_end = int(f.readline().strip('\n'))
                b_dodge = int(f.readline().strip('\n'))
                b_psyche = int(f.readline().strip('\n'))
                b_spirit = int(f.readline().strip('\n'))
                b_magick = int(f.readline().strip('\n'))
                area = int(f.readline().strip('\n'))
                if 'Foul_Familiar' in cantrips:
                    obj.cantrip_dict['Foul_Familiar'] = obj.foul_familiar
                if 'Hatred' in arcane:
                    obj.arcane_dict['Hatred'] = (obj.hatred, 9)
                if 'Vengeance' in arcane:
                    obj.arcane_dict['Vengeance'] = (obj.vengeance, 13)
                if 'Pain' in arcane:
                    obj.arcane_dict['Pain'] = (obj.pain, 7)
                if 'Torment' in arcane:
                    obj.arcane_dict['Torment'] = (obj.torment, 7)
                if 'Entomb' in arcane:
                    obj.arcane_dict['Entomb'] = (obj.entomb, 4)
                if 'Summon_Cenobite' in arcane:
                    obj.arcane_dict['Summon_Cenobite'] = (obj.summon_cenobite, 9)
                obj.summon_cap = sum_cap
                obj.base_str = b_str
                obj.str = b_str
                obj.base_agl = b_agl
                obj.agl = b_agl
                obj.base_end = b_end
                obj.end = b_end
                obj.base_dodge = b_dodge
                obj.dodge = b_dodge
                obj.base_psyche = b_psyche
                obj.psyche = b_psyche
                obj.base_spirit = b_spirit
                obj.spirit = b_spirit
                obj.base_magick = b_magick
                obj.magick = b_magick
                obj.current_area = area
                cmd = lambda obj = obj : self.load_game(obj)
                b = tk.Button(self.scroll_frame.interior, text = s, width = 13, wraplength = 190, fg = 'indianred', highlightbackground = 'black', font = ('chalkduster', 24), relief = 'raised', command = cmd)
                b.pack() 
                self.game_title.saves_buttons.append(b)
        cancel_b = tk.Button(self.scroll_frame.interior, text = 'Cancel', bg = 'black', fg = 'black', width = 13, highlightbackground = 'black', font = ('chalkduster', 24), relief = 'raised', command = self.scroll_frame.destroy)
        cancel_b.pack(side = 'bottom')
        self.game_title.saves_buttons.append(cancel_b)
                
    def load_game(self, obj):
        self.game_title.destroy()
        obj.move_type = 'normal'
        self.load_map_triggers(map_number = obj.current_area, protaganist_object = obj)
        
    def num_chose(self, num):
        self.num_players = num
        self.game_title.destroy()
        self.one_player.destroy()
        self.two_player.destroy()
        del self.title_screen
        del self.game_title
        del self.one_player
        del self.two_player
        if self.num_players == 2:
            self.choose_map()
        else:
        # first choose_witch() here
            self.choose_witch(player_num = 1)
#             self.load_map_triggers(map_number = 0)
            
    # make each branch load the intro scene for level, with 'continue' button when done reading/displaying to call create_map_curs_context
    def load_map_triggers(self, map_number, witch = None, protaganist_object = None):
        background_music.stop()
        if map_number == 0: # FIRST AREA, NO 'CONTINUATION from previous level' BY PASSING PROTAG OBJECT
            sound1 = mixer.Sound('Music/heroic_demise.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.6)
            # CLEANUP FROM CHOOSE_WITCH
            self.avatar_popup.destroy()
            del self.wrapped_funcs
            self.p1_witch = witch
            self.map_triggers = []
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            ############## GODHAND
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            ################
            def kill_all_enemies():
                all = [k for k,v in self.ent_dict.items() if v.owner == 'p2']
                if all == []:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(kill_all_enemies)
            
            self.load_intro_scene(map_number)# DONT NEED PROTAG OBJECT ON FIRST AREA
#             self.create_map_curs_context(map_number)
    # SECOND LEVEL
        elif map_number == 1:
            self.map_triggers = []
            sound1 = mixer.Sound('Music/Caves of sorrow.ogg')
            background_music.play(sound1, -1)
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
            self.map_triggers.append(summon_trick)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            def kill_all_undead():
                all = [k for k,v in self.ent_dict.items() if v.owner == 'p2']
                if all == []:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(kill_all_undead)
            
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
#             self.create_map_curs_context(map_number, protaganist_object = protaganist_object)
    # THRID LEVEL 
        elif map_number == 2:
            sound1 = mixer.Sound('Music/arabesque.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.3)
            self.map_triggers = []
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'door'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
#             depending on which is killed, load certain level
#             knight near stairway is b7, knight near doorway is b8
            def kill_stair_knight():
                all_knights = [v.number for k,v in self.ent_dict.items() if v.name == 'Undead_Knight']
                if 'b7' not in all_knights and 'b8' in all_knights:
                    return 'stairway'
                else:
                    return None
            self.map_triggers.append(kill_stair_knight)
            def kill_door_knight():
                all_knights = [v.number for k,v in self.ent_dict.items() if v.name == 'Undead_Knight']
                if 'b8' not in all_knights and 'b7' in all_knights:
                    return 'door'
                else:
                    return None
            self.map_triggers.append(kill_door_knight)
#             def kill_one_undead_knight(): # change to kill both handling
#                 all_knights = [v.name for k,v in self.ent_dict.items() if v.name == 'Undead_Knight']
#                 if len(all_knights) <= 1:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(kill_one_undead_knight)
            
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
#             self.create_map_curs_context(map_number, protaganist_object = protaganist_object)
        elif map_number == 121:
            sound1 = mixer.Sound('Music/field_of_dreams.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(1)
            self.map_triggers = []
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            # add generate revenants to global effects
            # DEBUG should not be map trigger, happen only once per turn
            def generate_revenants():
                if self.turn_counter % 4 == 0:
                    # get empty sqr near
#                     empty_sqrs = [s for s in app.coords if app.grid[s[0]][s[1]] == '' and dist([24,4], s) <= 3]
#                     if empty_sqrs != []:
#                         loc = choice(empty_sqrs)
                    if app.grid[24][4] == '':
                        img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
#                         enemy_ents = [k for k,v in app.ent_dict.items() if v.owner == 'p2']
                        # needs to be unique number
                        counter = self.effects_counter+3 # seed with 3 to prevent collision existing Ents
                        self.effects_counter += 3
                        id = 'b' + str(counter)
                        app.grid[24][4] = id
                        app.ent_dict[id] = Revenant(name = 'Revenant', img = img, loc = [24,4], owner = 'p2', number = id)
            self.map_triggers.append(generate_revenants)
            #   CREATE SPARKLES
            def create_sparkles():
                app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [28,15])
                app.canvas.create_image(2800+50-app.moved_right, 1500+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                ##
                app.vis_dict['Sparkle2'] = Vis(name = 'Sparkle', loc = [11,1])
                app.canvas.create_image(1100+50-app.moved_right, 100+50-app.moved_down, image = app.vis_dict['Sparkle2'].img, tags = 'Sparkle2')
                self.map_triggers.remove(create_sparkles)
            self.map_triggers.append(create_sparkles)
            # victory, kill ghost
            def kill_ghost():
                if 'b2' not in [k for k in self.ent_dict.keys()]:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(kill_ghost)
            # trigger ghost
            # Need to ensure spot is not blocked
            def ghost_teleport1():
                if app.ent_dict['b2'].spirit < 50:
                    if app.grid[7][2] != '':
#                         coords = [[x,y] for x in range(self.map_width//100) for y in range(self.map_height//100)]
                        empt_coords = [c for c in app.coords if app.grid[c[0]][c[1]] == '']
                        sqr = choice(empt_coords)
                    else:
                        sqr = [7,2]
                    oldloc = app.ent_dict['b2'].loc[:]
                    app.grid[oldloc[0]][oldloc[1]] = ''
                    app.ent_dict['b2'].loc = sqr[:]
                    app.grid[sqr[0]][sqr[1]] = 'b2'
                    app.canvas.delete('b2')
                    app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.ent_dict['b2'].img, tags = 'b2')
                    self.map_triggers.remove(ghost_teleport1)
            self.map_triggers.append(ghost_teleport1)
            def ghost_teleport2():
                if app.ent_dict['b2'].spirit < 30:
                    if app.grid[26][17] != '':
#                         coords = [[x,y] for x in range(self.map_width//100) for y in range(self.map_height//100)]
                        empt_coords = [c for c in app.coords if app.grid[c[0]][c[1]] == '']
                        sqr = choice(empt_coords)
                    else:
                        sqr = [26,17]
                    oldloc = app.ent_dict['b2'].loc[:]
                    app.grid[oldloc[0]][oldloc[1]] = ''
                    app.ent_dict['b2'].loc = sqr[:]
                    app.grid[sqr[0]][sqr[1]] = 'b2'
                    app.canvas.delete('b2')
                    app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.ent_dict['b2'].img, tags = 'b2')
                    self.map_triggers.remove(ghost_teleport2)
            self.map_triggers.append(ghost_teleport2)
            # READ BOOK
            def read_book():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [27,15]:
                    del app.vis_dict['Sparkle1']
                    app.canvas.delete('Sparkle1')
                    app.unbind_all()
                    self.book121 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_121_book)
                    app.canvas.create_window(2700-app.moved_right, 1500-app.moved_down, window = self.book121)
                    self.book121_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_121_book)
                    app.canvas.create_window(2700-app.moved_right+25, 1500-app.moved_down+33, window = self.book121_cancel)
                    self.map_triggers.remove(read_book)
            self.map_triggers.append(read_book)
            def inspect_painting():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [11,2]:
                    del app.vis_dict['Sparkle2']
                    app.canvas.delete('Sparkle2')
                    app.unbind_all()
                    self.painting121 = tk.Button(root, text = 'Inspect Painting', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.inspect_121_painting)
                    app.canvas.create_window(1100-app.moved_right, 200-app.moved_down, window = self.painting121)
                    self.painting121_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_121_painting)
                    app.canvas.create_window(1100-app.moved_right+25, 200-app.moved_down+34, window = self.painting121_cancel)
                    self.map_triggers.remove(inspect_painting)
            self.map_triggers.append(inspect_painting)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
        # LABRYNTH 
        elif map_number == 21:
            sound1 = mixer.Sound('Music/Blackmoor_Colossus.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.3)
            self.map_triggers = []
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            def area_eleven():
                if app.ent_dict[app.p1_witch].loc in [[20,18],[21,18],[22,18]]:
                    coords = [[24,18],[25,18],[26,18],[27,18],[28,18],[24,17],[25,17],[26,17],[24,16],[25,16],[26,16],[22,15],[23,15],[24,15],[25,15],[26,15],[27,15],[28,15],[22,14],[22,13],[22,12],[22,11],[22,10],[22,9],[23,14],[23,13],[23,12],[23,11],[23,10],[23,9],[20,9],[21,9],[20,10],[21,10],[25,14],[26,14],[27,14],[28,14],[25,13],[26,13],[25,12],[26,12],[28,13],[23,18]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/11_top.png')
                    bot = Image.open('1_player_map_fog/map21/11.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_eleven)
            self.map_triggers.append(area_eleven)
            
            def area_ten():
                if app.ent_dict[app.p1_witch].loc in [[25,13],[26,13],[25,12],[26,12]]:
                    coords = [[25,5],[25,6],[25,7],[25,8],[25,9],[25,10],[25,11],[26,5],[26,6],[26,7],[26,8],[26,9],[26,10],[26,11]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/10_top.png')
                    bot = Image.open('1_player_map_fog/map21/10.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_ten)
            self.map_triggers.append(area_ten)
            
            def area_nine():
                if app.ent_dict[app.p1_witch].loc in [[25,5],[25,6],[26,5],[26,6]]:
                    coords = [[20,5],[21,5],[22,5],[23,5],[24,5],[20,6],[21,6],[22,6],[23,6],[24,6]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/9_top.png')
                    bot = Image.open('1_player_map_fog/map21/9.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_nine)
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
                    app.ent_dict['b7'] = Revenant(name = 'Revenant', img = img, loc =[21,5], owner = 'p2', number = 'b7')
                    app.grid[21][5] = 'b7'
                    app.ent_dict['b8'] = Revenant(name = 'Revenant', img = img, loc =[20,6], owner = 'p2', number = 'b8')
                    app.grid[20][6] = 'b8'
            self.map_triggers.append(area_nine)
            
            def area_eight():
                if app.ent_dict[app.p1_witch].loc in [[20,9],[21,9],[20,10],[21,10]]:
                    coords = [[19,9],[19,10],[18,6],[18,7],[18,8],[18,9],[18,10],[17,6],[17,7],[17,8],[16,8],[15,8],[14,8],[13,8],[12,8],[11,8],[10,8],[9,8],[8,8],[7,8],[7,9],[8,9],[9,9],[10,9],[11,9],[12,9]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/8_top.png')
                    bot = Image.open('1_player_map_fog/map21/8.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_eight)
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
                    app.ent_dict['b5'] = Revenant(name = 'Revenant', img = img, loc =[9,8], owner = 'p2', number = 'b5')
                    app.grid[9][8] = 'b5'
            self.map_triggers.append(area_eight)
            
            def area_seven():
                if app.ent_dict[app.p1_witch].loc in [[8,8],[7,8],[7,9],[8,9]]:
                    coords = [[6,8],[6,9],[5,8],[5,9],[5,10],[5,11],[5,12],[4,12],[3,12]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/7_top.png')
                    bot = Image.open('1_player_map_fog/map21/7.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_seven)
            self.map_triggers.append(area_seven)
            
            def area_six():
                if app.ent_dict[app.p1_witch].loc in [[5,12],[4,12],[3,12]]:
                    coords = [[2,12],[1,12],[1,13],[1,14],[1,15],[1,16],[1,17],[1,18]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/6_top.png')
                    bot = Image.open('1_player_map_fog/map21/6.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_six)
            self.map_triggers.append(area_six)
            
            def area_five():
                if app.ent_dict[app.p1_witch].loc in [[1,17],[1,18]]:
                    coords = [[2,18],[3,18],[4,18],[5,18],[6,18],[7,18],[8,18],[9,18],[10,18],[11,18],[12,18],[13,18],[14,18],[15,18],[16,18]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/5_top.png')
                    bot = Image.open('1_player_map_fog/map21/5.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_five)
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
                    app.ent_dict['b6'] = Revenant(name = 'Revenant', img = img, loc =[16,8], owner = 'p2', number = 'b6')
                    app.grid[16][8] = 'b6'
                    # SPARKLE
                    def create_sparkle2():
                        app.vis_dict['Sparkle2'] = Vis(name = 'Sparkle', loc = [17,18])
                        app.canvas.create_image(1700+50-app.moved_right, 1800+50-app.moved_down, image = app.vis_dict['Sparkle2'].img, tags = 'Sparkle2')
                        self.map_triggers.remove(create_sparkle2)
                    self.map_triggers.append(create_sparkle2)
                    # BOOK TRIGGER
                    def read_book():
                        loc = app.ent_dict[app.p1_witch].loc[:]
                        if loc == [16,18]:
                            del app.vis_dict['Sparkle2']
                            app.canvas.delete('Sparkle2')
                            app.unbind_all()
                            self.book21 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_21_book)
                            app.canvas.create_window(1600-app.moved_right, 1800-app.moved_down, window = self.book21)
                            self.book21_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_21_book)
                            app.canvas.create_window(1600-app.moved_right+25, 1800-app.moved_down+33, window = self.book21_cancel)
                            self.map_triggers.remove(read_book)
                    self.map_triggers.append(read_book)
            self.map_triggers.append(area_five)
            
            def area_four():
                if app.ent_dict[app.p1_witch].loc in [[17,6],[18,6]]:
                    coords = [[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],[13,5],[14,5],[15,5],[16,5],[17,5],[18,5]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/4_top.png')
                    bot = Image.open('1_player_map_fog/map21/4.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_four)
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
                    app.ent_dict['b4'] = Revenant(name = 'Revenant', img = img, loc =[9,5], owner = 'p2', number = 'b4')
                    app.grid[9][5] = 'b4'
            self.map_triggers.append(area_four)
            
            def area_three():
                if app.ent_dict[app.p1_witch].loc in [[5,5],[6,5]]:
                    coords = [[4,5],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/3_top.png')
                    bot = Image.open('1_player_map_fog/map21/3.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_three)
            self.map_triggers.append(area_three)
            
            def area_two():
                if app.ent_dict[app.p1_witch].loc in [[28,13],[28,14]]:
                    coords = [[28,4],[28,5],[28,6],[28,7],[28,8],[28,9],[28,10],[28,11],[28,12]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/2_top.png')
                    bot = Image.open('1_player_map_fog/map21/2.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_two)
            self.map_triggers.append(area_two)
            
            def area_one():
                if app.ent_dict[app.p1_witch].loc in [[28,4]]:
                    coords = [[28,3],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2],[13,2],[14,2],[15,2],[16,2],[17,2],[18,2],[19,2],[20,2],[21,2],[22,2],[23,2],[24,2],[25,2],[26,2],[27,2],[28,2]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/1_top.png')
                    bot = Image.open('1_player_map_fog/map21/1.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_one)
                    # Place chest trigger and revenant
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Revenant.png'))
                    app.ent_dict['b2'] = Revenant(name = 'Revenant', img = img, loc =[7,2], owner = 'p2', number = 'b2')
                    app.grid[7][2] = 'b2'
                    # SPARKLE
                    def create_sparkle1():
                        app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [6,2])
                        app.canvas.create_image(600+50-app.moved_right, 200+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                        self.map_triggers.remove(create_sparkle1)
                    self.map_triggers.append(create_sparkle1)
                    # CHEST
                    def chest1():
                        loc = app.ent_dict[app.p1_witch].loc[:]
                        if loc == [7,2]:
                            del app.vis_dict['Sparkle1']
                            app.canvas.delete('Sparkle1')
                            app.unbind_all()
                            self.chest21_1 = tk.Button(root, text = 'Open Chest', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.open_chest21_1)
                            app.canvas.create_window(700-app.moved_right, 200-app.moved_down, window = self.chest21_1)
                            self.chest21_1_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_chest1)
                            app.canvas.create_window(700-app.moved_right+25, 200-app.moved_down+34, window = self.chest21_1_cancel)
                            self.map_triggers.remove(chest1)
                    self.map_triggers.append(chest1)
            self.map_triggers.append(area_one)
            
            def area_zero():
                if app.ent_dict[app.p1_witch].loc in [[3,10]]:
                    coords = [[2,10],[1,10],[1,9],[1,8],[1,7],[1,6],[1,5],[1,4],[1,3],[1,2],[2,2],[3,2],[4,2],[3,1]]
                    for c in coords:
                        app.grid[c[0]][c[1]] = ''
                    top = Image.open('1_player_map_fog/map21/0_top.png')
                    bot = Image.open('1_player_map_fog/map21/0.png')
                    newbot = self.map_bottom_image
                    newtop = self.map_top_image
                    newbot = Image.alpha_composite(newbot, bot)
                    newtop = Image.alpha_composite(newtop, top)
                    self.map_bottom_image = newbot
                    self.map_top_image = newtop
                    self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
                    self.map_top = ImageTk.PhotoImage(self.map_top_image)
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_bottom, tags = ('map','mapbottom'))
                    self.canvas.create_image(0-app.moved_right, 0-app.moved_down, anchor = 'nw', image = self.map_top, tags = ('map','maptop'))
                    app.canvas.tag_lower('mapbottom')
                    self.map_triggers.remove(area_zero)
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Ghost.png'))
                    app.ent_dict['b3'] = Ghost(name = 'Ghost', img = img, loc =[1,2], owner = 'p2', number = 'b3')
                    app.grid[1][2] = 'b3'
                    def ghost_death():
                        if 'b3' not in [k for k in app.ent_dict.keys()]:
                            return 'victory'
                    self.map_triggers.append(ghost_death)
            self.map_triggers.append(area_zero)
            
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
        elif map_number == 22:
            sound1 = mixer.Sound('Music/Dark_Amulet.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.4)
            self.map_triggers = []
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            # SPARKLE
            def create_sparkle1():
                app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [22,8])
                app.canvas.create_image(2200+50-app.moved_right, 800+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                self.map_triggers.remove(create_sparkle1)
            self.map_triggers.append(create_sparkle1)
            def inspect_column():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [22,9]:
                    del app.vis_dict['Sparkle1']
                    app.canvas.delete('Sparkle1')
                    app.unbind_all()
                    self.column22 = tk.Button(root, text = 'Inspect Column', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.inspect_22_column)
                    app.canvas.create_window(2200-app.moved_right, 900-app.moved_down, window = self.column22)
                    self.column22_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_22_column)
                    app.canvas.create_window(2200-app.moved_right+25, 900-app.moved_down+33, window = self.column22_cancel)
                    self.map_triggers.remove(inspect_column)
            self.map_triggers.append(inspect_column)
            def awaken_orcs():
                sqrs_near = [s for s in app.coords if dist(app.ent_dict['b7'].loc,s) <= 7 or dist(app.ent_dict['b8'].loc,s) <= 7]
                player_ent_locs = [v.loc for k,v in app.ent_dict.items() if v.owner == 'p1']
                sentinel = False
                for loc in player_ent_locs:
                    if loc in sqrs_near:
                        sentinel = True
                if app.ent_dict['b1'].spirit < 127 or sentinel == True:
                    app.ent_dict['b7'].waiting = False
                    app.ent_dict['b8'].waiting = False
                    self.map_triggers.remove(awaken_orcs)
            self.map_triggers.append(awaken_orcs)
            def awaken_dragon():
                sqrs = [s for s in app.coords if dist(s, app.ent_dict['b1'].loc) <= 9]
                ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
                for ent in ents:
                    if app.ent_dict[ent].owner == 'p1':
                        app.ent_dict['b1'].waiting = False
                        self.map_triggers.remove(awaken_dragon)
                        break
            self.map_triggers.append(awaken_dragon)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            def kill_dragon():
                if 'b1' not in app.ent_dict.keys():
                    return 'victory'
            self.map_triggers.append(kill_dragon)
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
        elif map_number == 122:
            sound1 = mixer.Sound('Music/Dark_Descent.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.3)
            self.map_triggers = []
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            # SPARKLE
            def create_sparkle1():
                app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [7,1])
                app.canvas.create_image(700+50-app.moved_right, 100+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                self.map_triggers.remove(create_sparkle1)
            self.map_triggers.append(create_sparkle1)
            # BOOK TRIGGER
            def read_book():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [7,2]:
                    del app.vis_dict['Sparkle1']
                    app.canvas.delete('Sparkle1')
                    app.unbind_all()
                    self.book122 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_122_book)
                    app.canvas.create_window(700-app.moved_right, 200-app.moved_down, window = self.book122)
                    self.book122_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_122_book)
                    app.canvas.create_window(700-app.moved_right+25, 200-app.moved_down+33, window = self.book122_cancel)
                    self.map_triggers.remove(read_book)
            self.map_triggers.append(read_book)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            def kill_warlock():
                if 'b1' not in app.ent_dict.keys():
                    return 'victory'
            self.map_triggers.append(kill_warlock)
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
        # LEVEL 3 SANCTUM ENTRYWAY
        elif map_number == 3:
            sound1 = mixer.Sound('Music/radakan - old crypt.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.8)
            self.map_triggers = []
#             def summon_trick():
#                 all = [v.name for k,v in self.ent_dict.items() if v.owner == 'p1']
#                 if 'Bard' in all:
#                     return 'victory'
#                 else:
#                     return None
#             self.map_triggers.append(summon_trick)
            def kill_all():
                ents = app.ent_dict.keys()
                if 'b0' not in ents and 'b1' not in ents and 'b2' not in ents:
                    return 'victory'
            self.map_triggers.append(kill_all)
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            # BOOK AND SPARKLE 1
            def create_sparkle1():
                app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [1,29])
                app.canvas.create_image(100+50-app.moved_right, 2900+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                self.map_triggers.remove(create_sparkle1)
            self.map_triggers.append(create_sparkle1)
            def read_book1():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [2,29]:
                    del app.vis_dict['Sparkle1']
                    app.canvas.delete('Sparkle1')
                    app.unbind_all()
                    self.book3_1 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_1_book)
                    app.canvas.create_window(100-app.moved_right, 2900-app.moved_down, window = self.book3_1)
                    self.book3_1_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_1_book)
                    app.canvas.create_window(100-app.moved_right+25, 2900-app.moved_down+33, window = self.book3_1_cancel)
                    self.map_triggers.remove(read_book1)
            self.map_triggers.append(read_book1)
            # BOOK AND SPARKLE 2
            def create_sparkle2():
                app.vis_dict['Sparkle2'] = Vis(name = 'Sparkle', loc = [18,29])
                app.canvas.create_image(1800+50-app.moved_right, 2900+50-app.moved_down, image = app.vis_dict['Sparkle2'].img, tags = 'Sparkle2')
                self.map_triggers.remove(create_sparkle2)
            self.map_triggers.append(create_sparkle2)
            def read_book2():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [17,29]:
                    del app.vis_dict['Sparkle2']
                    app.canvas.delete('Sparkle2')
                    app.unbind_all()
                    self.book3_2 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_2_book)
                    app.canvas.create_window(1800-app.moved_right, 2900-app.moved_down, window = self.book3_2)
                    self.book3_2_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_2_book)
                    app.canvas.create_window(1800-app.moved_right+25, 2900-app.moved_down+33, window = self.book3_2_cancel)
                    self.map_triggers.remove(read_book2)
            self.map_triggers.append(read_book2)
            # BOOK AND SPARKLE 3
            def create_sparkle3():
                app.vis_dict['Sparkle3'] = Vis(name = 'Sparkle', loc = [1,19])
                app.canvas.create_image(100+50-app.moved_right, 1900+50-app.moved_down, image = app.vis_dict['Sparkle3'].img, tags = 'Sparkle3')
                self.map_triggers.remove(create_sparkle3)
            self.map_triggers.append(create_sparkle3)
            def read_book3():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [2,19]:
                    del app.vis_dict['Sparkle3']
                    app.canvas.delete('Sparkle3')
                    app.unbind_all()
                    self.book3_3 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_3_book)
                    app.canvas.create_window(100-app.moved_right, 1900-app.moved_down, window = self.book3_3)
                    self.book3_3_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_3_book)
                    app.canvas.create_window(100-app.moved_right+25, 1900-app.moved_down+33, window = self.book3_3_cancel)
                    self.map_triggers.remove(read_book3)
            self.map_triggers.append(read_book3)
            # BOOK AND SPARKLE 4
            def create_sparkle4():
                app.vis_dict['Sparkle4'] = Vis(name = 'Sparkle', loc = [18,19])
                app.canvas.create_image(1800+50-app.moved_right, 1900+50-app.moved_down, image = app.vis_dict['Sparkle4'].img, tags = 'Sparkle4')
                self.map_triggers.remove(create_sparkle4)
            self.map_triggers.append(create_sparkle4)
            def read_book4():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [17,19]:
                    del app.vis_dict['Sparkle4']
                    app.canvas.delete('Sparkle4')
                    app.unbind_all()
                    self.book3_4 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_4_book)
                    app.canvas.create_window(1800-app.moved_right, 1900-app.moved_down, window = self.book3_4)
                    self.book3_4_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_4_book)
                    app.canvas.create_window(1800-app.moved_right+25, 1900-app.moved_down+33, window = self.book3_4_cancel)
                    self.map_triggers.remove(read_book4)
            self.map_triggers.append(read_book4)
            # BOOK AND SPARKLE 5
            def create_sparkle5():
                app.vis_dict['Sparkle5'] = Vis(name = 'Sparkle', loc = [18,9])
                app.canvas.create_image(1800+50-app.moved_right, 900+50-app.moved_down, image = app.vis_dict['Sparkle5'].img, tags = 'Sparkle5')
                self.map_triggers.remove(create_sparkle5)
            self.map_triggers.append(create_sparkle5)
            def read_book5():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [17,9]:
                    del app.vis_dict['Sparkle5']
                    app.canvas.delete('Sparkle5')
                    app.unbind_all()
                    self.book3_5 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_5_book)
                    app.canvas.create_window(1800-app.moved_right, 900-app.moved_down, window = self.book3_5)
                    self.book3_5_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_5_book)
                    app.canvas.create_window(1800-app.moved_right+25, 900-app.moved_down+33, window = self.book3_5_cancel)
                    self.map_triggers.remove(read_book5)
            self.map_triggers.append(read_book5)
            # BOOK AND SPARKLE 6
            def create_sparkle6():
                app.vis_dict['Sparkle6'] = Vis(name = 'Sparkle', loc = [1,9])
                app.canvas.create_image(100+50-app.moved_right, 900+50-app.moved_down, image = app.vis_dict['Sparkle6'].img, tags = 'Sparkle6')
                self.map_triggers.remove(create_sparkle6)
            self.map_triggers.append(create_sparkle6)
            def read_book6():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [2,9]:
                    del app.vis_dict['Sparkle6']
                    app.canvas.delete('Sparkle6')
                    app.unbind_all()
                    self.book3_6 = tk.Button(root, text = 'Read Book', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.read_3_6_book)
                    app.canvas.create_window(200-app.moved_right, 900-app.moved_down, window = self.book3_6)
                    self.book3_6_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_3_6_book)
                    app.canvas.create_window(200-app.moved_right+25, 900-app.moved_down+33, window = self.book3_6_cancel)
                    self.map_triggers.remove(read_book6)
            self.map_triggers.append(read_book6)
            
            def awaken_group_2(): 
                friendly_ent_locs = [v.loc for k,v in app.ent_dict.items() if v.owner == 'p1']
                for loc in friendly_ent_locs:
                    if loc[1] < 19:
                        app.ent_dict['b1'].waiting = False
                        app.ent_dict['b2'].waiting = False
                        app.ent_dict['b7'].waiting = False
                        app.ent_dict['b8'].waiting = False
                        app.ent_dict['b9'].waiting = False
                        app.ent_dict['b10'].waiting = False
                        self.map_triggers.remove(awaken_group_2)
                        break
            self.map_triggers.append(awaken_group_2)
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
        elif map_number == 4:
            sound1 = mixer.Sound('Music/The Peculiar Habits of the Cave Hermits.ogg')
            background_music.play(sound1, -1)
            sound1.set_volume(0.8)
            self.map_triggers = []
            # powerup sparkle, added after death of firemage
            def create_sparkle1():
                app.vis_dict['Sparkle1'] = Vis(name = 'Sparkle', loc = [5,5])
                app.canvas.create_image(500+50-app.moved_right, 500+50-app.moved_down, image = app.vis_dict['Sparkle1'].img, tags = 'Sparkle1')
                self.map_triggers.remove(create_sparkle1)
            self.map_triggers.append(create_sparkle1)
            def inspect_baphomet_statue():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [5,5]:
                    del app.vis_dict['Sparkle1']
                    app.canvas.delete('Sparkle1')
                    app.unbind_all()
                    self.baphomet_statue = tk.Button(root, text = 'Inspect Statue', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.baphomet_statue)
                    app.canvas.create_window(500-app.moved_right, 500-app.moved_down, window = self.baphomet_statue)
                    self.baphomet_statue_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_baphomet_statue)
                    app.canvas.create_window(500-app.moved_right+25, 500-app.moved_down+33, window = self.baphomet_statue_cancel)
                    self.map_triggers.remove(inspect_baphomet_statue)
            # powerup sparkle, added after death of earthmage
            def create_sparkle2():
                app.vis_dict['Sparkle2'] = Vis(name = 'Sparkle', loc = [34,5])
                app.canvas.create_image(3400+50-app.moved_right, 500+50-app.moved_down, image = app.vis_dict['Sparkle2'].img, tags = 'Sparkle2')
                self.map_triggers.remove(create_sparkle2)
            self.map_triggers.append(create_sparkle2)
            def inspect_astrolabe():
                loc = app.ent_dict[app.p1_witch].loc[:]
                if loc == [34,5]:
                    del app.vis_dict['Sparkle2']
                    app.canvas.delete('Sparkle2')
                    app.unbind_all()
                    self.astrolabe = tk.Button(root, text = 'Inspect Device', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.astrolabe)
                    app.canvas.create_window(3400-app.moved_right, 500-app.moved_down, window = self.astrolabe)
                    self.astrolabe_cancel = tk.Button(root, text = 'Leave Alone', font = ('chalkduster', 18), highlightbackground = 'black', fg = 'indianred', command = self.cancel_astrolabe)
                    app.canvas.create_window(3400-app.moved_right+25, 500-app.moved_down+33, window = self.astrolabe_cancel)
                    self.map_triggers.remove(inspect_astrolabe)
            # victory condition for level is death of final elemental mage (water), appended after airmage death
            def watermage_death():
                if 'Water_Mage' not in [v.name for k,v in app.ent_dict.items()]:
                    return 'victory'
            def self_death():
                if app.p1_witch not in app.ent_dict.keys():
                    return 'game over'
            self.map_triggers.append(self_death)
            # airmage death trigger, appended after earthmage death
            def airmage_death():
                if 'Air_Mage' not in [v.name for k,v in app.ent_dict.items()]:
                    # kill air elementals (find by name not id)
                    for e in list(app.ent_dict.keys()):
                        if app.ent_dict[e].name == 'Air_Elemental':
                            app.kill(app.ent_dict[e].number)
                    # spawn water mage
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Water_Mage.png'))
                    num = app.effects_counter
                    app.effects_counter += 1
                    # find open spawn square
                    sqrs = [[x,y] for x in range(17,24) for y in range(14,20) if app.grid[x][y] == '']
                    loc = choice(sqrs)
                    app.ent_dict['b'+str(num)] = Water_Mage(name = 'Water_Mage', img = img, loc = loc[:], owner = 'p2', number = 'b'+str(num))
                    app.grid[loc[0]][loc[1]] = 'b'+str(num)
                    self.map_triggers.remove(airmage_death)
                    self.map_triggers.append(watermage_death)
            # earthmage death trigger, appended after firemage death
            def earthmage_death():
                if 'Earth_Mage' not in [v.name for k,v in app.ent_dict.items()]:
                    # add sparkle2 powerup
                    self.map_triggers.append(inspect_astrolabe)
                    # kill earth elementals (find by name not id)
                    for e in list(app.ent_dict.keys()):
                        if app.ent_dict[e].name == 'Earth_Elemental':
                            app.kill(app.ent_dict[e].number)
                    # spawn air mage
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Air_Mage.png'))
                    num = app.effects_counter
                    app.effects_counter += 1
                    # find open spawn square
                    sqrs = [[x,y] for x in range(17,24) for y in range(14,20) if app.grid[x][y] == '']
                    loc = choice(sqrs)
                    app.ent_dict['b'+str(num)] = Air_Mage(name = 'Air_Mage', img = img, loc = loc[:], owner = 'p2', number = 'b'+str(num))
                    app.grid[loc[0]][loc[1]] = 'b'+str(num)
                    self.map_triggers.remove(earthmage_death)
                    self.map_triggers.append(airmage_death)
            # add firemage death trigger
            def firemage_death():
                if 'b0' not in app.ent_dict.keys():
                    # add sparkle1 powerup
                    self.map_triggers.append(inspect_baphomet_statue)
                    # kill fire elementals (find by name not id)
                    for e in list(app.ent_dict.keys()):
                        if app.ent_dict[e].name == 'Fire_Elemental':
                            app.kill(app.ent_dict[e].number)
                    # spawn earth mage
                    img = ImageTk.PhotoImage(Image.open('summon_imgs/Earth_Mage.png'))
                    num = app.effects_counter
                    app.effects_counter += 1
                    # find open spawn square
                    sqrs = [[x,y] for x in range(17,24) for y in range(14,20) if app.grid[x][y] == '']
                    loc = choice(sqrs)
                    app.ent_dict['b'+str(num)] = Earth_Mage(name = 'Earth_Mage', img = img, loc = loc[:], owner = 'p2', number = 'b'+str(num))
                    app.grid[loc[0]][loc[1]] = 'b'+str(num)
                    self.map_triggers.remove(firemage_death)
                    self.map_triggers.append(earthmage_death)
            self.map_triggers.append(firemage_death)
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
    # END OF GAME
        else:
            print('you are winner hahaha')
        
    # Move trigger funcs for organization?
    # baphomet trigger
    def inspect_baphomet_statue(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Baphomet', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].arcane_dict['Summon_Cenobite'] = (app.ent_dict[app.p1_witch].summon_cenobite, 9)
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_baphomet_statue)
    def cancel_baphomet_statue(self):
        self.baphomet.destroy()
        self.baphomet_cancel.destroy()
        app.rebind_all()
        
    # astrolabe trigger
    def inspect_astrolabe(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Astrolabe', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_astrolabe)
    def cancel_astrolabe(self):
        self.astrolabe.destroy()
        self.astrolabe.destroy()
        app.rebind_all()
    
    def read_3_1_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Permanent +20 Magick', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].base_magick += 20
        app.ent_dict[app.p1_witch].magick += 20
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_1_book)
    def cancel_3_1_book(self):
        self.book3_1.destroy()
        self.book3_1_cancel.destroy()
        app.rebind_all()
        
    def read_3_2_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Permanent +10 Spirit', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].base_spirit += 10
        app.ent_dict[app.p1_witch].spirit += 10
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_2_book)
    def cancel_3_2_book(self):
        self.book3_2.destroy()
        self.book3_2_cancel.destroy()
        app.rebind_all()
        
    def read_3_3_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Summon Cap +1', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].summon_cap += 1
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_3_book)
    def cancel_3_3_book(self):
        self.book3_3.destroy()
        self.book3_3_cancel.destroy()
        app.rebind_all()
        
    def read_3_4_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Permanent Endurance +1', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].base_end += 1
        app.ent_dict[app.p1_witch].end += 1
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_4_book)
    def cancel_3_4_book(self):
        self.book3_4.destroy()
        self.book3_4_cancel.destroy()
        app.rebind_all()
        
    def read_3_5_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].arcane_dict['Entomb'] = (app.ent_dict[app.p1_witch].entomb, 4)
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Arcane Spell\n-ENTOMB-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_5_book)
    def cancel_3_5_book(self):
        self.book3_5.destroy()
        self.book3_5_cancel.destroy()
        app.rebind_all()
        
    def read_3_6_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].cantrip_dict['Foul_Familiar'] = app.ent_dict[app.p1_witch].foul_familiar
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Cantrip Spell\n-FOUL FAMILIAR-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_3_6_book)
    def cancel_3_6_book(self):
        self.book3_6.destroy()
        self.book3_6_cancel.destroy()
        app.rebind_all()
        
    
    def inspect_22_column(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].arcane_dict['Hatred'] = (app.ent_dict[app.p1_witch].hatred, 9)
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Arcane Spell\n-HATRED-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_22_column)
        
    def cancel_22_column(self):
        self.column22.destroy()
        self.column22_cancel.destroy()
        app.rebind_all()
    
    
    def read_122_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].arcane_dict['Torment'] = (app.ent_dict[app.p1_witch].torment, 7)
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Arcane Spell\n-TORMENT-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_122_book)
        
    def cancel_122_book(self):
        self.book122.destroy()
        self.book122_cancel.destroy()
        app.rebind_all()
    
    def read_21_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].arcane_dict['Vengeance'] = (app.ent_dict[app.p1_witch].vengeance, 13)
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Arcane Spell\n-VENGEANCE-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_21_book)
        
    def cancel_21_book(self):
        self.book21.destroy()
        self.book21_cancel.destroy()
        app.rebind_all()
    
    def open_chest21_1(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Amulet of Circe\nPermanent +2 Psyche', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        app.ent_dict[app.p1_witch].psyche += 2
        app.ent_dict[app.p1_witch].base_psyche += 2
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_chest1)
        
    def cancel_chest1(self):
        self.chest21_1.destroy()
        self.chest21_1_cancel.destroy()
        app.rebind_all()
    
    def read_121_book(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].arcane_dict['Pain'] = (app.ent_dict[app.p1_witch].pain, 7)
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Arcane Spell\n-PAIN-\nLearned', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_121_book)
        
    def cancel_121_book(self):
        self.book121.destroy()
        self.book121_cancel.destroy()
        app.rebind_all()
        
    def inspect_121_painting(self):
        loc = app.ent_dict[app.p1_witch].loc[:]
        app.ent_dict[app.p1_witch].str += 1
        app.ent_dict[app.p1_witch].base_str += 1
        app.ent_dict[app.p1_witch].end += 1
        app.ent_dict[app.p1_witch].base_end += 1
        app.ent_dict[app.p1_witch].agl += 1
        app.ent_dict[app.p1_witch].base_agl += 1
        app.ent_dict[app.p1_witch].psyche += 1
        app.ent_dict[app.p1_witch].base_psyche += 1
        app.canvas.create_text(loc[0]*100-app.moved_right, loc[1]*100-app.moved_down+85, text = 'Permanent +1\nAll Stats', justify = 'center', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
        root.after(2999, lambda t = 'text' : app.canvas.delete(t))
        root.after(2999, self.cancel_121_painting)
        
    def cancel_121_painting(self):
        self.painting121.destroy()
        self.painting121_cancel.destroy()
        app.rebind_all()
        
        
    def load_intro_scene(self, map_number = None, protaganist_object = None):
        self.intro_scene = ImageTk.PhotoImage(Image.open('intro_scenes/intro_scene'+str(map_number)+'.png').resize((root.winfo_screenwidth(),root.winfo_screenheight())))
        self.intro_canvas = tk.Canvas(root, width = root.winfo_screenwidth(), bg = 'black', highlightthickness = 0, height = root.winfo_screenheight())
        self.intro_canvas.create_image(0,0, image =self.intro_scene, anchor = 'nw')
        self.intro_canvas.pack(side = 'top')
        filename = 'intro_scene_texts/intro_scene_text'+str(map_number)+'.txt'
        with open(filename) as f:
            text = f.read()
        self.intro_text = tk.Label(root, text = text, wraplength = root.winfo_screenwidth()-90, bg = 'black', fg = 'indianred', font = ('kokonor', 18))
        self.intro_canvas.create_window(root.winfo_screenwidth()/2, root.winfo_screenheight()-180, anchor='s', window = self.intro_text)
# CONT OR SAVE BUTTONS        
        self.start_area_button = tk.Button(root, text = 'Start Area', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda n = map_number, po = protaganist_object : self.create_map_curs_context(n,po))
        self.intro_canvas.create_window(root.winfo_screenwidth()/2-100, root.winfo_screenheight()-80, anchor='s', window = self.start_area_button)
        
    # ONLY CALLED IN 2 PLAYER MODE
    def choose_map(self):
        self.choosemap = tk.Label(root, text = 'Choose Map', fg = 'tan3', bg = 'black', font = ('chalkduster', 38))
        self.choosemap.pack()
        # CHOOSE MAPS
        maps = [m for r,d,m in walk('./2_player_map_portraits')][0]
        maps = [m for m in maps[:] if m[0] != '.']
        self.map_button_list = []
        self.tmp_mapimg_dict = {}
        for i,map in enumerate(maps):
            b = tk.Button(root)
            cmd = lambda indx = i : self.map_choice_cleanup(indx)
            photo = ImageTk.PhotoImage(Image.open('./2_player_map_portraits/' + map).resize((300,300)))
            self.tmp_mapimg_dict['map'+str(i)] = photo
            b.config(image = self.tmp_mapimg_dict['map'+str(i)], bg = 'black', highlightbackground = 'tan3', command = cmd)
            # DEBUG packing will have to be fixed here for different screen sizes
            b.pack(side = 'left', padx = 55)
            self.map_button_list.append(b)
        
    def map_choice_cleanup(self, map_number):
        self.two_player_map_num = map_number
        self.choosemap.destroy()
        del self.tmp_mapimg_dict
        for b in self.map_button_list:
            b.destroy()
        del self.map_button_list
        self.choose_witch(player_num = 1)
#         self.create_map_curs_context(map_number)
        
        
        # IF PROTAG, LOAD PROTAG AND DO NOT RE-INIT WITCH
    def create_map_curs_context(self, map_number, protaganist_object = None):
        global curs_pos, grid_pos
        self.map_number = map_number
        try: self.intro_canvas.destroy()
        except: pass
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
        self.coords = [[x,y] for x in range(self.map_width//100) for y in range(self.map_height//100)]
        # START LOC
        if self.num_players == 1:
            self.start_loc = eval(self.map_info[2])
        else:
            self.start_loc = eval(self.map_info[2])[0]
            self.p2_start_loc = eval(self.map_info[2])[1]
        # LOAD MAP / GRID INFO / IMPASSABLE TERRAIN
        terrain = eval(self.map_info[3])
        for coord in terrain:
            self.grid[coord[0]][coord[1]] = 'block'
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
            topfname = '1_player_map_tops/'
        else:
            fname = '2_player_maps/'
            topfname = '2_player_map_tops/'
        self.map_bottom_image = Image.open(fname + 'map'+str(map_number)+'.png')
        self.map_bottom = ImageTk.PhotoImage(self.map_bottom_image)
#         self.map_bottom = ImageTk.PhotoImage(Image.open(fname + 'map'+str(map_number)+'.png'))
#         self.image_holder.append(map_bottom)
        self.map_top_image = Image.open(topfname + 'map_top'+str(map_number)+'.png')
        self.map_top = ImageTk.PhotoImage(self.map_top_image)
        self.canvas.create_image(0, 0, anchor='nw', image= self.map_bottom, tags=('mapbottom','map'))
        self.canvas.create_image(0, 0, anchor='nw', image= self.map_top, tags = ('maptop','map'))
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.vis_dict['cursor'] = Vis(name = 'cursor', loc = [0,0])
        curs_pos = [0,0]
        grid_pos = [0,0]
        self.canvas.create_image(0, 0, image=self.cursor_img, tags='cursor')
        # CHOOSE WITCH IF 2 PLAYER OR FIRST LEVEL
        if protaganist_object:
            self.load_witch(witch = protaganist_object.name, player_num = 1, protaganist_object = protaganist_object)
        else:# LOADING FIRST LEVEL, NOT SAVE GAME
            self.load_witch(witch = self.p1_witch, player_num = 1, protaganist_object = None)
#             self.choose_witch()
        
    # Called twice for 2player mode, first call defaults to first player choice, second call passes player_num = 2
    def choose_witch(self, player_num = 1):
        self.avatar_popup = tk.Toplevel(root)
        self.avatar_popup.attributes('-topmost', 'true')
        self.avatar_popup.attributes("-fullscreen", True)
        self.avatar_popup.config(bg = 'black')
#         self.avatar_popup.grab_set()
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
            # change below to call load_map_trigger(witchname)
            if player_num == 1 and self.num_players == 2:
                def wrap(somePartial, witch_name):
                    self.p1_witch = witch_name
                    somePartial()
                p1 = partial(self.choose_witch, player_num = 2)
                p = partial(wrap, p1, witch[:-4])
            elif player_num == 2 and self.num_players == 2:
                def wrap(somePartial, witch_name):
                    self.p2_witch = witch_name
                    somePartial()
                p1 = partial(self.create_map_curs_context, map_number = self.two_player_map_num)
                p = partial(wrap, p1, witch[:-4])
            else:
                p = partial(self.load_map_triggers, map_number = 0, witch = witch[:-4])
#             p = partial(self.load_witch, witch[:-4], player_num)
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
        
    def load_witch(self, witch = None, player_num = None, protaganist_object = None):
        if player_num == 1:
            self.p1_witch = witch
            if self.num_players == 2:
                loc = [2,2]
            else:
                loc = self.start_loc
        elif player_num == 2:
            self.p2_witch = witch
            loc = self.p2_start_loc
        # if protaganist_object, instead load its data, RE-INIT IMAGES THAT CANNOT BE SERIALIZED BY PICKLE DUMP
        # changing from pickle to 'write attrs to encoded text file'... DEBUG
        if protaganist_object:
            protaganist_object.loc = loc[:]
            witch_img = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png'))
            protaganist_object.img = witch_img
            protaganist_object.init_normal_anims()
            self.ent_dict[witch] = protaganist_object
        else:
            witch_img = ImageTk.PhotoImage(Image.open('avatars/' + witch +'.png'))
            self.ent_dict[witch] = Witch(name = witch, img = witch_img, loc = loc, owner = 'p' + str(player_num))
        self.canvas.create_image(self.ent_dict[witch].loc[0]*100+50-self.moved_right, self.ent_dict[witch].loc[1]*100+50-self.moved_down, image = self.ent_dict[witch].img, tags = self.ent_dict[witch].tags)
        self.grid[self.ent_dict[witch].loc[0]][self.ent_dict[witch].loc[1]] = witch
        # EXIT FOR 1 PLAYER
        if self.num_players == 1:
            # DEBUG LOAD BOT ENEMIES FOR PLAYER 1 HERE
            # LOAD 1 PLAYER MAP BOT UNITS
            lst = self.map_info[4:]
            c1 = 0
            end = len(lst)
            itlst = iter(lst)
            for x in itlst:
                img = eval(x)
                ent = eval(next(itlst))
                self.ent_dict[ent.number] = ent
                self.canvas.create_image(ent.loc[0]*100+50, ent.loc[1]*100+50, image = ent.img, tags = ent.tags)
                self.grid[self.ent_dict[ent.number].loc[0]][self.ent_dict[ent.number].loc[1]] = ent.number
                c1 += 1
                if c1 == end:
                    break
            root.after(999, self.start_turn)
            root.after(999, self.rebind_all)
            self.animate()
            self.map_trigger_loop()
        # CHOOSE SECOND PLAYER WITCH
        elif self.num_players == 2 and player_num == 1:# and self.p2_witch == '':
            self.load_witch(witch = self.p2_witch, player_num = 2)
#             self.choose_witch(player_num = 2)
        # EXIT CHOOSING IF BOTH FINISHED AND START TURN
        else: #self.num_players == 2 and self.p2_witch != '':
            self.start_turn()
            self.animate()
        
            
    def start_turn(self):
        p = self.active_player
        ents_list = [v for k,v in app.ent_dict.items() if v.owner == p]
        ent = ents_list[0]
        self.sot_loop(ent, ents_list)
        
    def sot_loop(self, ent, ents_list):
        ef_list = [v for k,v in ent.effects_dict.items()]
        if ef_list != []:
            ef = ef_list[0]
            self.sot_effects_loop(ef, ef_list, ent, ents_list)
        else: # NO EFFECTS FOR ENT, POP ENT_LIST, CHECK IF EMPTY, CONTINUE OR FINISH_START_TURN
            ents_list = ents_list[1:]
            if ents_list != []:
                ent = ents_list[0]
                self.sot_loop(ent, ents_list)
            else: # ENTS_LIST EMPTY, FINISH_START_TURN
                self.finish_start_turn()
            
    def sot_effects_loop(self, ef, ef_list, ent, ents_list):
        k = [k for k,v in self.ent_dict.items() if v == ent]
        if ef.sot_func() != None:
            self.get_focus(k[0])
            if ent.spirit <= 0: # ENT KILLED, DO NOT EXEC ANY MORE OF ITS EFFECTS, POP ENTS LIST OR EXIT
                root.after(1999, lambda e = k[0] : self.kill(e))
                ents_list = ents_list[1:]
                if ents_list != []:
                    root.after(1666, lambda t = 'text' : app.canvas.delete(t))
                    root.after(1999, lambda e = ents_list[0], el = ents_list : self.sot_eot_loop(e, el))
                else: # NO MORE ENTS, FINISH_START_TURN
                    root.after(1333, self.finish_start_turn)
            else:# CONTINUE PROCESSING THIS EFFECT 
                # CHECK IF EFFECT DURATION ENDS AND CALL UNDO IF SO, no durating for sot_effects
#                 ef.duration -= 1
#                 if ef.duration <= 0:
#                     ef.undo()
#                     key = [k for k,v in ent.effects_dict.items() if v == ef]
#                     del ent.effects_dict[key[0]]
                # MORE EFFECTS?
                ef_list = ef_list[1:]
                if ef_list != []: # MORE EFFECTS FOR THIS ENT
                    root.after(1666, lambda t = 'text' : self.canvas.delete(t))
                    root.after(1999, lambda ef = ef_list[0], efl = ef_list, en = ent, enl = ents_list : self.sot_effects_loop(ef, efl, en, enl))
                else: # NO MORE FOR THIS ENT, CHECK IF MORE ENTS
                    ents_list = ents_list[1:]
                    if ents_list != []: # MORE ENTS TO PROCESS EFFECTS FOR
                        root.after(1666, lambda t = 'text' : app.canvas.delete(t))
                        root.after(1999, lambda e = ents_list[0], el = ents_list : self.sot_loop(e, el))
                    else: # NO MORE ENTS, FINISH_END_TURN
                        root.after(1333, self.finish_start_turn)
        else:
            # CHECK IF EFFECT DURATION ENDS AND CALL UNDO IF SO, no durating for sot_effects
#             ef.duration -= 1
#             if ef.duration <= 0:
#                 ef.undo()
#                 key = [k for k,v in ent.effects_dict.items() if v == ef]
#                 del ent.effects_dict[key[0]]
            # MORE EFFECTS?
            ef_list = ef_list[1:]
            if ef_list != []: # MORE EFFECTS FOR THIS ENT
#                 root.after(999, lambda t = 'text' : self.canvas.delete(t))
#                 root.after(1333, lambda ef = ef_list[0], efl = ef_list, en = ent, enl = ents_list : 
                self.sot_effects_loop(ef_list[0], ef_list, ent, ents_list)
            else: # NO MORE FOR THIS ENT, CHECK IF MORE ENTS
                ents_list = ents_list[1:]
                if ents_list != []: # MORE ENTS TO PROCESS EFFECTS FOR
#                     root.after(999, lambda e = ents_list[0], el = ents_list : 
                    self.sot_loop(ents_list[0], ents_list)
                else: # NO MORE ENTS, FINISH_END_TURN
#                     root.after(999, 
                    self.finish_start_turn()
        
        
    def finish_start_turn(self):
        p = self.active_player
        if self.num_players == 1 and p == 'p1':
            self.rebind_all()
            self.get_focus(self.p1_witch)
        elif self.num_players == 2:
            self.rebind_all()
            w = self.p1_witch if p == 'p1' else self.p2_witch
            self.get_focus(w)
        elif self.num_players == 1 and p == 'p2':
            to_act = [x for x in self.ent_dict.keys() if self.ent_dict[x].owner == 'p2']
            root.after(1666, lambda ents = to_act : self.do_ai_loop(ents))
        
        
    # fix 'only some ents waiting' causes 'no enemies to act' text to appear
    def do_ai_loop(self, ents):
        global grid_pos
        if ents == []:
            waiting_status = [v.waiting for k,v in self.ent_dict.items() if v.owner == 'p2']
            if False not in waiting_status: # ARE ALL ENTS WAITING
                self.canvas.create_text(grid_pos[0]*100+50-self.moved_right, grid_pos[1]*100+50-self.moved_down, text = 'No Enemies to Act...', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
                root.after(1999, lambda t = 'text' : self.canvas.delete(t))
            root.after(1999, self.end_turn)
        else:
        # CHECK FOR ENTS THAT DIED DURING AN AI ENT TURN
            for e in ents[:]:
                if e not in app.ent_dict.keys():
                    ents.remove(e)
            if ents == []:
                root.after(1666, self.end_turn)
            else:
                ent = ents[0]
                if self.ent_dict[ent].waiting == True: # IS THIS ENT WAITING
                    waiting_status = [v.waiting for k,v in self.ent_dict.items() if v.owner == 'p2']
                    if False not in waiting_status: # ARE ALL ENTS WAITING
                        self.canvas.create_text(grid_pos[0]*100+50-self.moved_right, grid_pos[1]*100+50-self.moved_down, text = 'No Enemies to Act...', font = ('Andale Mono', 16), fill = 'white', tags = 'text')
                        root.after(1999, lambda t = 'text' : self.canvas.delete(t))
                        root.after(1999, self.end_turn)
                    else: # CONTINUE WITH ENTS NOT WAITING
                        ents = ents[1:]
        #                 if ents == []:
        #                     self.end_turn()
        #                 else:
                        self.do_ai_loop(ents)
                else:
                    self.get_focus(ent)
                    if self.ent_dict[ent].name == 'Undead':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Orc_Axeman':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Tortured_Soul':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Troll':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Undead_Knight':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Revenant':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Ghost':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Minotaur':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'White_Dragon':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Warlock':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Kensai':
                        self.ent_dict[ent].times_attacked = 0
                        self.ent_dict[ent].attacked_ids = []
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Barbarian':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Sorceress':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Fire_Mage':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Fire_Elemental':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Earth_Mage':
                        self.ent_dict[ent].do_ai(ents)
                    elif self.ent_dict[ent].name == 'Earth_Elemental':
                        self.ent_dict[ent].do_ai(ents)
        
        
        
    def end_turn(self):
        self.unbind_all()
        self.depop_context(event = None)
        # first do EOT loop, rest of this becomes finish_end_turn()
        # get list of all ents, pass in first ent, loop pops front and calls 
        # handle global effects
        g_effects = [k for k in self.global_effects_dict.keys()]
        self.g_effect_loop(g_effects)
        
    def g_effect_loop(self, g_effects):
        if g_effects == []:
            ents_list = [v for k,v in self.ent_dict.items() if v.owner == self.active_player]
            if ents_list == []:
                self.finish_end_turn()
            else:
                self.eot_loop(ents_list[0], ents_list)
        else:
            key = g_effects[0]
            ef = self.global_effects_dict[key]
            if ef.eot_func() != None:
                # check if things need to die
                pass
            else:
                ef.duration -= 1
                if ef.duration <= 0:
                    if ef.undo() != None:
                        del self.global_effects_dict[key]
                        g_effects = g_effects[1:]
                        root.after(2666, lambda g = g_effects : self.g_effect_loop(g))
                    else:
                        del self.global_effects_dict[key]
                        g_effects = g_effects[1:]
                        self.g_effect_loop(g_effects)
                else:
                    g_effects = g_effects[1:]
                    self.g_effect_loop(g_effects)
        
        
    # HANDLE EACH ENT BY PASSING ENT AND ITS EFFECTS TO EFFECTS_LOOP
    def eot_loop(self, ent, ents_list):
        ef_list = [v for k,v in ent.effects_dict.items()]
        if ef_list != []:
            ef = ef_list[0]
            self.effects_loop(ef, ef_list, ent, ents_list)
        else: # NO EFFECTS FOR ENT, POP ENT_LIST, CHECK IF EMPTY, CONTINUE OR FINISH_END_TURN
            ents_list = ents_list[1:]
            if ents_list != []:
                ent = ents_list[0]
                self.eot_loop(ent, ents_list)
            else: # ENTS_LIST EMPTY, FINISH_END_TURN
                self.finish_end_turn()
            
    # when effect exec returns None, still need to durate, check for undo, check for more effects
    # exec an ef.eot_func, pop ef_list continue
    def effects_loop(self, ef, ef_list, ent, ents_list):
        k = [k for k,v in self.ent_dict.items() if v == ent]
        if ef.eot_func() != None:
            self.get_focus(k[0])
            if ent.spirit <= 0: # ENT KILLED, DO NOT EXEC ANY MORE OF ITS EFFECTS, POP ENTS LIST OR EXIT
                root.after(1333, lambda e = k[0] : self.kill(e))
                ents_list = ents_list[1:]
                if ents_list != []:
                    root.after(1111, lambda t = 'text' : app.canvas.delete(t))
                    root.after(1333, lambda e = ents_list[0], el = ents_list : self.eot_loop(e, el))
                else: # NO MORE ENTS, FINISH_END_TURN
                    root.after(1333, self.finish_end_turn)
            else:# CONTINUE PROCESSING THIS EFFECT 
                # CHECK IF EFFECT DURATION ENDS AND CALL UNDO IF SO
                ef.duration -= 1
                if ef.duration <= 0:
                    ef.undo()
                    key = [k for k,v in ent.effects_dict.items() if v == ef]
                    del ent.effects_dict[key[0]]
                # MORE EFFECTS?
                ef_list = ef_list[1:]
                if ef_list != []: # MORE EFFECTS FOR THIS ENT
                    root.after(1111, lambda t = 'text' : self.canvas.delete(t))
                    root.after(1333, lambda ef = ef_list[0], efl = ef_list, en = ent, enl = ents_list : self.effects_loop(ef, efl, en, enl))
                else: # NO MORE FOR THIS ENT, CHECK IF MORE ENTS
                    ents_list = ents_list[1:]
                    if ents_list != []: # MORE ENTS TO PROCESS EFFECTS FOR
                        root.after(1111, lambda t = 'text' : app.canvas.delete(t))
                        root.after(1333, lambda e = ents_list[0], el = ents_list : self.eot_loop(e, el))
                    else: # NO MORE ENTS, FINISH_END_TURN
                        root.after(1333, self.finish_end_turn)
        else:
            # CHECK IF EFFECT DURATION ENDS AND CALL UNDO IF SO
            ef.duration -= 1
            if ef.duration <= 0:
                ef.undo()
                key = [k for k,v in ent.effects_dict.items() if v == ef]
                del ent.effects_dict[key[0]]
            # MORE EFFECTS?
            ef_list = ef_list[1:]
            if ef_list != []: # MORE EFFECTS FOR THIS ENT
#                 root.after(999, lambda t = 'text' : self.canvas.delete(t))
#                 root.after(1333, lambda ef = ef_list[0], efl = ef_list, en = ent, enl = ents_list : 
                self.effects_loop(ef_list[0], ef_list, ent, ents_list)
            else: # NO MORE FOR THIS ENT, CHECK IF MORE ENTS
                ents_list = ents_list[1:]
                if ents_list != []: # MORE ENTS TO PROCESS EFFECTS FOR
#                     root.after(999, lambda e = ents_list[0], el = ents_list : 
                    self.eot_loop(ents_list[0], ents_list)
                else: # NO MORE ENTS, FINISH_END_TURN
#                     root.after(999, 
                    self.finish_end_turn()
                
                    
    def finish_end_turn(self):
        self.canvas.delete('text') # deletes the last text object when exiting loops
        ents = [v for k,v in self.ent_dict.items()]
        for ent in ents:
            # RESET SPELLS / MOVEMENT / ATTACKS
            ent.move_used = False
            if isinstance(ent, Witch):
                ent.cantrip_used = False
                ent.arcane_used = False
                ent.summon_used = False
            elif isinstance(ent, Summon):
                ent.attack_used = False
        if self.active_player == 'p1':
            self.unbind_all()
            self.active_player = 'p2'
        elif self.active_player == 'p2':
            app.turn_counter += 1
            self.active_player = 'p1'
        self.start_turn()
                    
                    
    def get_focus(self, w):
        while grid_pos[0] < self.ent_dict[w].loc[0]:
            self.move_curs(dir = 'Right')
        while grid_pos[0] > self.ent_dict[w].loc[0]:
            self.move_curs(dir = 'Left')
        while grid_pos[1] < self.ent_dict[w].loc[1]:
            self.move_curs(dir = 'Down')
        while grid_pos[1] > self.ent_dict[w].loc[1]:
            self.move_curs(dir = 'Up')
            
    def focus_square(self, s):
        while grid_pos[0] < s[0]:
            self.move_curs(dir = 'Right')
        while grid_pos[0] > s[0]:
            self.move_curs(dir = 'Left')
        while grid_pos[1] < s[1]:
            self.move_curs(dir = 'Down')
        while grid_pos[1] > s[1]:
            self.move_curs(dir = 'Up')
    
        
    def animate(self):
        global selected, selected_vis
        for ent in self.ent_dict.keys():
            if ent not in selected:
                self.ent_dict[ent].rotate_image()
                self.canvas.delete(ent)
                self.canvas.create_image(self.ent_dict[ent].loc[0]*100+50-self.moved_right, self.ent_dict[ent].loc[1]*100+50-self.moved_down, image = self.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
                
                app.canvas.tag_lower((app.ent_dict[ent].tags), 'maptop')
#                 try: app.canvas.tag_lower((app.ent_dict[ent].tags), ('fog'))
#                 except: pass
        for sqr in self.sqr_dict.keys():
            self.sqr_dict[sqr].rotate_image()
            self.canvas.delete(sqr)
            self.canvas.create_image(self.sqr_dict[sqr].loc[0]*100+50-self.moved_right, self.sqr_dict[sqr].loc[1]*100+50-self.moved_down, image = self.sqr_dict[sqr].img, tags = sqr)
        try: app.canvas.tag_raise('large')
        except: pass
#         app.canvas.tag_raise('maptop')
        app.canvas.tag_raise('cursor')
        for vis in self.vis_dict.keys():
            if vis != selected_vis:
            
                self.vis_dict[vis].rotate_image()
                self.canvas.delete(vis)
                if vis == 'cursor':
                    self.canvas.create_image(self.vis_dict[vis].loc[0]*100+50, self.vis_dict[vis].loc[1]*100+50, image = self.vis_dict[vis].img, tags = vis)
                else:
                    self.canvas.create_image(self.vis_dict[vis].loc[0]*100+50-self.moved_right, self.vis_dict[vis].loc[1]*100+50-self.moved_down, image = self.vis_dict[vis].img, tags = vis)
                    
                app.canvas.tag_raise(vis)
        try: # LOWER THE CURSOR BELOW MOVING ANIMATIONS (VIS)
            app.canvas.tag_lower(('cursor'), (selected_vis))
        except: pass
        try: app.canvas.tag_raise('text')
        except: pass
#         try: app.canvas.tag_raise('fog')
#         except: pass
        self.animate_id = root.after(300, self.animate)
        
        # MAP TRIGGER LOOP
        # ALL MAP TRIGGERS ARE FUNCTIONS THAT CHECK FOR CONDITIONS AND EITHER DO STUFF IN RESPONSE
        # OR IF THEY RETURN 'victory', END LEVEL
    # need to make specific for each level
    def map_trigger_loop(self):
        if self.map_number == 0:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level()
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 1:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level()
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 2:
            for mt in self.map_triggers:
                result = mt()
                if result == 'stairway':
                    app.unbind_all()
                    self.end_level(alt_route = 21)
                    break
                elif result == 'door':
                    app.unbind_all()
                    self.end_level(alt_route = 121)
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 121:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level() # next map is 122 on this route
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 21:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level() # next map is 22 on this route
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 22:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level(alt_route = 3) 
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 122:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level(alt_route = 3) 
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 3:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level()
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        elif self.map_number == 4:
            for mt in self.map_triggers:
                result = mt()
                if result == 'victory':
                    app.unbind_all()
                    self.end_level()
                    break
                elif result == 'game over':
                    self.reset()
                    break
            else:
                self.map_trigger_id = root.after(1666, self.map_trigger_loop)
        
    def end_level(self, alt_route = None):
        global curs_pos, is_object_selected, selected, selected_vis, map_pos, grid_pos
        root.after_cancel(self.animate_id)
        root.after_cancel(self.map_trigger_id)
        # for each effect in witch and global, call its undo
        
        protaganist_object  = app.ent_dict[self.p1_witch]
        protaganist_object.reset_transient_vars()
        if alt_route:
            prev_map_num = int(self.map[3:])
            new_map_num = alt_route
        else:
            prev_map_num = int(self.map[3:])
            new_map_num = prev_map_num + 1
        for child in root.winfo_children():
            child.destroy()
        # THIS WORKS, JUST NEED TO CLEAN ALL VARS LIKE GRID, SELF.STUFF, GLOBALS
        # GLOBALS
        curs_pos = [2, 2]
        is_object_selected = False
        selected = []
        selected_vis = ''
        map_pos = [0, 0]
        grid_pos = [0,0]
        
        self.ent_dict = {}
        self.sqr_dict = {}
        self.vis_dict = {}
        self.image_holder = []
        self.map_triggers = []
        self.active_player = 'p1'
        self.moved_right = 0
        self.moved_down = 0
        self.context_buttons = []
        self.help_buttons = []
        # list to hold entity that is being animated as 'attacking'
        self.attacking = []
        self.turn_counter = 0
        self.effects_counter = 0 # used for uniquely naming Effects with the same prefix/name
        # CALL IN-BETWEEN LEVEL SCREEN / VICTORY SCREEN
        # GIVE ANY STORYLINE RELATED TO FINISHED AND NEXT LEVEL
        # GIVE OPTION TO SAVE PROGRESS
        # WILL NEED, AT SOME POINT, TO SAVE ACTUAL WITCH OBJECT (NOT JUST STRING NAME), TO HOLD PERSISTENT CHANGES
        self.load_cutscene(prev_map_num, new_map_num, protaganist_object)
        
        
    def load_cutscene(self, prev_map_num, new_map_num, protaganist_object):
        # Make cutscene using background pictures and overlay unit models
        self.cut_scene = ImageTk.PhotoImage(Image.open('cut_scenes/cut_scene'+str(prev_map_num)+'.png').resize((root.winfo_screenwidth(),root.winfo_screenheight())))
        self.cut_canvas = tk.Canvas(root, width = root.winfo_screenwidth(), bg = 'black', highlightthickness = 0, height = root.winfo_screenheight())
        self.cut_canvas.create_image(0,0, image =self.cut_scene, anchor = 'nw')
        self.cut_canvas.pack(side = 'top')
        filename = 'cut_scene_texts/cut_scene_text'+str(prev_map_num)+'.txt'
        with open(filename) as f:
            text = f.read()
        self.cut_text = tk.Label(root, text = text, wraplength = root.winfo_screenwidth()-90, bg = 'black', fg = 'indianred', font = ('kokonor', 18))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2, root.winfo_screenheight()-180, anchor='s', window = self.cut_text)
# CONT OR SAVE BUTTONS        
        self.next_area_button = tk.Button(root, text = 'Next Area', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda n = new_map_num, po = protaganist_object : self.next_area(n,po))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2-100, root.winfo_screenheight()-80, anchor='s', window = self.next_area_button)
        self.save_game_button = tk.Button(root, text = 'Save Game', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda n = new_map_num, po = protaganist_object : self.save_game(n, po))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2+100, root.winfo_screenheight()-80, anchor='s', window = self.save_game_button)
        
    def next_area(self, new_map_num, protaganist_object):
        self.cut_canvas.destroy()
        # LOAD NEXT MAP
        self.load_map_triggers(new_map_num, protaganist_object)
        
    def save_game(self, new_map_num, protaganist_object):
        protaganist_object.current_area = new_map_num
        # make text input, put in cut_canvas with create_window
        self.save_game_button.destroy()
        text_var = tk.StringVar()
        text_var.set('filename')
        entry = tk.Entry(root, textvariable = text_var, font = ('Andale Mono', 15), highlightbackground = 'black')
        save_b = tk.Button(root, text = 'Save', font = ('chalkduster', 22), fg = 'tan3', highlightbackground = 'black', command = lambda t = text_var, p = protaganist_object : self.do_save(t, p))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2+100, root.winfo_screenheight()-45, anchor='s', window = save_b)
        self.cut_canvas.create_window(root.winfo_screenwidth()/2+100, root.winfo_screenheight()-80, anchor='s', window = entry)
        
        
        # change from using pickle dump to write to text file, on load decode the written gibberish (make it gibberish in stored form)
    def do_save(self, text_var, protag_obj):
        fname = text_var.get()
        saves = [s for r,d,s in walk('./save_games')][0]
        saves = [s for s in saves[:] if s[0] != '.']
        if fname in saves:
            text_var.set('filename already exists')
            return
        with open('save_games/'+fname, 'w+') as f:
            text_var.set('game saved')
            ####********
            # strip attrs, write all spell names to file
            f.write(protag_obj.name+'\n')
            f.write(str(list(protag_obj.cantrip_dict.keys()))+'\n')
            f.write(str(list(protag_obj.arcane_dict.keys()))+'\n')
            f.write(str(protag_obj.summon_cap)+'\n')
            f.write(str(protag_obj.base_str)+'\n')
            f.write(str(protag_obj.base_agl)+'\n')
            f.write(str(protag_obj.base_end)+'\n')
            f.write(str(protag_obj.base_dodge)+'\n')
            f.write(str(protag_obj.base_psyche)+'\n')
            f.write(str(protag_obj.base_spirit)+'\n')
            f.write(str(protag_obj.base_magick)+'\n')
            f.write(str(protag_obj.current_area)+'\n')
            ####********
#             have to strip tkinter objects from protag obj
#             protag_obj.img = None
#             protag_obj.anim_dict = {}
            # below, get all needed attributes of protag_obj, do a rudimentary 'encoding' to disguise
            # on load, ensure values are 'legal'
            # 
#             dump(protag_obj, f)
    
    
    def populate_context(self, event):
        e = self.current_pos()
        if e == '' or e == 'block':
            return
        if self.context_buttons != []:
            return
        self.repop_help_buttons()
        expanded_name = e.replace('_',' ')
        # if generic summon (name ends with number), show class name instead ent.name
        try:
            num = int(e[-1])
            expanded_name = self.ent_dict[e].__class__.__name__.replace('_',' ')
        except:
            pass
        # DEBUG make info button into label that holds the info
        self.cntxt_info_bg = ImageTk.PhotoImage(Image.open('page.png'))
        bg = tk.Canvas(self.context_menu, width = 190, height = 363, bg = 'burlywood4', bd=0, relief='raised', highlightthickness=0)
        bg.pack(side = 'top')
        bg.create_image(0,0, image = self.cntxt_info_bg, anchor = 'nw')
        bg.create_text(15, 15, text=expanded_name + '\n' + self.get_info_text(e), width = 190, anchor = 'nw', font = ('chalkduster', 18), fill = 'indianred')
        self.context_buttons.append(bg)
        if self.ent_dict[e].owner == self.active_player:
            act_dict = self.ent_dict[e].actions
            for i, act_call in enumerate(act_dict.items()):
                act = act_call[0]
                call = act_call[1]
                i += 1
                root.bind(str(i), call)
                p = partial(call, None)
                b = tk.Button(self.context_menu, text = str(i) + ' : ' + act, wraplength = 190, font = ('chalkduster', 24), fg = 'tan3', highlightbackground = 'tan3', command = p)
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
        
        # map_pos is how much map has moved [x,y]
        # curs_pos is relative to screen (stays within around [0,0] to [9,6] relative to screen size
        # grid_pos is always absolute position of grid where cursor appears (relates to app.grid)
        if event.keysym == 'Left' or dir == 'Left':
            if curs_pos[0] > 1: # leftmost possible cursor position
                curs_pos[0] -= 1
                grid_pos[0] -= 1
                app.vis_dict['cursor'].loc = curs_pos[:]
                app.canvas.delete('cursor')
                app.canvas.create_image(curs_pos[0]*100+50,curs_pos[1]*100+50, image = app.vis_dict['cursor'].img, tags = 'cursor')
            elif map_pos[0] > 0 : # leftmost possible map position, always zero
                map_pos[0] -= 1
                self.move_map('Left')
                grid_pos[0] -= 1
                
        elif event.keysym == 'Right' or dir == 'Right':
            if grid_pos[0] == ((self.map_width//100) - 1):
                return
            if curs_pos[0] < ((frame_width//100)-1):
                curs_pos[0] += 1
                grid_pos[0] += 1
                app.vis_dict['cursor'].loc = curs_pos[:]
                app.canvas.delete('cursor')
                app.canvas.create_image(curs_pos[0]*100+50,curs_pos[1]*100+50, image = app.vis_dict['cursor'].img, tags = 'cursor')
            elif map_pos[0] < ((self.map_width//100)-(frame_width//100)-1):
                self.move_map('Right')
                map_pos[0] += 1
                grid_pos[0] += 1
        elif event.keysym == 'Up' or dir == 'Up':
            if curs_pos[1] > 1: # topmost
                curs_pos[1] -= 1
                grid_pos[1] -= 1
                app.vis_dict['cursor'].loc = curs_pos[:]
                app.canvas.delete('cursor')
                app.canvas.create_image(curs_pos[0]*100+50,curs_pos[1]*100+50, image = app.vis_dict['cursor'].img, tags = 'cursor')
            elif map_pos[1] > 0: # topmost, always zero
                self.move_map('Down')
                map_pos[1] -= 1
                grid_pos[1] -= 1
        elif event.keysym == 'Down' or dir == 'Down':
            if grid_pos[1] == ((self.map_height//100)-1):
                return
            if curs_pos[1] < ((frame_height//100)-1):
                curs_pos[1] += 1
                grid_pos[1] += 1
                app.vis_dict['cursor'].loc = curs_pos[:]
                app.canvas.delete('cursor')
                app.canvas.create_image(curs_pos[0]*100+50,curs_pos[1]*100+50, image = app.vis_dict['cursor'].img, tags = 'cursor')
            elif map_pos[1] < ((self.map_height//100)-(frame_height//100)-1):
                self.move_map('Up')
                map_pos[1] += 1
                grid_pos[1] += 1

    def move_map(self, direction):
        tmp = self.ent_dict.keys()
        ents = [x for x in tmp if x not in selected]
        pers_vis = [y for y in self.vis_dict.keys() if y != selected_vis]
        if direction == 'Left':
            self.canvas.move('map', 100, 0)
            self.moved_right -= 100
            for ent in ents:
                self.canvas.move(ent, 100, 0)
            for vis in pers_vis:
                self.canvas.move(vis, 100, 0)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 100, 0)
        elif direction == 'Right':
            self.canvas.move('map', -100, 0)
            self.moved_right += 100
            for ent in ents:
                self.canvas.move(ent, -100, 0)
            for vis in pers_vis:
                self.canvas.move(vis, -100, 0)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, -100, 0)
        elif direction == 'Up':
            self.canvas.move('map', 0, -100)
            self.moved_down += 100
            for ent in ents:
                self.canvas.move(ent, 0, -100)
            for vis in pers_vis:
                self.canvas.move(vis, 0,-100)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 0, -100)
        elif direction == 'Down':
            self.canvas.move('map', 0, 100)
            self.moved_down -= 100
            for ent in ents:
                self.canvas.move(ent, 0, 100)
            for vis in pers_vis:
                self.canvas.move(vis, 0, 100)
            for sqr in self.sqr_dict.keys():
                self.canvas.move(sqr, 0, 100)

    # Helper functions
    def help(self):
        self.help_popup = tk.Toplevel()
        self.help_popup.grab_set()
        self.help_popup.attributes('-topmost', 'true')
        help_text = '''
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
        txt += 'Agl:' + str(self.ent_dict[ent].get_attr('agl')) + '\n'
        txt += 'End:' + str(self.ent_dict[ent].get_attr('end')) + '\n'
        txt += 'Dodge:' + str(self.ent_dict[ent].get_attr('dodge')) + '\n'
        txt += 'Psyche:' + str(self.ent_dict[ent].get_attr('psyche')) + '\n'
        txt += 'Spirit:' + str(self.ent_dict[ent].spirit) + '\n'
        if isinstance(self.ent_dict[ent], Witch):# or isinstance(self.ent_dict[ent], Trickster):
            txt += 'Magick:' + str(self.ent_dict[ent].magick) + '\n'
        if isinstance(self.ent_dict[ent], Witch):
            txt += 'Summon Cap: ' + str(self.ent_dict[ent].summon_cap) + '\n'
        for ef in self.ent_dict[ent].effects_dict.keys():
            txt += self.ent_dict[ent].effects_dict[ef].name.replace('_',' ') + '\n'
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
        
        
        # kokonor
    def show_avatar_info(self, witch):
        self.info_popup = tk.Toplevel()
        self.info_popup.grab_set()
        self.info_popup.attributes('-topmost', 'true')
        self.info_popup.title(witch)
        text = open('avatar_info/' + witch + '.txt', 'r').read()
        f = tk.Frame(self.info_popup, bg = 'black')
        f.pack()
        l = tk.Label(f, text = text, wraplength = root.winfo_screenwidth()-90, bg = 'black', fg = 'indianred', font = ('kokonor', 18))
        l.pack()
        close = tk.Button(f, text = 'close', font = ('chalkduster', 24), highlightbackground = 'black', command = lambda win = self.info_popup : self.destroy_release(win))
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
        if app.ent_dict[id].death_trigger() == None:
            return_val = None
        else:
            return_val = 'Not None'
        # DEBUG handle if killing witch
        # If witch is dead, show popup with victory/defeat
        self.canvas.delete(id)
        # destroy surrounding squares of large Ents
        if app.ent_dict[id].type == 'large_bottom':
            app.ent_dict[id].large_undo()
        self.grid[self.ent_dict[id].loc[0]][self.ent_dict[id].loc[1]] = ''
        del self.ent_dict[id]
        return return_val

            
    def unbind_all(self):
        for x in range(10):
            root.unbind(str(x))
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
        # DEBUG ####
#         root.bind('<d>', app.debugger)

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
        self.depop_context(event = None)
#         for b in self.context_buttons:
#             b.destroy()
#         self.repop_help_buttons()
        self.rebind_all()
        
    def repop_help_buttons(self):
        menu_button = tk.Button(self.context_menu, text="Menu", font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command=self.open_menu)
        menu_button.pack(side = 'bottom')
        self.context_buttons.append(menu_button)
        end_turn_button = tk.Button(self.context_menu, text = 'End Turn', font = ('chalkduster', 24), highlightbackground = 'tan3', command = self.confirm_end)
        end_turn_button.pack(side = 'bottom')
        self.context_buttons.append(end_turn_button)
        
    def open_menu(self):
        self.depop_context(event = None)
        self.unbind_all()    
        quit_button = tk.Button(self.context_menu, text="QUIT", font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command=self.confirm_quit)
        quit_button.pack(side = 'bottom')
        self.context_buttons.append(quit_button)
        help_button = tk.Button(self.context_menu, text = 'Help', font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command = self.help)
        help_button.pack(side = 'bottom')
        self.context_buttons.append(help_button)
        close_button = tk.Button(self.context_menu, text = 'Close Menu', font = ('chalkduster', 24), fg='indianred', highlightbackground = 'tan3', command = self.cancel_quit)
        close_button.pack(side = 'bottom')
        self.context_buttons.append(close_button)
        
    # called when you die in 1player mode
    def reset(self):
        from sys import executable, argv
        from os import execl
        python = executable
        execl(python, python, * argv)

        
#     def debugger(self, event):
#         print(app.ent_dict['b2'].base_spirit)
#         print(app.ent_dict['b2'].waiting)

root = tk.Tk()
app = App(master=root)

root.bind('<Right>', app.move_curs)
root.bind('<Left>', app.move_curs)
root.bind('<Up>', app.move_curs)
root.bind('<Down>', app.move_curs)
root.bind('<a>', app.populate_context)
root.bind('<q>', app.depop_context)
app.unbind_all()
# root.bind('<Escape>', app.exit_fullscreen)
#### DEBUG ####
# root.bind('<d>', app.debugger)


root.configure(background = 'black')

root.attributes('-transparent', True)
root.attributes("-fullscreen", True)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))

app.mainloop()