import numpy as np
from colorama import Fore, init,Back, Style
import random
import time
import os

class Boss():
    def __init__(self,a,b):

        temp = np.zeros((22,40),dtype='<U20')
        temp[:] = ' '
        y=0
        self._lives = 30
        with open("boss.txt") as boss:
            mx=0
            for line in boss:
                x = 0
                for char in line:
                    if char == '\n':
                        break
                    else:
                        temp[y][x] = char 
                    x += 1
                
                if x>mx:
                    mx=x
                y += 1

        self.__grid8 = np.zeros((b,a),dtype='<U20')
        self.__grid8[:] = ' '
        self.__bombgrid = np.zeros((b,a),dtype='<U20')
        self.__bombgrid[:] = ' '
        self.__body = temp
        self._xrange = y
        self._yrange = mx
        self._x1 = 7
        self._y1 = 12
        self._bomb = np.array([[Fore.LIGHTBLACK_EX + Back.RED+'B'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'B'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.RED+'B'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'B'+Style.RESET_ALL]])


    def get_boss_grid(self):
        return self.__grid8

    def get_bombgrid(self):
        return self.__bombgrid

    def place_boss(self,a,b,boardx,grid,grid8):

        grid[self._x1:self._x1+self._xrange , self._y1:self._y1+self._yrange] = ' '
        for i in range(self._x1,self._x1+self._xrange):
            for j in range(self._y1,self._y1+self._yrange):
                grid8[i][j] = ' '

        if boardx-(int)(self._yrange/2) < 3:
            t1 = 2
            t2=t1+37
        elif boardx+(int)(self._yrange/2) > a-3:
            t2 = a-3
            t1 = t2-37
        else:
            t2 = boardx+(int)(self._yrange/2)
            t1=t2-37

        self._y1 = t1
        grid[6:6+self._xrange , t1:t2+1] = self.__body[0:self._xrange,0:self._yrange]

        for i in range(6,6+self._xrange):
            for j in range(t1,t2+1):
                if grid[i][j]!= ' ':
                    grid8[i][j] = 20

    def add_bomb(self,grid,grid2,a,b):
        grid2[b][a] = 1
        bomb = self._bomb
        grid[b:b+2,a:a+2] = np.tile(bomb,1)

    def move_bomb(self,width,height,grid,grid2,brd):
        for i in reversed(range(height-1)):
            for j in range (width):
                if grid2[i][j]!= " ":
                    if i == height-5:
                        # print(i)
                        # time.sleep(1)
                        if grid[height-3][j]!= " " or grid[height-3][j+1]!= " ":
                            
                            brd.lives -= 1
                            os.system("aplay sounds/sound_collision_brick.wav -q &")

                        grid2[i][j] = ' '
                        grid[i:i+2,j:j+2] = " "    
                    
                    elif i < height-5:

                        grid2[i+1][j] = grid2[i][j]
                        grid[i+1:i+3,j:j+2] = self._bomb
                        grid2[i][j] = ' '
                        grid[i:i+1,j:j+2] = ' '

