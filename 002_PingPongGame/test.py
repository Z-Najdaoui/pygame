import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the canvas
canvas_width = 800
canvas_height = 600

# Create a new Surface object with the given width and height
canvas = pygame.Surface((canvas_width, canvas_height))

# Set the background color of the canvas
canvas.fill((255, 255, 255))

# Create a rectangle object for the moving object
object_width = 50
object_height = 50
object_rect = pygame.Rect(0, canvas_height/2 - object_height/2, object_width, object_height)

# Set the speed of the object
object_speed = 5

# Display the canvas on the screen
screen = pygame.display.set_mode((canvas_width, canvas_height))
screen.blit(canvas, (0, 0))
pygame.display.flip()

# Keep the program running until the user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the object to the right or left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_rect.move_ip(-object_speed, 0)
    if keys[pygame.K_RIGHT]:
        object_rect.move_ip(object_speed, 0)

    # Check if the object has hit the edge of the canvas
    if object_rect.left < 0:
        object_rect.left = 0
    if object_rect.right > canvas_width:
        object_rect.right = canvas_width

    # Fill the canvas with the background color
    canvas.fill((255, 255, 255))

    # Draw the object at its new position
    pygame.draw.rect(canvas, (0, 0, 255), object_rect)

    # Update the screen
    screen.blit(canvas, (0, 0))
    pygame.display.flip()
