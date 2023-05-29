import pygame
pygame.init()
# This is the first commit
# This is my second commit
# this is my third commit

win = pygame.display.set_mode((500, 500))

x = 50
y = 400
width = 40
height = 60
speed = 5

run = True

while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= speed
        
    if keys[pygame.K_RIGHT]:
        x += speed
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 250), (x, y, width, height))
    pygame.display.update()

pygame.quit()
