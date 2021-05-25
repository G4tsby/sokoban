import pygame.font
import time
from platform import system

def set_font(size):
    if "나눔바른고딕" in pygame.font.get_fonts():
        default_font = pygame.font.SysFont("나눔바른고딕", size)
    else:
        if system() == "Windows":
            default_font = pygame.font.SysFont("malgungothic", size)
        elif system() == "Darwin":
            default_font = pygame.font.SysFont("AppleGothic", size)
        elif system() == "Linux":
            default_font = pygame.font.SysFont("NanumBarunGothic", size)
    return default_font

def draw_menu(screen: pygame.surface, res_x, res_y, default_font: pygame.font.Font, stage):

    text_surface = default_font.render("좌우 방향키를 이용해 단계를 선택하세요", False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.15))
    screen.blit(text_surface, rect)

    cr = '1'

    ft = set_font(90)
    text_surface = ft.render(cr, False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.5))
    screen.blit(text_surface, rect)

    pygame.display.update()
    time.sleep(4)
    
    return None