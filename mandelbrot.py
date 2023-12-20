from matplotlib import pyplot as plt
from matplotlib import cm
import random, math

def initialize_image(x_p, y_p):
    image = []
    for y in range(y_p):
        row = []
        for x in range(x_p):
            row.append(0)
        image.append(row)
    return image

def color_points():
    x_p = 500
    y_p = 500
    max_iter = 500
    image = initialize_image(x_p, y_p)
    for y in range(y_p):
        for x in range(x_p):
            diverged = False
            z = 0+0j
            c = (x/x_p*3-2) + (y/y_p*3-1.5)*1j
            for i in range(max_iter):
                if abs(z) >= 2:
                    diverged = True
                    break
                z = z**2 + c
            if diverged:
                image[y][x] = math.log(i)
            else:
                image[y][x] = 0

    fig, ax = plt.subplots()
    ax.imshow(image, origin='lower', extent=(-2,1,-1.5,1.5),
               cmap=cm.Greys_r, interpolation='nearest')
    
    fig.canvas.mpl_connect('button_press_event', lambda event: onclick(image, plt, event))
    
    #plt.colorbar()
    plt.show()

def onclick(image, plt, event):
    x_p = 500
    y_p = 500
    max_iter = 500
    c = event.xdata + event.ydata*1j
    for y in range(y_p):
        for x in range(x_p):
            diverged = False
            z = (x/x_p*4-2) + (y/y_p*4-2)*1j
            for i in range(max_iter):
                if abs(z) >= 2:
                    diverged = True
                    break
                z = z**2 + c
            if diverged:
                image[y][x] = math.log(i+1)
            else:
                image[y][x] = 0

    fig, ax = plt.subplots()
    ax.imshow(image, origin='lower', extent=(-2,2,-2,2),
                    cmap=cm.Greys_r, interpolation='nearest')
    fig.show()

if __name__ == '__main__':
    color_points()
