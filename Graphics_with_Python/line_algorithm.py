import matplotlib
matplotlib.use('TkAgg')   # Force GUI backend for Ubuntu

import matplotlib.pyplot as plt
import time

def drawline(x1, y1, x2, y2):
    points_x = []
    points_y = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    s1 = 1 if x2 > x1 else -1
    s2 = 1 if y2 > y1 else -1

    x = x1
    y = y1

    # Decide which is the driving axis
    if dy > dx:
        dx, dy = dy, dx
        interchange = 1
    else:
        interchange = 0

    d = 2 * dy - dx

    for i in range(dx + 1):
        points_x.append(x)
        points_y.append(y)

        if d >= 0:
            y += s2
            x += s1 if interchange == 1 else 0
            d -= 2 * dx
        
        x += s1 if interchange == 0 else 0
        d += 2 * dy

    # Plot
    plt.scatter(points_x, points_y)
    plt.plot(points_x, points_y)
    plt.gca().invert_yaxis()
    plt.title("Bresenham Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()   # interactive window


# User input
x1, y1 = map(int, input("Enter co-ordinates of first point: ").split())
x2, y2 = map(int, input("Enter co-ordinates of second point: ").split())

drawline(x1, y1, x2, y2)
