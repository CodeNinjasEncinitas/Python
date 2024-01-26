# INSTRUCTIONS:
# walk the student through the following code and make sure they get it all to run on their own machine
# have them create a simple art piece using circles, squares, and lines to complete this assignment

import pygame
import sys

pygame.init()

# Set up the window
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Square on White Window")

# black square properties
square_size = 100
square_color = (0, 0, 0)  # RGB values for black
square_rect = pygame.Rect((width - square_size) // 2, (height - square_size) // 2, square_size, square_size) # // is math.floor division operator

# Set up the red circle
circle_radius = 100
circle_color = (255, 0, 0)  # RGB values for red
circle_center = (width // 2, (height - square_size) // 2 - circle_radius) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with white color
    window.fill((255, 255, 255))  # RGB values for white

    # Draw the black square
    pygame.draw.rect(window, square_color, square_rect)

    # Draw the red circle
    pygame.draw.circle(window, circle_color, circle_center, circle_radius)

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()