import pygame
import tkinter as tk
import csv
import re
from player import Player
import copy

from mainmenu import draw_menu, set_font
from game import sokoban

def init_map():
    # 저장된 맵 불러오기
    f = open("map.csv",'r')
    origin = csv.reader(f)
    m = re.compile('[0-5]')
    level = [[m.findall(j) for j in i] for i in origin]
    f.close()
    return level

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

    level = init_map()
    player = Player()
    
    screen.fill((255, 255, 255))
    run_game(screen, level, player, res_x, res_y, default_font)

def run_game(screen, level, player, res_x, res_y, default_font):
    clock = pygame.time.Clock()
    mode = "menu"
    selected_stage = 0
    selected_exit = 0
    inited = False
    x, y = 0, 0

    while True:
        clock.tick(10)
        screen.fill((255, 255, 255))

        # 이벤트 처리
        for event in pygame.event.get():

            # 게임 종료
            if event.type == pygame.QUIT:
                break
            # 키 입력 처리
            # 메인매뉴일때
            if event.type == pygame.KEYDOWN:
                if mode == "menu":
                    if event.key == pygame.K_LEFT:
                        if selected_exit == 0 and selected_stage != 0:
                            selected_stage -= 1
                        elif selected_exit == 2:
                            selected_exit = 1
                    elif event.key == pygame.K_RIGHT:
                        if selected_exit == 0  and selected_stage != len(level)-1:
                            selected_stage += 1
                        elif selected_exit == 1:
                            selected_exit = 2
                    elif event.key == pygame.K_ESCAPE:
                        selected_exit = 1
                    elif event.key == pygame.K_RETURN:
                        if selected_exit == 0:
                            level = init_map()
                            mode = "game"
                        elif selected_exit == 1:
                            pygame.quit()
                        elif selected_exit == 2:
                            selected_exit = 0

                # 게임 진행중일때
                elif mode == "game":
                    if event.key == pygame.K_LEFT:
                        if x != 0:
                            x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if x != len(level[selected_stage][0])-1:
                            x += 1
                    elif event.key == pygame.K_UP:
                        if y != 0:
                            y -= 1
                    elif event.key == pygame.K_DOWN:
                        if y != len(level[selected_stage])-1:
                            y += 1
                    elif event.key == pygame.K_r:
                        inited = False

        # 모드별 함수 호출
        if mode == "menu":
            draw_menu(screen, res_x, res_y, default_font, selected_stage, selected_exit)
        elif mode == "game":
            inited, x, y, mode = sokoban(screen, player, level[selected_stage], inited, res_x, res_y, x, y)
        pygame.display.update()

if __name__ == '__main__':
    init_game()
