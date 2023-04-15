import pygame
import random

# windows size
WINDOW_SIZE = (900, 650)
# initialize all imported pygame modules
pygame.init()
# set window display size
window = pygame.display.set_mode(WINDOW_SIZE)
window.fill((20, 20, 20))
# create canvas main for make play on it
main_features = {'color': (50, 50, 50), 'position': (50, 90)}
main_SIZE = (WINDOW_SIZE[0]-100, WINDOW_SIZE[1]-100)
main = pygame.Surface(main_SIZE)
main.fill(main_features['color'])

# return random color from gray to white
def random_color() -> tuple:
    return (random.randint(70, 255), random.randint(70, 255), random.randint(70, 255))

# players bar
# bar object or dict have default value of bars
bar = {"w": 50, "h": 5, 'wallSp': 5, 'speed': 5, 'color': (210, 210, 210)}
bar_max_R = main_SIZE[0]-bar['w']-5
bar_1 = pygame.Rect(main_SIZE[0]//2-bar['w']//2, bar['wallSp'], bar['w'], bar['h'])
bar_2 = pygame.Rect(main_SIZE[0]//2-bar['w']//2, main_SIZE[1]-bar['h']-bar['wallSp'], bar['w'], bar['h'])
bar1_M = bar2_M = 0
run: bool = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Move the object to the right or left
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bar_1.move_ip(-bar['speed'], 0)
    if keys[pygame.K_RIGHT]:
        bar_1.move_ip(bar['speed'], 0)
    if keys[pygame.K_a]:
        bar_2.move_ip(-bar['speed'], 0)
    if keys[pygame.K_d]:
        bar_2.move_ip(bar['speed'], 0)

    # Check if the object has hit the edge of the canvas
    if bar_1.left < 0:
        bar_1.left = 0
    if bar_1.right > main_SIZE[0]:
        bar_1.right = main_SIZE[0]
    if bar_2.left < 0:
        bar_2.left = 0
    if bar_2.right > main_SIZE[0]:
        bar_2.right = main_SIZE[0]

    # refill main for remove last position of rect draw
    main.fill(main_features['color'])

    # Draw the object at its new position
    pygame.draw.rect(main, random_color(), bar_1)
    pygame.draw.rect(main, random_color(), bar_2)

    # Update the window
    window.blit(main, main_features['position'])
    pygame.display.flip()

