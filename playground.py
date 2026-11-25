from tkinter import *
from levels import levels
window = Tk()
window.geometry('500x500')
window.resizable(False, False)
window.title('Labyrinth')
canvas=Canvas(height=450, width=450, relief=SOLID, bg='white')
canvas.pack(expand=True)
a=Label(canvas, text='''You Won The Game!!!!!
                        (через 5 секунд игра будет запущена заново)''', fg='green', font=1000)
b=Label(canvas, text='''You Lost!!!!
                        (через 5 секунд игра будет запущена заново)''', fg='red', font=1000)
walls=[]
doors=[]
keys=[]
exits=[]
players=[]
obstacles=[]
currentLevel=0
def creat_Level(level):
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    obstacles.clear()
    x=0
    y=0
    side=25
    for line in level:
        for block in line:
            if block=='W':
                wall=canvas.create_rectangle(x, y, x+side, y+side,
                                            fill='black', outline='black')
                walls.append(wall)
            elif block=='S':
                secret=canvas.create_rectangle(x, y, x+side, y+side,
                                              fill='black', outline='black')
            elif block=='K':
                key=canvas.create_rectangle(x, y, x+side, y+side,
                                            fill='yellow', outline='yellow')
                keys.append(key)
            elif block=='D':
                door=canvas.create_rectangle(x, y, x+side, y+side,
                                            fill='red', outline='red')
                doors.append(door)
            elif block=='E':
                exite=canvas.create_rectangle(x, y, x+side, y+side,
                                            fill='orange', outline='orange')
                exits.append(exite)
            elif block=='P':
                player=canvas.create_rectangle(x + 1, y + 1, x + side - 1, y + side - 1,
                                               fill='blue', outline='blue')
                players.append(player)
            elif block=='L':
                lawa=canvas.create_rectangle(x, y, x+side, y+side,
                                             fill='#f74600', outline='#f74600')
                obstacles.append(lawa)
            elif block=='F':
                canvas.create_rectangle(x, y, x+side, y+side,
                              fill='#f74600', outline='#f74600')
            x+=side
        y+=side
        x=0
if __name__=='__main__':
    window.mainloop()
