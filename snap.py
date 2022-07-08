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
    else: #there are no more shapes in the list, game is over and show winner score on GUI
        c.unbind('q')
        c.unbind('p')
        if player1_score > player2_score:
            c.create_text(200,200,text='Winner: Player 1')
        elif player2_score > player1_score:
            c.create_text(200,200,text='Winner: Player 2')
        else:
            c.create_text(200, 200, text='Draw')
        c.pack()


def snap(event):
    global shape
    global player1_score
    global player2_score
    valid = False

    c.delete(shape)

    if previous_color == current_color:
        valid = True

    if valid:
        if event.char == 'q':
            player1_score+=1
        else:
            player2_score+=1
        shape = c.create_text(200,200,text='SNAP! You score 1 point')
    c.pack()
    root.update_idletasks() #forces to update the progrma immediately
    time.sleep(1) #wait 1 second while the user reasds the message


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