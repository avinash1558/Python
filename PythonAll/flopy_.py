import random
import sys
import pygame
from pygame import * 
# for window show
SHOWTIME = 30
SCREENWIDTH=289
SCREENHIEGTH=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHIEGTH))
GROUND=SCREENHIEGTH*0.8
GAME_ASSET={}
GAME_SOUND={}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
def welcomeScreen():
    playerX=int(SCREENWIDTH/6)
    playerY=int((SCREENHIEGTH-GAME_ASSET['player'].get_height())/2)
    # messageX = int((SCREENWIDTH - GAME_ASSET['message'].get_width())/2)
    # messageY = int(SCREENHIEGTH*0.13)
    # messageY = int(SCREENHIEGTH/7)
    baseX=0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type== KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_ASSET['background'],(0, 0))
                SCREEN.blit(GAME_ASSET['player'],(playerX,playerY))
                # SCREEN.blit(GAME_ASSET['message'],(messageX,messageY))
                SCREEN.blit(GAME_ASSET['base'],(baseX, GROUND))
                pygame.display.update()
                show.tick(SHOWTIME)

def mainScreen():
    pygame.display.set_caption('Flappy Bird by CodeWithHarry')
    playerX=int((SCREENWIDTH-GAME_ASSET['player'].get_width())/2)
    playerY=int((SCREENHIEGTH-GAME_ASSET['player'].get_height()-(SCREENHIEGTH-GROUND))/2)
    baseX=0
    newPipe1=getPipe()
    upperPipe=[
        {'x':SCREENWIDTH+200,'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe1[0]['y']}
    ]
    lowerPipe=[
        {'x':SCREENWIDTH+200,'y':newPipe1[1]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2),'y':newPipe1[1]['y']}
    ]
    score=0
    pipeleft=-4
    playerDown=7
    playerUp=-70
    playerFlapped = False 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                playerY +=playerUp
                playerFlapped=True
                GAME_SOUND['wing'].play()
        
        
        # playerMidPosition = playerX+ GAME_ASSET['player'].get_width()/2
        for pipe in upperPipe:
            pipeMidPosition = pipe['x'] + GAME_ASSET['pipe'][0].get_width()/2
            if pipeMidPosition<= playerX < pipeMidPosition +4:
                score+=1
                GAME_SOUND["point"].play()

        if not playerFlapped:
            show.tick(50)
            playerY+=playerDown
        if playerFlapped:
            playerFlapped = False
        
        for upper , lower in zip(upperPipe, lowerPipe):
            upper['x'] += pipeleft
            lower['x'] += pipeleft

        if 0<upperPipe[0]['x']<5:
            newPipe=getPipe()
            upperPipe.append(newPipe[0])
            lowerPipe.append(newPipe[1])

        if upperPipe[0]['x'] < -GAME_ASSET['pipe'][0].get_width():
            upperPipe.pop(0)
            lowerPipe.pop(0)

        SCREEN.blit(GAME_ASSET['background'], (0,0))
        for upper , lower in zip(upperPipe, lowerPipe):
            SCREEN.blit(GAME_ASSET['pipe'][0],( upper['x'],upper['y']))
            SCREEN.blit(GAME_ASSET['pipe'][1],( lower['x'],lower['y']))

        SCREEN.blit(GAME_ASSET['base'],( baseX,GROUND))
        SCREEN.blit(GAME_ASSET['player'], (playerX,playerY))
        pygame.display.update()
        show.tick(SHOWTIME)
        myDigits = [int(x) for x in list(str(score))]
        for digit in myDigits:
            width = GAME_ASSET['number'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_ASSET['number'][digit], (Xoffset, SCREENHIEGTH*0.12))
            Xoffset += GAME_ASSET['number'][digit].get_width()
        pygame.display.update()
        show.tick(60)
        crash=iscrash(playerX, playerY, upperPipe, lowerPipe)
        if crash:
            return

def iscrash(playerx, playery, upperPipe, lowerPipe):
    if playery> GROUND- 25  or playery<0:
        GAME_SOUND['hit'].play()
        return True
    
    for pipe in upperPipe:
        pipeHeight = GAME_ASSET['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x'])+20 < GAME_ASSET['pipe'][0].get_width()):
            GAME_SOUND['hit'].play()
            return True
    for pipe in lowerPipe:
        if (playery + GAME_ASSET['player'].get_height() > pipe['y']) and abs(playerx - pipe['x'])+20 < GAME_ASSET['pipe'][0].get_width():
            GAME_SOUND['hit'].play()
            return True
    return False

def getPipe():
    pipeHeight=GAME_ASSET['pipe'][0].get_height()
    freespace=SCREENHIEGTH/3
    y2=freespace+random.randrange(0,int(SCREENHIEGTH-GAME_ASSET['base'].get_height()-1.2*freespace))
    X=SCREENWIDTH+10
    y1=pipeHeight-y2+freespace
    pipe=[
        {'x':X,'y':-y1},
        {'x':X,'y':y2}
    ]
    return pipe

if __name__ == "__main__":
    pygame.init()
    show=pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird by Avinash")
    GAME_ASSET['number']=( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha()
    )
    # GAME_ASSET['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_ASSET['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_ASSET['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_ASSET['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_ASSET['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SOUND['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUND['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUND['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUND['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    while True:
        welcomeScreen()
        mainScreen()