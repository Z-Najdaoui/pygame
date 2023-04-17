import pygame
import sys

pygame.init()

# Set up the window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Load the image
image = pygame.image.load('./images/arrow.png')
image_rect = image.get_rect(center=screen.get_rect().center)

# Set the initial angle of the image
angle = 0

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the user closes the window
            pygame.quit()
            sys.exit()

    # Rotate the image
    angle += 1
    rotated_image = pygame.transform.rotate(image, angle)

    # Draw the rotated image
    screen.fill((255, 255, 255))
    screen.blit(rotated_image, rotated_image.get_rect(center=image_rect.center))
    pygame.display.update()