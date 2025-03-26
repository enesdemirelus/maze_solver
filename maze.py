import pygame
import random

pygame.init()

WIDTH, HEIGHT = 15, 15
CELL_SIZE = 40
SCREEN_WIDTH = WIDTH * CELL_SIZE
SCREEN_HEIGHT = HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze')

def create_maze(width, height):
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            if x % 2 != 0 or y % 2 != 0:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)
    return maze

def draw_maze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), rect)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rect)
                
def move_player(player_pos, direction, maze):
    x, y = player_pos
    moves = {pygame.K_UP: "UP", 
             pygame.K_DOWN: "DOWN", 
             pygame.K_LEFT: "LEFT",
             pygame.K_RIGHT: "RIGHT"}
        
    try:    
        if moves[direction] == "UP" and y >= 1: 
            y -= 1   
        elif moves[direction] == "DOWN" and y < HEIGHT - 1:
            y += 1       
        elif moves[direction] == "LEFT" and x >= 1:
            x -= 1      
        elif moves[direction] == "RIGHT" and x < WIDTH - 1:        
            x += 1     
    except:
        print("Wrong Key")
        
        
    return (x, y)

running = True
maze = create_maze(WIDTH, HEIGHT)
player_pos = (0,0)

while running:
    draw_maze(maze)
    
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            player_pos = move_player(player_pos, event.key, maze)


    pygame.display.flip()

pygame.quit()
