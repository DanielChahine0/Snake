import time

import pygame
import random

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
snake_position = [SNAKE_SIZE*10, SNAKE_SIZE*5]
SNAKE = [[SNAKE_SIZE*10, SNAKE_SIZE*5],
         [SNAKE_SIZE*9, SNAKE_SIZE*5],
         [SNAKE_SIZE*8, SNAKE_SIZE*5],
         [SNAKE_SIZE*7, SNAKE_SIZE*5],
         [SNAKE_SIZE*6, SNAKE_SIZE*5],
         [SNAKE_SIZE*5, SNAKE_SIZE*5]]
DIRECTION = "right"
CHANGE = "right"
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


"""
----------------------------------------------------------------------------------
                                    FUNCTIONS
----------------------------------------------------------------------------------                                    
"""


# Functions that draws and generate the fruit
def generate_fruit():
    global FRUIT
    FRUIT = [random.randint(0, WIDTH//SNAKE_SIZE-1)*SNAKE_SIZE, random.randint(0, HEIGHT//SNAKE_SIZE-1)*SNAKE_SIZE]


def draw_fruit():
    global FRUIT, SPAWNED

    if not SPAWNED:
        generate_fruit()
        SPAWNED = True

    fruit_rect = pygame.Rect(FRUIT[0], FRUIT[1], SNAKE_SIZE, SNAKE_SIZE)
    # print(FRUIT)
    pygame.draw.rect(WINDOW, "red", fruit_rect)


# Game over function
def game_over():
    global SPEED

    GO_Surface = GAME_OVER_FONT.render("YOUR SCORE IS: "+str(SCORE), True, "black")
    height = GO_Surface.get_height()
    width = GO_Surface.get_width()
    X = (WIDTH-width)/2
    Y = (HEIGHT-height)/2
    margin = 50
    RED_REC = pygame.Rect(X-margin, Y-margin, width+2*margin, height+2*margin)
    pygame.draw.rect(WINDOW, "red", RED_REC)
    WINDOW.blit(GO_Surface, (X, Y))
    pygame.display.update()

    SPEED = 0


# Function to display the current score of the game
def display_score():
    score_surface = FONT.render("Score: " + str(SCORE), True, "white")
    WINDOW.blit(score_surface, (10, 10))


# Function to check for collision with the wall and self collision
def check_collision():
    # Out of border mechanism
    if not (0 <= snake_position[0] <= WIDTH-SNAKE_SIZE):
        game_over()
    if not (0 <= snake_position[1] <= HEIGHT-SNAKE_SIZE):
        game_over()

    # Self collision
    for block in SNAKE[1:]:
        if block[0] == snake_position[0] and block[1] == snake_position[1]:
            game_over()


# Drawing functions
def draw_bg():
    image = pygame.transform.scale(pygame.image.load("Resources/Block.png"), (SNAKE_SIZE, SNAKE_SIZE))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH//width+1):
        for j in range(HEIGHT//height+1):
            pos = (i*width, j*height)
            tiles.append(pos)

    for tile in tiles:
        WINDOW.blit(image, tile)


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
        pygame.draw.rect(WINDOW, "green", pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))


# Draw everything
def draw():
    draw_bg()
    draw_snake()
    draw_fruit()
    display_score()

    # Makes sure to update the display after drawing
    pygame.display.update()


def restart():
    global SPEED, SNAKE_SIZE, snake_position, SNAKE, DIRECTION, CHANGE, SCORE

    # Snake
    SNAKE_SIZE = 25
    snake_position = [SNAKE_SIZE * 10, SNAKE_SIZE * 5]
    SNAKE = [[SNAKE_SIZE * 10, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 9, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 8, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 7, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 6, SNAKE_SIZE * 5],
             [SNAKE_SIZE * 5, SNAKE_SIZE * 5]]
    DIRECTION = "right"
    CHANGE = "right"
    SPEED = SNAKE_SIZE
    SCORE = 0
    generate_fruit()


# Main function
def main():
    # global variables
    global CHANGE, Eat

    running = True

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
                if event.key == pygame.K_r:
                    restart()

        # Draw everything
        draw()
        check_collision()
        # Control game speed
        clock = pygame.time.Clock()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
