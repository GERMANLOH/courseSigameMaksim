import sys
import pygame as pg
import random
import pygame.mixer as mixer

mixer.init()
pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
ORANGE = (220,120,0)
def_font = pg.font.Font(pg.font.get_default_font(), 30)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800 
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 30
BALL_WIDTH = 50
BALL_HEIGHT = 50
FPS = 30
sound_over = pg.mixer.Sound('ay-menya-snaypnuli-v-polte.mp3')
sound_collision = pg.mixer.Sound('est-probitie.mp3')
sound_background = pg.mixer.Sound('otkryitie-filma-korotkaya-muzyika-korotkaya-muzyika-38490.mp3')
sound_background.play(100)
def game(screen,clock,assets):
    

    counter = 0
    start_time = pg.time.get_ticks()
    PLATFORM_X = (SCREEN_WIDTH - PLATFORM_WIDTH) //2
    PLATFORM_Y =int(SCREEN_HEIGHT * 0.8)
    screen = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    TOP_BORDER = pg.Rect(0,0,SCREEN_WIDTH,1)
    BOTTOM_BORDER = pg.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
    LEFT_BORDER = pg.Rect(0,0,1,SCREEN_HEIGHT)
    RIGHT_BORDER = pg.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)

    
    BALL_X = (250) 
    BALL_Y =int(0)

    PLATFORM_SPEED = 30
    BALL_SPEED = 30
    BALL_DIRECTION=pg.math.Vector2(0,1).normalize()

    
    while True: 
        for i in pg.event.get():
            if i.type==pg.QUIT:
                sys.exit()

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            PLATFORM_X -= PLATFORM_SPEED
            PLATFORM_X = max(0, PLATFORM_X)
        if keys[pg.K_RIGHT]:
            PLATFORM_X += PLATFORM_SPEED
            PLATFORM_X =min(SCREEN_WIDTH - PLATFORM_WIDTH, PLATFORM_X)
        
        speed_vector = BALL_DIRECTION * BALL_SPEED


        BALL_Y += speed_vector.y 
        BALL_X += speed_vector.x
        

    
        screen.blit(assets['background'], (0,0))
        
    
        

        ball = assets['ball'].get_rect()
        ball.x=BALL_X
        ball.y=BALL_Y

        screen.blit(assets['ball'],ball)
        
        platform = assets['panel'].get_rect()
        platform.x=PLATFORM_X
        platform.y=PLATFORM_Y
        screen.blit(assets['panel'],platform)

        ball_center = (ball.x + ball.width/2, ball.y + ball.height/2)
        platform_center = (platform.x + platform.width/2, platform.y + platform.height/2)
        text_surface = def_font.render(str(counter) , False,  GREEN)
        time_surface = def_font.render(str(int((pg.time.get_ticks()-start_time)/FPS)) , False,  GREEN)
        
        if ball.colliderect(platform):
            
            sound_collision.play()
            t = random.Random().random()/2
            collision_vector = (ball_center[0]- platform_center[0], ball_center[1]- platform_center[1])
            BALL_DIRECTION =pg.math.Vector2(collision_vector).normalize()
            counter = counter + 1
        if ball.colliderect(TOP_BORDER):
            BALL_DIRECTION = BALL_DIRECTION. reflect(pg.math.Vector2(0,1))
        if ball.colliderect(BOTTOM_BORDER):
            
            break
            BALL_DIRECTION =BALL_DIRECTION .reflect(pg.math.Vector2(0,-1))
        if ball.colliderect(LEFT_BORDER):
            BALL_DIRECTION =BALL_DIRECTION .reflect(pg.math.Vector2(1,0))
        if ball.colliderect(RIGHT_BORDER):
            BALL_DIRECTION =BALL_DIRECTION .reflect(pg.math.Vector2(-1,0))

        screen.blit(text_surface,(20,20))
        screen.blit(time_surface,(50,20))
        pg.display.flip()  
        clock.tick(FPS)
    return counter


    

if __name__=='__main__':
    screen_out = pg.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    assets = {
        'ball' : pg.transform.scale(pg.image.load('ball.png').convert_alpha(),(BALL_WIDTH,BALL_HEIGHT)),
        'background' :pg.transform.scale(pg.image.load('background.png').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT)),
        'panel' : pg.image.load('pannel.png').convert(),
    }
    clock_out= pg.time.Clock()
    while True:
        sound_background.play(100)
        count_final = game(screen_out,clock_out,assets)
        finish_text = def_font.render('GAME OVER ! press R to restart ' , False ,(GREEN))
        sound_background.stop()
        sound_over.play()
        screen_out.blit(finish_text, (SCREEN_WIDTH/6-20, SCREEN_HEIGHT/2))
        pg.display.flip()
        while True:
            for event in pg.event.get():
               if event.type==pg.QUIT:
                    sys.exit()
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                break