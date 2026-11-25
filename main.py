from levels import levels
from playground import window
from playground import canvas
from playground import players
from playground import exits
from playground import keys
from playground import doors
from playground import walls
from playground import creat_Level
from playground import currentLevel
from playground import a
from playground import obstacles
from playground import b
creat_Level(levels[currentLevel])
def player_Move(event):
    global currentLevel
    player=players[0]
    key=event.keysym
    x=0
    y=0
    if key=='Up':
        y-=5
    elif key=='Down':
        y+=5
    elif key=='Right':
        
        x+=5
    elif key=='Left':
        x-=5
    canvas.move(player, x, y)
    for wall in walls:
        x1, y1, x2, y2=canvas.coords(wall)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.move(player, -x, -y)
    for key in keys:
        x3, y3, x4, y4=canvas.coords(key)
        if player in canvas.find_overlapping(x3, y3, x4, y4):
            canvas.delete(key)
            keys.remove(key)
            if len(keys)==0:
                for door in doors:
                    canvas.itemconfig(door, fill='green', outline='green')
    for door in doors:
        x3, y3, x4, y4=canvas.coords(door)
        if player in canvas.find_overlapping(x3, y3, x4, y4):
            if canvas.itemcget(door, 'fill')=='red':
                canvas.move(player, -x, -y)
    for lawa in obstacles:
        x7, y7, x8, y8=canvas.coords(lawa)
        if player in canvas.find_overlapping(x7, y7, x8, y8):
            canvas.delete('all')
            b.pack(expand=True)
            canvas.unbind_all('<Key>')
            return
    for exite in exits:
         x5, y5, x6, y6=canvas.coords(exite)
         if player in canvas.find_overlapping(x5, y5, x6, y6):
             canvas.delete('all')
             currentLevel+=1
             if currentLevel<len(levels):
                 creat_Level(levels[currentLevel])
             else:
                 a.pack(expand=True)
                 canvas.unbind_all('<Key>')
                 return
canvas.bind_all('<Key>', player_Move)
window.mainloop()
