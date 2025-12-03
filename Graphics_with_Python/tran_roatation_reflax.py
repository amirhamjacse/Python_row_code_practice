import math

def translation():
    x1, y1, x2, y2 = 200, 150, 300, 250
    tx, ty = 50, 50
    print("Rectangle before translation")
    rect_before = [(x1, y1), (x2, y2)]
    print("Coordinates:", rect_before)
    print("Rectangle after translation")
    rect_after = [(x1 + tx, y1 + ty), (x2 + tx, y2 + ty)]
    print("Coordinates:", rect_after)

def rotation():
    x1, y1, x2, y2 = 200, 200, 300, 300
    print("Rectangle with rotation")
    rect_before = [(x1, y1), (x2, y2)]
    print("Coordinates:", rect_before)
    a = float(input("Angle of rotation: "))
    a = (a * math.pi) / 180  # degree → radian
    xr = x1 + ((x2 - x1) * math.cos(a) - (y2 - y1) * math.sin(a))
    yr = y1 + ((x2 - x1) * math.sin(a) + (y2 - y1) * math.cos(a))
    rect_after = [(x1, y1), (int(xr), int(yr))]
    print("Coordinates after rotation:", rect_after)

def scaling():
    x1, y1, x2, y2 = 30, 30, 70, 70
    x, y = 2, 2
    print("Before scaling")
    rect_before = [(x1, y1), (x2, y2)]
    print("Coordinates:", rect_before)
    print("After scaling")
    rect_after = [(x1 * x, y1 * y), (x2 * x, y2 * y)]
    print("Coordinates:", rect_after)

def reflection():
    x1, y1, x2, y2, x3, y3 = 200, 300, 500, 300, 350, 400
    print("Triangle before reflection")
    triangle_before = [(x1, y1), (x2, y2), (x3, y3)]
    print("Coordinates:", triangle_before)
    print("Triangle after reflection")
    triangle_after = [(x1, -y1 + 500), (x2, -y2 + 500), (x3, -y3 + 500)]
    print("Coordinates:", triangle_after)

def shearing():
    x1, y1, x2, y2, x3, y3, x4, y4 = 200, 100, 300, 100, 200, 150, 300, 150
    shx = 2
    print("Before shearing of rectangle")
    rect_before = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    print("Coordinates:", rect_before)
    print("After shearing of rectangle")
    x1, x2, x3, x4 = x1 + shx * y1, x2 + shx * y2, x3 + shx * y3, x4 + shx * y4
    rect_after = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    print("Coordinates:", rect_after)

def main():
    print("1.Translation\n2.Rotation\n3.Scaling\n4.Reflection\n5.Shearing")
    s = int(input("Selection: "))
    if s == 1:
        translation()
    elif s == 2:
        rotation()
    elif s == 3:
        scaling()
    elif s == 4:
        reflection()
    elif s == 5:
        shearing()
    else:
        print("Invalid Selection")

if __name__ == "__main__":
    main()
