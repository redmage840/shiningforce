# real-life educational material, reveal information/artifacts related to real life events/people
# use this information/artifacts in game
# ie discover davinci ornithopter for limited flying (obvious use)
# besides obvious use, esoteric knowledge to actually give creative insight, ie use of contextual/historical period symbology in order to 'decode' written messages...

# make 'animations', image is updated using 'after' to rotate through series of images
# so each animation will have corresponding dictionary/atlas? of images

# constrain 'magic numbers' to size relative to screen/frame size instead of pixels except with movement/borders to avoid partial fractions

import tkinter as tk
from PIL import ImageTk,Image

# probably wont need this, was for checking position of cursor relative to grid
# grid should indicate what is located where on map, ie what 'units' are on a given coordinate
col = 24
row = 36
# z = [[x,y] for x in range(col) for y in range(row)]
# z.reverse()
grid = [[''] * col for i in range(row)]
# for i in range(col):
#     for j in range(row):
#         grid[j][i] = z.pop()

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_map_curs()
        self.create_units()
        
        
    def create_units(self):
        self.img_list = []
        # test image/unit process
        self.greenface = ImageTk.PhotoImage(Image.open("greenface.png").resize((100,100)))
        c = 3
        r = 0
        self.canvas.create_image(c*100,r*100, anchor='nw', image=self.greenface, tags='greenface')
        self.img_list.append(['greenface', [c,r]])
        # add position [c,r] to grid
        grid[c][r] = 'greenface'
#         print('grid pos ',c,' ',r,' holds ', grid[c][r])
        # END test image


    def create_map_curs(self):
        # CANVAS
        self.canvas = tk.Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())  
        self.canvas.pack()
        
        # MAP, gives 24X36 grid
        self.map_img = ImageTk.PhotoImage(Image.open("map.jpg").resize((2400, 3600)))
        self.canvas.create_image(0, 0, anchor='nw', image=self.map_img, tags='map')
        print(self.canvas.bbox('map'))
        
        # CURSOR
        self.cursor_img = ImageTk.PhotoImage(Image.open("cursor.png").resize((100,100)))
        self.canvas.create_image(0,0, anchor='nw', image=self.cursor_img, tags='curs')
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
    
    def depress_curs(self, event):
        # show visual cue that cursor is depressed
        # change cursor global is_depressed
        # memo objects in current space as 'selected'
        print(curs_pos)
        print(grid_pos)
        print(grid[curs_pos[0]][curs_pos[1]])
    
    # from start pos, update grid_pos with every keypress UNLESS not moving curs OR map (at edge)
    # just need to reverse grid_pos xy
    def move_curs(self, event):
        if event.keysym == 'Left':
            if curs_pos[0] > 0:
                self.canvas.move('curs', -100, 0)
                curs_pos[0] -= 1
                grid_pos[0] -= 1
            elif map_pos[0] > 0:
                map_pos[0] -= 1
                self.move_map('Left')
                grid_pos[0] -= 1
        elif event.keysym == 'Right':
            if curs_pos[0] < 11:
                self.canvas.move('curs', 100, 0)
                curs_pos[0] += 1
                grid_pos[0] += 1
            elif map_pos[0] < 12:
                self.move_map('Right')
                map_pos[0] += 1
                grid_pos[0] += 1
        elif event.keysym == 'Up':
            if curs_pos[1] > 0:
                self.canvas.move('curs', 0, -100)
                curs_pos[1] -= 1
                grid_pos[1] -= 1
            elif map_pos[1] > 0:
                self.move_map('Down')
                map_pos[1] -= 1
                grid_pos[1] -= 1
        elif event.keysym == 'Down':
            if curs_pos[1] < 6:
                self.canvas.move('curs', 0, 100)
                curs_pos[1] += 1
                grid_pos[1] += 1
            elif map_pos[1] < 29:
                self.move_map('Up')
                map_pos[1] += 1
                grid_pos[1] += 1
        # DEBUG
#         print('grid pos is ', grid_pos)
        print('curs pos is ', curs_pos)
#         print('grid value at pos it ', grid[grid_pos[1]][grid_pos[0]])
        # DEBUG


    def move_map(self, direction):
        if direction == 'Left':
            self.canvas.move('map', 100, 0)
            for img in self.img_list:
                self.canvas.move(img[0], 100, 0)
        elif direction == 'Right':
            self.canvas.move('map', -100, 0)
            for img in self.img_list:
                self.canvas.move(img[0], -100, 0)
        elif direction == 'Up':
            self.canvas.move('map', 0, -100)
            for img in self.img_list:
                self.canvas.move(img[0], 0, -100)
        elif direction == 'Down':
            self.canvas.move('map', 0, 100)
            for img in self.img_list:
                self.canvas.move(img[0], 0, 100)


# make cursor position corespond to grid/map position
# CURSOR GLOBALS
curs_pos = [0, 0]
is_depressed = 0

# MAP POSITION GLOBALS
map_pos = [0, 0]

# GRID GLOBALS grid[0][0] to grid[35][23]
grid_pos = [0,0]



root = tk.Tk()
app = App(master=root)

root.bind('<Right>', app.move_curs)
root.bind('<Left>', app.move_curs)
root.bind('<Up>', app.move_curs)
root.bind('<Down>', app.move_curs)
root.bind('<space>', app.depress_curs)


# set window size to screen size
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%sx%s' % (width, height))

app.mainloop()