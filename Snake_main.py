import pygame


"""
----------------------------------------------------------------------------------
                                    CONSTANTS
----------------------------------------------------------------------------------                                    
"""
# Window sizes
WIDTH = 750
HEIGHT = 750

# Game speed
FPS = 12.5
TICKS = 15

# initializing pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake_position = [100, 50]
SNAKE = [[100, 50], [90, 50], [80, 50], [70, 50]]

SNAKE_SIZE = 25
DIRECTION = "right"
SPEED = 25

"""
----------------------------------------------------------------------------------
                                    FUNCTIONS
----------------------------------------------------------------------------------                                    
"""


# Drawing functions
def draw_bg():
    image = pygame.image.load("Resources/Block.png")
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

    if DIRECTION == "right":
        snake_position[0] += SPEED

    if DIRECTION == "left":
        snake_position[0] -= SPEED

    if DIRECTION == "up":
        snake_position[1] -= SPEED

    if DIRECTION == "down":
        snake_position[1] += SPEED

    for pos in SNAKE:
        pygame.draw.rect(WINDOW, "green",
                         pygame.Rect(pos[0], pos[1], 25, 25))


# Draw everything
def draw():
    draw_bg()
    draw_snake()

    # Makes sure to update the display after drawing
    pygame.display.update()


# Main function
def main():
    # global variables
    global DIRECTION

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

        # Check for pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and DIRECTION != "up":
            DIRECTION = "down"
        if keys[pygame.K_UP] and DIRECTION != "down":
            DIRECTION = "up"
        if keys[pygame.K_LEFT] and DIRECTION != "right":
            DIRECTION = "left"
        if keys[pygame.K_RIGHT] and DIRECTION != "left":
            DIRECTION = "right"

        # Control game speed
        clock = pygame.time.Clock()
        clock.tick(FPS)

        # Draw everything
        draw()


if __name__ == "__main__":
    main()
