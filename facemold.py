import pygame
import sys
import random

# 클래스 초기화 함수 인자로 이미지 경로를 넣기 위해 PIL모듈 추가
import PIL
from PIL import Image
import glob

class Eyelid(pygame.sprite.Sprite): # generate to express emotion more effectively

    def __init__(self, picture_path):
        super().__init__()
        self.sprites = []
        for filename in glob.glob(picture_path):  # assuming png
            im = filename
            self.sprites.append(pygame.image.load(im))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def update(self):
        self.current_sprite += 0.07
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

class Eyeball(pygame.sprite.Sprite):

    def __init__(self, picture_path):
        super().__init__()
        self.sprites = []
        for filename in glob.glob(picture_path):  # assuming png
            im = filename
            self.sprites.append(pygame.image.load(im))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def update(self):
        self.current_sprite += 0.07
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


class Pupil(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        # 눈동자 좌표
        self.to_x = 0
        self.to_y = 0
        self.sprites = []
        for filename in glob.glob(picture_path):  # assuming png
            im = filename
            self.sprites.append(pygame.image.load(im))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.size = self.image.get_rect().size

        self.rect[0] = self.rect[0]  # 0 현재 눈동자의 x 위치
        self.rect[1] = self.rect[1]  # 0 현재 눈동자의 y 위치

    def update(self):
        self.current_sprite += 0.07
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def movingPupilLeft(self):
        if self.rect[0] <= -24:
            self.rect[0] = -24
        self.rect[0] -= 3

    def movingPupilRight(self):
        if self.rect[0] >= 26:
            self.rect[0] = 26
        self.rect[0] += 3

    def movingPupilDown(self):
        if self.rect[1] >= 30:
            self.rect[1] = 30
        self.rect[1] += 3

    def movingPupilUp(self):
        if self.rect[1] <= -22:
            self.rect[1] = -22
        self.rect[1] -= 3


class Nostril(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.sprites = []
        for filename in glob.glob(picture_path):  # assuming png
            im = filename
            self.sprites.append(pygame.image.load(im))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def update(self):
        self.current_sprite += 0.07
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]


class Mouth(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.sprites = []
        for filename in glob.glob(picture_path):  # assuming png
            im = filename
            self.sprites.append(pygame.image.load(im))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def update(self):
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
