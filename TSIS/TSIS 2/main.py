import pygame
import math
import datetime
from collections import deque

# Initialize Pygame
pygame.init()

# Canvas Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint - TSIS 2")

# base_layer stores the permanent drawing
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0)) # Start with black background

# Colors
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

# Global State
clock = pygame.time.Clock()
LMBpressed = False
thickness = 5
curr_color = colorRED
current_tool = 'pencil' # Default tool

# Coordinates
currX, currY = 0, 0
prevX, prevY = 0, 0

# Text Tool Variables
text_active = False
text_buffer = ""
text_pos = (0, 0)
font = pygame.font.SysFont("Arial", 24)

def flood_fill(surface, start_pos, fill_color):
    """Fills a closed region using BFS algorithm."""
    target_color = surface.get_at(start_pos)
    if target_color == fill_color:
        return
    
    width, height = surface.get_size()
    queue = deque([start_pos])
    visited = {start_pos}

    while queue:
        x, y = queue.popleft()
        surface.set_at((x, y), fill_color)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited and surface.get_at((nx, ny)) == target_color:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

def draw_shape(surface, tool, color, start_pos, end_pos, thickness):
    """Draws geometric shapes on the provided surface."""
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx, dy = x2 - x1, y2 - y1

    if tool == 'rect':
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(dx), abs(dy))
        pygame.draw.rect(surface, color, rect, thickness)
    elif tool == 'circle':
        radius = int(math.hypot(dx, dy))
        pygame.draw.circle(surface, color, (x1, y1), radius, thickness)
    elif tool == 'line':
        pygame.draw.line(surface, color, start_pos, end_pos, thickness)
    elif tool == 'square':
        side = max(abs(dx), abs(dy))
        sx = x1 if x2 > x1 else x1 - side
        sy = y1 if y2 > y1 else y1 - side
        pygame.draw.rect(surface, color, (sx, sy, side, side), thickness)
    elif tool == 'right_tri':
        pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], thickness)
    elif tool == 'equi_tri':
        side = int(math.hypot(dx, dy))
        h = side * math.sqrt(3) / 2
        pygame.draw.polygon(surface, color, [(x1, y1), (x1 - side//2, y1 + h), (x1 + side//2, y1 + h)], thickness)
    elif tool == 'rhombus':
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        pygame.draw.polygon(surface, color, [(mx, y1), (x2, my), (mx, y2), (x1, my)], thickness)

running = True
print("--- Controls ---")
print("P: Pencil, L: Line, R: Rect, C: Circle, E: Eraser")
print("S: Square, T: Right Tri, Q: Equi Tri, H: Rhombus, F: Fill, X: Text")
print("Sizes: 1 (2px), 2 (5px), 3 (10px) | Colors: 4: Red, 5: Blue, 6: Green, 0: Black")
print("Ctrl+S: Save Canvas | Text: Enter to save, Esc to cancel")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            # Check for Save (Ctrl+S)
            if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"paint_save_{timestamp}.png"
                pygame.image.save(base_layer, filename)
                print(f"Canvas saved as {filename}")

            # If text tool is active, handle typing
            if text_active:
                if event.key == pygame.K_RETURN:
                    # Commit text to base layer
                    text_surf = font.render(text_buffer, True, curr_color)
                    base_layer.blit(text_surf, text_pos)
                    text_active = False
                    text_buffer = ""
                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_buffer = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_buffer = text_buffer[:-1]
                else:
                    text_buffer += event.unicode
            else:
                # Tool Selection
                if event.key == pygame.K_p: current_tool = 'pencil'
                if event.key == pygame.K_l: current_tool = 'line'
                if event.key == pygame.K_r: current_tool = 'rect'
                if event.key == pygame.K_c: current_tool = 'circle'
                if event.key == pygame.K_e: current_tool = 'eraser'
                if event.key == pygame.K_s: current_tool = 'square'
                if event.key == pygame.K_t: current_tool = 'right_tri'
                if event.key == pygame.K_q: current_tool = 'equi_tri'
                if event.key == pygame.K_h: current_tool = 'rhombus'
                if event.key == pygame.K_f: current_tool = 'fill'
                if event.key == pygame.K_x: current_tool = 'text'

                # Brush Size Selection
                if event.key == pygame.K_1: thickness = 2
                if event.key == pygame.K_2: thickness = 5
                if event.key == pygame.K_3: thickness = 10
                
                # Color Selection
                if event.key == pygame.K_4: curr_color = colorRED
                if event.key == pygame.K_5: curr_color = colorBLUE
                if event.key == pygame.K_6: curr_color = colorGREEN
                if event.key == pygame.K_0: curr_color = colorBLACK

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_tool == 'text':
                text_active = True
                text_pos = event.pos
                text_buffer = ""
            elif current_tool == 'fill':
                flood_fill(base_layer, event.pos, curr_color)
            else:
                LMBpressed = True
                prevX, prevY = event.pos

        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos
            if LMBpressed:
                if current_tool == 'pencil':
                    pygame.draw.line(base_layer, curr_color, (prevX, prevY), (currX, currY), thickness)
                    prevX, prevY = currX, currY
                elif current_tool == 'eraser':
                    pygame.draw.circle(base_layer, colorBLACK, (currX, currY), thickness * 3)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            # Draw finalized shapes onto the base_layer
            if current_tool not in ['pencil', 'eraser', 'fill', 'text']:
                draw_shape(base_layer, current_tool, curr_color, (prevX, prevY), (currX, currY), thickness)

    # Render Section
    screen.blit(base_layer, (0, 0)) # Draw permanent canvas
    
    # Render shape preview while dragging
    if LMBpressed and current_tool not in ['pencil', 'eraser', 'fill', 'text']:
        draw_shape(screen, current_tool, curr_color, (prevX, prevY), (currX, currY), thickness)
    
    # Render text preview while typing
    if text_active:
        text_surf = font.render(text_buffer + "|", True, curr_color)
        screen.blit(text_surf, text_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()