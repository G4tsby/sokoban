import pygame
import tkinter as tk
from math import ceil
import csv

from mainmenu import draw_menu, set_font

class Player:
    def __init__(self, size):
        self.x = ceil(size//2)
        self.y = ceil(size//2)
        self.count = 0

        self.sprite = pygame.image.load("assets/sprite/player_idle.png")
        self.player_image = pygame.transform.scale(self.player_image, (64, 64))

        f = open("map.csv",'r')
        origin = csv.reader(f)
        self.level = []
        for i in origin:
            self.level.append(i)
        f.close()

    def move(direction):
        pass

def draw_map(level, size, res_x, res_y):
    pass

def init_game():
    # 컴퓨터 해상도 받아오기
    root = tk.Tk()
    res_x = root.winfo_screenwidth()
    res_y = root.winfo_screenheight()

    # Pygame 초기 설정
    pygame.init()
    pygame.display.set_caption("SOKOBAN")
    screen = pygame.display.set_mode((res_x, res_y))

    # 폰트 불러오기
    pygame.font.init()
    default_font = set_font(30)
    
    screen.fill((255, 255, 255))
    draw_menu(screen, res_x, res_y, default_font)

def run_game():
    pass

if __name__ == '__main__':
    init_game()
