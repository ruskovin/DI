import pygame
from game import Game
from player import Player
pygame.init()


#window of the game
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))
 

# background of the game
background = pygame.image.load('python-game/assets/bg.jpg')

# loading our game
game = Game()

#loading our player
player = Player()

running = True
# condition for the game keep running
while running:

    #background setting
    screen.blit(background,(0,-200))

    #applying player image
    screen.blit(game.player.image,game.player.rect)

    # moving condition
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x <= 920:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -40 :
        game.player.move_left()

    print(game.player.rect.x)

    # updating the screen
    pygame.display.flip()

    # if the player close this window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Game closing")
        
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False