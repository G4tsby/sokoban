import pygame
from mainmenu import set_font

def sokoban(screen: pygame.surface, player, level, init, res_x, res_y, x ,y, selected_exit):
    def check_able(box_y, box_x):
        off_x = 0
        off_y = 0

        # 벽이 어느 위치에 있는지 검사
        if level[box_y][box_x+1] == '1':
            off_x = 1
        elif level[box_y][box_x-1] == '1':
            off_x = -1
        elif level[box_y+1][box_x] == '1':
            off_y = 1
        elif level[box_y-1][box_x] == '1':
            off_y = -1

        # 상자가 모서리에 있을 경우
        if off_x != 0 and off_y != 0:
            return False

        # Y축 방향으로 검사
        if off_x != 0:
            flag_plus, flag_minus = -1, -1 # 이동 불가 0, 이동 가능 1 
            depth = 0
            while flag_plus == -1 and flag_minus == -1:
                depth += off_x
                if flag_plus == -1:
                    if level[box_y+depth][box_x] == '1':
                        flag_plus = 1
                    elif level[box_y+depth][box_x] == '0':
                        if level[box_y+depth][box_x+off_x] == '0':
                            flag_plus = 2
                    elif level[box_y+depth][box_x] == '4':
                        flag_plus = 2

                if flag_minus == -1:
                    if level[box_y-depth][box_x] == '1':
                        flag_minus = 1
                    elif level[box_y-depth][box_x] == '0':
                        if level[box_y-depth][box_x+off_x] == '0':
                            flag_plus = 2
                    elif level[box_y+depth][box_x] == '4':
                        flag_minus = 2
        # X축 방향으로 검사
        if off_y != 0:
            flag_plus, flag_minus = -1, -1 # 이동 불가 0, 이동 가능 1 
            depth = 0
            while flag_plus == -1 and flag_minus == -1:
                depth += off_y

                if flag_plus == -1:
                    if level[box_y][box_x+depth] == '1':
                        flag_plus = 1
                    elif level[box_y][box_x+depth] == '0':
                        if level[box_y+off_x][box_x+depth] == '0':
                            flag_plus = 2
                    elif level[box_y][box_x+depth] == '4':
                        flag_plus = 2

                if flag_minus == -1:
                    if level[box_y][box_x-depth] == '1':
                        flag_minus = 1
                    elif level[box_y][box_x-depth] == '0':
                        if level[box_y+off_x][box_x-depth] == '0':
                            flag_minus = 2
                    elif level[box_y][box_x+depth] == '4':
                        flag_minus = 2            

        if flag_minus == 2 or flag_plus == 2:
            return True
        else:
            return False

        return True
    def draw_map(_level, _screen, _res_x, _res_y):
        # 화면 내에서 맵의 원점을 설정
        origin_point_x = _res_x/2 - len(_level[0])*round(res_x*0.03333)/2
        origin_point_y = _res_y/2 - len(_level)*round(res_x*0.03333)/2

        for i in range(len(_level)):
            for j in range(len(_level[0])):
                if level[i][j] == '1':
                    block = pygame.image.load("assets/sprite/block.png")
                elif level[i][j] == '2':
                    block = pygame.image.load("assets/sprite/box.png")
                elif level[i][j] == '4' or level[i][j] == '6':
                    block = pygame.image.load("assets/sprite/target.png")
                elif level[i][j] == '5':
                    block = pygame.image.load("assets/sprite/box_target.png")
                elif level[i][j] == '0' or level[i][j] == '3':
                    block = pygame.image.load("assets/sprite/tile.png")
                block = pygame.transform.scale(block, (round(res_x*0.03333), round(res_x*0.03333)))
                _screen.blit(block, [origin_point_x+j*round(res_x*0.03333), origin_point_y+i*round(res_x*0.03333)])

                if level[i][j] == '3' or level[i][j] == '6':
                    block = pygame.image.load("assets/sprite/idle.png")
                    block = pygame.transform.scale(block, (round(res_x*0.03333), round(res_x*0.03333)))
                    _screen.blit(block, [origin_point_x+j*round(res_x*0.03333), origin_point_y+i*round(res_x*0.03333)])

    if not init:
        player.__init__(res_x)
        for i in range(len(level)):
            for j in range(len(level[0])):
                if level[i][j] == '3':
                    player.x, player.y = j, i
                    x,y = j, i
                elif level[i][j] == '4':
                    player.count += 1
        draw_map(level, screen, res_x, res_y)
        init = True

    # 플레이어가 움직였을때
    if player.x != x or player.y != y:
        # 움직일 좌표가 목표나 빈곳이라면
        if level[y][x] == '0' or level[y][x] == '4':
            if level[player.y][player.x] == '3':
                level[player.y][player.x] = '0'
            elif level[player.y][player.x] == '6':
                level[player.y][player.x] = '4'
            # 캐릭터가 이동할 위치 처리
            if level[y][x] == '0':
                level[y][x] = '3'
                player.x, player.y = x, y
            elif level[y][x] == '4':
                level[y][x] = '6'
                player.x, player.y = x, y
            
        # 움직일 좌표가 상자나 목표에 있는 상자라면
        elif level[y][x] == '2' or level[y][x] == '5':
            # 상자를 움직일 수 있으면
            if level[y+y-player.y][x+x-player.x] == '0' or level[y+y-player.y][x+x-player.x] == '4':
                # 상자가 이동할 위치 처리
                if level[y+y-player.y][x+x-player.x] == '0':
                    level[y+y-player.y][x+x-player.x] = '2'
                elif level[y+y-player.y][x+x-player.x] == '4':
                    level[y+y-player.y][x+x-player.x] = '5'
                    player.count -= 1
                # 캐릭터가 있던 위치 처리
                if level[player.y][player.x] == '3':
                    level[player.y][player.x] = '0'
                elif level[player.y][player.x] == '6':
                    level[player.y][player.x] = '4'
                # 캐릭터가 이동할 위치 처리
                if level[y][x] == '5':
                    level[y][x] = '6'
                    player.count += 1
                    player.x, player.y = x, y
                elif level[y][x] == '2':
                    level[y][x] = '3'
                    player.x, player.y = x, y

    draw_map(level, screen, res_x, res_y)

    if selected_exit != 0:
        rect1 = pygame.Rect(res_x*0.332, res_y*0.75, res_x*0.335, res_y*0.17)
        pygame.draw.rect(screen, (0,0,0), rect1)
        ft = set_font(round(res_x*0.026))
        text_surface = ft.render("메인메뉴로 돌아가시겠습니까?", False, (255, 255, 255))
        rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.8))
        screen.blit(text_surface, rect)

        text_surface = ft.render("예          아니오", False, (255, 255, 255))
        rect = text_surface.get_rect(center=(res_x*0.5, res_y*0.87))
        screen.blit(text_surface, rect)
        
        offset = (selected_exit-1)*0.1
        pygame.draw.polygon(screen, (255, 255, 255), [[res_x*(0.382+offset), res_y*0.845], [res_x*(0.382+offset), res_y*0.890], [res_x*(0.402+offset), res_y*0.865]])

    if player.count == 0 and init:
        return False, player.x, player.y, 'menu', selected_exit

    return init, player.x, player.y, 'game', selected_exit