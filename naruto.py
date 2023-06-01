import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))

walkRight = [pygame.image.load('pics\\NR2.png'), pygame.image.load('pics\\NR3.png')]
walkleft = [pygame.image.load('pics\\NR2.png'), pygame.image.load('pics\\NR3.png')]

bg = pygame.image.load('pics\\bg.png')
stan = pygame.image.load('pics\\Nstanding.png')

x = 50
y = 400
width = 40
height = 60
speed = 5
isjump = False

jumpheight = 10

run = True


def redrawgamewindow():
    win.blit(bg, (0, 0))


while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed

    if keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed

    if isjump == False:
        if keys[pygame.K_SPACE]:
            isjump = True

    else:
        if jumpheight >= -10:
            neg = 1

            if jumpheight < 0:
                neg = -1

            y -= (jumpheight ** 2) * 0.5 * neg
            jumpheight -= 1

        else:
            isjump = False
            jumpheight = 10

    pygame.draw.rect(win, (255, 255, 250), (x, y, width, height))
    pygame.display.update()

    redrawgamewindow()

pygame.quit()
