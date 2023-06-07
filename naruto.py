import pygame

pygame.init()

win = pygame.display.set_mode((700, 500))

walkRight = [pygame.image.load('pics/NR2.png'), pygame.image.load('pics/NR3.png')]
walkLeft = [pygame.image.load('pics/NL2.png'), pygame.image.load('pics/NL3.png')]

bg = pygame.image.load('pics/bg.png')
stan = pygame.image.load('pics/Nstanding.png')

clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 10
        self.isJump = False
        self.jumpHeight = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 6:
            self.walkCount = 0

        if self.left and not self.isJump:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.right and not self.isJump:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.isJump:
            win.blit(walkRight[1], (self.x, self.y))

        else:
            win.blit(stan, (self.x, self.y))


run = True


def redrawGameWindow():
    win.blit(bg, (0, 0))
    naruto.draw(win)
    pygame.display.update()


naruto = Player(50, 400, 100, 100)

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Left
    if keys[pygame.K_LEFT] and naruto.x > naruto.speed:
        naruto.x -= naruto.speed
        naruto.left = True
        naruto.right = False

    # Right
    elif keys[pygame.K_RIGHT] and naruto.x < 690 - naruto.width - naruto.speed:
        naruto.x += naruto.speed
        naruto.right = True
        naruto.left = False
    else:
        naruto.right = False
        naruto.left = False
        naruto.walkCount = 0

    # Jump
    if not naruto.isJump:
        if keys[pygame.K_SPACE]:
            naruto.isJump = True
            naruto.right = False
            naruto.left = False
            naruto.walkCount = 0
    else:
        if naruto.jumpHeight >= -10:
            neg = 1
            if naruto.jumpHeight < 0:
                neg = -1
            naruto.y -= (naruto.jumpHeight ** 2) * 0.5 * neg
            naruto.jumpHeight -= 1
        else:
            naruto.isJump = False
            naruto.jumpHeight = 10

    redrawGameWindow()

pygame.quit()
