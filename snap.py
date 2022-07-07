"""Snap"""

import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL

def next_shape():
    global shape
    global previous_color
    global current_color

    previous_color=current_color

    c.delete(shape) #delete current shape
    if len(shapes)>0:
        shape = shapes.pop() #pop off the next shape in the array
        c.itemconfigure(shape,state=NORMAL) #show the shape on GUI
        current_color = c.itemcget(shape,'fill') #retrieve the 'fill' color form current shape
        root.after(1000,next_shape)


def snap():

############### setup ###############################
root = Tk()
root.title('Snap')
c = Canvas(root, width=400,height=400)

shapes = []
#creeate circles of different colors
circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(circle) ##ads circle to list of shapes
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(circle)

#create rectangles of different colors
rectangle = c.create_rectangle(35, 100, 365, 270, outline='black', fill='black', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='red', fill='red', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
shapes.append(rectangle)
rectangle = c.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
shapes.append(rectangle)

#create squares of different colors
square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', state=HIDDEN)
shapes.append(square)

c.pack() #puts shapes onto the canvas

random.shuffle(shapes) #shuffle all of the shapes in the list
shape = None
previous_color = ''
current_color = ''
player1_score = 0
player2_score = 0


root.after(3000,next_shape) #program waits 3 seconds before changing to next shape
c.bind('q',snap)
c.bind('p',snap)
c.focus_set() #this tells the the key presses to go to the canvas, without this, GUI wouldn't react to key presses
root.mainloop()