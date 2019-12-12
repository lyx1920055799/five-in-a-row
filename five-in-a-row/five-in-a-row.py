import matplotlib.pyplot as plt
import numpy as np
import math

flag = 0
b = 0
w = 0
arr = np.zeros((15,15),int)

def run(event):
    global b
    global w
    if b == 0 and w == 0:
        global flag
        global arr
        for x in range(15):
            for y in range(15):
                len = np.sqrt(((x-event.xdata)**2)+((y-event.ydata)**2))
                if len <= 0.25 and arr[x][y] == 0:
                    if flag == 0:
                        flag = 1
                        arr[x][y] = 1
                        plt.title('Blue',color='blue')
                        plt.scatter(x,y,125,'r',zorder=2)
                        plt.draw()
                    elif flag == 1:
                        flag = 0
                        arr[x][y] = 2
                        plt.title('Red',color='red')
                        plt.scatter(x,y,125,'b',zorder=2)
                        plt.draw()
        for x in range(2,13):
            for y in range(2,13):
                if arr[x][y] == 1 and arr[x][y+1] == 1 and arr[x][y+2] == 1 and arr[x][y-1] == 1 and arr[x][y-2] == 1:
                    b = 1
                elif arr[x][y] == 1 and arr[x+1][y] == 1 and arr[x+2][y] == 1 and arr[x-1][y] == 1 and arr[x-2][y] == 1:
                    b = 1
                elif arr[x+1][y] == 1 and arr[x+1][y+1] == 1 and arr[x+1][y+2] == 1 and arr[x+1][y-1] == 1 and arr[x+1][y-2] == 1:
                    b = 1
                elif arr[x-1][y] == 1 and arr[x-1][y+1] == 1 and arr[x-1][y+2] == 1 and arr[x-1][y-1] == 1 and arr[x-1][y-2] == 1:
                    b = 1
                elif arr[x+2][y] == 1 and arr[x+2][y+1] == 1 and arr[x+2][y+2] == 1 and arr[x+2][y-1] == 1 and arr[x+2][y-2] == 1:
                    b = 1
                elif arr[x-2][y] == 1 and arr[x-2][y+1] == 1 and arr[x-2][y+2] == 1 and arr[x-2][y-1] == 1 and arr[x-2][y-2] == 1:
                    b = 1
                elif arr[x][y+1] == 1 and arr[x+1][y+1] == 1 and arr[x+2][y+1] == 1 and arr[x-1][y+1] == 1 and arr[x-2][y+1] == 1:
                    b = 1
                elif arr[x][y-1] == 1 and arr[x+1][y-1] == 1 and arr[x+2][y-1] == 1 and arr[x-1][y-1] == 1 and arr[x-2][y-1] == 1:
                    b = 1
                elif arr[x][y+2] == 1 and arr[x+1][y+2] == 1 and arr[x+2][y+2] == 1 and arr[x-1][y+2] == 1 and arr[x-2][y+2] == 1:
                    b = 1
                elif arr[x][y-2] == 1 and arr[x+1][y-2] == 1 and arr[x+2][y-2] == 1 and arr[x-1][y-2] == 1 and arr[x-2][y-2] == 1:
                    b = 1
                elif arr[x][y] == 1 and arr[x-1][y-1] == 1 and arr[x-2][y-2] == 1 and arr[x+1][y+1] == 1 and arr[x+2][y+2] == 1:
                    b = 1
                elif arr[x][y] == 1 and arr[x+1][y-1] == 1 and arr[x+2][y-2] == 1 and arr[x-1][y+1] == 1 and arr[x-2][y+2] == 1:
                    b = 1
                elif arr[x][y] == 2 and arr[x][y+1] == 2 and arr[x][y+2] == 2 and arr[x][y-1] == 2 and arr[x][y-2] == 2:
                    w = 1
                elif arr[x][y] == 2 and arr[x+1][y] == 2 and arr[x+2][y] == 2 and arr[x-1][y] == 2 and arr[x-2][y] == 2:
                    w = 1
                elif arr[x+1][y] == 2 and arr[x+1][y+1] == 2 and arr[x+1][y+2] == 2 and arr[x+1][y-1] == 2 and arr[x+1][y-2] == 2:
                    w = 1
                elif arr[x-1][y] == 2 and arr[x-1][y+1] == 2 and arr[x-1][y+2] == 2 and arr[x-1][y-1] == 2 and arr[x-1][y-2] == 2:
                    w = 1
                elif arr[x+2][y] == 2 and arr[x+2][y+1] == 2 and arr[x+2][y+2] == 2 and arr[x+2][y-1] == 2 and arr[x+2][y-2] == 2:
                    w = 1
                elif arr[x-2][y] == 2 and arr[x-2][y+1] == 2 and arr[x-2][y+2] == 2 and arr[x-2][y-1] == 2 and arr[x-2][y-2] == 2:
                    w = 1
                elif arr[x][y+1] == 2 and arr[x+1][y+1] == 2 and arr[x+2][y+1] == 2 and arr[x-1][y+1] == 2 and arr[x-2][y+1] == 2:
                    w = 1
                elif arr[x][y-1] == 2 and arr[x+1][y-1] == 2 and arr[x+2][y-1] == 2 and arr[x-1][y-1] == 2 and arr[x-2][y-1] == 2:
                    w = 1
                elif arr[x][y+2] == 2 and arr[x+1][y+2] == 2 and arr[x+2][y+2] == 2 and arr[x-1][y+2] == 2 and arr[x-2][y+2] == 2:
                    w = 1
                elif arr[x][y-2] == 2 and arr[x+1][y-2] == 2 and arr[x+2][y-2] == 2 and arr[x-1][y-2] == 2 and arr[x-2][y-2] == 2:
                    w = 1
                elif arr[x][y] == 2 and arr[x-1][y-1] == 2 and arr[x-2][y-2] == 2 and arr[x+1][y+1] == 2 and arr[x+2][y+2] == 2:
                    w = 1
                elif arr[x][y] == 2 and arr[x+1][y-1] == 2 and arr[x+2][y-2] == 2 and arr[x-1][y+1] == 2 and arr[x-2][y+2] == 2:
                    w = 1
                if b == 1:
                    plt.title('Red win',color='red')
                    return
                elif w == 1:
                    plt.title('Blue win',color='blue')
                    return

if __name__ == '__main__':
    fig=plt.figure(1)
    fig.canvas.mpl_connect('button_press_event', run)
    for i in range(15):
        plt.vlines(i,0,14,'peru')
        plt.hlines(i,0,14,'peru')
    plt.axis('off')
    plt.show()