import pygame, sys, random

# Player클래스는 Blink 클래스로 수정하자 프로그램 실행 시 눈 계속 깜빡이게 
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("./frogPlayer/attack_1.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_2.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_3.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_4.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_5.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_6.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_7.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_8.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_9.png"))
        self.sprites.append(pygame.image.load("./frogPlayer/attack_10.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
    def update(self):
        self.current_sprite +=1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

# 놀람
class Surpring(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("./surprise/1_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/1_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/2_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/3_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/4_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/5_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/6_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/7_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/8_blink.jpg"))
        self.sprites.append(pygame.image.load("./surprise/9_blink.jpg"))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def animate(self):
        self.is_animating = True

    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]





class Hand(pygame.sprite.Sprite):
    def __init__(self, picture_path): # 인자로 '이미지 경로'를 설정함
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.giggle = pygame.mixer.Sound("giggle.wav")
    def giggling (self):
        self.giggle.play()
        # pygame.sprite.spritecollide(hand, cheeks_group, True) 볼 누르면 볼 없어짐
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
class Cheeks(pygame.sprite.Sprite):
    def __init__(self,picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()

        # 이 클래스로 만들어질 객체는 마우스 따라 움직이지 않고, 제자리에 고정됨
        


        


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

# Hand
hand = Hand("./hand64.jpg")
hand_group = pygame.sprite.Group()
hand_group.add(hand)

# Cheeks (static)
cheeks = Cheeks("./cheeks.jpg")
cheeks_group = pygame.sprite.Group()
cheeks_group.add(cheeks)

# Surprising
surprising_sprites = pygame.sprite.Group()
surprising = Surpring()
surprising_sprites.add(surprising)

# Player
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.MOUSEMOTION:
            moving_sprites.draw(screen)
            moving_sprites.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hand.giggling()
        
                
        # if event.type == pygame.KEYBOARDUP: && keypress 'S'
        #    surprise.surprised() # 놀라는 음성 추가
    
    # Drawing #############################################################
    pygame.display.flip()
    screen.blit(background, (0,0))
    # cheeks_group.draw(screen)
    

    if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 스페이스바를 누르면 놀란다
                surprising.animate() # excute just Once!
                surprising_sprites.draw(screen)
                surprising_sprites.update()

    

    hand_group.draw(screen)
    hand_group.update()

    clock.tick(60)
