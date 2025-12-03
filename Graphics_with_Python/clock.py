import pygame
import math
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rotating Analog Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARKGRAY = (80, 80, 80)
LIGHTBLUE = (0, 180, 255)

cx, cy = 300, 200
radius = 150
clock = pygame.time.Clock()

def rotate_point(x, y, cx, cy, angle):
    rad = math.radians(angle)
    x -= cx
    y -= cy
    x_new = x * math.cos(rad) - y * math.sin(rad)
    y_new = x * math.sin(rad) + y * math.cos(rad)
    return (int(x_new + cx), int(y_new + cy))

def draw_clock():
    pygame.draw.circle(screen, LIGHTBLUE, (cx, cy), radius, 3)

    # Draw 60 tick-marks
    for i in range(60):
        angle = -6 * i
        x1, y1 = rotate_point(cx, cy - 140, cx, cy, angle)
        size = 4 if i % 5 == 0 else 2
        pygame.draw.circle(screen, BLACK, (x1, y1), size)

def draw_hand(angle, length, color, width):
    x, y = rotate_point(cx, cy - length, cx, cy, angle)
    pygame.draw.line(screen, color, (cx, cy), (x, y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_clock()

    # Real time
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    # Angles
    sec_angle = -6 * sec
    min_angle = -6 * minute - (sec * 0.1)
    hour_angle = -30 * hour - (minute * 0.5)

    draw_hand(sec_angle, 130, MAGENTA, 2)
    draw_hand(min_angle, 110, CYAN, 5)
    draw_hand(hour_angle, 80, DARKGRAY, 8)

    pygame.display.update()
    clock.tick(1)  # Runs once per second (smooth & stable)

pygame.quit()
