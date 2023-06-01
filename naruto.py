import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))

walkRight = [pygame.image.load('pics\\NR2.png'), pygame.image.load('pics\\NR3.png')]
walkleft = [pygame.image.load('pics\\NR2.png'), pygame.image.load('pics\\NR3.png')]

bg = pygame.image.load('pics\\bg.png')
stan = pygame.image.load('pics\\Nstanding.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 40
height = 60
speed = 5
isjump = False

jumpheight = 10

left = False
right = False
walkcount = 0

run = True


def redrawgamewindow():
    global left
    global right
    global walkcount
    win.blit(bg, (0, 0))

    if walkcount + 1 > 6:
        walkcount = 0

    if left and isjump == False:
        win.blit(walkleft[walkcount // 2], (x, y))

    elif right and isjump == False:
        win.blit(walkRight[walkcount // 2], (x, y))

    elif right and isjump:
        win.blit(walkRight[2], (x, y))

    elif left and isjump:
        win.blit(walkleft[1], (x, y))

    elif not (isjump):
        win.blit(stan, (x, y))


while run:

    ###  jump
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
    # broundry
    if keys[pygame.K_RIGHT] and x < 692 - width - speed:
        x += speed
        right = False
        left = True

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

    pygame.display.update()

    redrawgamewindow()

pygame.quit()
