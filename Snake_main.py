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
FPS = 20
TICKS = 15

# initializing pygame
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake
snake_position = [100, 50]
SNAKE = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

SNAKE_SIZE = 10
DIRECTION = "right"
SPEED = 10

"""
----------------------------------------------------------------------------------
                                    FUNCTIONS
----------------------------------------------------------------------------------                                    
"""


# Game over function
def game_over():
    print("LOST")


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

    SNAKE.insert(0, list(snake_position))
    SNAKE.pop()
    for pos in SNAKE:
        pygame.draw.rect(WINDOW, "green", pygame.Rect(pos[0], pos[1], 10, 10))




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
                if event.key == pygame.K_DOWN and DIRECTION != "up":
                    DIRECTION = "down"
                if event.key == pygame.K_UP and DIRECTION != "down":
                    DIRECTION = "up"
                if event.key == pygame.K_LEFT and DIRECTION != "right":
                    DIRECTION = "left"
                if event.key == pygame.K_RIGHT and DIRECTION != "left":
                    DIRECTION = "right"
        # Draw everything
        draw()
        check_collision()
        # Control game speed
        clock = pygame.time.Clock()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
