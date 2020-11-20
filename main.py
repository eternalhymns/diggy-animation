import pygame
import sys
import random
import facemold as fm

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 480
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("./background.jpg")
pygame.display.set_caption("larva animation")
pygame.mouse.set_visible(False)



############## Creating sprites and groups ##############


## bagic
# eyelid
bagic_eyelid_sprites = pygame.sprite.Group()
bagic_eyelid = fm.Eyelid('./default-face-image/eyelid/*.png')
bagic_eyelid_sprites.add(bagic_eyelid)

# eyeball
bagic_eyeball_sprites = pygame.sprite.Group()
bagic_eyeball = fm.Eyeball('./default-face-image/eyeball/*.png')
bagic_eyeball_sprites.add(bagic_eyeball)

# pupil
bagic_pupil_sprites = pygame.sprite.Group()
bagic_pupil = fm.Pupil("./default-face-image/pupil/*.png")
bagic_pupil_sprites.add(bagic_pupil)


# nostril
bagic_nostril_sprites = pygame.sprite.Group()
bagic_nostril = fm.Nostril("./default-face-image/nostril/*.png")
bagic_nostril_sprites.add(bagic_nostril)

#mouth
bagic_mouth_sprites = pygame.sprite.Group()
bagic_mouth = fm.Mouth("./default-face-image/mouth/*.png")
bagic_mouth_sprites.add(bagic_mouth)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Drawing #############################################################
    pygame.display.flip()
    screen.blit(background, (0, 0))
  
    bagic_eyeball_sprites.draw(screen)
    bagic_eyeball_sprites.update()

    bagic_eyelid_sprites.draw(screen)
    bagic_eyelid_sprites.update()

    bagic_pupil_sprites.draw(screen)
    bagic_pupil_sprites.update()
    # print(bagic_pupil.rect) # <rect(0, 0, 480, 800)> 0, 0 은 위치, 480, 800은 이미지 사이즈

    bagic_nostril_sprites.draw(screen)
    bagic_nostril_sprites.update()

    bagic_mouth_sprites.draw(screen)
    bagic_mouth_sprites.update()
 

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT: # 눈동자 왼쪽으로
            bagic_pupil.movingPupilLeft()

        elif event.key == pygame.K_RIGHT: # 눈동자 오른쪽으로
            bagic_pupil.movingPupilRight()
        elif event.key == pygame.K_UP: # 눈동자 위쪽으로
            bagic_pupil.movingPupilUp()
        elif event.key == pygame.K_DOWN: # 눈동자 아래쪽으로
            bagic_pupil.movingPupilDown()
    
    

        if event.key == pygame.K_h:  # press 'h' , diggy smiles!
            # # eyeball
            # bagic_eyeball_sprites = pygame.sprite.Group()
            # bagic_eyeball = fm.Eyeball("./")
            # bagic_eyeball_sprites.add(bagic_eyeball)

            # # pupil
            # bagic_pupil_sprites = pygame.sprite.Group()
            # bagic_pupil = fm.Pupil("./")
            # bagic_pupil_sprites.add(bagic_pupil)

            # # nostril
            # bagic_nostril_sprites = pygame.sprite.Group()
            # bagic_nostril = fm.Nostril("./")
            # bagic_nostril_sprites.add(bagic_nostril)

            #mouth
            bagic_mouth_sprites = pygame.sprite.Group()
            bagic_mouth = fm.Mouth("./happy-face-image/mouth/*.png")
            bagic_mouth_sprites.add(bagic_mouth)
            
            # bagic_eyeball_sprites.draw(screen)
            # bagic_eyeball_sprites.update()

            # bagic_pupil_sprites.draw(screen)
            # bagic_pupil_sprites.update()

            # bagic_nostril_sprites.draw(screen)
            # bagic_nostril_sprites.update()

            # bagic_mouth_sprites.draw(screen)
            # bagic_mouth_sprites.update()

#    if event.type == pygame.KEYUP: # 방향키 떼면 멈춤
#         if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#             to_x = 0
#         elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#             to_y = 0

# if he cries, eyes are rotaiting
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     hand.giggling()
    #     happy.animate()  # excute just Once!
    #     happy_sprites.draw(screen)
    #     happy_sprites.update()

   

    clock.tick(60)
