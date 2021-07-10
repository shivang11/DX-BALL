import numpy as np
from colorama import Fore, init,Back, Style
import random
import time
import os

from scene import *

class Powerup:

    def __init__(self , width , height):

        self._xspeed = 0
        self._yspeed = 1
        self._staytime = 20
        self._power1 = np.array([[Fore.LIGHTBLACK_EX + Back.YELLOW+'1'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.YELLOW+'1'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.YELLOW+'1'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.YELLOW+'1'+Style.RESET_ALL]])
        
        self._power2 = np.array([[Fore.LIGHTBLACK_EX + Back.GREEN+'2'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.GREEN+'2'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.GREEN+'2'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.GREEN+'2'+Style.RESET_ALL]])

        self._power3 = np.array([[Fore.LIGHTBLACK_EX + Back.MAGENTA+'3'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.MAGENTA+'3'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.MAGENTA+'3'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.MAGENTA+'3'+Style.RESET_ALL]])

        self._power4 = np.array([[Fore.LIGHTBLACK_EX + Back.BLUE+'4'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLUE+'4'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.BLUE+'4'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLUE+'4'+Style.RESET_ALL]])

        self._power5 = np.array([[Fore.LIGHTBLACK_EX + Back.RED+'5'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'5'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.RED+'5'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'5'+Style.RESET_ALL]])

        self._power6 = np.array([[Fore.LIGHTBLACK_EX + Back.CYAN+'6'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.CYAN+'6'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.CYAN+'6'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.CYAN+'6'+Style.RESET_ALL]])

        self._power7 = np.array([[Fore.LIGHTBLACK_EX + Back.CYAN+'F'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.CYAN+'F'+Style.RESET_ALL],
                                [Fore.LIGHTBLACK_EX + Back.CYAN+'F'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.CYAN+'F'+Style.RESET_ALL]])


    def create_struct(self , width , height):
        self.__rows = height
        self.__columns = width
        self.__powergrid = np.zeros((height,width),dtype='<U20')
        self.__powergrid[:] = ' '

        self.__powergrid2 = np.zeros((height,width),dtype='<U20')
        self.__powergrid2[:] = ' '

        self._speedx = np.zeros((height,width),dtype='<U20')
        self._speedx[:] = ' '

        self._speedy = np.zeros((height,width),dtype='<U20')
        self._speedy[:] = ' '


        self.__activate = np.zeros(10 , dtype=int)
        self.__activate2 = np.zeros(10 , dtype=int)

    def get_powergrid(self):
        return self.__powergrid

    def get_powergrid2(self):
        return self.__powergrid2
    
    def get_activate(self):
        return self.__activate

    def get_activate2(self):
        return self.__activate2

    def move_powerup(self,width,height,grid,powergrid,activate,brd,speedx,speedy):
        temp = np.zeros((height,width),dtype='<U20')
        temp[:] = ' '
        for i in reversed(range(height-1)):
            for j in range (width):
                if powergrid[i][j]!= " ":
                    if i >= height-5:
                        # print(i)
                        # time.sleep(1)
                        if grid[height-3][j]!= " " or grid[height-3][j+1]!= " ":
                            
                            num = (int)(powergrid[i][j])
                            st = time.time()

                            # print(num)
                            # time.sleep(2)
                            
                            if num == 1 and activate[2] == 0 and activate[1] == 0:
                                brd.increase_length(width,height,grid)
                            
                            if num == 2 and activate[1] == 0 and activate[2] == 0:
                                brd.decrease_length(width,height,grid)

                            if num == 4:
                                brd.increase_speed()
                            
                            activate[num] = st
                            os.system("aplay sounds/sound_powerup.wav -q &")

                        powergrid[i][j] = ' '
                        grid[i:i+2,j:j+2] = ' '
                        speedx[i][j] = ' '
                        speedy[i][j] = ' '
                        temp[i][j] = powergrid[i][j]    
                    
                    elif i < height-5:
                        # print("aaya")
                        # time.sleep(2)
                        # if speedx[i][j]!=" ":

                        if speedx[i][j] == ' ':
                            speedx[i][j] = 1
                        
                        if speedy[i][j] == ' ':
                            speedy[i][j] = 1

                        x = (int)(speedx[i][j])
                        y = (int)(speedy[i][j])
                        tempx = x
                        tempy = y
                        posy = i+(int)(speedy[i][j])
                        posx = j+(int)(speedx[i][j])
                        if posx > width-4:
                            num1 = posx - width + 3
                            posx = width-4 - num1
                            tempx = -x
                            tempy = y

                        elif posx < 3:
                            
                            num1 = 2 - posx 
                            posx = 2 + num1
                            tempx = -x
                            tempy = y

                        if posy < 7:
                            
                            num1 = 6 - posy 
                            posy = 6 + num1
                            tempx = x
                            tempy = -y
                            
                    # else:
                    #     posx=i+1
                    #     posy=j

                        grid[i:i+2,j:j+2] = ' '

                        if posy <= height - 5:
                            temp[posy][posx] = powergrid[i][j]
                            speedx[posy][posx] = tempx
                            speedy[posy][posx] = tempy
                            y = (int)(speedy[posy][posx])

                            
                            if y<= 0:
                                y = y+1
                            speedy[posy][posx] = y

                            if powergrid[i][j] == "1":
                                grid[posy:posy+2,posx:posx+2] = self._power1
                            if powergrid[i][j] == "2":
                                grid[posy:posy+2,posx:posx+2] = self._power2
                            if powergrid[i][j] == "3":
                                grid[posy:posy+2,posx:posx+2] = self._power3
                            if powergrid[i][j] == "4":
                                grid[posy:posy+2,posx:posx+2] = self._power4
                            if powergrid[i][j] == "5":
                                grid[posy:posy+2,posx:posx+2] = self._power5
                            if powergrid[i][j] == "6":
                                grid[posy:posy+2,posx:posx+2] = self._power6
                            if powergrid[i][j] == "7":
                                grid[posy:posy+2,posx:posx+2] = self._power7
                        powergrid[i][j] = ' '
                        speedx[i][j] = ' '
                        speedy[i][j] = ' '


        for i in range(height):
            for j in range(width):
                powergrid[i][j] = temp[i][j]
            
                        
                       

class power_class1(Powerup):

    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power1
        grid[a:a+2,b:b+2] = num

class power_class2(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power2
        grid[a:a+2,b:b+2] = num

class power_class3(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power3
        grid[a:a+2,b:b+2] = num
        

class power_class4(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power4
        grid[a:a+2,b:b+2] = num

class power_class5(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power5
        grid[a:a+2,b:b+2] = num

class power_class6(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power6
        grid[a:a+2,b:b+2] = num

class power_class7(Powerup):
    
    def __init__(self, a,b,grid):
        super().__init__(a,b)
        num = self._power7
        grid[a:a+2,b:b+2] = num

class create_powerup:

    def __init__(self,a,b,c,grid):

        if c=="1":
            power1 = power_class1(a,b,grid)
        if c=="2":
            power2 = power_class2(a,b,grid)
        if c=="3":
            power3 = power_class3(a,b,grid)
        if c=="4":
            power4 = power_class4(a,b,grid)
        if c=="5":
            power5 = power_class5(a,b,grid)
        if c=="6":
            power6 = power_class6(a,b,grid)
        if c=="10":
            power7 = power_class7(a,b,grid)


        