import pygame
import math
import time
from datetime import datetime

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Neon Analog Clock")

# Modern Color Palette - Neon/Cyberpunk Theme
BG_COLOR = (20, 20, 40)  # Deep dark blue
CLOCK_BG = (35, 40, 65)  # Darker blue gradient
BORDER_COLOR = (0, 255, 200)  # Cyan neon
ACCENT_COLOR = (255, 0, 150)  # Magenta neon
TEXT_COLOR = (0, 255, 200)  # Cyan text
HOUR_HAND = (255, 100, 200)  # Pink/Magenta
MINUTE_HAND = (0, 255, 150)  # Cyan/Turquoise
SECOND_HAND = (255, 50, 100)  # Hot pink
MARKER_COLOR = (100, 200, 255)  # Light blue
MARKER_HOUR_COLOR = (0, 255, 200)  # Bright cyan

# Clock dimensions
cx, cy = WIDTH // 2, HEIGHT // 2
clock_radius = 280
inner_radius = 250

# FPS
clock = pygame.time.Clock()
FPS = 60

def draw_glow_circle(center_x, center_y, radius, color, glow_width=10):
    """Draw a circle with neon glow effect"""
    # Draw glow layers
    for glow in range(glow_width, 0, -1):
        alpha = int(50 * (1 - glow / glow_width))
        glow_color = tuple(min(c + alpha, 255) for c in color)
        pygame.draw.circle(screen, glow_color, (center_x, center_y), radius + glow, 1)
    
    # Draw main circle
    pygame.draw.circle(screen, color, (center_x, center_y), radius)

def polar_to_cartesian(center_x, center_y, length, angle_deg):
    """Convert polar coordinates to cartesian (clock angle convention)"""
    rad = math.radians(90 - angle_deg)
    x = center_x + length * math.cos(rad)
    y = center_y - length * math.sin(rad)
    return int(x), int(y)

def draw_clock_face():
    """Draw modern minimal clock face"""
    
    # Draw outer rings
    pygame.draw.circle(screen, ACCENT_COLOR, (cx, cy), clock_radius + 20, 3)
    pygame.draw.circle(screen, BORDER_COLOR, (cx, cy), clock_radius + 15, 1)
    pygame.draw.circle(screen, ACCENT_COLOR, (cx, cy), clock_radius, 2)
    
    # Draw clock face
    pygame.draw.circle(screen, CLOCK_BG, (cx, cy), clock_radius - 5)
    
    # Draw concentric circles for depth
    pygame.draw.circle(screen, (50, 60, 100), (cx, cy), clock_radius - 30, 1)
    pygame.draw.circle(screen, (40, 50, 90), (cx, cy), clock_radius - 60, 1)
    
    # Draw hour markers - Modern blocky design
    for i in range(12):
        angle = i * 30
        x_out, y_out = polar_to_cartesian(cx, cy, clock_radius - 20, angle)
        x_in, y_in = polar_to_cartesian(cx, cy, clock_radius - 50, angle)
        
        # Draw thick neon lines
        pygame.draw.line(screen, MARKER_HOUR_COLOR, (x_out, y_out), (x_in, y_in), 6)
        
        # Draw circle markers
        pygame.draw.circle(screen, MARKER_HOUR_COLOR, (x_out, y_out), 8)
        pygame.draw.circle(screen, ACCENT_COLOR, (x_out, y_out), 8, 2)
    
    # Draw minute markers - Minimal dots
    for i in range(60):
        if i % 5 != 0:
            angle = i * 6
            x, y = polar_to_cartesian(cx, cy, clock_radius - 28, angle)
            pygame.draw.circle(screen, MARKER_COLOR, (x, y), 3)
    
    # Draw numbers (1-12) with modern font
    font_numerals = pygame.font.Font(None, 48)
    numerals = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    
    for i, numeral in enumerate(numerals):
        angle = i * 30
        x, y = polar_to_cartesian(cx, cy, clock_radius - 75, angle)
        text_surface = font_numerals.render(numeral, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

def draw_hand(angle, length, color, width):
    """Draw a modern clock hand with glow"""
    
    x, y = polar_to_cartesian(cx, cy, length, angle)
    
    # Draw glow effect for hand
    for glow in range(width + 4, 0, -1):
        glow_alpha = int(80 * (1 - glow / (width + 4)))
        glow_color = tuple(min(c + glow_alpha, 255) for c in color)
        pygame.draw.line(screen, glow_color, (cx, cy), (x, y), glow)
    
    # Draw main hand
    pygame.draw.line(screen, color, (cx, cy), (x, y), width)
    
    # Draw arrow/pointer at end
    if length > 100:
        # Calculate the point before the end
        x_prev, y_prev = polar_to_cartesian(cx, cy, length - 20, angle)
        pygame.draw.circle(screen, color, (x, y), width // 2 + 2)
        pygame.draw.circle(screen, CLOCK_BG, (x, y), width // 2 - 1)

def draw_center_decoration():
    """Draw center knob with modern design"""
    # Outer ring
    pygame.draw.circle(screen, BORDER_COLOR, (cx, cy), 20, 3)
    pygame.draw.circle(screen, ACCENT_COLOR, (cx, cy), 20)
    
    # Inner core
    pygame.draw.circle(screen, MARKER_HOUR_COLOR, (cx, cy), 12)
    pygame.draw.circle(screen, TEXT_COLOR, (cx, cy), 12, 1)

def draw_digital_time(t):
    """Draw digital time display"""
    font_digital = pygame.font.Font(None, 60)
    time_text = time.strftime("%H:%M:%S", t)
    
    text_surface = font_digital.render(time_text, True, HOUR_HAND)
    text_rect = text_surface.get_rect(center=(cx, cy + clock_radius + 100))
    
    # Draw glowing background box
    box_rect = text_rect.inflate(80, 40)
    pygame. draw.rect(screen, CLOCK_BG, box_rect)
    pygame.draw.rect(screen, BORDER_COLOR, box_rect, 3)
    pygame.draw.rect(screen, ACCENT_COLOR, box_rect, 1)
    
    screen.blit(text_surface, text_rect)

def draw_date():
    """Draw date display"""
    font_date = pygame.font.Font(None, 32)
    date_text = datetime.now().strftime("%A, %B %d")
    
    text_surface = font_date.render(date_text, True, MINUTE_HAND)
    text_rect = text_surface.get_rect(center=(cx, cy - clock_radius - 80))
    
    screen.blit(text_surface, text_rect)

def draw_year():
    """Draw year with neon effect"""
    font_year = pygame.font.Font(None, 28)
    year_text = datetime.now().strftime("%Y")
    
    text_surface = font_year. render(year_text, True, SECOND_HAND)
    text_rect = text_surface.get_rect(center=(cx, cy - clock_radius - 40))
    
    screen.blit(text_surface, text_rect)

def draw_milliseconds():
    """Draw millisecond indicator"""
    font_ms = pygame.font.Font(None, 24)
    ms = int((time.time() % 1) * 1000)
    ms_text = f"ms: {ms}"
    
    text_surface = font_ms.render(ms_text, True, ACCENT_COLOR)
    text_rect = text_surface.get_rect(center=(cx + 150, cy - 50))
    
    screen. blit(text_surface, text_rect)

def draw_decorative_lines():
    """Draw decorative lines around the clock"""
    # Top line
    pygame.draw.line(screen, BORDER_COLOR, (cx - 300, 30), (cx + 300, 30), 2)
    # Bottom line
    pygame.draw. line(screen, ACCENT_COLOR, (cx - 300, HEIGHT - 30), (cx + 300, HEIGHT - 30), 2)

# Main loop
running = True
frame_count = 0

while running:
    for event in pygame. event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background with subtle animation
    screen.fill(BG_COLOR)
    
    # Draw decorative elements
    draw_decorative_lines()
    
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
    
    # Draw clock
    draw_clock_face()
    
    # Draw hands with proper layering
    draw_hand(hour_angle, 110, HOUR_HAND, 16)
    draw_hand(minute_angle, 170, MINUTE_HAND, 12)
    draw_hand(second_angle, 190, SECOND_HAND, 4)
    
    # Draw center
    draw_center_decoration()
    
    # Draw information displays
    draw_date()
    draw_year()
    draw_digital_time(t)
    draw_milliseconds()
    
    pygame.display.update()
    clock. tick(FPS)
    frame_count += 1

pygame.quit()