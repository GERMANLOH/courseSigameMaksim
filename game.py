import sys
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800 

PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 30
PLATFORM_X = (SCREEN_WIDTH - PLATFORM_WIDTH) //2
PLATFORM_Y =int(SCREEN_HEIGHT * 0.8)
screen = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
clock= pg.time.Clock()

BALL_WIDTH = 50
BALL_HEIGHT = 50
BALL_X = (250) 
BALL_Y =int(0)
BALL2_WIDTH = 50
BALL2_HEIGHT = 50
BALL2_X = (0) 
BALL2_Y =int(0)


PLATFORM_SPEED = 3
BALL_SPEED = 3
BALL2_SPEED = 3
FPS = 120
while True: 
    for i in pg.event.get():
        if i.type==pg.QUIT:
            sys.exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        PLATFORM_X -=PLATFORM_SPEED
        PLATFORM_X = max(0, PLATFORM_X)
    if keys[pg.K_RIGHT]:
        PLATFORM_X += PLATFORM_SPEED
        PLATFORM_X =min(SCREEN_WIDTH - PLATFORM_WIDTH, PLATFORM_X)
        
    BALL_X = max(0, BALL_X)
    BALL2_X = max(0, BALL2_X)
    BALL_Y += BALL_SPEED
    BALL_Y =min(SCREEN_WIDTH - BALL_WIDTH, BALL_Y)
    BALL2_Y += BALL2_SPEED
    BALL2_Y =min(SCREEN_WIDTH - BALL2_WIDTH, BALL2_Y)
    PLATFORM_X =min(SCREEN_WIDTH - BALL_WIDTH, BALL_X)
    BALL2_X =min(SCREEN_WIDTH - BALL2_WIDTH, BALL2_X)

    screen.fill(GREEN)
    
    platform = pg.Rect(PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    pg.draw.rect(screen ,YELLOW, platform)
    ball = pg.Rect(BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)
    pg.draw.rect(screen ,RED, ball)
    ball2 = pg.Rect(BALL2_X, BALL2_Y, BALL2_WIDTH, BALL2_HEIGHT)
    pg.draw.rect(screen ,RED, ball2)
    

    
    
    platform.colliderect(ball)
    
    ball.colliderect(ball)

    pg.display.flip()  
    clock.tick(FPS)