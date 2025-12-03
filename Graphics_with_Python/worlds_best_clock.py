import pygame
import math
import time
from datetime import datetime

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1400, 900
screen = pygame. display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The World's Greatest Clock")

# Premium Color Palette
BG_COLOR = (8, 12, 20)  # Deep space black
PRIMARY_COLOR = (24, 200, 255)  # Quantum cyan
SECONDARY_COLOR = (255, 100, 200)  # Premium magenta
ACCENT_COLOR = (200, 255, 100)  # Neon lime
GOLD_COLOR = (255, 215, 0)  # Pure gold
SILVER_COLOR = (220, 220, 220)  # Premium silver
TEXT_COLOR = (240, 245, 255)  # Crystal white
DARK_TEXT = (20, 20, 30)  # Deep text
HAND_HOUR = (255, 100, 150)  # Rose gold
HAND_MINUTE = (100, 220, 255)  # Sky blue
HAND_SECOND = (255, 200, 100)  # Solar gold

# Main clock position
cx, cy = 350, HEIGHT // 2
main_radius = 280

# Secondary clocks
clock2_x, clock2_y = WIDTH - 350, HEIGHT // 2 - 200
clock2_radius = 180

clock3_x, clock3_y = WIDTH - 350, HEIGHT // 2 + 200
clock3_radius = 180

# FPS
clock = pygame.time.Clock()
FPS = 60
elapsed_time = 0

def draw_particle_field():
    """Draw animated particle field background"""
    for i in range(50):
        x = (elapsed_time * 0.5 + i * 20) % WIDTH
        y = (elapsed_time * 0.2 + i * 15) % HEIGHT
        size = max(1, 3 - (elapsed_time * 0.01) % 3)
        pygame.draw.circle(screen, PRIMARY_COLOR, (int(x), int(y)), int(size), 1)

def draw_orbiting_rings(center_x, center_y, radius, color, rotation):
    """Draw orbiting rings around clock"""
    # Multiple rings
    for ring_radius in [radius + 50, radius + 80, radius + 110]:
        # Rotated ring
        for angle in range(0, 360, 5):
            adjusted_angle = angle + rotation
            rad = math.radians(adjusted_angle)
            x = center_x + ring_radius * math.cos(rad)
            y = center_y + ring_radius * math.sin(rad)
            
            # Gradient effect
            intensity = int(128 * (math.sin(adjusted_angle * 0.1) + 1) / 2)
            glow_color = (
                min(color[0], 255),
                min(color[1], 255),
                min(color[2], 255)
            )
            pygame.draw.circle(screen, glow_color, (int(x), int(y)), 2)

def draw_quantum_glow(center_x, center_y, radius, color, intensity=1.0):
    """Draw quantum glow effect"""
    steps = 30
    for i in range(steps, 0, -1):
        alpha = int(100 * intensity * (1 - i / steps))
        glow_radius = radius + (steps - i) * 2
        
        r = min(int(color[0] * (i / steps)), 255)
        g = min(int(color[1] * (i / steps)), 255)
        b = min(int(color[2] * (i / steps)), 255)
        
        pygame.draw.circle(screen, (r, g, b), (center_x, center_y), glow_radius, 1)

def draw_luxe_clock_face(center_x, center_y, radius, clock_number=1):
    """Draw the most luxurious clock face"""
    
    # Quantum glow effect
    draw_quantum_glow(center_x, center_y, radius, PRIMARY_COLOR, 0.8)
    
    # Outer diamond frame
    diamond_offset = 30
    diamond_points = [
        (center_x, center_y - radius - diamond_offset),  # Top
        (center_x + radius + diamond_offset, center_y),  # Right
        (center_x, center_y + radius + diamond_offset),  # Bottom
        (center_x - radius - diamond_offset, center_y),  # Left
    ]
    pygame.draw.polygon(screen, GOLD_COLOR, diamond_points, 4)
    
    # Premium circular frame
    pygame.draw.circle(screen, SILVER_COLOR, (center_x, center_y), radius + 20, 3)
    pygame.draw.circle(screen, GOLD_COLOR, (center_x, center_y), radius + 15, 1)
    pygame.draw.circle(screen, PRIMARY_COLOR, (center_x, center_y), radius + 10, 1)
    
    # Main clock face
    pygame.draw.circle(screen, BG_COLOR, (center_x, center_y), radius)
    pygame.draw.circle(screen, SECONDARY_COLOR, (center_x, center_y), radius - 5, 2)
    
    # Inner gradient effect
    for i in range(radius - 5, radius - 20, -1):
        intensity = (radius - i) / 15
        color = (
            int(20 + intensity * 50),
            int(20 + intensity * 30),
            int(40 + intensity * 60)
        )
        pygame. draw.circle(screen, color, (center_x, center_y), i, 1)
    
    # Luxury hour markers (triangular diamonds)
    for i in range(12):
        angle = i * 30
        rad = math.radians(90 - angle)
        
        # Outer point
        x_out = center_x + (radius - 15) * math.cos(rad)
        y_out = center_y - (radius - 15) * math.sin(rad)
        
        # Create diamond marker
        diamond_size = 12
        angle_rad = math.radians(angle)
        marker_points = [
            (x_out, y_out - diamond_size),  # Top
            (x_out + diamond_size, y_out),  # Right
            (x_out, y_out + diamond_size),  # Bottom
            (x_out - diamond_size, y_out),  # Left
        ]
        
        pygame.draw.polygon(screen, GOLD_COLOR, marker_points)
        pygame.draw.polygon(screen, PRIMARY_COLOR, marker_points, 2)
        
        # Glow effect
        pygame.draw.circle(screen, SECONDARY_COLOR, (int(x_out), int(y_out)), diamond_size + 3, 1)
    
    # Premium minute markers (small circles)
    for i in range(60):
        if i % 5 != 0:
            angle = i * 6
            rad = math.radians(90 - angle)
            
            x = center_x + (radius - 22) * math.cos(rad)
            y = center_y - (radius - 22) * math.sin(rad)
            
            pygame.draw.circle(screen, ACCENT_COLOR, (int(x), int(y)), 4)
            pygame.draw.circle(screen, PRIMARY_COLOR, (int(x), int(y)), 4, 1)
    
    # Roman numerals with premium styling
    font_numerals = pygame.font.Font(None, 52)
    numerals = ['XII', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
    
    for i, numeral in enumerate(numerals):
        angle = i * 30
        rad = math.radians(90 - angle)
        
        x = center_x + (radius - 70) * math.cos(rad)
        y = center_y - (radius - 70) * math.sin(rad)
        
        text_surface = font_numerals.render(numeral, True, GOLD_COLOR)
        text_rect = text_surface.get_rect(center=(int(x), int(y)))
        
        # Text shadow
        shadow_surface = font_numerals.render(numeral, True, DARK_TEXT)
        screen.blit(shadow_surface, (text_rect.x + 2, text_rect.y + 2))
        screen.blit(text_surface, text_rect)

def draw_premium_hand(angle, length, color, width, center_x, center_y):
    """Draw premium clock hand with multiple layers"""
    
    rad = math.radians(90 - angle)
    x = center_x + length * math.cos(rad)
    y = center_y - length * math.sin(rad)
    
    # Multiple glow layers
    for glow_width in range(width + 8, 0, -1):
        glow_intensity = int(100 * (1 - glow_width / (width + 8)))
        glow_color = (
            min(color[0] + glow_intensity, 255),
            min(color[1] + glow_intensity, 255),
            min(color[2] + glow_intensity, 255)
        )
        pygame.draw.line(screen, glow_color, (center_x, center_y), (int(x), int(y)), glow_width)
    
    # Main hand
    pygame.draw.line(screen, color, (center_x, center_y), (int(x), int(y)), width)
    
    # Gradient tip
    tip_x, tip_y = int(x), int(y)
    pygame.draw.circle(screen, color, (tip_x, tip_y), width // 2 + 3)
    pygame.draw.circle(screen, ACCENT_COLOR, (tip_x, tip_y), width // 2)

def draw_premium_center(center_x, center_y):
    """Draw premium center knob"""
    # Outer rings
    pygame.draw.circle(screen, GOLD_COLOR, (center_x, center_y), 25, 3)
    pygame. draw.circle(screen, PRIMARY_COLOR, (center_x, center_y), 22, 2)
    pygame.draw.circle(screen, SECONDARY_COLOR, (center_x, center_y), 18, 1)
    
    # Inner jewel
    pygame.draw.circle(screen, ACCENT_COLOR, (center_x, center_y), 15)
    pygame.draw.circle(screen, GOLD_COLOR, (center_x, center_y), 15, 2)
    
    # Center point
    pygame.draw.circle(screen, SILVER_COLOR, (center_x, center_y), 8)
    pygame.draw.circle(screen, DARK_TEXT, (center_x, center_y), 5)

def draw_info_panel():
    """Draw premium information panel"""
    panel_x = 50
    panel_y = 50
    panel_width = 250
    panel_height = 200
    
    # Panel background
    pygame.draw.rect(screen, BG_COLOR, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, GOLD_COLOR, (panel_x, panel_y, panel_width, panel_height), 2)
    pygame.draw.rect(screen, PRIMARY_COLOR, (panel_x, panel_y, panel_width, panel_height), 1)
    
    # Title
    font_title = pygame.font.Font(None, 24)
    title = font_title.render("LUXURY TIMEPIECE", True, GOLD_COLOR)
    screen.blit(title, (panel_x + 20, panel_y + 15))
    
    # Digital time
    font_time = pygame.font.Font(None, 32)
    t = time.localtime()
    time_text = time. strftime("%H:%M:%S", t)
    time_surf = font_time.render(time_text, True, PRIMARY_COLOR)
    screen.blit(time_surf, (panel_x + 25, panel_y + 50))
    
    # Date
    font_date = pygame. font.Font(None, 16)
    date_text = datetime.now().strftime("%A")
    date_surf = font_date.render(date_text, True, SECONDARY_COLOR)
    screen.blit(date_surf, (panel_x + 25, panel_y + 90))
    
    # Sub-info
    info_text = datetime.now().strftime("%B %d, %Y")
    info_surf = font_date.render(info_text, True, ACCENT_COLOR)
    screen.blit(info_surf, (panel_x + 25, panel_y + 115))
    
    # FPS counter
    fps_text = font_date.render(f"FPS: {int(clock.get_fps())}", True, TEXT_COLOR)
    screen.blit(fps_text, (panel_x + 25, panel_y + 140))
    
    # Status
    status_text = font_date.render("SYNCED", True, ACCENT_COLOR)
    screen.blit(status_text, (panel_x + 25, panel_y + 165))

def draw_statistics_panel():
    """Draw statistics panel on right"""
    panel_x = WIDTH - 300
    panel_y = 50
    panel_width = 250
    panel_height = 200
    
    pygame.draw.rect(screen, BG_COLOR, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, SECONDARY_COLOR, (panel_x, panel_y, panel_width, panel_height), 2)
    pygame.draw.rect(screen, PRIMARY_COLOR, (panel_x, panel_y, panel_width, panel_height), 1)
    
    font_label = pygame.font.Font(None, 20)
    
    # Title
    title = font_label.render("WORLD CLOCKS", True, SECONDARY_COLOR)
    screen.blit(title, (panel_x + 20, panel_y + 15))
    
    # Clock info
    t = time.localtime()
    
    timezones = [
        ("UTC", 0),
        ("EST", -5),
        ("JST", 9),
    ]
    
    y_offset = panel_y + 50
    for tz_name, tz_offset in timezones:
        tz_hour = (t.tm_hour + tz_offset) % 24
        tz_text = f"{tz_name}: {tz_hour:02d}:{t.tm_min:02d}"
        text_surf = font_label.render(tz_text, True, PRIMARY_COLOR)
        screen.blit(text_surf, (panel_x + 20, y_offset))
        y_offset += 30

def draw_main_title():
    """Draw main title with premium styling"""
    font_title = pygame.font.Font(None, 72)
    title = "⏰ WORLD'S GREATEST CLOCK ⏰"
    
    title_surf = font_title.render(title, True, GOLD_COLOR)
    title_rect = title_surf.get_rect(center=(WIDTH // 2, 30))
    
    # Shadow
    shadow_surf = font_title.render(title, True, DARK_TEXT)
    screen.blit(shadow_surf, (title_rect.x + 3, title_rect.y + 3))
    screen.blit(title_surf, title_rect)

def draw_decorative_elements():
    """Draw decorative elements"""
    # Top line
    pygame.draw.line(screen, GOLD_COLOR, (50, 95), (WIDTH - 50, 95), 2)
    pygame.draw.line(screen, PRIMARY_COLOR, (50, 96), (WIDTH - 50, 96), 1)
    
    # Bottom line
    pygame.draw.line(screen, SECONDARY_COLOR, (50, HEIGHT - 50), (WIDTH - 50, HEIGHT - 50), 2)
    pygame.draw.line(screen, ACCENT_COLOR, (50, HEIGHT - 49), (WIDTH - 50, HEIGHT - 49), 1)

# Main loop
running = True
frame_count = 0

while running:
    for event in pygame. event.get():
        if event.type == pygame.QUIT:
            running = False
    
    elapsed_time += 1
    frame_count += 1
    
    # Fill background
    screen.fill(BG_COLOR)
    
    # Draw particle field
    draw_particle_field()
    
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
    
    # Draw main luxurious clock
    rotation = (elapsed_time * 0.5) % 360
    draw_orbiting_rings(cx, cy, main_radius, PRIMARY_COLOR, rotation)
    draw_luxe_clock_face(cx, cy, main_radius)
    
    # Draw hands on main clock
    draw_premium_hand(hour_angle, 100, HAND_HOUR, 18, cx, cy)
    draw_premium_hand(minute_angle, 140, HAND_MINUTE, 12, cx, cy)
    draw_premium_hand(second_angle, 150, HAND_SECOND, 5, cx, cy)
    
    # Draw center
    draw_premium_center(cx, cy)
    
    # Draw secondary clocks (time zones)
    draw_luxe_clock_face(clock2_x, clock2_y, clock2_radius)
    draw_premium_hand(hour_angle + 30, 80, HAND_HOUR, 12, clock2_x, clock2_y)
    draw_premium_hand(minute_angle + 30, 110, HAND_MINUTE, 8, clock2_x, clock2_y)
    draw_premium_hand(second_angle + 30, 115, HAND_SECOND, 3, clock2_x, clock2_y)
    draw_premium_center(clock2_x, clock2_y)
    
    draw_luxe_clock_face(clock3_x, clock3_y, clock3_radius)
    draw_premium_hand(hour_angle - 30, 80, HAND_HOUR, 12, clock3_x, clock3_y)
    draw_premium_hand(minute_angle - 30, 110, HAND_MINUTE, 8, clock3_x, clock3_y)
    draw_premium_hand(second_angle - 30, 115, HAND_SECOND, 3, clock3_x, clock3_y)
    draw_premium_center(clock3_x, clock3_y)
    
    # Draw UI panels
    draw_main_title()
    draw_decorative_elements()
    draw_info_panel()
    draw_statistics_panel()
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()