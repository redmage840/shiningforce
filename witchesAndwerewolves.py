# need to hold references to all images outside of 'creation' functions, maybe dict with name/tag corresponding to opened photoimage object

# real-life educational material, reveal information/artifacts related to real life events/people
# use this information/artifacts in game
# ie discover davinci ornithopter for limited flying (obvious use)
# besides obvious use, esoteric knowledge to actually give creative insight, ie use of contextual/historical period symbology in order to 'decode' written messages...

# make 'animations', image is updated using 'after' to rotate through series of images
# so each animation will have corresponding dictionary/atlas? of images

# constrain 'magic numbers' to size relative to screen/frame size instead of pixels except with movement/borders to avoid partial fractions

import tkinter as tk
import os
from PIL import ImageTk,Image

# CURSOR GLOBALS
curs_pos = [0, 0]
object_selected = False
selected = ''

# MAP POSITION GLOBALS
map_pos = [0, 0]

# GRID GLOBALS grid[0][0] to grid[35][23]
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
        
        
    def place_witch(self):
        pass
        
    def create_units(self):
        # test image/unit process
        self.greenface = ImageTk.PhotoImage(Image.open("greenface.png").resize((100,100)))
        c = 3
        r = 0
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.greenface, tags='greenface')
        self.img_dict['greenface'] = [c,r]
        grid[c][r] = 'greenface'
        # END test image
        self.orangeface = ImageTk.PhotoImage(Image.open("orangeface.png").resize((100,100)))
        c = 5
        r = 2
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.orangeface, tags='orangeface')
        self.img_dict['orangeface'] = [c,r]
        grid[c][r] = 'orangeface'
        #
        self.scrawl = ImageTk.PhotoImage(Image.open("scrawl.png").resize((100,100)))
        c = 6
        r = 3
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.scrawl, tags='scrawl')
        self.img_dict['scrawl'] = [c,r]
        grid[c][r] = 'scrawl'
        #
        self.wolfy = ImageTk.PhotoImage(Image.open("wolfy.png").resize((100,100)))
        c = 7
        r = 3
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.wolfy, tags='wolfy')
        self.img_dict['wolfy'] = [c,r]
        grid[c][r] = 'wolfy'
        #
    
    def choose_map(self):
        self.marquee = tk.Label(root, text = 'Choose your map', font=("Helvetica", 36))
        self.marquee.pack(side = 'top')
        # CHOOSE MAPS
        maps = [m for r,d,m in os.walk('./maps')][0]
        self.button_list = []
        for i,map in enumerate(maps):
            b = tk.Button(root)
            cmd = lambda indx = i : self.load_map(indx)
            photo = ImageTk.PhotoImage(Image.open('./maps/' + map).resize((200,200)))
            self.img_dict['map'+str(i)] = photo
            b.config(image = self.img_dict['map'+str(i)], width="200", height="200", command = cmd)
            b.pack(side = 'left')
            self.button_list.append(b)
            
    def load_map(self, map_number):
        for b in self.button_list:
            print(b.config)
        print(map_number)
            
    def create_map_curs(self):
        # CANVAS
        self.canvas = tk.Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())  
        self.canvas.pack()
        
        # MAP, gives 24X36 grid
        # !! be able to load different maps dynamically, no static size requirements
        self.map_img = ImageTk.PhotoImage(Image.open("map.jpg").resize((2400, 3600)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        print(self.canvas.bbox('map'))
        
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    # needs to delete object from grid on pickup
    def pickup_putdown(self, event):
        global object_selected, selected, curs_pos, grid
        # 'pick up' unit, check what/if unit in space, remove from img_dict, put in selected
        if object_selected == False and current_pos() != '':
            object_selected = True
            unit = current_pos()
            del self.img_dict[unit]
            selected = unit
            grid[grid_pos[0]][grid_pos[1]] = ''
        # 'put down' unit, check that grid is empty, remove unit from selected, put in img_dict
        elif object_selected == True and current_pos() == '':
            object_selected = False
            unit = selected
            selected = ''
            self.img_dict[unit] = grid_pos[:]
            grid[grid_pos[0]][grid_pos[1]] = unit

            
        # show visual cue that cursor is depressed
        print(curs_pos)
        print(grid_pos)
        print(grid[curs_pos[0]][curs_pos[1]])
        
    
    def move_curs(self, event):
        if event.keysym == 'Left':
            if curs_pos[0] > 0:
                self.canvas.move('curs', -100, 0)
                self.canvas.move(selected, -100, 0)
                curs_pos[0] -= 1
                grid_pos[0] -= 1
            elif map_pos[0] > 0:
                map_pos[0] -= 1
                self.move_map('Left')
                grid_pos[0] -= 1
        elif event.keysym == 'Right':
            if curs_pos[0] < 11:
                self.canvas.move('curs', 100, 0)
                self.canvas.move(selected, 100, 0)
                curs_pos[0] += 1
                grid_pos[0] += 1
            elif map_pos[0] < 12:
                self.move_map('Right')
                map_pos[0] += 1
                grid_pos[0] += 1
        elif event.keysym == 'Up':
            if curs_pos[1] > 0:
                self.canvas.move('curs', 0, -100)
                self.canvas.move(selected, 0, -100)
                curs_pos[1] -= 1
                grid_pos[1] -= 1
            elif map_pos[1] > 0:
                self.move_map('Down')
                map_pos[1] -= 1
                grid_pos[1] -= 1
        elif event.keysym == 'Down':
            if curs_pos[1] < 6:
                self.canvas.move('curs', 0, 100)
                self.canvas.move(selected, 0, 100)
                curs_pos[1] += 1
                grid_pos[1] += 1
            elif map_pos[1] < 29:
                self.move_map('Up')
                map_pos[1] += 1
                grid_pos[1] += 1
        # DEBUG
#         print('grid pos is ', grid_pos)
#         print('curs pos is ', curs_pos)
#         print('grid value at pos it ', grid[grid_pos[1]][grid_pos[0]])
        # DEBUG


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
root.geometry('%sx%s' % (width, height))

app.mainloop()