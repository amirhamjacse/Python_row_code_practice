import pygame
import math
import time
from datetime import datetime

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1000, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digestive System Clock")

# Color Palette - Biological Theme
BG_COLOR = (30, 20, 40)  # Dark flesh tone
SKIN_COLOR = (220, 180, 150)  # Skin tone
ORGAN_COLOR = (200, 100, 80)  # Organ/tissue red
ESOPHAGUS_COLOR = (180, 120, 100)  # Esophagus brown
STOMACH_COLOR = (220, 140, 100)  # Stomach pink
SMALL_INTESTINE_COLOR = (200, 150, 100)  # Small intestine tan
LARGE_INTESTINE_COLOR = (180, 130, 90)  # Large intestine brown
TEXT_COLOR = (50, 50, 50)  # Dark text
HAND_COLOR_HOUR = (200, 80, 80)  # Blood red for hour
HAND_COLOR_MINUTE = (100, 150, 200)  # Blue for minute
HAND_COLOR_SECOND = (255, 200, 0)  # Gold for second
ORGAN_OUTLINE = (100, 50, 50)  # Dark outline

# Positions
cx, cy = WIDTH // 2, HEIGHT // 2 - 100
clock_radius = 200

# FPS
clock = pygame.time.Clock()
FPS = 60

def draw_mouth():
    """Draw mouth at the top"""
    mouth_y = cy - clock_radius - 150
    # Lips
    pygame.draw.ellipse(screen, (200, 100, 100), (cx - 50, mouth_y - 15, 100, 30))
    pygame.draw.ellipse(screen, (150, 70, 70), (cx - 50, mouth_y - 15, 100, 30), 3)
    
    # Teeth marks
    for i in range(6):
        x_pos = cx - 40 + i * 15
        pygame.draw.line(screen, TEXT_COLOR, (x_pos, mouth_y - 10), (x_pos, mouth_y + 10), 2)

def draw_esophagus():
    """Draw esophagus (tube from mouth to stomach)"""
    start_x, start_y = cx, cy - clock_radius - 120
    end_x, end_y = cx, cy - clock_radius + 50
    
    # Main tube
    pygame.draw.line(screen, ESOPHAGUS_COLOR, (start_x - 15, start_y), (end_x - 15, end_y), 25)
    pygame.draw.line(screen, ESOPHAGUS_COLOR, (start_x + 15, start_y), (end_x + 15, end_y), 25)
    
    # Outline
    pygame.draw.line(screen, ORGAN_OUTLINE, (start_x - 20, start_y), (end_x - 20, end_y), 3)
    pygame. draw.line(screen, ORGAN_OUTLINE, (start_x + 20, start_y), (end_x + 20, end_y), 3)
    
    # Muscle rings
    for i in range(5):
        y_pos = start_y + i * 35
        pygame.draw.arc(screen, ORGAN_OUTLINE, (start_x - 25, y_pos - 10, 50, 20), 0, math.pi, 2)

def draw_stomach():
    """Draw stomach as a pouch"""
    stomach_x = cx - 60
    stomach_y = cy - clock_radius + 80
    
    # Stomach shape (irregular pouch)
    points = [
        (stomach_x - 40, stomach_y - 20),
        (stomach_x - 50, stomach_y + 30),
        (stomach_x - 30, stomach_y + 60),
        (stomach_x + 40, stomach_y + 50),
        (stomach_x + 50, stomach_y + 10),
        (stomach_x + 30, stomach_y - 30),
    ]
    
    pygame.draw.polygon(screen, STOMACH_COLOR, points)
    pygame.draw.polygon(screen, ORGAN_OUTLINE, points, 3)
    
    # Internal lines (stomach folds)
    pygame.draw.line(screen, ORGAN_OUTLINE, points[0], (stomach_x, stomach_y + 30), 2)
    pygame.draw.line(screen, ORGAN_OUTLINE, points[5], (stomach_x + 10, stomach_y + 40), 2)

def draw_small_intestine():
    """Draw small intestine (coiled loops)"""
    start_x = cx - 60
    start_y = cy - clock_radius + 150
    
    # Coiled intestine loops
    radius = 50
    for loop in range(3):
        center_y = start_y + loop * 100
        
        for i in range(2):
            if i == 0:
                # Left loop
                pygame.draw.arc(screen, SMALL_INTESTINE_COLOR, 
                              (start_x - radius - 30, center_y - radius, radius * 2, radius * 2),
                              0, math.pi, 15)
            else:
                # Right loop
                pygame.draw.arc(screen, SMALL_INTESTINE_COLOR,
                              (start_x + radius - 30, center_y - radius, radius * 2, radius * 2),
                              math.pi, 2 * math.pi, 15)
    
    # Connection lines
    pygame.draw.line(screen, ORGAN_OUTLINE, (cx - 60, start_y - 30), (cx - 60, start_y), 3)

def draw_large_intestine():
    """Draw large intestine (colon shape)"""
    base_y = cy - clock_radius + 350
    
    # Left vertical part
    pygame.draw.line(screen, LARGE_INTESTINE_COLOR, (cx - 120, base_y), (cx - 120, base_y + 80), 20)
    pygame.draw.line(screen, ORGAN_OUTLINE, (cx - 120, base_y), (cx - 120, base_y + 80), 3)
    
    # Top horizontal part
    pygame.draw. line(screen, LARGE_INTESTINE_COLOR, (cx - 120, base_y), (cx + 80, base_y), 20)
    pygame.draw. line(screen, ORGAN_OUTLINE, (cx - 120, base_y), (cx + 80, base_y), 3)
    
    # Right vertical part
    pygame.draw.line(screen, LARGE_INTESTINE_COLOR, (cx + 80, base_y), (cx + 80, base_y + 80), 20)
    pygame.draw.line(screen, ORGAN_OUTLINE, (cx + 80, base_y), (cx + 80, base_y + 80), 3)

def draw_rectum():
    """Draw rectum"""
    rect_x = cx + 80
    rect_y = cy - clock_radius + 430
    
    pygame.draw.line(screen, ORGAN_OUTLINE, (rect_x, rect_y), (rect_x, rect_y + 40), 15)
    pygame.draw.line(screen, ORGAN_COLOR, (rect_x, rect_y), (rect_x, rect_y + 40), 10)

def draw_liver():
    """Draw liver on the right side"""
    liver_x = cx + 150
    liver_y = cy - clock_radius + 100
    
    # Liver shape (rounded rectangle)
    pygame.draw.ellipse(screen, (180, 80, 60), (liver_x - 40, liver_y - 30, 80, 70))
    pygame.draw.ellipse(screen, ORGAN_OUTLINE, (liver_x - 40, liver_y - 30, 80, 70), 3)
    
    # Internal structure
    pygame.draw.line(screen, ORGAN_OUTLINE, (liver_x, liver_y - 25), (liver_x, liver_y + 25), 2)

def draw_pancreas():
    """Draw pancreas"""
    pan_x = cx + 50
    pan_y = cy - clock_radius + 120
    
    pygame.draw.line(screen, (200, 150, 100), (pan_x - 30, pan_y), (pan_x + 40, pan_y), 12)
    pygame.draw.line(screen, ORGAN_OUTLINE, (pan_x - 30, pan_y), (pan_x + 40, pan_y), 2)

def draw_clock_face():
    """Draw the digestive system as clock face"""
    
    # Draw all digestive organs
    draw_mouth()
    draw_esophagus()
    draw_stomach()
    draw_liver()
    draw_pancreas()
    draw_small_intestine()
    draw_large_intestine()
    draw_rectum()
    
    # Draw clock circle in the center (on the stomach area)
    # This will be the main clock face
    stomach_clock_x = cx - 60
    stomach_clock_y = cy - clock_radius + 120
    
    pygame.draw.circle(screen, SKIN_COLOR, (stomach_clock_x, stomach_clock_y), 120)
    pygame.draw.circle(screen, ORGAN_OUTLINE, (stomach_clock_x, stomach_clock_y), 120, 4)
    
    # Draw hour markers (enzymes/cells around the stomach clock)
    for i in range(12):
        angle = i * 30
        rad = math.radians(90 - angle)
        
        x_out = stomach_clock_x + 120 * math.cos(rad)
        y_out = stomach_clock_y - 120 * math.sin(rad)
        x_in = stomach_clock_x + 95 * math.cos(rad)
        y_in = stomach_clock_y - 95 * math.sin(rad)
        
        pygame.draw.line(screen, TEXT_COLOR, (x_out, y_out), (x_in, y_in), 4)
        
        # Draw cell circles
        pygame.draw.circle(screen, ORGAN_COLOR, (x_out, y_out), 6)
    
    # Draw minute markers (bacteria/cells)
    for i in range(60):
        if i % 5 != 0:
            angle = i * 6
            rad = math.radians(90 - angle)
            
            x = stomach_clock_x + 115 * math.cos(rad)
            y = stomach_clock_y - 115 * math. sin(rad)
            
            pygame.draw.circle(screen, (150, 100, 80), (x, y), 2)
    
    # Draw numbers
    font_num = pygame.font.Font(None, 36)
    numerals = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    
    for i, numeral in enumerate(numerals):
        angle = i * 30
        rad = math.radians(90 - angle)
        
        x = stomach_clock_x + 75 * math.cos(rad)
        y = stomach_clock_y - 75 * math. sin(rad)
        
        text_surface = font_num.render(numeral, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

def polar_to_cartesian(center_x, center_y, length, angle_deg):
    """Convert polar coordinates to cartesian"""
    rad = math.radians(90 - angle_deg)
    x = center_x + length * math.cos(rad)
    y = center_y - length * math.sin(rad)
    return int(x), int(y)

def draw_hand(angle, length, color, width, center_x, center_y):
    """Draw clock hand (representing food/nutrients moving through system)"""
    
    x, y = polar_to_cartesian(center_x, center_y, length, angle)
    
    # Shadow
    pygame.draw.line(screen, (50, 30, 30), (center_x + 2, center_y + 2), (x + 2, y + 2), width + 1)
    
    # Main hand with gradient effect
    pygame.draw.line(screen, color, (center_x, center_y), (x, y), width)
    
    # End circle (nutrient particle)
    pygame.draw.circle(screen, color, (x, y), width // 2 + 2)
    pygame.draw.circle(screen, SKIN_COLOR, (x, y), width // 2)

def draw_center_cell():
    """Draw center nucleus"""
    stomach_clock_x = cx - 60
    stomach_clock_y = cy - clock_radius + 120
    
    pygame.draw.circle(screen, ORGAN_COLOR, (stomach_clock_x, stomach_clock_y), 15)
    pygame.draw.circle(screen, TEXT_COLOR, (stomach_clock_x, stomach_clock_y), 15, 2)
    pygame.draw.circle(screen, SKIN_COLOR, (stomach_clock_x, stomach_clock_y), 8)

def draw_title():
    """Draw title"""
    font_title = pygame.font.Font(None, 48)
    title = "DIGESTIVE SYSTEM CLOCK"
    text_surface = font_title.render(title, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text_surface, text_rect)

def draw_digital_time(t):
    """Draw digital time"""
    font_digital = pygame.font.Font(None, 36)
    time_text = time.strftime("%H:%M:%S", t)
    
    text_surface = font_digital.render(time_text, True, HAND_COLOR_HOUR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 60))
    
    # Background box
    box_rect = text_rect.inflate(60, 30)
    pygame. draw.rect(screen, SKIN_COLOR, box_rect)
    pygame.draw.rect(screen, ORGAN_OUTLINE, box_rect, 3)
    
    screen.blit(text_surface, text_rect)

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BG_COLOR)
    
    # Get current time
    t = time.localtime()
    now = time.time()
    
    # Calculate smooth time values
    seconds = t.tm_sec + (now % 1)
    minutes = t.tm_min + seconds / 60
    hours = (t.tm_hour % 12) + minutes / 60
    
    # Calculate angles
    second_angle = seconds * 6
    minute_angle = minutes * 6
    hour_angle = hours * 30
    
    # Draw digestive system
    draw_clock_face()
    
    # Draw hands (food moving through digestive system)
    stomach_clock_x = cx - 60
    stomach_clock_y = cy - clock_radius + 120
    
    draw_hand(hour_angle, 80, HAND_COLOR_HOUR, 14, stomach_clock_x, stomach_clock_y)
    draw_hand(minute_angle, 100, HAND_COLOR_MINUTE, 10, stomach_clock_x, stomach_clock_y)
    draw_hand(second_angle, 105, HAND_COLOR_SECOND, 4, stomach_clock_x, stomach_clock_y)
    
    # Draw center cell
    draw_center_cell()
    
    # Draw title and time
    draw_title()
    draw_digital_time(t)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()