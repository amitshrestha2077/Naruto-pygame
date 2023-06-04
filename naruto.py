import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))

walkRight = [pygame.image.load('pics/NR2.png'), pygame.image.load('pics/NR3.png')]
walkLeft = [pygame.image.load('pics/NL2.png'), pygame.image.load('pics/NL3.png')]

bg = pygame.image.load('pics/bg.png')
stan = pygame.image.load('pics/Nstanding.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 40
height = 60
speed = 5
isJump = False

jumpHeight = 10

left = False
right = False
walkCount = 0

run = True


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))

    if walkCount + 1 >= 6:
        walkCount = 0

    if left and not isJump:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right and not isJump:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    elif isJump:
        win.blit(walkRight[1], (x, y))
    else:
        win.blit(stan, (x, y))

    pygame.display.update()


while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
###########   left  ###################
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False

    ###########   Right  ##################
    elif keys[pygame.K_RIGHT] and x < 678 - width - speed:
        x += speed
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    ###########   jump  ##################
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpHeight >= -10:
            neg = 1
            if jumpHeight < 0:
                neg = -1
            y -= (jumpHeight ** 2) * 0.5 * neg
            jumpHeight -= 1
        else:
            isJump = False
            jumpHeight = 10

    redrawGameWindow()

pygame.quit()
