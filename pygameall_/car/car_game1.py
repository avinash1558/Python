import pygame
import random
import  time
# it is important for using pygame
pygame.init()
# it is use for time hendling
clock=pygame.time.Clock()
#display_surface 
#                         (( width and height))
gd=pygame.display.set_mode((800,600))
# color 
#   (red,green,blue)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
light_green=(0,200,0)
gray=(119,118,110)
blue=(0,0,255)
# image
car_img=pygame.image.load("car.jpg")
background=pygame.image.load("back.jpg")
grass=pygame.image.load("grass.jpg")
# image size
car_img=pygame.transform.scale(car_img,(100,100))

# for message
def Message(size,mess,x_pos,y_pos):
    # font size         (None,size)
    font=pygame.font.SysFont(None,size)
    # render     ('word',True,color)
    render=font.render(mess,True,white)
    # display the word
    gd.blit(render , (x_pos,y_pos))

Message(100,"START",150,100)
# sleep time
clock.tick(1)

# car position
def car(x,y):
    # display the word
    # car            (posi,posi)
    gd.blit(car_img, (x, y))
    # grass       left
    gd.blit(grass, (0,0))
    #             right
    gd.blit(grass, (700,0))
    # car are teace grass
    if 0<x<90 or 710<x<800:
        # message function call 
        Message(100, "GAME-OVER", 300, 400)
        # change are use so update the display
        pygame.display.update()
        # sleep time
        clock.tick(0.17)
        # intro function call
        game_intro()
# enamy car
def enmy_car(x_r,y_r):
    # car display
    gd.blit(car_img,(x_r,y_r))

# button for start and end
def button(x_button,y_button,mess_b):
    # 1st button
    # draw the rectengular box  
    #               (dis,color,[x ,y ,width,heigth])
    pygame.draw.rect(gd,green,[x_button,y_button,100,30])
    # message print on rect box
    Message(50,mess_b,x_button,y_button)
    # position of mouse
    #    [x,y]
    mouse=pygame.mouse.get_pos()
    # click of mouse button
    #   (1,0,0) for right c.  (0,0,1)for left c.
    click=pygame.mouse.get_pressed()      #      _______________
    #        |-this position-|            #      _______________  
    # [x_button,      y_button     ,100                           ,30])
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        # 1nd button color change
        pygame.draw.rect(gd, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        # right click then play
        if click==(1,0,0) and mess_b=="PLAY":
            # game call
            Game_loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            # end the program
            pygame.quit()
            quit()
    # function for crash for car
def car_crash(x , x_r , y , y_r):
    #     | car |           |  car  |             _______           _______
    # if x_r < x <x_r+50 and y_r < y < y_r+74 or x_r<x+50<x_r+90 and y_r<y<y_r+90:
    if x_r< x <x_r+90 and y_r<y<y_r+90 or x_r<x+90<x_r+90 and y_r<y+90<y_r+90:
        Message(50,"CRASHED!",200,200)
        # pygame.display.update()
        time.sleep(1)
        game_intro()
        # where press 
        for i in pygame.event.get():
            # which place  | X |
            if i.type == pygame.QUIT:  
                pygame.quit()
# score function
def score(count):
    font = pygame.font.SysFont(None, 30)
    # add text
    screen_text = font.render('score :' + str(count), True, white)
    gd.blit(screen_text, (0, 0))

def game_intro():
    intro=False
    while (1):
        # display back image
        gd.blit(background, (0, 0))
        # button call
        button(370,200,"PLAY")
        button(370,270,"QUIT")
        #press key in keybord
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def Game_loop():
   #  randrange it is use range
   s=random.randrange(100, 600)
   x=s
   y=490
   x_r=random.randrange(100,600)
   y_r=0
   count=0
   x_change=0
   game_over=False
   while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=+10
            elif event.key==pygame.K_RIGHT:
                x_change=-10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
    gd.fill(gray)


    car(x,y)
    score(count)
    enmy_car(x_r,y_r)
    y_r+=10
    if y_r==600:
        y_r=0
        x_r=random.randrange(100,600)
        count+=1
    car_crash(x,x_r,y,y_r)
    x=x-x_change
    clock.tick(20)
    pygame.display.update()

game_intro()
pygame.display.update()
pygame.quit()
quit()