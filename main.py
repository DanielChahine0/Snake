import pygame
import random
import asyncio


"""
----------------------------------------------------------------------------------
                                    CONSTANTS
----------------------------------------------------------------------------------                                    
"""
# Window sizes
WIDTH = 750
HEIGHT = 750


# initializing pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
SNAKE_SIZE = 25
snake_position = [SNAKE_SIZE*5, SNAKE_SIZE*5]
SNAKE = [[SNAKE_SIZE*5, SNAKE_SIZE*5],
         [SNAKE_SIZE*4, SNAKE_SIZE*5],
         [SNAKE_SIZE*3, SNAKE_SIZE*5],
         [SNAKE_SIZE*2, SNAKE_SIZE*5],
         [SNAKE_SIZE*1, SNAKE_SIZE*5],
         [SNAKE_SIZE*0, SNAKE_SIZE*5]]
DIRECTION = "right"
CHANGE = "right"
DEAD = False
SPEED = SNAKE_SIZE

# Game speed
FPS = 10

# Fruit
FRUIT = [0, 0]
SPAWNED = False
Eat = False

# Score
SCORE = 0
FONT = pygame.font.SysFont("Times New Roman", 30)
GAME_OVER_FONT = pygame.font.SysFont("Time New Roman", 60)

# Settings
SETTING = 0
THEME_Fruit = "white"
THEME_Snake = "yellow"
THEME_Border = "green"
THEME_Ground = "black"
THEME_NAME = "Basic"


"""
----------------------------------------------------------------------------------
                                    FUNCTIONS
----------------------------------------------------------------------------------                                    
"""


# Functions that draws and generate the fruit
def generate_fruit():
    global FRUIT
    FRUIT = [random.randint(1, WIDTH//SNAKE_SIZE-2)*SNAKE_SIZE, random.randint(1, HEIGHT//SNAKE_SIZE-2)*SNAKE_SIZE]


def draw_fruit():
    global FRUIT, SPAWNED

    if not SPAWNED:
        generate_fruit()
        SPAWNED = True

    fruit_rect = pygame.Rect(FRUIT[0], FRUIT[1], SNAKE_SIZE, SNAKE_SIZE)
    # print(FRUIT)
    pygame.draw.rect(WINDOW, THEME_Fruit, fruit_rect)


# Game over function
def game_over():
    global SPEED, DEAD

    DEAD = True
    GO_Surface = GAME_OVER_FONT.render("YOUR SCORE IS: "+str(SCORE), True, "black")
    height = GO_Surface.get_height()
    width = GO_Surface.get_width()
    X = (WIDTH-width)/2
    Y = (HEIGHT-height)/2
    margin = 25
    RED_REC = pygame.Rect(X-margin, Y-margin, width+2*margin, height+2*margin)
    pygame.draw.rect(WINDOW, THEME_Fruit, RED_REC, 0, 10)
    WINDOW.blit(GO_Surface, (X, Y))
    pygame.display.update()

    SPEED = 0


# Function to display the current score of the game
def display_score():
    score_surface = FONT.render("Score: " + str(SCORE), True, THEME_Fruit)
    margin = 10
    WINDOW.blit(score_surface, (SNAKE_SIZE+margin, SNAKE_SIZE+margin))


def display_theme():
    name = FONT.render("Theme: " + str(THEME_NAME), True, THEME_Fruit)
    WINDOW.blit(name, (WIDTH-SNAKE_SIZE-200, HEIGHT-SNAKE_SIZE-40))


# Function to check for collision with the wall and self collision
def check_collision():
    # Out of border mechanism
    if not (SNAKE_SIZE <= snake_position[0] <= WIDTH-SNAKE_SIZE*2):
        game_over()
    if not (SNAKE_SIZE <= snake_position[1] <= HEIGHT-SNAKE_SIZE*2):
        game_over()

    # Self collision
    for block in SNAKE[1:]:
        if block[0] == snake_position[0] and block[1] == snake_position[1]:
            game_over()


# Drawing functions
def draw_bg():

    # image = pygame.transform.scale(pygame.image.load("Resources/Block.png"), (SNAKE_SIZE, SNAKE_SIZE))
    # _, _, width, height = image.get_rect()
    # tiles = []
    #
    # for i in range(WIDTH//width+1):
    #     for j in range(HEIGHT//height+1):
    #         pos = (i*width, j*height)
    #         tiles.append(pos)
    # for tile in tiles:
    #     WINDOW.blit(image, tile)

    bg = pygame.Rect(0, 0, WIDTH, HEIGHT)
    pygame.draw.rect(WINDOW, THEME_Ground, bg)


# function that draws the snake
def draw_snake():
    global SPAWNED, Eat, DIRECTION, SCORE

    if CHANGE == "up" and DIRECTION != "down":
        DIRECTION = "up"
    if CHANGE == "down" and DIRECTION != "up":
        DIRECTION = "down"
    if CHANGE == "left" and DIRECTION != "right":
        DIRECTION = "left"
    if CHANGE == "right" and DIRECTION != "left":
        DIRECTION = "right"

    if DIRECTION == "right":
        snake_position[0] += SPEED
    if DIRECTION == "left":
        snake_position[0] -= SPEED
    if DIRECTION == "up":
        snake_position[1] -= SPEED
    if DIRECTION == "down":
        snake_position[1] += SPEED

    SNAKE.insert(0, list(snake_position))
    if (snake_position[0] == FRUIT[0] and snake_position[1] == FRUIT[1]) or Eat:
        SPAWNED = False
        Eat = False
        SCORE += 10
    else:
        SNAKE.pop()
    for pos in SNAKE:
        pygame.draw.rect(WINDOW, THEME_Snake, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))


def draw_border():
    left = pygame.Rect(0, 0, SNAKE_SIZE, HEIGHT)
    right = pygame.Rect(WIDTH-SNAKE_SIZE, 0, SNAKE_SIZE, HEIGHT)
    top = pygame.Rect(0, 0, WIDTH, SNAKE_SIZE)
    bottom = pygame.Rect(0, HEIGHT-SNAKE_SIZE, WIDTH, SNAKE_SIZE)
    pygame.draw.rect(WINDOW, THEME_Border, left)
    pygame.draw.rect(WINDOW, THEME_Border, right)
    pygame.draw.rect(WINDOW, THEME_Border, top)
    pygame.draw.rect(WINDOW, THEME_Border, bottom)


# Draw everything
def draw():
    draw_bg()
    draw_snake()
    draw_fruit()
    draw_border()
    display_score()
    display_theme()

    # Makes sure to update the display after drawing
    pygame.display.update()


def restart():
    global SPEED, SNAKE_SIZE, snake_position, SNAKE, DIRECTION, CHANGE, SCORE, DEAD

    DEAD = False
    snake_position = [SNAKE_SIZE * 5, SNAKE_SIZE * 5]
    SNAKE = [[SNAKE_SIZE * 5, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 4, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 3, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 2, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 1, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 0, SNAKE_SIZE * 5]]
    DIRECTION = "right"
    CHANGE = "right"
    SPEED = SNAKE_SIZE
    SCORE = 0
    generate_fruit()


def theme(number):
    global THEME_Border, THEME_Fruit, THEME_Snake, THEME_Ground, THEME_NAME

    # Normal
    if number == 0:
        THEME_Snake = "white"
        THEME_Fruit = "white"
        THEME_Ground = "black"
        THEME_Border = "white"
        THEME_NAME = "Basic"

    # Desert
    if number == 1:
        THEME_Snake = (252, 186, 3)
        THEME_Fruit = (252, 132, 3)
        THEME_Ground = (179, 99, 14)
        THEME_Border = (105, 63, 19)
        THEME_NAME = "Desert"

    # Snow
    if number == 2:
        THEME_Snake = (72, 193, 219)
        THEME_Fruit = (200, 241, 250)
        THEME_Ground = (125, 231, 255)
        THEME_Border = (22, 79, 92)
        THEME_NAME = "Snow"

    # Space
    if number == 3:
        THEME_Snake = (0, 0, 0)
        THEME_Fruit = (234, 242, 7)
        THEME_Ground = (13, 29, 110)
        THEME_Border = (7, 13, 43)
        THEME_NAME = "Space"

    # Jungle
    if number == 4:
        THEME_Snake = (88, 173, 9)
        THEME_Fruit = (255, 0, 0)
        THEME_Ground = (19, 102, 4)
        THEME_Border = (87, 54, 12)
        THEME_NAME = "Jungle"


# Main function
async def main():
    # global variables
    global CHANGE, Eat

    running = True
    theme(0)

    # main loop
    while running:

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_DOWN:
                    CHANGE = "down"
                if event.key == pygame.K_UP:
                    CHANGE = "up"
                if event.key == pygame.K_LEFT:
                    CHANGE = "left"
                if event.key == pygame.K_RIGHT:
                    CHANGE = "right"
                if event.key == pygame.K_t:
                    Eat = True
                if event.key == pygame.K_SPACE and DEAD:
                    restart()
                if event.key == pygame.K_KP1:
                    theme(1)
                if event.key == pygame.K_KP0:
                    theme(0)
                if event.key == pygame.K_KP2:
                    theme(2)
                if event.key == pygame.K_KP3:
                    theme(3)
                if event.key == pygame.K_KP4:
                    theme(4)


        # Draw everything
        draw()
        check_collision()
        # Control game speed
        clock = pygame.time.Clock()
        clock.tick(FPS)
        await asyncio.sleep(0)


asyncio.run(main())
