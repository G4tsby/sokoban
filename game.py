from math import ceil
import pygame

def sokoban(screen: pygame.surface, player, level, init, res_x, res_y,x ,y):
    if init == False:
        for i in range(len(level)):
            for j in range(len(level[0])):
                if level[i][j] == '3':
                    player.x, player.y = j, i
        _level = [[j for j in i] for i in level]
        init = True

    def draw_map(_level, _screen, _res_x, _res_y):
        # 화면 내에서 맵의 원점을 설정
        origin_point_x = _res_x/2 - len(_level[0])*64/2
        origin_point_y = _res_y/2 - len(_level)*64/2

        for i in range(len(_level)):
            for j in range(len(_level[0])):
                if level[i][j] == '1':
                    block = pygame.image.load("assets/sprite/block.png")
                elif level[i][j] == '2':
                    block = pygame.image.load("assets/sprite/box.png")
                elif level[i][j] == '4':
                    block = pygame.image.load("assets/sprite/target.png")
                elif level[i][j] == '0' or level[i][j] == '3':
                    block = pygame.image.load("assets/sprite/tile.png")
                block = pygame.transform.scale(block, (64, 64))
                _screen.blit(block, [origin_point_x+j*64, origin_point_y+i*64])

                if level[i][j] == '3':
                    block = pygame.image.load("assets/sprite/idle.png")
                    block = pygame.transform.scale(block, (64, 64))
                    _screen.blit(block, [origin_point_x+j*64, origin_point_y+i*64])

    if player.x != x or player.y != y:
        if level[y][x] == '0':
            level[player.y][player.x] = '0'
            level[y][x] = '3'
            player.x, player.y = x, y
        elif level[y][x] == '2':
            if level[y+y-player.y][x+x-player.x] == '0':
                level[y+y-player.y][x+x-player.x] = '2'
                level[player.y][player.x] = '0'
                level[y][x] = '3'
                player.x, player.y = x, y
            

    draw_map(level, screen, res_x, res_y)

    return init, player.x, player.y