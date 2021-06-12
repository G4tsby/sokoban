import pygame.font
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

def draw_menu(screen: pygame.surface, res_x, res_y, default_font: pygame.font.Font, stage, exit):

    text_surface = default_font.render("좌우 방향키와 Enter를 이용해 단계를 선택하세요", False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.05))
    screen.blit(text_surface, rect)

    text_surface = default_font.render("ESC를 눌러 게임 종료", False, (0, 0, 0))
    rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.1))
    screen.blit(text_surface, rect)


    ft = set_font(round(res_x*0.046875))
    sprite = pygame.image.load(f"assets/stage_image/{stage}.png")
    rect = sprite.get_rect(center=(res_x*0.5, res_y*0.5))
    screen.blit(sprite, rect)

    if exit != 0:
        ft = set_font(round(res_x*0.026))
        rect = pygame.Rect(res_x*0.332, res_y*0.75, res_x*0.335, res_y*0.17)
        pygame.draw.rect(screen, (0,0,0), rect)
        text_surface = ft.render("게임을 종료하시겠습니까?", False, (255, 255, 255))
        rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.8))
        screen.blit(text_surface, rect)

        text_surface = ft.render("예          아니오", False, (255, 255, 255))
        rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.87))
        screen.blit(text_surface, rect)
        
        offset = (exit-1)*0.1
        pygame.draw.polygon(screen, (255, 255, 255), [[res_x*(0.382+offset), res_y*0.845], [res_x*(0.382+offset), res_y*0.890], [res_x*(0.402+offset), res_y*0.865]])