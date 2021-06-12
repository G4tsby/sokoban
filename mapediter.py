import csv
import os
from platform import system
from time import sleep
import keyboard
import shutil
import datetime
import re

today = datetime.datetime.today()

DATA_LIST = ['0','1','2','3','4']
# 0:빈곳 1:벽 2:상자 3:캐릭터 4:목표

def clear_screen():
    if system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class Stage:
    def __init__(self):
        # 맵 데이터 열기
        f = open("map.csv",'r')
        origin = csv.reader(f)
        m = re.compile('[0-5]')
        self.data = [[m.findall(j) for j in i] for i in origin]
        f.close()
    
    def show_data(self, idx, select=None):
        clear_screen()
        if select == None:
            for i in self.data[idx]:
                print(i)
        else:
            x,y = select
            print("방향키로 커서 이동, 숫자를 입력해 해당 칸 데이터 변경, p키로 종료")
            print("0:빈공간 1:벽 2:상자 3:캐릭터 4:목표 5: 목표에 들어가 있는 상자")
            for i in range(len(self.data[idx])):
                for j in range(len(self.data[idx][0])):
                    if i==y and j==x:
                        print("|"+str(self.data[idx][i][j])+"|",end='')
                    else:
                        print(' '+str(self.data[idx][i][j])+' ',end='')
                print()

    def add_data(self):
        clear_screen()

        while True:
            try:
                x,y = input("맵의 크기를 가로,세로 형태로 입력해 주세요: ").split(',')
                x,y = int(x), int(y)
                break
            except:
                print("잘못 입력하셨습니다.")

        self.data.append([[0 for _ in range(x)] for _ in range(y)])
        for i in range(y):
            for j in range(x):
                if i==0 or j==0 or i==y-1 or j==x-1:
                    self.data[len(self.data)-1][i][j] = 1
        idx = len(self.data)-1
        self.edit_data(idx)

    def edit_data(self, idx):
        clear_screen()
        x,y = 0,0

        while True:
            self.show_data(idx, select=(x,y))
            inp = keyboard.read_key()
            if inp == "up" and y != 0:
                y -= 1
            elif inp == "down" and y != len(self.data[idx])-1:
                y += 1
            elif inp == "left" and x != 0:
                x -= 1
            elif inp == "right" and x != len(self.data[idx][y])-1:
                x += 1
            elif inp in DATA_LIST:
                self.data[idx][y][x] = int(inp)
            elif inp == "p":
                break
            sleep(0.05)

    def delete_data(self, idx):
        self.show_data(idx)
        if input("위 맵을 삭제하겠습니까? (y/n): ") == 'y':
            self.data.remove(self.data[idx])

    def save_map(self):
        shutil.copy2("map.csv",f"./backup/{today.year}_{today.month}_{today.day}_{today.hour}_{today.minute}_map.csv")
        print(f"./backup/{today.year}_{today.month}_{today.day}_{today.hour}_{today.minute}_map.csv 로 백업됨")
        f = open('map.csv','w', newline='')
        wr = csv.writer(f)
        wr.writerows(self.data)
        f.close()

stage = Stage()

while True:
    print(f"\n현재 {len(stage.data)}개의 맵이 있음.\n")
    print("작업 목록")
    print("1. 맵 추가")
    print("2. 맵 수정")
    print("3. 맵 삭제")
    print("4. 맵 보기")
    print("5. 변경사항 저장")
    print("\n0. 프로그램 종료\n")
    tesk = input("작업 번호 입력: ")

    if tesk == '0':
        break
    elif tesk == '1':
        stage.add_data()
    elif tesk == '2':
        if len(stage.data):
            idx = int(input("\n수정할 맵 번호를 입력해 주세요: "))
            stage.edit_data(idx)
        else:
            print("\n맵이 존재하지 않습니다.")
    elif tesk == '3':
        if len(stage.data):
            idx = int(input("\n맵 번호를 입력: "))
            stage.delete_data(idx)
        else:
            print("\n맵이 존재하지 않습니다.")
    elif tesk == '4':
        if len(stage.data):
            idx = int(input("\n맵 번호를 입력: "))
            stage.show_data(idx)
        else:
            print("\n맵이 존재하지 않습니다.")
    elif tesk == '5':
        stage.save_map()