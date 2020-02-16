from tkinter import Tk, Canvas
from math import sqrt


count = 0

size = 380
border = 15
spacing = (size-2*border)/14
player = "black"
flag = True
lists = [[0 for i in range(15)] for i in range(15)]
stack = []


def draw_chessboard():
    global count
    for i in range(15):
        canvas.create_line(border, border+i*spacing, border+14*spacing, border+i*spacing)
        canvas.create_line(border+i*spacing, border, border+i*spacing, border+14*spacing)
        count = count + 2
    point = [(border+7*spacing, border+7*spacing), (border+3*spacing, border+3*spacing), (border+11*spacing, border+3*spacing), (border+3*spacing, border+11*spacing), (border+11*spacing, border+11*spacing)]
    for x,y in point:
        canvas.create_rectangle(x-2, y-2, x+2, y+2, fill='black')
        count = count + 1


def draw_chessman(event):
    global player, count
    if flag:
        for i in range(15):
            for j in range(15):
                x = border+j*spacing
                y = border+i*spacing
                r = sqrt(pow(x-event.x, 2) + pow(y-event.y, 2))
                if r <= 10 and lists[i][j] == 0:
                    if player == "black":
                        canvas.create_oval(x-10, y-10, x+10, y+10, fill='black')
                        lists[i][j] = 1
                        player = "white"
                    else:
                        canvas.create_oval(x-10, y-10, x+10, y+10, fill='white')
                        lists[i][j] = 2
                        player = "black"
                    count = count + 1
                    stack.append((count, i, j))
                    game_over()


def game_over():
    global flag, count
    black_chess = 0
    white_chess = 0
    for i in range(15):
        for j in range(11):
            if lists[i][j] == 1 and lists[i][j+1] == 1 and lists[i][j+2] == 1 and lists[i][j+3] == 1 and lists[i][j+4] == 1:
                black_chess = 1
            elif lists[i][j] == 2 and lists[i][j+1] == 2 and lists[i][j+2] == 2 and lists[i][j+3] == 2 and lists[i][j+4] == 2:
                white_chess = 1
    for i in range(15):
        for j in range(11):
            if lists[j][i] == 1 and lists[j+1][i] == 1 and lists[j+2][i] == 1 and lists[j+3][i] == 1 and lists[j+4][i] == 1:
                black_chess = 1
            elif lists[j][i] == 2 and lists[j+1][i] == 2 and lists[j+2][i] == 2 and lists[j+3][i] == 2 and lists[j+4][i] == 2:
                white_chess = 1
    for i in range(11):
        for j in range(4, 15):
            if lists[i][j] == 1 and lists[i+1][j-1] == 1 and lists[i+2][j-2] == 1 and lists[i+3][j-3] == 1 and lists[i+4][j-4] == 1:
                black_chess = 1
            elif lists[i][j] == 2 and lists[i+1][j-1] == 2 and lists[i+2][j-2] == 2 and lists[i+3][j-3] == 2 and lists[i+4][j-4] == 2:
                white_chess = 1
    for i in range(11):
        for j in range(11):
            if lists[i][j] == 1 and lists[i+1][j+1] == 1 and lists[i+2][j+2] == 1 and lists[i+3][j+3] == 1 and lists[i+4][j+4] == 1:
                black_chess = 1
            elif lists[i][j] == 2 and lists[i+1][j+1] == 2 and lists[i+2][j+2] == 2 and lists[i+3][j+3] == 2 and lists[i+4][j+4] == 2:
                white_chess = 1
    if black_chess == 1:
        canvas.create_text(border+7*spacing, border+7*spacing, text="black win", fill='red')
        flag = False
        count = count + 1
    elif white_chess == 1:
        canvas.create_text(border+7*spacing, border+7*spacing, text="white win", fill='green')
        flag = False
        count = count + 1


def restart(event):
    global flag
    while len(stack) > 0:
        tag, i, j = stack.pop()
        canvas.delete(tag)
        lists[i][j] = 0
    flag = True
    draw_chessboard()


def undo(event):
    if len(stack) > 0:
        tag, i, j = stack.pop()
        canvas.delete(tag)
        lists[i][j] = 0
        global player
        if player == "white":
            player = "black"
        else:
            player = "white"


root = Tk()
root.title("five-in-a-row")
root.resizable(0, 0)
canvas = Canvas(root, width=size, height=size, background='white')
canvas.pack()
draw_chessboard()
canvas.bind('<Button-1>', draw_chessman)
canvas.bind('<Button-2>', restart)
canvas.bind('<Button-3>', undo)
root.mainloop()