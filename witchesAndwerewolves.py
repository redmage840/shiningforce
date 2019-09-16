# dumb bfs shows weakness, finding random paths that arent very close to shortest

# moveloops and shadows tag_raise or lower

# bricks in wall in maptop cover units, fallen bricks 

# contagion Vis will last longer than it takes to get to next action, either make faster cleanup or wait for cleanup or extend time between AI loop

# move 'choose witch screen' before first 'intro screen'


# orcs now make 'best attempt' to minimize distance when no path can be found
# this still results in moving 'wrong' direction when better paths are blocked by Ents
# instead of 'best attempt to min distance', remove temporary blocks (any Ents) from grid repr, then find path, then iterate over path backwards and move to the first legal sqr, if no legal_moves along path do not move just wait (better than moving wrong direction)
# could be improved by replacing one Ent at a time, find path, then after all paths are accumulated, choose one with greatest distance or that minimizes distance to closest target and move as far as possible along it

# warrior movement encourages engaging everything from 'top -> down', probably should change

# death anims, at least delay before something like contagion

# replace undead ai with orc pathfinding, maybe just leave them dumb...

# orcs need to get focus on move square

# check tag raise/lower priority, some redundancy,  i think its the general Ent do_move or loop

# Units using bfs for pathfinding should make best attempt to minimize distance if no path can be found


# Bards being able to freely replenish magic and having AI units 'wait' until close combines not well, encourages waiting around until built all the way back up. Not only this, but you could stay out of range of triggers and keep on summoning, maybe have a max amount of summons... Enemy triggers would 'see' you as soon as close enough to cast any spell to prevent staying on edge of triggers and using spells.
# with above approach, still encourages waiting outside of triggers until replenished/full summons
# probably better to not have wait triggers, since that encourages slowplay (isolating AI units, drawing them out, waiting until replenished)
# general structure is ALL enemies will begin to advance on protag, this way the structure of difficulty can be controlled by staggering waves of enemies based on initial placement/movement
# this encourages a constant, increasing pace where you are more pressed for 'time', no slow-play
# what would encourage protag to do anything but sit back and wait for the waves?
# moving around the map could influence the structure of waves by outpacing the slower AI units, encouraging the faster ones to engage prematurely
# try and structure level terrain/groups of AI units so that protag cannot continuously 'kite' slow units
# do this by having movement outpace the killing of units, so that you can move to increase distance between slow and faster waves, but eventually be backed into a corner
# still need to stop the possibility of maxing out on bards so you have infi replenish magick, and then can summon infi, can this be prevented just with pressure of approaching enemies?
# if there only exist units that can be outpaced, can just run around and heal and keep summoning or casting
# can this be controlled with 'tight hallway' levels, where you will be quickly backed into a corner?
# a lot of this points to the fact that free magick replenish is problematic
# a hard limit on magick might be preferable

# do entrance finish bard, expand on shadow, maybe change warrior around (moves randomly, moves back and side only 1 space, ...)

# make first level with triggers, undead, orcs, orc leader

# change position of intro_scene text

# add 'start position dependent on map' get from map_info

# AI units have property 'target' (unit they will try to minimize distance to) target is updated under certain conditions or prevented from updating under conditions, will need to check for existence if not updating 'get_target()'

# consider removing 'smoke' from agnes casting anims

# is origin still used without old movement setup?

# in ai_loop have some AI units hold 'state' of either 'active' or 'waiting', when map trigger is met (move closely enough) turn them 'active', when no user units 'close' enough turn to 'waiting'

# what is difference in move_loop and psionic push move loop? psipush is much faster...

# AI can get stuck behind obstacles trying to minimize distance only, needs to pathfind

# doublecast / quick

# place summon could have animations (gradual appearance)

# maybe make dragon attack further 'down' since he doesn't 'see' from his lower square, maybe make range longer, do attack anims

# undead ai chooses a 'closest target' before moving, then after moving if it cannot attack the previously chosen target, it will forgo attacking even if it could now reach another target, this occurs when randomly choosing from equidistant targets to 'move towards' and being unable to reach the one targeted due to obstacles/otherEnts

# would it be possible to 'pause' in the middle of a move_loop or to keep text object on screen

# make unholy chant only show actual gains, do entrance()

# witches need something to do when run out of magick

# make get_info scroll a bit longer to hold more effects

# make AI ent that will bring out the flaw in warriors

# make walking/movement animations

# need better animations for psionic push, gravity

# magick regen rate or squares on maps that regen

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
from pickle import dump, load
from copy import deepcopy
# filehandler = open(filename, 'r') 
# object = pickle.load(filehandler)


# convenience funcs
def dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

# getting to goal but it isnt EMPTY it has the target!
# Need to have goal of empty square within range of target
def bfs(start, goal, grid):
    coords = [[x,y] for x in range(len(grid[0])) for y in range(len(grid[1]))] # get list of coords from gridsize
    path = []
    q = [[start]]
    visited = [start]
    while q:
        path = q[0]
        q = q[1:]
        last = path[-1]
        if dist(last, goal) == 1:
            return path + [goal]
        adj = [c for c in coords if dist(c, last) == 1 and grid[c[0]][c[1]] == '']
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
    def __init__(self, name, info, eot_func, undo, duration):
        self.name = name
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
            if isinstance(self, Witch) or isinstance(self, Trickster):
                self.base_magick = self.magick
            
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
            a = (a*2)*10
        rand = randrange(-1, 102)
        if a > rand:
            return True
        else:
            return False
            
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
        app.unbind_all()
        app.cleanup_squares()
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
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
                app.canvas.tag_lower((self.tags), 'maptop')
#                 app.canvas.tag_lower((self.tags), 'large')
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
            try: app.canvas.tag_raise('large', (self.tags))
            except: pass
#             app.canvas.tag_raise('maptop')
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
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
        app.canvas.create_image(newloc[0]*100+50-app.moved_right, newloc[1]*100+50-app.moved_down, image = self.img, tags = self.tags)
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
        
class Trickster(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Simulacrum':self.simulacrum,'Gateway':self.gateway,'Move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 3
        self.end = 2
        self.dodge = 4
        self.psyche = 5
        self.spirit = 10
        self.magick = 23
        super().__init__(name, img, loc, owner, number)
        
        
    # for vis, maybe get image of target...
    # simu anims would be just a bunch of opaque 'glass' / greyscale opacity
    # then grab 2 copies of target image, drag one left, one right across the opacity
    # target gets + 4 dodge effect, lasts 3 turns
    # have to resize for larger units
    # create_image the targets image with 'left' tag
    # create_image simulacrum anim(img) with 'left' tag
    # create_image the targets image with 'right' tag
    # create_image simulacrum anim(img) with 'right' tag
    # move each in loop by tag
    def simulacrum(self, event):
        if self.attack_used == True or self.magick < 3:
            return
        app.depop_context(event = None)
        root.bind('<q>', self.cleanup_simulacrum)
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in coords if dist(self.loc, s) <= 4]
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
        self.set_attr('magick', -4)
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.attack_used = True
        # DO SIMULACRUM EFFECTS
        def simulacrum_effect(stat):
            stat += 4
            return stat
        f = simulacrum_effect
        app.ent_dict[id].dodge_effects.append(f)
        def un(i):
            app.ent_dict[i].dodge_effects.remove(simulacrum_effect)
        p = partial(un, id)
        def nothing():
            return None
        eot = nothing
        n = 'Simulacrum' + str(app.effects_counter)
        app.ent_dict[id].effects_dict['Simulacrum'] = Effect(name = 'Simulacrum', info = 'Simulacrum\nDodge incr by 4 for 3 turns', eot_func = eot, undo = p, duration = 3)
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
        # end loc is not another sqr just an offset to X coord (not Y), but 2 X offsets (going in each direction)
        end_left = start_loc[0]*100-app.moved_right # minus 50 from center
        end_right = start_loc[0]*100+100-app.moved_right # plus 50 from center
#         endy = sqr[1]*100+50-app.moved_down
        # prevent animation from redrawing at start_loc
#         selected = id
        selected_vis = 'Simulacrum'
        # will need two loops maybe
        # just moving the created images of target (not redrawing or preventing redraw of original)
        # each 'left' and 'right' vis image needs to be rotated, deleted, and redrawn (not moved)
        def simulacrum_loop_left(vis, x, y, end_left, tar):
            if x % 5 == 0: # this just gets new image (flickers simulacrum opacity)
                app.vis_dict[vis].rotate_image()
                app.canvas.delete('left') # this deletes both vis left and right
#                 app.canvas.delete(ent)
                app.canvas.create_image(x, y, image = app.ent_dict[tar].img, tags = 'left')
                app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = ('Simulacrum','left'))
#                 app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
            app.canvas.tag_raise(vis)
            # end_left always starts less than x
            if x > end_left:
                x -= 10
                app.canvas.move('left',-10,0)
            if x == end_left:
                pass
#                 root.after(666, self.cleanup_simulacrum)
            else:
                root.after(100, lambda vis = 'Simulacrum', x = x, y = y, end_left = end_left, tar = tar : simulacrum_loop_left(vis, x, y, end_left, tar))
                
        def simulacrum_loop_right(vis, x, y, end_right, tar):
            if x % 5 == 0: # this just gets new image (flickers simulacrum opacity)
                app.vis_dict[vis].rotate_image()
                app.canvas.delete('right') # this deletes both vis left and right
#                 app.canvas.delete(ent)
                app.canvas.create_image(x, y, image = app.ent_dict[tar].img, tags = 'right')
                app.canvas.create_image(x, y, image = app.vis_dict[vis].img, tags = ('Simulacrum','right'))
#                 app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
            app.canvas.tag_raise(vis)
            # end_right always starts greater than x
            if x < end_right:
                x += 10
                app.canvas.move('right',10,0)
            if x == end_right:
                root.after(666, self.cleanup_simulacrum)
            else:
                root.after(100, lambda vis = 'Simulacrum', x = x, y = y, end_right = end_right, tar = tar : simulacrum_loop_right(vis, x, y, end_right, tar))
                
        simulacrum_loop_left('Simulacrum', x, y, end_left, id)
        simulacrum_loop_right('Simulacrum', x, y, end_right, id)
        
        ###############################################################################################
#         app.vis_dict['Simulacrum'] = Vis(name = 'Simulacrum', loc = sqr)
#         app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Simulacrum'].img, tags = 'Simulacrum')
        
    def cleanup_simulacrum(self, event = None):
#         for x in range(1, len(self.spell_dict.keys())+1):
#             root.unbind(str(x))
        app.unbind_all()
        app.rebind_all()
        app.cleanup_squares()
        app.depop_context(event = None)
        app.canvas.delete('left')
        app.canvas.delete('right')
        app.canvas.delete('Simulacrum')
        try: del app.vis_dict['Simulacrum']
        except: pass
        app.canvas.delete('text')
        
        
    def gateway(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<q>')
        root.bind('<q>', self.cleanup_gateway)
        root.unbind('<a>')
        sqrs = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in coord_pairs:
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
        app.depop_context(event = None)
        app.unbind_all()
        app.rebind_all()
        root.unbind('<q>')
        root.unbind('<a>')
        self.attack_used = True
        self.set_attr('magick', -4)
        my_psyche = self.get_attr('psyche')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        distance = damage(my_psyche, target_dodge)
        app.cleanup_squares()
        sqrs = self.doorway_squares(distance)
        if sqrs == []:
            app.canvas.create_text(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+60-app.moved_down, text = 'No Available Area', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(999, self.cleanup_gateway)
        else:
            app.animate_squares(sqrs)
            root.bind('<a>', lambda e, id = id, sqrs = sqrs : self.do_gateway(e, id = id, sqrs = sqrs))
            b = tk.Button(app.context_menu, text = 'Choose Location', font = ('chalkduster', 24), fg = 'tan3', wraplength = 190, highlightbackground = 'tan3', command = lambda e = None, id = id, s = sqrs : self.do_gateway(e, id, s))
            b.pack(side = 'top')
            app.context_buttons.append(b)

    
    #Put VIS IN HERE
    def do_gateway(self, event = None, id = None, sqrs = None):
        if grid_pos not in sqrs:
            return
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        oldloc = app.ent_dict[id].loc[:]
        newloc = grid_pos[:]
        app.vis_dict['Gateway'] = Vis(name = 'Gateway', loc = oldloc[:])
        vis = app.vis_dict['Gateway']
        app.canvas.create_image(oldloc[0]*100+50-app.moved_right, oldloc[1]*100+50-app.moved_down, image = vis.img, tags = 'Gateway')
        root.after(1666, lambda newloc = newloc, id = id : self.finish_gateway(newloc, id))
        
    def finish_gateway(self, newloc, id):
        app.grid[app.ent_dict[id].loc[0]][app.ent_dict[id].loc[1]] = ''
        app.canvas.delete(id)
        app.ent_dict[id].loc = newloc[:]
        app.ent_dict[id].origin = newloc[:]
        app.grid[newloc[0]][newloc[1]] = id
        app.canvas.delete('Gateway')
        try: del app.vis_dict['Gateway']
        except: pass
        app.vis_dict['Gateway'] = Vis(name = 'Gateway', loc = newloc[:])
        vis = app.vis_dict['Gateway']
        root.after(1666, lambda id = id, newloc = newloc : self.place_entity(id, newloc))
        
    def place_entity(self, id, newloc):
        app.canvas.delete('Gateway')
        del app.vis_dict['Gateway']
        app.canvas.create_image(app.ent_dict[id].loc[0]*100+50-app.moved_right, app.ent_dict[id].loc[1]*100+50-app.moved_down, image = app.ent_dict[id].img, tags = app.ent_dict[id].tags)
        root.after(666, self.cleanup_gateway)
    
    def doorway_squares(self, distance):
        sqr_list = []
        coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in coord_pairs:
            if dist(c, self.loc) <= distance: 
                if app.grid[c[0]][c[1]] == '':
                    sqr_list.append(c)
        return sqr_list
    
    def cleanup_gateway(self, event = None):
        try:
            del app.vis_dict['Gateway']
        except: pass
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
        self.agl = 4
        self.end = 3
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
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        app.depop_context(event = None)
        id = app.current_pos()
        app.unbind_all()
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
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


# damages adjacent ents on death
class Plaguebearer(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'pox':self.pox, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 2
        self.end = 5
        self.dodge = 2
        self.psyche = 4
        self.spirit = 9
        super().__init__(name, img, loc, owner, number)
        
    # Override superclass set_attr(self, attr, amount) to check for own death, if no death call superclass set_attr
    def set_attr(self, attr, amount):
        # app.kill is handled by killer effect/attack, just do contagion
        if attr == 'spirit' and self.spirit + amount < 1: # amount is passed int 'negative' for subtracting attrs
            # DO CONTAGION
            # get Ents within AOE
            coord_pairs = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
            sqrs = [c for c in coord_pairs if dist(self.loc, c) == 1]
            ents = [app.grid[s[0]][s[1]] for s in sqrs if app.grid[s[0]][s[1]] != '' and app.grid[s[0]][s[1]] != 'block']
            for e in ents:
                # cannot stack contagion
                ef_names = [v for k,v in app.ent_dict[e].effects_dict.items() if v.name == 'Contagion']
                if 'Contagion' in ef_names:
                    continue
                else:
                    # create Effect, needs name, info, eot_func, undo, duration
                    n = 'Contagion' + str(app.effects_counter)
                    info = 'Contagion\n-2 Str -2 End for 3 turns'
                    def contagion_effect(stat):
                        stat -= 2
                        if stat < 1:
                            return 1
                        else:
                            return stat
                    f = contagion_effect
                    app.ent_dict[e].str_effects.append(f)
                    app.ent_dict[e].end_effects.append(f)
                    def un(id, func):# change to get name of effect, remove by name
#                         name = 'contagion_effect'
                        app.ent_dict[id].str_effects.remove(func)
                        app.ent_dict[id].end_effects.remove(func)
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
                    app.canvas.create_text(app.ent_dict[e].loc[0]*100-app.moved_right+50, app.ent_dict[e].loc[1]*100-app.moved_down+90, text = 'Contagion', justify = 'center', fill = 'white', font = ('Andale Mono', 16), tags = ('text','contagion_text'))# CALLED DURING A SET_ATTR, SO NEED A DIFFERENT TEXT TAG TO AVOID CLEANUP OF UNRELATED TEXT OBJECTS ON CANVAS
                    app.canvas.create_image(app.ent_dict[e].loc[0]*100+50-app.moved_right, app.ent_dict[e].loc[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Contagion')
            root.after(3666, self.cleanup_contagion)
            super(Plaguebearer, self).set_attr(attr, amount)
        else:
            super(Plaguebearer, self).set_attr(attr, amount)
        
    def cleanup_contagion(self):
        try:
            app.canvas.delete('Contagion')
            keys = [k for k,v in app.vis_dict.items() if v.name == 'Contagion']
            for k in keys:
                del app.vis_dict[k]
        except: pass
        app.canvas.delete('contagion_text')
        
    # give all adj units pox Effect if they have no pox effects, causes 2 spirit damage EOT, if affected ent's movement is blocked by obstacles it's movement is reduced by 1 to a minimum of 1, lasts 4 turns
    def pox(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_pox)
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in coords if dist(self.loc, c) == 1]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.do_pox(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Pox', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.do_pox(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_pox(self, event = None, sqrs = None):
        self.attack_used = True
#         self.init_attack_anims()
        app.depop_context(event = None)
        app.unbind_all()
        ents = []
        for s in sqrs:
            ent = app.grid[s[0]][s[1]]
            if ent != '' and ent != 'block' and isinstance(app.ent_dict[ent].__class__, Plaguebearer) == False:
                #GIVE POX EFFECT if doesn't exist
                ef_names = [v.name for k,v in app.ent_dict[ent].effects_dict.items()]
                if 'Pox' not in ef_names:
                    n2 = 'Pox' + str(app.effects_counter) # not an effect, just need unique int
                    app.effects_counter += 1 # that is why this is incr manually here, no Effect init
                    app.vis_dict[n2] = Vis(name = 'Pox', loc = s)
                    rand_start_anim = randrange(1,7)
                    for i in range(rand_start_anim):
                        app.vis_dict[n2].rotate_image()
                    app.canvas.create_image(s[0]*100+50-app.moved_right, s[1]*100+50-app.moved_down, image = app.vis_dict[n2].img, tags = 'Pox')
                    n = 'Pox'+str(app.effects_counter)
                    # needs name, info, eot_func, undo, duration
                    def take_2(tar):
                        app.get_focus(tar)
                        app.ent_dict[tar].set_attr('spirit', -2)
                        app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+60-app.moved_down, text = '2 Spirit\n Damage\nPox', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        return 'Not None'
                    # EOT
                    eot = partial(take_2, ent)
                    # UNDO
                    def un():
                        pass
                    u = un
                    # POX VIS
                    app.ent_dict[ent].effects_dict[n] = Effect(name = 'Pox', info = 'Pox\n2 Spirit damage EOT\n-1 to Entities with normal movement', eot_func = eot , undo = u, duration = 4)
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100-app.moved_right+50, app.ent_dict[ent].loc[1]*100-app.moved_down+90, text = 'Pox', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                
        root.after(1666, self.finish_pox)
        
    def finish_pox(self, event = None):
#         self.init_normal_anims()
        try:
            app.canvas.delete('Pox')
            keys = [k for k in app.vis_dict.keys() if k[:3] == 'Pox']
            for k in keys:
                del app.vis_dict[k]
        except: pass
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
            adj = [c for c in coords if abs(c[0] - loc[0]) + abs(c[1] - loc[1]) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, dist)
        findall(loc, 1, 2) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist



# force units to follow or attack?
# healer / magick recovery?
class Bard(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'Unholy Chant':self.unholy_chant, 'Entrance':self.entrance, 'move':self.move}
        self.attack_used = False
        self.str = 2
        self.agl = 4
        self.end = 2
        self.dodge = 4
        self.psyche = 4
        self.spirit = 11
        super().__init__(name, img, loc, owner, number)
        
        
    # All friendly units within dist2 regain 2 Spirit and 2 Magick, ensure not greater than base
    def unholy_chant(self, event = None):
        if self.attack_used == True:
            return
        root.unbind('<a>')
        root.unbind('<q>')
        root.bind('<q>', self.finish_unholy_chant)
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [c for c in coords if dist(self.loc, c) <= 2]
        app.animate_squares(sqrs)
        app.depop_context(event = None)
        root.bind('<a>', lambda e, s = sqrs : self.do_unholy_chant(event = e, sqrs = s)) 
        b = tk.Button(app.context_menu, text = 'Confirm Unholy Chant', wraplength = 190, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, s = sqrs : self.do_unholy_chant(event = e, sqrs = s))
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
    def do_unholy_chant(self, event = None, sqrs = None):
        self.attack_used = True
#         self.init_attack_anims()
        app.depop_context(event = None)
        app.unbind_all()
        ents = []
        for s in sqrs:
            ent = app.grid[s[0]][s[1]]
            if ent != '' and ent != 'block':
                if app.ent_dict[ent].owner == app.active_player:
                    app.ent_dict[ent].set_attr('spirit', 2)
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100-app.moved_right+50, app.ent_dict[ent].loc[1]*100-app.moved_down+50, text = '+2 Spirit', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
                    if isinstance(app.ent_dict[ent], Witch) or isinstance(app.ent_dict[ent], Trickster):
                        app.ent_dict[ent].set_attr('magick', 2)
                        app.canvas.create_text(app.ent_dict[ent].loc[0]*100-app.moved_right+50, app.ent_dict[ent].loc[1]*100-app.moved_down+70, text = '+2 Magick', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
        root.after(1666, self.finish_unholy_chant)
        
    def finish_unholy_chant(self, event = None):
#         self.init_normal_anims()
        app.rebind_all()
        app.canvas.delete('text')
        app.depop_context(event = None)
        app.cleanup_squares()
    
    
    #
    def entrance(self):
        pass
    
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
        findall(loc, 1, 4) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist
        
        
class White_Dragon(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.white_dragon_attack}
        self.attack_used = False
        self.str = 11
        self.agl = 9
        self.end = 11
        self.dodge = 3
        self.psyche = 8
        self.spirit = 1
#         self.type = 'large'
#         self.movement = 'flying'
        super().__init__(name, img, loc, owner, number, type = 'large')
        # BLOCK SQUARE BELOW
        sqr = [loc[0], loc[1]+1]
        app.grid[sqr[0]][sqr[1]] = self.number

        # For cleanup on death, all large Ents need a function similar
    def large_undo(self):
        app.grid[self.loc[0]][self.loc[1]+1] = ''
        
    def do_white_dragon_ai(self, ents_list):
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
            root.after(666, lambda t = target : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = target : self.white_dragon_attack(el, t))
        else: # EXIT OR MOVE
            mov_sqrs = self.legal_moves()
        # CANNOT MOVE AND COULD NOT ATTACK TARGET NOT WITHIN CURRENT RANGE, GO TO NEXT AI UNIT OR END TURN IF NONE
            if mov_sqrs == []:
                ents_list = ents_list[1:]
                if ents_list == []:
                    app.end_turn()
                else:
                    root.after(1666, lambda e = ents_list : app.do_ai_loop(e))
            else:
        # ATTEMPT MOVE TOWARDS TARGET AND ATTEMPT ATTACK ON TARGET
#                 app.get_focus(target)
                # make focus_square(sqr) which gets focus on a location instead of ent id
                mov_sqrs = self.legal_moves()
                best = mov_sqrs[0]
                min = dist(mov_sqrs[0], app.ent_dict[target].loc)
                for s in mov_sqrs:
                    if dist(s, app.ent_dict[target].loc) < min:
                        best = s
                        min = dist(s, app.ent_dict[target].loc)
                app.after(1333, lambda sqr = best : app.focus_square(sqr))
                app.after(1666, lambda el = ents_list, t = target, sqr = best : self.white_dragon_move(el, t, sqr))
            
    def white_dragon_move(self, ents_list, target, sqr):
        global selected
#         mov_sqrs = self.legal_moves()
#         # AMONG LEGAL MOVES, PICK ONE THAT MINIMIZES DISTANCE BETWEEN SELF AND TARGET
#         best = mov_sqrs[0]
#         min = dist(mov_sqrs[0], app.ent_dict[target].loc)
#         for s in mov_sqrs:
#             if dist(s, app.ent_dict[target].loc) < min:
#                 best = s
#                 min = dist(s, app.ent_dict[target].loc)
        id = self.number
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = sqr[0]*100+50-app.moved_right
        endy = sqr[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = sqr[:]
        selected = self.number
        # MOVE LOOP
        # get focus here?
        def move_loop(id, x, y, endx, endy, start_sqr, end_sqr):
            if x % 25 == 0 or y % 25 == 0:
                self.rotate_image()
                app.canvas.delete(id)
                app.canvas.create_image(x, y, image = self.img, tags = self.tags)
                app.canvas.tag_lower((self.tags), 'maptop')
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
#             app.canvas.tag_raise('large', (self.tags))
#             app.canvas.tag_raise('maptop')
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr, target, ents_list) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
            
            
    def finish_move(self, id, end_sqr, start_sqr, target, ents_list):
        global selected
        selected = ''
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[start_sqr[0]][start_sqr[1]+1] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
        app.grid[end_sqr[0]][end_sqr[1]+1] = self.number
        app.get_focus(self.number)
#         app.canvas.create_image(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, image = self.img, tags = self.number)
        # IF TARGET NOW WITHIN RANGE, MAKE ATTACK ON IT
        atk_sqrs = self.legal_attacks()
        t_loc = app.ent_dict[target].loc[:]
        if t_loc in atk_sqrs:
            root.after(666, lambda t = target : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = target : self.white_dragon_attack(el, t)) # EXIT THROUGH ATTACK()
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                root.after(666, app.end_turn)
            else:
                root.after(666, lambda el = ents_list : app.do_ai_loop(el))
    
    
    # ATTACK ANIMS
    # init attack anims
    # create a vis that begins at 'mouth' and is 'selected' so it isnt animated by animate loop
    # endpoint is target.loc
    # as progressing through anim loop, rotate vis image 
    # how to show 'direction'...
    # if x,y coords are less/more
    def white_dragon_attack(self, ents_list, id):
        app.get_focus(self.number)
        self.init_attack_anims()
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
            # HIT, SHOW VIS, DO DAMAGE, EXIT
            my_str = self.get_attr('str')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_str, target_end)
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+40, text = 'White Dragon\nAttack Hit!\n' + str(d) + ' Spirit Damage', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
        else:
            # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'White Dragon\nAttack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
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
        
        
        # Any sqr within dist 2
    def legal_attacks(self):
        sqrs = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coords:
            if dist(coord, self.loc) <= 2:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
        # has flight (not impeded by obstacles, must land in square where 'below' square is unoccupied
    def legal_moves(self):
        loc = self.loc
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for c in coords:
            if app.grid[c[0]][c[1]] == '' and dist(self.loc, c) <= 6:
                # make sure below square exists and is empty
                n = [c[0],c[1]+1]
                if n in coords and app.grid[n[0]][n[1]] == '':
                    mvlist.append(c)
        return mvlist
                 
#         def findall(loc, start, dist):
#             if start > dist:
#                 return
#             adj = [c for c in coords if abs(c[0] - loc[0]) + abs(c[1] - loc[1]) == 1 and app.grid[c[0]][c[1]] == '']
#             for s in adj:
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
        self.target = ''
        super().__init__(name, img, loc, owner, number)
        
    
    def do_target_ai(self, ents_list):
        pass
        
    #  ORC AXEMAN AI
    def do_undead_ai(self, ents_list):
        if self.target != '': # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.do_target_ai(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.undead_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
                for el in enemy_ent_locs:
                # REMEMBER NOT GETTING PATH TO UNIT LOCATION, ONLY TO SQUARE WITHIN RANGE
                    path = bfs(self.loc[:], el, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    tar_loc = apath[-1] # SQR CONTAINING TARGET TO ATTACK
                    root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = endloc, tar_loc = tar_loc : self.undead_move(el, endloc, tar_loc))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = ''
                    # NOW FIND PATH AND PASS TO MOVE
                    for el in enemy_ent_locs:
                        path = bfs(self.loc[:], el, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
                        if path:
                            paths.append(path)
                    smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                    if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                        apath = smallpaths[0]
                        # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                        moves = self.legal_moves()
                        
                        # if findspath on egrid, but replacing Ents removes all legal moves along path, endloc never assigned
                        endloc = None
                        for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                            if sqr in moves:
                                endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                                break
                        if endloc != None:
                            tar_loc = apath[-1] # SQR CONTAINING TARGET TO ATTACK
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc, tar_loc = tar_loc : self.undead_move(el, endloc, tar_loc))
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
            
            
    def undead_move(self, ents_list, endloc, tarloc):
        global selected
        # FIND SQUARE FURTHEST ALONG PATH THAT IS WITHIN MOVE RANGE
        target = app.grid[tarloc[0]][tarloc[1]]
        id = self.number
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = endloc[0]*100+50-app.moved_right
        endy = endloc[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = endloc[:]
        selected = self.number
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
            try: app.canvas.tag_raise('large', (self.tags))
            except: pass
#             app.canvas.tag_raise('maptop')
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr, target, ents_list) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
            
    # change to attack any within range, not ncsrly original target
    # DONE MOVING, ATTEMPT ATTACK AND EXIT
    def finish_move(self, id, end_sqr, start_sqr, target, ents_list):
        global selected
        selected = ''
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
#         app.canvas.create_image(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, image = self.img, tags = self.number)
        # IF TARGET NOW WITHIN RANGE, MAKE ATTACK ON IT
        atk_sqrs = self.legal_attacks()
        t_loc = app.ent_dict[target].loc[:]
        if t_loc in atk_sqrs:
            root.after(666, lambda t = target : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = target : self.undead_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def undead_attack(self, ents_list, id):
        app.get_focus(id)
#         self.init_attack_anims()
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
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 2) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist
        
        
class Orc_axeman(Summon):
    def __init__(self, name, img, loc, owner, number):
        self.actions = {'attack':self.orc_axeman_attack}
        self.attack_used = False
        self.str = 4
        self.agl = 3
        self.end = 4
        self.dodge = 3
        self.psyche = 2
        self.spirit = 12
        # if given target, override search for closest enemy
        # instead always attempt to attack/move towards target
        # IF CANNOT ATTACK TARGET, AFTER MOVING TOWARDS TARGET IF STILL CANNOT ATTACK TARGET, ATTEMPT TO ATTACK OTHER?
        self.target = ''
        super().__init__(name, img, loc, owner, number)
        
    def do_target_ai(self, ents_list):
        pass
        
    #  ORC AXEMAN AI
    def do_orc_axeman_ai(self, ents_list):
        if self.target != '': # GIVEN PRIORITY OVER OTHER ENTS, ONLY TRY TO ATTACK THIS ENT
            self.do_target_ai(ents_list)
        else: # NO TARGET PRIORITY, ATTEMPT ATTACK FROM STARTLOC
            atk_sqrs = self.legal_attacks()
            atk_sqrs = [x for x in atk_sqrs if app.ent_dict[app.grid[x[0]][x[1]]].owner == 'p1']
            if atk_sqrs != []:
                any = atk_sqrs[0]
                id = app.grid[any[0]][any[1]]
                root.after(666, lambda id = id : app.get_focus(id))
                root.after(1333, lambda el = ents_list, id = id : self.orc_axeman_attack(el, id)) # ATTACK
            else: # CANNOT ATTACK FROM START LOC, GET TARGET AND MOVE TOWARDS
                enemy_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p1']
                paths = []
                for el in enemy_ent_locs:
                # REMEMBER NOT GETTING PATH TO UNIT LOCATION, ONLY TO SQUARE WITHIN RANGE
                    path = bfs(self.loc[:], el, app.grid[:])
                    if path:
                        paths.append(path)
                smallpaths = [y for y in paths if len(y) == min(len(y) for y in paths)]
                if smallpaths != []: # MOVE ALONG PATH AS FAR AS POSSIBLE, ATTEMPT ATTACK
                    apath = smallpaths[0]
                    # FIND FURTHEST SQR ALONG PATH THAT CAN BE MOVED TO
                    moves = self.legal_moves()
                    for sqr in apath[::-1]: # START WITH SQRS CLOSEST TO TARGET
                        if sqr in moves:
                            endloc = sqr[:] # AMONG SQRS POSSIBLE TO MOVE TO, THIS IS CLOSEST TO GOAL
                            break
                    tar_loc = apath[-1] # SQR CONTAINING TARGET TO ATTACK
                    root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                    root.after(1333, lambda el = ents_list, endloc = endloc, tar_loc = tar_loc : self.orc_axeman_move(el, endloc, tar_loc))
                else: # NO PATHS TO TARGET, MAKE BEST EFFORT MINIMIZE DIST MOVE
                    # change to 'remove friendly ents', find path, move along path as far as possible
                    egrid = deepcopy(app.grid)
                    friendly_ent_locs = [app.ent_dict[x].loc for x in app.ent_dict.keys() if app.ent_dict[x].owner == 'p2']
                    for eloc in friendly_ent_locs:
                        egrid[eloc[0]][eloc[1]] = ''
                    # NOW FIND PATH AND PASS TO MOVE
                    for el in enemy_ent_locs:
                        path = bfs(self.loc[:], el, egrid[:]) # BFS ON ALTERED GRID (FRIENDLY ENTS REMOVED)
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
                        # here need to 'trim path' to prevent moving to square 'through' friendly ents
                        if endloc != None:
                            tar_loc = apath[-1] # SQR CONTAINING TARGET TO ATTACK
                            # here need to 'trim path' to prevent moving to square 'through' friendly ents
                            root.after(666, lambda sqr = endloc[:] : app.focus_square(sqr))
                            root.after(1333, lambda el = ents_list, endloc = endloc, tar_loc = tar_loc : self.undead_move(el, endloc, tar_loc))
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
            
            
    def orc_axeman_move(self, ents_list, endloc, tarloc):
        global selected
        # FIND SQUARE FURTHEST ALONG PATH THAT IS WITHIN MOVE RANGE
        target = app.grid[tarloc[0]][tarloc[1]]
        id = self.number
        x = self.loc[0]*100+50-app.moved_right
        y = self.loc[1]*100+50-app.moved_down
        endx = endloc[0]*100+50-app.moved_right
        endy = endloc[1]*100+50-app.moved_down
        start_sqr = self.loc[:]
        end_sqr = endloc[:]
        selected = self.number
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
            try: app.canvas.tag_raise('large', (self.tags))
            except: pass
#             app.canvas.tag_raise('maptop')
            app.canvas.tag_raise('cursor')
            if x == endx and y == endy:
                self.finish_move(id, end_sqr, start_sqr, target, ents_list) # EXIT
            else: # CONTINUE LOOP
                root.after(66, lambda id = id, x = x, y = y, e = endx, e2 = endy, s = start_sqr, s2 = end_sqr : move_loop(id, x, y, e, e2, s, s2))
        move_loop(id, x, y, endx, endy, start_sqr, end_sqr)
            
            
    # change to attack any within range, not ncsrly original target
    # DONE MOVING, ATTEMPT ATTACK AND EXIT
    def finish_move(self, id, end_sqr, start_sqr, target, ents_list):
        global selected
        selected = ''
        self.loc = end_sqr[:]
        self.origin = end_sqr[:]
        app.grid[start_sqr[0]][start_sqr[1]] = ''
        app.grid[end_sqr[0]][end_sqr[1]] = self.number
#         app.canvas.create_image(self.loc[0]*100+50-app.moved_right, self.loc[1]*100+50-app.moved_down, image = self.img, tags = self.number)
        # IF TARGET NOW WITHIN RANGE, MAKE ATTACK ON IT
        atk_sqrs = self.legal_attacks()
        t_loc = app.ent_dict[target].loc[:]
        if t_loc in atk_sqrs:
            root.after(666, lambda t = target : app.get_focus(t))
            root.after(1333, lambda el = ents_list, t = target : self.orc_axeman_attack(el, t)) # EXIT THROUGH ATTACK
        else:
        # CANNOT ATTACK, EXIT FUNC
            ents_list = ents_list[1:]
            if ents_list == []:
                app.end_turn()
            else:
                root.after(666, lambda e = ents_list : app.do_ai_loop(e))
    
    def orc_axeman_attack(self, ents_list, id):
        app.get_focus(id)
#         self.init_attack_anims()
        my_agl = self.get_attr('agl')
        target_dodge = app.ent_dict[id].get_attr('dodge')
        if to_hit(my_agl, target_dodge) == True:
            # HIT, SHOW VIS, DO DAMAGE, EXIT
            my_str = self.get_attr('str')
            target_end = app.ent_dict[id].get_attr('end')
            d = damage(my_str, target_end)
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Orc Axeman Attack Hit!\n' + str(d) + ' Spirit Damage', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            app.ent_dict[id].set_attr('spirit', -d)
            if app.ent_dict[id].spirit <= 0:
                app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
            root.after(2666, lambda e = ents_list, i = id : self.cleanup_attack(e, id)) # EXIT THROUGH CLEANUP_ATTACK()
        else:
            # MISSED, SHOW VIS, EXIT THROUGH CLEANUP_ATTACK()
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+50, text = 'Orc Axeman Attack Missed!', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
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
            root.after(666, lambda e = ents_list : app.do_ai_loop(e))
        
        
    def legal_attacks(self):
        sqrs = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        for coord in coords:
            if dist(coord, self.loc) == 1:
                if app.grid[coord[0]][coord[1]] != '' and app.grid[coord[0]][coord[1]] != 'block':
                    sqrs.append(coord)
        return sqrs
        
    def legal_moves(self):
        loc = self.loc[:]
        mvlist = []
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        def findall(loc, start, distance):
            if start > distance:
                return
            adj = [c for c in coords if dist(c, loc) == 1 and app.grid[c[0]][c[1]] == '']
            for s in adj:
                mvlist.append(s)
                findall(s, start+1, distance)
        findall(loc, 1, 3) 
        setlist = []
        for l in mvlist:
            if l not in setlist:
                setlist.append(l)
        return setlist
        
        
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
        if app.current_pos() == '' or app.current_pos() == 'block':
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
            app.canvas.create_text(app.ent_dict[id].loc[0]*100-app.moved_right+50, app.ent_dict[id].loc[1]*100-app.moved_down+75, text = app.ent_dict[id].name.replace('_', ' ') + ' Killed...', justify = 'center', fill = 'white', font = ('Andale Mono', 14), tags = 'text')
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
            self.spell_dict['Plague'] = (self.plague, 7)
            self.spell_dict['Psionic_Push'] = (self.psionic_push, 3)
            self.spell_dict['Curse_of_Oriax'] = (self.curse_of_oriax, 6)
            self.spell_dict['Gravity'] = (self.gravity, 5)
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
            
        super().__init__(name, img, loc, owner, type = 'normal')
        
    def reset_transient_vars(self):
        self.summon_dict = {}
        self.summon_ids = 0
        self.spell_used = False
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
    
    def summon(self, event = None):
                # show vis in context_menu, summon used? eventually DEBUG fine for now
        if self.summon_used == True:
            return
        app.depop_context(event = None)
        root.bind('1', lambda e, cls = 'Warrior', cost = 10 : self.place_summon(e, cls, cost))
        root.bind('2', lambda e, cls = 'Trickster', cost = 8 : self.place_summon(e, cls, cost))
        root.bind('3', lambda e, cls = 'Shadow', cost = 7 : self.place_summon(e, cls, cost))
        root.bind('4', lambda e, cls = 'Bard', cost = 9 : self.place_summon(e, cls, cost))
        root.bind('5', lambda e, cls = 'Plaguebearer', cost = 7 : self.place_summon(e, cls, cost))
        b1 = tk.Button(app.context_menu, text = '1:Warrior •10', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Warrior', cost = 10 : self.place_summon(e, cls, cost))
        b1.pack(side = 'top', pady = 2)
        app.context_buttons.append(b1)
        b2 = tk.Button(app.context_menu, text = '2:Trickster •8', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Trickster', cost = 8 : self.place_summon(e, cls, cost))
        b2.pack(side = 'top', pady = 2)
        app.context_buttons.append(b2)
        b3 = tk.Button(app.context_menu, text = '3:Shadow •7', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Shadow', cost = 7 : self.place_summon(e, cls, cost))
        b3.pack(side = 'top', pady = 2)
        app.context_buttons.append(b3)
        b4 = tk.Button(app.context_menu, text = '4:Bard •9', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Bard', cost = 9 : self.place_summon(e, cls, cost))
        b4.pack(side = 'top', pady = 2)
        app.context_buttons.append(b4)
        b5 = tk.Button(app.context_menu, text = '5:Plaguebearer\n•7', font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', command = lambda e = None, cls = 'Plaguebearer', cost = 7 : self.place_summon(e, cls, cost))
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

    
    def place_summon(self, event, type, cost):
        if self.magick < cost:
            return
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
        cmd = lambda e = None, x = cls, y = sqrs, c = cost : self.place(e, summon = x, sqrs = y, cost = c)
        root.bind('<a>', lambda e, x = cls, y = sqrs, c = cost: self.place(e, x, y, c))
        b = tk.Button(app.context_menu, text = 'Place '+type, font = ('chalkduster', 24), fg='tan3', highlightbackground = 'tan3', wraplength = 190, command = cmd)
        b.pack(side = 'top')
        app.context_buttons.append(b)
        
        
    def place(self, event, summon, sqrs, cost):
        if grid_pos not in sqrs:
            return
        self.set_attr('magick', -cost)
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
        app.canvas.create_image(grid_pos[0]*100+50-app.moved_right, grid_pos[1]*100+50-app.moved_down, image = img, tags = s.tags)
        app.grid[grid_pos[0]][grid_pos[1]] = number
        app.cleanup_squares()
        app.unbind_all()
        app.rebind_all()
        app.depop_context(event = None)
        self.summon_used = True
        
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
        self.init_normal_anims()
        for x in range(1, len(self.spell_dict.keys())+1):
            root.unbind(str(x))
        app.unbind_all()
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
            # attrs reduced to by 3 to a minimum of 1 (str, agl, end, dodge, psyche) lasting until 3 opp turns have passed
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
        self.magick -= self.spell_dict['Plague'][1]
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        app.vis_dict['Plague'] = Vis(name = 'Plague', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Plague'].img, tags = 'Plague')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Plague', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO PLAGUE EFFECTS
        def plague_effect(stat):
            stat -= 3
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
        p = partial(un, id)
        def nothing():
            return None
        eot = nothing
        n = 'Plague' + str(app.effects_counter)
        app.ent_dict[id].effects_dict['Plague'] = Effect(name = 'Plague', info = 'Plague\n Stats reduced by 3 for 3 turns', eot_func = eot, undo = p, duration = 3)
        root.after(3666, lambda  name = 'Plague' : self.cleanup_spell(name = name))
            
    # PSIONIC PUSH
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
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        # target must be Summon, Witch, (future type...)
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        # cannot target large
        if app.ent_dict[id].type == 'large':
            return
        app.depop_context(event = None)
        app.cleanup_squares()
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
            
    def choose_psi_square(self, event, id, sqr, sqrs):
        global selected, selected_vis
        if sqr not in sqrs:
            return
        self.spell_used = True
        self.init_cast_anims()
        self.magick -= self.spell_dict['Psionic_Push'][1]
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
                app.canvas.create_image(x, y, image = app.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
            app.canvas.tag_raise(vis)
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
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        adj_sqrs = [c for c in coords if dist(c, end_loc) == 1]
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
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = str(d) + ' Spirit\nDamage', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                    if app.ent_dict[ent].spirit <= 0:
                        app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+100-app.moved_down, text = app.ent_dict[ent].name + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
                        root.after(666, app.kill(ent))
                # MISS
                else:
                    app.canvas.create_text(app.ent_dict[ent].loc[0]*100+50-app.moved_right, app.ent_dict[ent].loc[1]*100+70-app.moved_down, text = 'Agility\nSave',justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            root.after(3666, lambda s = 'Psionic_Push' : self.cleanup_spell(name = s))
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
        if app.current_pos() == '' or app.current_pos() == 'block':
            return
        if sqr not in sqrs:
            return
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.spell_dict['Curse_of_Oriax'][1]
        self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        app.vis_dict['Curse_of_Oriax'] = Vis(name = 'Curse_of_Oriax', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Curse_of_Oriax'].img, tags = 'Curse_of_Oriax')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Curse\nof\nOriax', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
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
        p = partial(un, id)
        # EOT FUNC
        def take_2(tar):
            app.get_focus(tar)
            app.ent_dict[tar].set_attr('spirit', -2)
            app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+50-app.moved_down, text = '2 Spirit\n Damage\nCurse', justify ='center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
            if app.ent_dict[tar].spirit <= 0:
                app.canvas.create_text(app.ent_dict[tar].loc[0]*100+50-app.moved_right, app.ent_dict[tar].loc[1]*100+90-app.moved_down, text = app.ent_dict[tar].name + '\nKilled...', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
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
        coords = [[x,y] for x in range(app.map_width//100) for y in range(app.map_height//100)]
        sqrs = [s for s in coords if dist(self.loc, s) <= 4]
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
        id = app.current_pos()
        if not isinstance(app.ent_dict[id], Witch) and not isinstance(app.ent_dict[id], Summon):
             return
        self.magick -= self.spell_dict['Gravity'][1]
        self.init_cast_anims()
        app.unbind_all()
        app.depop_context(event = None)
        app.cleanup_squares()
        self.spell_used = True
        app.vis_dict['Gravity'] = Vis(name = 'Gravity', loc = sqr)
        app.canvas.create_image(sqr[0]*100+50-app.moved_right, sqr[1]*100+50-app.moved_down, image = app.vis_dict['Gravity'].img, tags = 'Gravity')
        app.canvas.create_text(sqr[0]*100+50-app.moved_right, sqr[1]*100+75-app.moved_down, text = 'Gravity', justify = 'center', font = ('Andale Mono', 14), fill = 'white', tags = 'text')
        # DO Curse_of_Oriax EFFECTS
        def gravity_effect(stat):
            stat - 2
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
        p = partial(un, id)
        # EOT FUNC
        def nothing():
            return None
        eot = nothing
        n = 'Gravity' + str(app.effects_counter)
        app.ent_dict[id].effects_dict[n] = Effect(name = 'Gravity', info = 'Gravity\nCannot move and agl and dodge reduced by 2 for 2 turns', eot_func = eot, undo = p, duration = 2)
        root.after(3666, lambda  name = 'Gravity' : self.cleanup_spell(name = name))
        print('gravity')
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

# maybe am still in some logical context while executing everything...
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
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
        self.effects_counter = 0 # used for uniquely naming Effects with the same prefix/name
        self.p1_witch = ''
        self.p2_witch = ''
        self.choose_num_players()
        
        # Luminari 280
        # Herculanum 240
        # Papyrus 240
    def choose_num_players(self):
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
            with open('save_games/'+s, 'rb') as f:
                obj = load(f)
                cmd = lambda obj = obj : self.load_game(obj)
                b = tk.Button(self.scroll_frame.interior, text = s, width = 13, wraplength = 190, fg = 'indianred', highlightbackground = 'black', font = ('chalkduster', 24), relief = 'raised', command = cmd)
                b.pack() 
                self.game_title.saves_buttons.append(b)
        cancel_b = tk.Button(self.scroll_frame.interior, text = 'Cancel', bg = 'black', fg = 'black', width = 13, highlightbackground = 'black', font = ('chalkduster', 24), relief = 'raised', command = self.scroll_frame.destroy)
        cancel_b.pack(side = 'bottom')
        self.game_title.saves_buttons.append(cancel_b)
                
    def load_game(self, obj):
        # destroy titlescreen
        self.game_title.destroy()
        # same problem with location had on new map area
        # was it setting grid_pos, curs_pos?
        self.load_map_triggers(map_number = obj.current_area, protaganist_object = obj)
#         self.create_map_curs_context(map_number = obj.current_area, protaganist_object = obj)
        
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
            self.load_map_triggers(map_number = 0)
            
    # make each branch load the intro scene for level, with 'continue' button when done reading/displaying to call create_map_curs_context
    def load_map_triggers(self, map_number, protaganist_object = None):
        if map_number == 0: # FIRST AREA, NO 'CONTINUATION' OF BY PASSING PROTAG OBJECT
            self.map_triggers = []
            def is_white_dragon_dead():
                if 'b12' not in [v.number for k,v in self.ent_dict.items() if isinstance(v, Summon)]:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(is_white_dragon_dead)
            
            self.load_intro_scene(map_number)# DONT NEED PROTAG OBJECT ON FIRST AREA
#             self.create_map_curs_context(map_number)
            
        elif map_number == 1:
            self.map_triggers = []
            def kill_all_undead():
                all = [k for k,v in self.ent_dict.items() if v.owner == 'p2']
                if all == []:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(kill_all_undead)
            
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
#             self.create_map_curs_context(map_number, protaganist_object = protaganist_object)
            
        elif map_number == 2:
            self.map_triggers = []
            def is_white_dragon_dead():
                if 'b12' not in [v.number for k,v in self.ent_dict.items() if isinstance(v, Summon)]:
                    return 'victory'
                else:
                    return None
            self.map_triggers.append(is_white_dragon_dead)
            
            self.load_intro_scene(map_number, protaganist_object = protaganist_object)
#             self.create_map_curs_context(map_number, protaganist_object = protaganist_object)
        else:
            print('you are winner hahaha')
        
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
        maps = [m for r,d,m in walk('./2_player_maps')][0]
        maps = [m for m in maps[:] if m[0] != '.']
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
        
        
        # IF PROTAG, LOAD PROTAG AND DO NOT RE-INIT WITCH
    def create_map_curs_context(self, map_number, protaganist_object = None):
        global curs_pos, grid_pos
        self.intro_canvas.destroy()
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
        # LOAD MAP / GRID INFO / IMPASSABLE TERRAIN
        terrain = eval(self.map_info[2])
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
        self.map_img = ImageTk.PhotoImage(Image.open(fname + 'map'+str(map_number)+'.png'))
        self.map_top = ImageTk.PhotoImage(Image.open(topfname + 'map_top'+str(map_number)+'.png'))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags=('mapbottom','map'))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_top, tags = ('maptop','map'))
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.vis_dict['cursor'] = Vis(name = 'cursor', loc = [2,2])
        curs_pos = [2,2]
        grid_pos = [2,2]
        self.canvas.create_image(250, 250, image=self.cursor_img, tags='cursor')
        # CHOOSE WITCH IF 2 PLAYER OR FIRST LEVEL
        # OTHERWISE LOAD WITCH FROM PREVIOUS LEVEL (EVENTUALLY SHOULD BE PERSISTENT OBJECT, CARRY OVER ANY LONG-TERM CHANGED STATE)
        if protaganist_object:
            self.load_witch(witch = protaganist_object.name, player_num = 1, protaganist_object = protaganist_object)
        else:
            self.choose_witch()
        
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
        
    def load_witch(self, witch = None, player_num = None, protaganist_object = None):
        if player_num == 1:
            self.p1_witch = witch
            loc = [2,2]
        elif player_num == 2:
            self.p2_witch = witch
            loc = [self.map_width//100-3, self.map_height//100-3]
        # if protaganist_object, instead load its data, RE-INIT IMAGES THAT CANNOT BE SERIALIZED BY PICKLE DUMP
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
            lst = self.map_info[3:]
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
            self.start_turn()
            self.animate()
            self.map_trigger_loop()
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
        elif self.ent_dict[ent].name == 'Orc_axeman':
            self.ent_dict[ent].do_orc_axeman_ai(ents)
        elif self.ent_dict[ent].name == 'White_Dragon':
            self.ent_dict[ent].do_white_dragon_ai(ents)
        
        
        
    def end_turn(self):
        self.unbind_all()
        self.depop_context(event = None)
        # first do EOT loop, rest of this becomes finish_end_turn()
        # get list of all ents, pass in first ent, loop pops front and calls 
        ents_list = [v for k,v in self.ent_dict.items() if v.owner == self.active_player]
        self.eot_loop(ents_list[0], ents_list)
        
        
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
            
                
    # exec an ef.eot_func, pop ef_list continue
    def effects_loop(self, ef, ef_list, ent, ents_list):
        k = [k for k,v in self.ent_dict.items() if v == ent]
        if ef.eot_func() != None:
            self.get_focus(k[0])
        if ent.spirit <= 0: # ENT KILLED, DO NOT EXEC ANY MORE OF ITS EFFECTS, POP ENTS LIST OR EXIT
            root.after(1333, lambda e = k[0] : self.kill(e))
            ents_list = ents_list[1:]
            if ents_list != []:
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
                root.after(999, lambda t = 'text' : self.canvas.delete(t))
                root.after(1333, lambda ef = ef_list[0], efl = ef_list, en = ent, enl = ents_list : self.effects_loop(ef, efl, en, enl))
            else: # NO MORE FOR THIS ENT, CHECK IF MORE ENTS
                ents_list = ents_list[1:]
                if ents_list != []: # MORE ENTS TO PROCESS EFFECTS FOR
                    root.after(999, lambda e = ents_list[0], el = ents_list : self.eot_loop(e, el))
                else: # NO MORE ENTS, FINISH_END_TURN
                    root.after(999, self.finish_end_turn)
                    
    def finish_end_turn(self):
        self.canvas.delete('text') # deletes the last text object when exiting loops
        ents = [v for k,v in self.ent_dict.items()]
        for ent in ents:
            # RESET SPELLS / MOVEMENT / ATTACKS
            ent.move_used = False
            if isinstance(ent, Witch):
                ent.spell_used = False
                ent.summon_used = False
            elif isinstance(ent, Summon):
                ent.attack_used = False
        if self.active_player == 'p1':
            self.unbind_all()
            self.active_player = 'p2'
        elif self.active_player == 'p2':
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
        for ent in self.ent_dict.keys():
            if ent != selected:
                self.ent_dict[ent].rotate_image()
                self.canvas.delete(ent)
                self.canvas.create_image(self.ent_dict[ent].loc[0]*100+50-self.moved_right, self.ent_dict[ent].loc[1]*100+50-self.moved_down, image = self.ent_dict[ent].img, tags = app.ent_dict[ent].tags)
                app.canvas.tag_lower((app.ent_dict[ent].tags), ('maptop'))
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
#         app.canvas.tag_raise('vis')
        try: app.canvas.tag_raise('text')
        except: pass
        self.animate_id = root.after(300, self.animate)
        
        # MAP TRIGGER LOOP
        # ALL MAP TRIGGERS ARE FUNCTIONS THAT CHECK FOR CONDITIONS AND EITHER DO STUFF IN RESPONSE
        # OR IF THEY RETURN 'victory', END LEVEL
    def map_trigger_loop(self):
        for mt in self.map_triggers:
            if mt() == 'victory':
                self.end_level()
            else:
                self.map_trigger_id = root.after(666, self.map_trigger_loop)
        
    def end_level(self):
        global curs_pos, is_object_selected, selected, selected_vis, map_pos, grid_pos
        print('level finished')
        root.after_cancel(self.animate_id)
        root.after_cancel(self.map_trigger_id)
        protaganist_object  = app.ent_dict[self.p1_witch]
        protaganist_object.reset_transient_vars()
        prev_map_num = int(self.map[3:])
        newmap_num = prev_map_num + 1
        for child in root.winfo_children():
            child.destroy()
        # THIS WORKS, JUST NEED TO CLEAN ALL VARS LIKE GRID, SELF.STUFF, GLOBALS
        # GLOBALS
        curs_pos = [2, 2]
        is_object_selected = False
        selected = ''
        selected_vis = ''
        map_pos = [0, 0]
        grid_pos = [2,2]
        
        self.ent_dict = {}
        self.sqr_dict = {}
        self.vis_dict = {}
        self.active_player = 'p1'
        self.moved_right = 0
        self.moved_down = 0
        self.context_buttons = []
        self.help_buttons = []
        # list to hold entity that is being animated as 'attacking'
        self.attacking = []
        self.effects_counter = 0 # used for uniquely naming Effects with the same prefix/name
        # CALL IN-BETWEEN LEVEL SCREEN / VICTORY SCREEN
        # GIVE ANY STORYLINE RELATED TO FINISHED AND NEXT LEVEL
        # GIVE OPTION TO SAVE PROGRESS
        # WILL NEED, AT SOME POINT, TO SAVE ACTUAL WITCH OBJECT (NOT JUST STRING NAME), TO HOLD PERSISTENT CHANGES
        self.load_cutscene(prev_map_num, protaganist_object)
        
        
    def load_cutscene(self, prev_map_num, protaganist_object):
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
        self.next_area_button = tk.Button(root, text = 'Next Area', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda n = prev_map_num+1, po = protaganist_object : self.next_area(n,po))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2-100, root.winfo_screenheight()-80, anchor='s', window = self.next_area_button)
        self.save_game_button = tk.Button(root, text = 'Save Game', fg = 'tan3', highlightbackground = 'tan3', font = ('chalkduster', 24), command = lambda n = prev_map_num+1, po = protaganist_object : self.save_game(n, po))
        self.cut_canvas.create_window(root.winfo_screenwidth()/2+100, root.winfo_screenheight()-80, anchor='s', window = self.save_game_button)
        
    def next_area(self, new_map_num, protaganist_object):
        self.cut_canvas.destroy()
        # LOAD NEXT MAP
        self.load_map_triggers(new_map_num, protaganist_object)
        
    def save_game(self, new_map_num, protaganist_object):
        protaganist_object.current_area = new_map_num
        saves = [s for r,d,s in walk('./save_games')][0]
        saves = [s for s in saves[:] if s[0] != '.']
        # later should open text input to write filename
        filename = 'save_games/savegame' + str(len(saves))
        with open(filename, 'wb+') as f:
            # have to strip tkinter objects from protag obj
            protaganist_object.img = None
            protaganist_object.anim_dict = {}
            dump(protaganist_object, f)
    
    
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
            expanded_name = self.ent_dict[e].__class__.__name__
        except:
            pass
        # DEBUG make info button into label that holds the info
        self.cntxt_info_bg = ImageTk.PhotoImage(Image.open('page.png'))
        bg = tk.Canvas(self.context_menu, width = 190, height = 295, bg = 'burlywood4', bd=0, relief='raised', highlightthickness=0)
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
        if isinstance(self.ent_dict[ent], Witch) or isinstance(self.ent_dict[ent], Trickster):
            txt += 'Magick:' + str(self.ent_dict[ent].magick) + '\n'
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
        # DEBUG handle if killing witch
        # If witch is dead, show popup with victory/defeat
        self.canvas.delete(id)
        # destroy surrounding squares of large Ents
        if app.ent_dict[id].type == 'large':
            app.ent_dict[id].large_undo()
        self.grid[self.ent_dict[id].loc[0]][self.ent_dict[id].loc[1]] = ''
        del self.ent_dict[id]
        # if id begins with 'a' belongs to protag_witch, else belongs to antag_witch
        if id[0] == 'a':
            del self.ent_dict[self.p1_witch].summon_dict[id]
        elif id[0] == 'b':
            if self.num_players == 2:
                del self.ent_dict[self.p2_witch].summon_dict[id]
            
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