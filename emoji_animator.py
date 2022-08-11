import math
from turtle import bgcolor
import pygame 
import time

pygame.init()

cell_size = 25
row = 25
column = 56

start = time.time()
canvas = {}
print(time.time() - start)

screen = pygame.display.set_mode((cell_size * column, cell_size * row))
screen.fill((255, 255, 255))

cell = pygame.surface.Surface((cell_size, cell_size))

brush_color = (49, 55, 61) # black
background_color = (50, 53, 59)
color_map = { #discord default
    pygame.K_1: (49, 55, 61),    # black
    pygame.K_2: (230, 231, 232), # white
    pygame.K_3: (221, 46, 68),   # red
    pygame.K_4: (83, 169, 233),  # blue
    pygame.K_5: (253, 203, 88),  # yellow
    pygame.K_6: (120, 176, 89),  # green
    pygame.K_7: (244, 144, 12),  # orange
    pygame.K_8: (170, 142, 214), # purple
    pygame.K_9: (192, 105, 79)   # brown
}
show_grid = True

def canvas_reload():
    cell.fill(background_color)
    
    if (show_grid): 
        pygame.draw.rect(cell, (0, 0, 0), (0, 0, cell_size, cell_size), 1)
    
    for r in range(row):
        for c in range(column):
            screen.blit(cell, (c * cell_size, r * cell_size))
    
    for color, coords in canvas.items():
        cell.fill(color)

        if (show_grid): 
            pygame.draw.rect(cell, (0, 0, 0), (0, 0, cell_size, cell_size), 1)

        for coord in coords:
            screen.blit(cell, (coord[0] * cell_size, coord[1] * cell_size))


def canvas_reset():
    canvas.clear()
    canvas_reload()    

def place_cell(coords: list):
    if brush_color not in canvas:
        canvas.update({brush_color: coords})
    else:
         color_coords.extend([x for x in coords if x not in color_coords])
    
    coords.update({ })
        

    cell.fill(brush_color)
    if (show_grid):
        pygame.draw.rect(cell, (0, 0, 0), (0, 0, cell_size, cell_size), 1)
    screen.blit(cell, [x * cell_size for x in canvas_coords])

def remove_cell():
    mouse_coords = pygame.mouse.get_pos()
    canvas_coords = [math.floor(mouse_coords[0] / cell_size), math.floor(mouse_coords[1] / cell_size)]

    mouse_color = tuple(list(screen.get_at([x * cell_size + int(cell_size / 2) for x in canvas_coords]))[:3])
    if mouse_color not in canvas:
        return
    else:
        color_coords = canvas[mouse_color]

        color_coords.remove(canvas_coords)
        if color_coords == []:
            canvas.pop(mouse_color)
            
        cell.fill(background_color)
        
        if show_grid: 
            pygame.draw.rect(cell, (0, 0, 0), (0, 0, cell_size, cell_size), 1)

        screen.blit(cell, [x * cell_size for x in canvas_coords])
    

def main():
    global show_grid, brush_color
    placing_cell = 0
    canvas_reset()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if  event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    placing_cell = 1
                elif event.button == 3:
                    placing_cell = -1
            if event.type == pygame.MOUSEBUTTONUP:
                placing_cell = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    canvas_reset()
                elif event.key == pygame.K_0:
                    show_grid = False if show_grid else True
                    canvas_reload()
                elif event.key in color_map:
                    brush_color = color_map[event.key]

        if placing_cell == 1:
            place_cell()
        elif placing_cell == -1:
            remove_cell()

        pygame.display.update()

if  "__main__" == __name__:
    main()
    pygame.quit()

    
