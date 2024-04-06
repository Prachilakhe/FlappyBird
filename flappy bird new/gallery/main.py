import random 
import sys
import pygame
from pygame.locals import*

FPS =32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = 'gallery/images/bird.png'
BACKGROUND = 'gallery/images/bag.png'
PIPE = 'gallery/images/pipe.png'

def welcomeScreen():
  playerx = int(SCREENWIDTH / 5)
  playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2
  messagex = int(SCREENHEIGHT - GAME_SPRITES['message'].get_width())/2
  messagey = int(SCREENHEIGHT*0.13)
  basex = 0

  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

          elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
              return
          else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0 ))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
               
def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    basex = 0



if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by team3')

    GAME_SPRITES['numbers'] = (
         pygame.image.load('gallery//images//1.png').convert_alpha(),
         pygame.image.load('gallery//images//2.png').convert_alpha(),
         pygame.image.load('gallery//images//3.png').convert_alpha(),
         pygame.image.load('gallery//images//4.png').convert_alpha(),
         pygame.image.load('gallery//images//5.png').convert_alpha(),
         pygame.image.load('gallery//images//6.png').convert_alpha(),
         pygame.image.load('gallery//images//7.png').convert_alpha(),
         pygame.image.load('gallery//images//8.png').convert_alpha(),
         pygame.image.load('gallery//images//9.png').convert_alpha(),
    )
    GAME_SPRITES['message'] = pygame.image.load('gallery/images/strt.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('gallery/images/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()
                            )


    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() 
        mainGame()