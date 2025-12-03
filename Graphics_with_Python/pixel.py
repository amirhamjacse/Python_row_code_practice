import math

def putpixel(x, y, color):
    print(f"Pixel at ({x}, {y}) with color {color}")

def main():
    YELLOW = 'yellow'  # Placeholder for color

    x1, y1 = map(int, input("put x1 and y1: ").split())
    x2, y2 = map(int, input("put x2 and y2: ").split())

    dx = x2 - x1
    dy = y2 - y1

    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = dx / step
    yinc = dy / step

    x = x1
    y = y1

    for i in range(int(step) + 1):
        print(round(x), ",", round(y))
        putpixel(round(x), round(y), YELLOW)
        x += xinc
        y += yinc

if __name__ == "__main__":
    main()
