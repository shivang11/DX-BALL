import numpy as np
from colorama import Fore, init,Back, Style
import random
import time
import os

from scene import *
from powerup import *

class Brick:

    def __init__(self , a ,b):

        self._fall_time = 30
        self._lev3 = np.array([Fore.LIGHTBLACK_EX + Back.RED+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'-'+Style.RESET_ALL , 
                                                    Fore.LIGHTBLACK_EX + Back.RED+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.RED+'-'+Style.RESET_ALL])

        self._lev5 = np.array([Fore.LIGHTBLACK_EX + Back.YELLOW+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.YELLOW+'-'+Style.RESET_ALL , 
                                                    Fore.LIGHTBLACK_EX + Back.YELLOW+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.YELLOW+'-'+Style.RESET_ALL])

        self._lev1 = np.array([Fore.LIGHTBLACK_EX + Back.GREEN+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.GREEN+'-'+Style.RESET_ALL , 
                                                    Fore.LIGHTBLACK_EX + Back.GREEN+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.GREEN+'-'+Style.RESET_ALL])

        self._lev20 = np.array([Fore.LIGHTBLACK_EX + Back.BLACK+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLACK+'-'+Style.RESET_ALL , 
                                                    Fore.LIGHTBLACK_EX + Back.BLACK+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLACK+'-'+Style.RESET_ALL])
        
        self._lev2 = np.array([Fore.LIGHTBLACK_EX + Back.BLUE+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLUE+'-'+Style.RESET_ALL , 
                                                    Fore.LIGHTBLACK_EX + Back.BLUE+'-'+Style.RESET_ALL , Fore.LIGHTBLACK_EX + Back.BLUE+'-'+Style.RESET_ALL])
        
        # num_brick = 25
    
    def create_grid(self , a , b):
        self.__score = 0
        self.__rows = b
        self.__columns = a
        self.__grid2 = np.zeros((b,a),dtype='<U20')
        self.__grid2[:] = ' '

        self.__grid5 = np.zeros((b,a),dtype='<U20')
        self.__grid5[:] = ' '

        self.__grid7 = np.zeros((b,a),dtype='<U20')
        self.__grid7[:] = ' '

        self.__placepower = np.zeros((b,a),dtype='<U20')
        self.__placepower[:] = ' '

        self.__placepower2 = np.zeros((b,a),dtype='<U20')
        self.__placepower2[:] = ' '

    def create_rainbow_grid(self,a,b):
        self.__rainbow = np.zeros((b,a),dtype='<U20')
        self.__rainbow[:] = ' '
        self.__rainbow2 = np.zeros((b,a),dtype='<U20')
        self.__rainbow2[:] = ' '


    def get_rainbow(self):
        return self.__rainbow

    def get_rainbow2(self):
        return self.__rainbow2

    def get_grid (self):
        return self.__grid2

    def get_placepower(self):
        return self.__placepower

    def get_grid2(self):
        return self.__grid5

    def get_grid3(self):
        return self.__grid7

    def get_placepower2(self):
        return self.__placepower2

    def get_score(self):
        return self.__score

    def update_score(self,score):
        self.__score = score

    def change_color(self,a,b,rainbow,grid,grid2):
        for i in range(b):
            for j in range(a):
                if rainbow[i][j]!=" ":
                    if grid2[i][j]=="1":
                        grid2[i][j] = 2
                        grid[i:i+3,j:j+8] = np.tile(self._lev2,2)
                    
                    elif grid2[i][j]=="2":
                        grid2[i][j] = 3
                        grid[i:i+3,j:j+8] = np.tile(self._lev3,2)

                    elif grid2[i][j]=="3":
                        grid2[i][j] = 1
                        grid[i:i+3,j:j+8] = np.tile(self._lev1,2)




class class1(Brick):

    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump4 = self._lev1

        # grid2 = get_grid()
        grid[8:11,86:94] = np.tile(nump4,2)
        grid2[8][86] = 1
        grid[8:11 , 95:103] = np.tile(nump4,2)
        grid2[8][95] = 1
        placepower[8][95] = 1

        grid[11:14,41:49] = np.tile(nump4,2)
        grid2[11][41] = 1
        grid[11:14,50:58] = np.tile(nump4,2)
        grid2[11][50] = 1
        grid[11:14,77:85] = np.tile(nump4,2)
        grid2[11][77] = 1
        grid[14:17 , 59:67] = np.tile(nump4,2)
        grid2[14][59] = 1
        grid[14:17,68:76] = np.tile(nump4,2)
        grid2[14][68] = 1
        placepower[14][68] = 5
        grid[14:17,95:103] = np.tile(nump4,2)
        grid2[14][95] = 1
        placepower[14][95] = 4
        grid[17:20,32:40] = np.tile(nump4,2)
        grid2[17][32] = 1
        rainbow[17][32] = 1
        grid[20:23,41:49] = np.tile(nump4,2)
        grid2[20][41] = 1
        grid[20:23 , 59:67] = np.tile(nump4,2)
        grid2[20][59] = 1
        placepower[20][59] = 4
        grid[20:23,77:85] = np.tile(nump4,2)
        grid2[20][77] = 1
        grid[20:23,104:112] = np.tile(nump4,2)
        grid2[20][104] = 1
        grid[20:23,122:130] = np.tile(nump4,2)
        grid2[20][122] = 1
        grid[26:29,50:58] = np.tile(nump4,2)
        grid2[26][50] = 1
        grid[26:29,68:76] = np.tile(nump4,2)
        grid2[26][68] = 1
        placepower[26][77] = 6
        grid[26:29,77:85] = np.tile(nump4,2)
        grid2[26][77] = 1

class class2(Brick):
    
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump6 = self._lev2

        grid[8:11,5:13] = np.tile(nump6,2)
        grid2[8][5] = 2
        placepower[8][5] = 2
        grid[8:11,14:22] = np.tile(nump6,2)
        grid2[8][14] = 2
       
        placepower[8][14] = 6
        grid[8:11,68:76] = np.tile(nump6,2)
        grid2[8][68] = 2
        grid[8:11,77:85] = np.tile(nump6,2)
        grid2[8][77] = 2
        grid[8:11,122:130] = np.tile(nump6,2)
        grid2[8][122] = 2
        placepower[8][122] = 1
        grid[8:11,131:139] = np.tile(nump6,2)
        grid2[8][131] = 2
        grid[11:14 , 59:67] = np.tile(nump6,2)
        grid2[11][59] = 2
        placepower[11][59] = 2
        grid[14:17,14:22] = np.tile(nump6,2)
        grid2[14][14] = 2
        grid[14:17 , 23:31] = np.tile(nump6,2)
        grid2[14][23] = 2
        
        grid[14:17 , 41:49] = np.tile(nump6,2)
        grid2[14][41] = 2
        placepower[14][41] = 5
        grid[14:17,86:94] = np.tile(nump6,2)
        grid2[14][86] = 2
    
        grid[14:17,104:112] = np.tile(nump6,2)
        grid2[14][104] = 2
        rainbow[14][104] = 1
        grid[14:17,113:121] = np.tile(nump6,2)
        grid2[14][113] = 2
        grid[17:20,77:85] = np.tile(nump6,2)
        grid2[17][77] = 2
        placepower[17][77] = 1
        grid[20:23,68:76] = np.tile(nump6,2)
        grid2[20][68] = 2
        grid[20:23 , 95:103] = np.tile(nump6,2)
        grid2[20][95] = 2
        grid[23:26,77:85] = np.tile(nump6,2)
        # grid[24:25,77:85] = np.tile(nump6,2)
        grid2[23][77] = 2
        grid[23:26,86:94] = np.tile(nump6,2)
        # grid[24:25,86:94] = np.tile(nump6,2)
        grid2[23][86] = 2
        placepower[23][86] = 1
        grid[26:29 , 59:67] = np.tile(nump6,2)
        # grid[27:28 ,59:67] = np.tile(nump2,2)
        grid2[26][59] = 2
        grid[29:32,68:76] = np.tile(nump6,2)
        # grid[30:31,68:76] = np.tile(nump6,2)
        grid2[29][68] = 2
        grid[23:26,50:58] = np.tile(nump6,2)
        # grid[24:25,50:58] = np.tile(nump5,2)
        grid2[23][50] = 2  

class class3(Brick):
    
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump2 = self._lev3


        grid[8:11,41:49] = np.tile(nump2,2)
        # grid[9:10,41:49] = np.tile(nump2,2)
        grid2[8][41] = 3
        grid[8:11,50:58] = np.tile(nump2,2)
        # grid[9:10,50:58] = np.tile(nump2,2)
        grid2[8][50] = 3
        grid[8:11 , 59:67] = np.tile(nump2,2)
        # grid[9:10 ,59:67] = np.tile(nump2,2)
        grid2[8][59] = 3
        grid[11:14,68:76] = np.tile(nump2,2)
        # grid[12:13,68:76] = np.tile(nump2,2)
        grid2[11][68] = 3
        grid[14:17,32:40] = np.tile(nump2,2)
        # grid[15:16,32:40] = np.tile(nump2,2)
        grid2[14][32] = 3
        placepower[14][32] = 1
        grid[14:17,50:58] = np.tile(nump2,2)
        # grid[15:16,50:58] = np.tile(nump4,2)
        grid2[14][50] = 3
        rainbow[14][50] = 1
        grid[14:17,77:85] = np.tile(nump2,2)
        # grid[15:16,77:85] = np.tile(nump2,2)
        grid2[14][77] = 3
        grid[14:17,122:130] = np.tile(nump2,2)
        # grid[15:16,122:130] = np.tile(nump2,2)
        grid2[14][122] = 3
        grid[17:20,5:13] = np.tile(nump2,2)
        # grid[18:19,5:13] = np.tile(nump2,2)
        grid2[17][5] = 3
        grid[17:20 , 23:31] = np.tile(nump2,2)
        # grid[18:19 , 23:31] = np.tile(nump2,2)
        grid2[17][23] = 3
        rainbow[17][23] = 1
        grid[17:20,41:49] = np.tile(nump2,2)
        # grid[18:19,41:49] = np.tile(nump2,2)
        grid2[17][41] = 3
        grid[17:20 , 59:67] = np.tile(nump2,2)
        # grid[18:19 ,59:67] = np.tile(nump2,2)
        grid2[17][59] = 3
        placepower[17][59] = 3
        grid[17:20,68:76] = np.tile(nump2,2)
        # grid[18:19,68:76] = np.tile(nump2,2)
        grid2[17][68] = 3
        grid[17:20 , 95:103] = np.tile(nump2,2)
        # grid[18:19 , 95:103] = np.tile(nump2,2)
        grid2[17][95] = 3
        placepower[17][95] = 6
        grid[17:20,104:112] = np.tile(nump2,2)
        # grid[18:19,104:112] = np.tile(nump2,2)
        grid2[17][104] = 3
        grid[17:20,113:121] = np.tile(nump2,2)
        # grid[18:19,113:121] = np.tile(nump2,2)
        grid2[17][113] = 3
        grid[17:20,131:139] = np.tile(nump2,2)
        # grid[18:19,131:139] = np.tile(nump2,2)
        grid2[17][131] = 3
        grid[20:23,14:22] = np.tile(nump2,2)
        # grid[21:22,14:22] = np.tile(nump2,2)
        grid2[20][14] = 3
        grid[20:23,32:40] = np.tile(nump2,2)
       
        # grid[21:22,32:40] = np.tile(nump2,2)
        grid2[20][32] = 3
        grid[20:23,50:58] = np.tile(nump2,2)
        # grid[21:22,50:58] = np.tile(nump2,2)
        grid2[20][50] = 3
        grid[20:23,86:94] = np.tile(nump2,2)
        # grid[21:22,86:94] = np.tile(nump2,2)
        grid2[20][86] = 3
        grid[23:26 , 23:31] = np.tile(nump2,2)
        # grid[24:25 , 23:31] = np.tile(nump2,2)
        grid2[23][23] = 3
        placepower[23][23] = 7
        grid[23:26,41:49] = np.tile(nump2,2)
        # grid[24:25,41:49] = np.tile(nump2,2)
        grid2[23][41] = 3
        grid[23:26,68:76] = np.tile(nump2,2)
        # grid[24:25,68:76] = np.tile(nump2,2)
        grid2[23][68] = 3
        placepower[23][68] = 5
        grid[23:26 , 95:103] = np.tile(nump2,2)
        # grid[24:25 , 95:103] = np.tile(nump6,2)
        grid2[23][95] = 3
        grid[23:26,113:121] = np.tile(nump2,2)
        # grid[24:25,113:121] = np.tile(nump2,2)
        grid2[23][113] = 3
        placepower[23][113] = 6
        grid[26:29,32:40] = np.tile(nump2,2)
        # grid[27:28,32:40] = np.tile(nump2,2)
        grid2[26][32] = 3
        
        grid[26:29,86:94] = np.tile(nump2,2)
        # grid[27:28,86:94] = np.tile(nump2,2)
        grid2[26][86] = 3
        rainbow[26][86] = 1
        grid[26:29,104:112] = np.tile(nump2,2)
        # grid[27:28,104:112] = np.tile(nump2,2)
        grid2[26][104] = 3

        grid[29:32,41:49] = np.tile(nump2,2)
        # grid[30:31,41:49] = np.tile(nump2,2)
        grid2[29][41] = 3
        placepower[29][41] = 4
        grid[29:32 , 59:67] = np.tile(nump2,2)
        # grid[30:31 ,59:67] = np.tile(nump2,2)
        grid2[29][59] = 3
        grid[29:32,77:85] = np.tile(nump2,2)
        # grid[30:31,77:85] = np.tile(nump2,2)
        grid2[29][77] = 3
        grid[29:32 , 95:103] = np.tile(nump2,2)
        # grid[30:31 , 95:103] = np.tile(nump2,2)
        grid2[29][95] = 3
        placepower[29][95] = 1
        grid[32:35,50:58] = np.tile(nump2,2)
        # grid[33:34,50:58] = np.tile(nump2,2)
        grid2[32][50] = 3
        grid[32:35,68:76] = np.tile(nump2,2)
        # grid[33:34,68:76] = np.tile(nump2,2)
        grid2[32][68] = 3
        grid[32:35,86:94] = np.tile(nump2,2)
        # grid[33:34,86:94] = np.tile(nump2,2)
        grid2[32][86] = 3
        grid[35:38 , 59:67] = np.tile(nump2,2)
        # grid[36:37 ,59:67] = np.tile(nump2,2)
        grid2[35][59] = 3
        placepower[35][59] = 4
        grid[35:38,77:85] = np.tile(nump2,2)
        # grid[36:37,77:85] = np.tile(nump2,2)
        grid2[35][77] = 3
        placepower[35][77] = 1


class class5(Brick):
    
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump3 = self._lev5

                
        grid[14:17,5:13] = np.tile(nump3,2)
        # grid[15:16,5:13] = np.tile(nump3,2)
        grid2[14][5] = 5
        grid[14:17,131:139] = np.tile(nump3,2)
        # grid[15:16,131:139] = np.tile(nump3,2)
        grid2[14][131] = 5
        grid[17:20,14:22] = np.tile(nump3,2)
        # grid[18:19,14:22] = np.tile(nump3,2)
        grid2[17][14] = 5
        grid[17:20,122:130] = np.tile(nump3,2)
        # grid[18:19,122:130] = np.tile(nump3,2)
        grid2[17][122] = 5
        grid[20:23 , 23:31] = np.tile(nump3,2)
        # grid[21:22 , 23:31] = np.tile(nump3,2)
        grid2[20][23] = 5
        grid[20:23,113:121] = np.tile(nump3,2)
        # grid[21:22,113:121] = np.tile(nump3,2)
        grid2[20][113] = 5
        grid[23:26,32:40] = np.tile(nump3,2)
        # grid[24:25,32:40] = np.tile(nump3,2)
        grid2[23][32] = 5
        grid[23:26,104:112] = np.tile(nump3,2)
        # grid[24:25,104:112] = np.tile(nump3,2)
        grid2[23][104] = 5
        grid[26:29,41:49] = np.tile(nump3,2)
        # grid[27:28,41:49] = np.tile(nump3,2)
        grid2[26][41] = 5
        grid[26:29 , 95:103] = np.tile(nump3,2)
        # grid[27:28 , 95:103] = np.tile(nump3,2)
        grid2[26][95] = 5
        grid[29:32,50:58] = np.tile(nump3,2)
        # grid[30:31,50:58] = np.tile(nump3,2)
        grid2[29][50] = 5
        grid[29:32,86:94] = np.tile(nump3,2)
        # grid[30:31,86:94] = np.tile(nump3,2)
        grid2[29][86] = 5
        grid[32:35 , 59:67] = np.tile(nump3,2)
        # grid[33:34 ,59:67] = np.tile(nump3,2)
        grid2[32][59] = 5
        grid[32:35,77:85] = np.tile(nump3,2)
        # grid[33:34,77:85] = np.tile(nump3,2)
        grid2[32][77] = 5
        grid[35:38,68:76] = np.tile(nump3,2)
        # grid[36:37,68:76] = np.tile(nump3,2)
        grid2[35][68] = 5

class class20(Brick):
    
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump5 = self._lev20

        grid[17:20,50:58] = np.tile(nump5,2)
        # grid[18:19,50:58] = np.tile(nump5,2)
        grid2[17][50] = 20
        grid[17:20,86:94] = np.tile(nump5,2)
        # grid[18:19,86:94] = np.tile(nump5,2)
        grid2[17][86] = 20
        grid[23:26 , 59:67] = np.tile(nump5,2)
        # grid[24:25 ,59:67] = np.tile(nump2,2)
        grid2[23][59] = 20   

class create_struct(Brick):
        
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        level1 = class1(a,b,grid,grid2,placepower,rainbow)
        level2 = class2(a,b,grid,grid2,placepower,rainbow)
        level3 = class3(a,b,grid,grid2,placepower,rainbow)
        level5 = class5(a,b,grid,grid2,placepower,rainbow)
        level20 = class20(a,b,grid,grid2,placepower,rainbow)

class class12(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump4 = self._lev1


        grid[8:11,86:94] = np.tile(nump4,2)
        grid2[8][86] = 1
        grid[8:11 , 95:103] = np.tile(nump4,2)
        grid2[8][95] = 1
        placepower[8][95] = 2

        grid[11:14,41:49] = np.tile(nump4,2)
        grid2[11][41] = 1
        grid[14:17 , 59:67] = np.tile(nump4,2)
        grid2[14][59] = 1
        grid[14:17,68:76] = np.tile(nump4,2)
        grid2[14][68] = 1
        placepower[14][68] = 5
        grid[17:20,32:40] = np.tile(nump4,2)
        grid2[17][32] = 1
        rainbow[17][32] = 1
        grid[20:23 , 59:67] = np.tile(nump4,2)
        grid2[20][59] = 1
        placepower[20][59] = 4
        grid[20:23,104:112] = np.tile(nump4,2)
        grid2[20][104] = 1
        grid[26:29,50:58] = np.tile(nump4,2)
        grid2[26][50] = 1
        grid[26:29,68:76] = np.tile(nump4,2)
        grid2[26][68] = 1
        placepower[26][77] = 6

        grid[29:32,5:13] = np.tile(nump4,2)
        grid2[29][5] = 1
        placepower[29][5] = 1

        grid[29:32,14:22] = np.tile(nump4,2)
        grid2[29][14] = 1

        grid[29:32,23:31] = np.tile(nump4,2)
        grid2[29][23] = 1

        grid[29:32,32:40] = np.tile(nump4,2)
        grid2[29][32] = 1
        placepower[29][32] = 2

        grid[29:32,59:67] = np.tile(nump4,2)
        grid2[29][59] = 1

        # grid[29:32,68:76] = np.tile(nump4,2)
        # grid2[29][68] = 1

        grid[29:32,86:94] = np.tile(nump4,2)
        grid2[29][86] = 1
        placepower[29][86] = 1

        grid[29:32,104:112] = np.tile(nump4,2)
        grid2[29][104] = 1

        grid[29:32,113:121] = np.tile(nump4,2)
        grid2[29][113] = 1

        grid[29:32,122:130] = np.tile(nump4,2)
        grid2[29][122] = 1
        placepower[29][122] = 6

        grid[29:32,131:139] = np.tile(nump4,2)
        grid2[29][131] = 1


class class22(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump6 = self._lev2

        grid[8:11,5:13] = np.tile(nump6,2)
        grid2[8][5] = 2
        placepower[8][5] = 2
        grid[8:11,122:130] = np.tile(nump6,2)
        grid2[8][122] = 2
        placepower[8][122] = 1
        grid[11:14 , 59:67] = np.tile(nump6,2)
        grid2[11][59] = 2
        placepower[11][59] = 4
        grid[14:17 , 23:31] = np.tile(nump6,2)
        grid2[14][23] = 2
        grid[14:17 , 41:49] = np.tile(nump6,2)
        grid2[14][41] = 2
        placepower[14][41] = 5
        grid[14:17,104:112] = np.tile(nump6,2)
        grid2[14][104] = 2
        grid[14:17,113:121] = np.tile(nump6,2)
        grid2[14][113] = 2
        grid[17:20,77:85] = np.tile(nump6,2)
        grid2[17][77] = 2
        placepower[17][77] = 2
        grid[23:26 , 77:85] = np.tile(nump6,2)
        grid2[23][77] = 2
        rainbow[23][77] = 1
        grid[23:26,86:94] = np.tile(nump6,2)
        grid2[23][86] = 2
        placepower[23][86] = 1
        
        grid[23:26 , 5:13] = np.tile(nump6,2)
        grid2[23][5] = 2

        grid[23:26 , 14:22] = np.tile(nump6,2)
        grid2[23][14] = 2
        placepower[23][14] =1
        grid[23:26 , 32:40] = np.tile(nump6,2)
        grid2[23][32] = 2

        grid[23:26 , 41:49] = np.tile(nump6,2)
        grid2[23][41] = 2
        placepower[23][14] =2
        grid[23:26 , 50:58] = np.tile(nump6,2)
        grid2[23][50] = 2

        grid[23:26 , 59:67] = np.tile(nump6,2)
        grid2[23][59] = 2
        placepower[23][14] =6
        grid[23:26 , 95:103] = np.tile(nump6,2)
        grid2[23][95] = 2

        grid[23:26 , 104:112] = np.tile(nump6,2)
        grid2[23][104] = 2
        placepower[23][14] =1
        grid[23:26 , 122:130] = np.tile(nump6,2)
        grid2[23][122] = 2

        grid[23:26 , 131:139] = np.tile(nump6,2)
        grid2[23][131] = 2


class class32(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump2 = self._lev3

        grid[8:11,41:49] = np.tile(nump2,2)
        # grid[9:10,41:49] = np.tile(nump2,2)
        grid2[8][41] = 3
        grid[8:11 , 59:67] = np.tile(nump2,2)
        # grid[9:10 ,59:67] = np.tile(nump2,2)
        grid2[8][59] = 3
        grid[14:17,32:40] = np.tile(nump2,2)
        # grid[15:16,32:40] = np.tile(nump2,2)
        grid2[14][32] = 3
        placepower[14][32] = 1
        grid[14:17,77:85] = np.tile(nump2,2)
        # grid[15:16,77:85] = np.tile(nump2,2)
        grid2[14][77] = 3
        grid[14:17,122:130] = np.tile(nump2,2)
        # grid[15:16,122:130] = np.tile(nump2,2)
        grid2[14][122] = 3
        grid[17:20,5:13] = np.tile(nump2,2)
        # grid[18:19,5:13] = np.tile(nump2,2)
        grid2[17][5] = 3
        grid[17:20 , 59:67] = np.tile(nump2,2)
        # grid[18:19 ,59:67] = np.tile(nump2,2)
        grid2[17][59] = 3
        placepower[17][59] = 4
        grid[17:20 , 95:103] = np.tile(nump2,2)
        # grid[18:19 , 95:103] = np.tile(nump2,2)
        grid2[17][95] = 3
        placepower[17][95] = 7
        grid[17:20,113:121] = np.tile(nump2,2)
        # grid[18:19,113:121] = np.tile(nump2,2)
        grid2[17][113] = 3

        grid[17:20 , 14:22] = np.tile(nump2,2)
        grid[17:20 , 23:31] = np.tile(nump2,2)
        grid[17:20 , 41:49] = np.tile(nump2,2)
        grid[17:20 , 68:76] = np.tile(nump2,2)
        grid2[17][14] = 3
        grid2[17][23] = 3
        placepower[17][23] = 1
        grid2[17][41] = 3
        rainbow[17][41] = 1
        grid2[17][68] = 3
        placepower[17][68] = 1

        grid[17:20 , 104:112] = np.tile(nump2,2)
        grid2[17][104] = 3
        grid[17:20 , 122:130] = np.tile(nump2,2)
        placepower[17][122] = 6
        grid2[17][122] = 3
        grid[17:20 , 131:139] = np.tile(nump2,2)
        placepower[17][131] = 5
        grid2[17][131] = 3


        grid2[20][50] = 3
        grid[20:23,50:58] = np.tile(nump2,2)
        grid[23:26 , 23:31] = np.tile(nump2,2)
        # grid[24:25 , 23:31] = np.tile(nump2,2)
        grid2[23][23] = 3
        placepower[23][23] = 1
        grid[23:26,68:76] = np.tile(nump2,2)
        # grid[24:25,68:76] = np.tile(nump2,2)
        grid2[23][68] = 3
        placepower[23][68] = 6
        grid[23:26,113:121] = np.tile(nump2,2)
        # grid[24:25,113:121] = np.tile(nump2,2)
        grid2[23][113] = 3
        placepower[23][113] = 6
        grid[26:29,104:112] = np.tile(nump2,2)
        # grid[27:28,104:112] = np.tile(nump2,2)
        grid2[26][104] = 3
        grid[29:32,41:49] = np.tile(nump2,2)
        # grid[30:31,41:49] = np.tile(nump2,2)
        grid2[29][41] = 3
        placepower[29][41] = 4
        grid[29:32,77:85] = np.tile(nump2,2)
        # grid[30:31,77:85] = np.tile(nump2,2)
        grid2[29][77] = 3
        grid[29:32 , 95:103] = np.tile(nump2,2)
        # grid[30:31 , 95:103] = np.tile(nump2,2)
        grid2[29][95] = 3
        placepower[29][95] = 6
        # grid[32:35,68:76] = np.tile(nump2,2)
        # grid[33:34,68:76] = np.tile(nump2,2)
        # grid2[32][68] = 3
        # grid[35:38 , 59:67] = np.tile(nump2,2)
        # # grid[36:37 ,59:67] = np.tile(nump2,2)
        # grid2[35][59] = 3
        # placepower[35][59] = 4
        
class class52(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump3 = self._lev5
        
        grid[20:23 , 23:31] = np.tile(nump3,2)
        grid2[20][23] = 5
        grid[26:29,41:49] = np.tile(nump3,2)
        # grid[27:28,41:49] = np.tile(nump3,2)
        grid2[26][41] = 5
        grid[26:29 , 95:103] = np.tile(nump3,2)
        # grid[27:28 , 95:103] = np.tile(nump3,2)
        grid2[26][95] = 5

class class202(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        nump5 = self._lev20

        grid[17:20,50:58] = np.tile(nump5,2)
        # grid[18:19,50:58] = np.tile(nump5,2)
        grid2[17][50] = 20
        grid[17:20,86:94] = np.tile(nump5,2)
        # grid[18:19,86:94] = np.tile(nump5,2)
        grid2[17][86] = 20

class create_struct2(Brick):
    def __init__(self , a ,b , grid , grid2 , placepower,rainbow):
        super().__init__(a,b)
        level1 = class12(a,b,grid,grid2,placepower,rainbow)
        level2 = class22(a,b,grid,grid2,placepower,rainbow)
        level3 = class32(a,b,grid,grid2,placepower,rainbow)
        level5 = class52(a,b,grid,grid2,placepower,rainbow)
        level20 = class202(a,b,grid,grid2,placepower,rainbow)

class class203(Brick):
    def __init__(self , a ,b , grid , grid2):
        super().__init__(a,b)
        nump5 = self._lev20

        grid[29:32,30:38] = np.tile(nump5,2)
        # grid[18:19,50:58] = np.tile(nump5,2)
        grid2[29][30] = 20
        grid[29:32,104:112] = np.tile(nump5,2)
        # grid[18:19,86:94] = np.tile(nump5,2)
        grid2[29][104] = 20
        grid[33:36,67:75] = np.tile(nump5,2)
        # grid[18:19,86:94] = np.tile(nump5,2)
        grid2[33][67] = 20

class class13(Brick):
    def __init__(self , a ,b , grid , grid2):
        super().__init__(a,b)
        nump5 = self._lev1

        grid[25:28,5:13] = np.tile(nump5,2)
        grid[25:28,14:22] = np.tile(nump5,2)
        grid[25:28,23:31] = np.tile(nump5,2)
        grid[25:28,32:40] = np.tile(nump5,2)
        grid[25:28,41:49] = np.tile(nump5,2)
        grid[25:28,50:58] = np.tile(nump5,2)
        grid[25:28,59:67] = np.tile(nump5,2)
        grid[25:28,68:76] = np.tile(nump5,2)
        grid[25:28,77:85] = np.tile(nump5,2)
        grid[25:28,86:94] = np.tile(nump5,2)
        grid[25:28,95:103] = np.tile(nump5,2)
        grid[25:28,104:112] = np.tile(nump5,2)
        grid[25:28,113:121] = np.tile(nump5,2)
        grid[25:28,122:130] = np.tile(nump5,2)
        grid[25:28,131:139] = np.tile(nump5,2)
        grid[25:28,140:148] = np.tile(nump5,2)

        grid2[25][5] = 1
        grid2[25][14] = 1
        grid2[25][23] = 1
        grid2[25][32] = 1
        grid2[25][41] = 1
        grid2[25][50] = 1
        grid2[25][59] = 1
        grid2[25][68] = 1
        grid2[25][77] = 1
        grid2[25][86] = 1
        grid2[25][95] = 1
        grid2[25][104] = 1
        grid2[25][113] = 1
        grid2[25][122] = 1
        grid2[25][131] = 1
        grid2[25][140] = 1


class create_struct3(Brick):
    def __init__(self , a ,b , grid , grid2):
        super().__init__(a,b)
        level20 = class203(a,b,grid,grid2)



class update_struct(Brick):

    def __init__(self , width , height , grid , grid2):
        super().__init__(width,height)
        for i in range (height):
            for j in range (width):
                if grid2[i][j] != ' ':
                    # print(grid2[i][j])
                    # time.sleep(1)
                    if grid2[i][j] == "20":
                        grid[i:i+3,j:j+8] = np.tile(self._lev20 , 2)
                    if grid2[i][j] == "5" :
                        grid[i:i+3,j:j+8] = np.tile(self._lev5 , 2)
                    if grid2[i][j] == "3" :
                        grid[i:i+3,j:j+8] = np.tile(self._lev3 , 2)
                    if grid2[i][j] == "2" :
                        grid[i:i+3,j:j+8] = np.tile(self._lev2 , 2)
                    if grid2[i][j] == "1" :
                        grid[i:i+3,j:j+8] = np.tile(self._lev1 , 2)    



def collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy):
    flag  = 1
    st1 = j
    st2 = k
    queue1 = []
    queue2 = []
    queue1.append(j)
    queue2.append(k)
    while flag == 1:
        if len(queue1) == 0:
            break
        st1 = queue1.pop(0)
        st2 = queue2.pop(0)
        grid2[st1][st2]= ' '
        grid[st1:st1+3,st2:st2+8]=" "
        score = brick.get_score()
        score += 2
        brick.update_score(score)

        if placepower[st1][st2] != " ":
            powergrid[st1][st2] = placepower[st1][st2]
            speedx[st1][st2] = 0
            speedy[st1][st2] = 1
            create_powerup(st1,st2,placepower[st1][st2],grid)
            placepower[st1][st2] = " "
        
        if placepower[st1-3][st2] != " ":
            powergrid[st1-3][st2] = placepower[st1-3][st2]
            speedx[st1-3][st2] = 0
            speedy[st1-3][st2] = 1
            create_powerup(st1-3,st2,placepower[st1-3][st2],grid)
            placepower[st1-3][st2] = " "
        
        if placepower[st1+3][st2] != " ":
            powergrid[st1+3][st2] = placepower[st1+3][st2]
            speedx[st1+3][st2] = 0
            speedy[st1+3][st2] = 1
            create_powerup(st1+3,st2,placepower[st1+3][st2],grid)
            placepower[st1+3][st2] = " "
        
        if placepower[st1][st2+9] != " ":
            powergrid[st1][st2+9] = placepower[st1][st2+9]
            speedx[st1][st2+9] = 0
            speedy[st1][st2+9] = 1
            create_powerup(st1,st2+9,placepower[st1][st2+9],grid)
            placepower[st1][st2+9] = " "

        if placepower[st1-3][st2+9] != " ":
            powergrid[st1-3][st2+9] = placepower[st1-3][st2+9]
            speedx[st1-3][st2+9] = 0
            speedy[st1-3][st2+9] = 1
            create_powerup(st1-3,st2+9,placepower[st1-3][st2+9],grid)
            placepower[st1-3][st2+9] = " "

        if placepower[st1+3][st2+9] != " ":
            powergrid[st1+3][st2+9] = placepower[st1+3][st2+9]
            speedx[st1+3][st2+9] = 0
            speedy[st1+3][st2+9] = 1
            create_powerup(st1+3,st2+9,placepower[st1+3][st2+9],grid)
            placepower[st1+3][st2+9] = " "

        if placepower[st1][st2-9] != " ":
            powergrid[st1][st2-9] = placepower[st1][st2-9]
            speedx[st1][st2-9] = 0
            speedy[st1][st2-9] = 1
            create_powerup(st1,st2-9,placepower[st1][st2-9],grid)
            placepower[st1][st2-9] = " "
        
        if placepower[st1-3][st2-9] != " ":
            powergrid[st1-3][st2-9] = placepower[st1-3][st2-9]
            speedx[st1-3][st2-9] = 0
            speedy[st1-3][st2-9] = 1
            create_powerup(st1-3,st2-9,placepower[st1-3][st2-9],grid)
            placepower[st1-3][st2-9] = " "

        if placepower[st1+3][st2-9] != " ":
            powergrid[st1+3][st2+9] = placepower[st1+3][st2+9]
            speedx[st1+3][st2+9] = 0
            speedy[st1+3][st2+9] = 1
            create_powerup(st1+3,st2+9,placepower[st1+3][st2+9],grid)
            placepower[st1+3][st2+9] = " "
        
        if grid2[st1-3][st2] == "5":
            queue1.append(st1-3)
            queue2.append(st2)
        if grid2[st1+3][st2] == "5":
            queue1.append(st1+3)
            queue2.append(st2)
        if grid2[st1][st2] == "5":
            queue1.append(st1)
            queue2.append(st2)
        if grid2[st1][st2+9] == "5":
            queue1.append(st1)
            queue2.append(st2+9)
        if grid2[st1-3][st2+9] == "5":
            queue1.append(st1-3)
            queue2.append(st2+9)
        if grid2[st1+3][st2+9] == "5":
            queue1.append(st1+3)
            queue2.append(st2+9)
        if grid2[st1-3][st2-9] == "5":
            queue1.append(st1-3)
            queue2.append(st2-9)
        if grid2[st1][st2-9] == "5":
            queue1.append(st1)
            queue2.append(st2-9)
        if grid2[st1+3][st2-9] == "5":
            queue1.append(st1+3)
            queue2.append(st2-9)
        
        grid2[st1-3][st2] = " "
        grid2[st1+3][st2] = " "
        grid2[st1][st2] = " "
        grid2[st1][st2+9] = " "
        grid2[st1-3][st2+9] = " "
        grid2[st1+3][st2+9] = " "
        grid2[st1-3][st2-9] = " "
        grid2[st1][st2-9] = " "
        grid2[st1+3][st2-9] = " "

        grid[st1-3:st1,st2:st2+8] = " "
        grid[st1+3:st1+6,st2:st2+8] = " "
        grid[st1:st1+3,st2:st2+8] = " "
        grid[st1:st1+3,st2+9:st2+17] = " "
        grid[st1-3:st1,st2+9:st2+17] = " "
        grid[st1+3:st1+6,st2+9:st2+17] = " "
        grid[st1-3:st1,st2-9:st2+1] = " "
        grid[st1:st1+3,st2-9:st2+1] = " "
        grid[st1+3:st1+6,st2-9:st2+1] = " "
class brick_ball(Brick):

    def __init__ (self , a , b):
        super().__init__(a,b)

    def checkcoll(self , a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,boss,present_screen,speedx,speedy):
        ball_inst = Scene()
        sx = c-a
        sy = d-b
        b = -b
        d = -d
        n1 = (c-a)/5
        n2 = (d-b)/5
        p = 1
        # print("%d %d %d %d",a,b,c,d)
        # print(c)
        # print(b)
        # print(d)
        if c!=a:
            p=1
            slope = (d-b)/(c-a)
            intercept = b - slope*a
        else:
            p=0
            slope =1
            intercept = - c
        done = 0
        for i in range(5):
            a = a+n1
            b = b+n2
            if done ==1 and activate[5] == 0:
                break

            for j in range (height):
                if done == 1 and activate[5] == 0:
                    break
                for k in range (width):
                    if done == 1 and activate[5] == 0:
                        break
                    if grid2[j][k]!=" ":
                        # if present_screen!=3:
                        y1 = -j
                        y2 = -j-3
                        x1 = k
                        x2 = k+8
                        # else:
                        #     y1 = -j
                        #     y2 = -j-1
                        #     x1 = k
                        #     x2 = k+1

                        if n1 >=0 and n2 >=0 and a+1>=x1 and a<=x2 and b>=y2 and b<=y1:
                            os.system("aplay sounds/sound_collision_brick.wav -q &")
                            if activate[7]!=0:
                                grid2[j][k] = 5
                            if activate[5] != 0:
                                if grid2[j][k] == "5":
                                    collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy)
                                else:
                                    grid2[j][k]= ' '
                                    grid[j:j+3,k:k+8]=" "
                                    score = brick.get_score()
                                    score += 2
                                    brick.update_score(score)
                    
                                    if placepower[j][k] != " ":
                                        powergrid[j][k] = placepower[j][k]
                                        speedx[j][k] = sx
                                        speedy[j][k] = sy
                                        create_powerup(j,k,placepower[j][k],grid)
                                continue
                            done=1
                            # print("down left")
                            # print(x1)
                            # print(y1)
                            
                            num1 = p*y1 - slope*x1 - intercept
                            num2 = p*y2 - slope*x1 - intercept
                            # print(slope)
                            # print(intercept)
                            # print(num1)
                            # print(num2)
                            # time.sleep(2)
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_left(x1-1,b,grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_down(a,y2,grid,brd)
                        
                        if n1 >=0 and n2 <= 0 and a+1>=x1 and a<=x2 and b-1<=y1 and b>=y2:
                            os.system("aplay sounds/sound_collision_brick.wav -q &")
                            if activate[7]!=0:
                                grid2[j][k] = 5
                            if activate[5] != 0:
                                if grid2[j][k] == "5":
                                    collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy)
                                else:
                                    grid2[j][k]= ' '
                                    grid[j:j+3,k:k+8]=" "
                                    score = brick.get_score()
                                    score += 2
                                    brick.update_score(score)
                    
                                    if placepower[j][k] != " ":
                                        powergrid[j][k] = placepower[j][k]
                                        speedx[j][k] = sx
                                        speedy[j][k] = sy
                                        create_powerup(j,k,placepower[j][k],grid)
                                continue
                            done=1
                            # print("up left")
                            num1 = p*y1 - slope*x1 - intercept
                            num2 = p*y2 - slope*x1 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_left(x1-1,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_up((int)(a),y1-1,grid,brd)
                        
                        if n1 <= 0 and n2 >=0 and a>=x1 and a<=x2 and b<=y1 and b>=y2:
                            os.system("aplay sounds/sound_collision_brick.wav -q &")
                            if activate[7]!=0:
                                grid2[j][k] = 5
                            if activate[5] != 0:
                                if grid2[j][k] == "5":
                                    collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy)
                                else:
                                    grid2[j][k]= ' '
                                    grid[j:j+3,k:k+8]=" "
                                    score = brick.get_score()
                                    score += 2
                                    brick.update_score(score)
                    
                                    if placepower[j][k] != " ":
                                        powergrid[j][k] = placepower[j][k]
                                        speedx[j][k] = sx
                                        speedy[j][k] = sy
                                        create_powerup(j,k,placepower[j][k],grid)
                                continue
                            done=1
                            # print("down right")
                            num1 = p*y1 - slope*x2 - intercept
                            num2 = p*y2 - slope*x2 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_right(x2,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_down((int)(a),y2,grid,brd)

                        if n1 <= 0 and n2 <= 0 and a>=x1 and a<=x2 and b-1<=y1 and b>=y2:
                            os.system("aplay sounds/sound_collision_brick.wav -q &")
                            if activate[7]!=0:
                                grid2[j][k] = 5
                            if activate[5] != 0:
                                if grid2[j][k] == "5":
                                    collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy)
                                else:
                                    grid2[j][k]= ' '
                                    grid[j:j+3,k:k+8]=" "
                                    score = brick.get_score()
                                    score += 2
                                    brick.update_score(score)
                    
                                    if placepower[j][k] != " ":
                                        powergrid[j][k] = placepower[j][k]
                                        speedx[j][k] = sx
                                        speedy[j][k] = sy
                                        create_powerup(j,k,placepower[j][k],grid)
                                continue
                            done=1
                            # print("up right")
                            num1 = p*y1 - slope*x2 - intercept
                            num2 = p*y2 - slope*x2 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_right(x2,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_up((int)(a),y1-1,grid,brd)

                    if done == 1:
                        
                        # print("%d %d",j,k)
                        # print(grid2[j][k])
                        # time.sleep(2)

                        if grid2[j][k] == "1":
                            score = brick.get_score()
                            score += 2
                            rainbow[j][k] = " "
                            brick.update_score(score)
                            grid2[j][k]= ' '
                            grid[j:j+3,k:k+8]=" "
                            if placepower[j][k] != " ":
                                powergrid[j][k] = placepower[j][k]
                                speedx[j][k] = sx
                                speedy[j][k] = sy
                                create_powerup(j,k,placepower[j][k],grid)
                                placepower[j][k] = " "


                        elif grid2[j][k] == "2":
                            score = brick.get_score()
                            score += 1
                            rainbow[j][k]=" "
                            brick.update_score(score)
                            grid2[j][k]=1
                            grid[j:j+3,k:k+8]=" "
                            grid[j:j+3,k:k+8]= np.tile(self._lev1 , 2)

                        elif grid2[j][k] == "3":
                            score = brick.get_score()
                            score += 1
                            rainbow[j][k] = " "
                            brick.update_score(score)
                            grid2[j][k]=2
                            grid[j:j+3,k:k+8]=" "
                            grid[j:j+3,k:k+8]= np.tile(self._lev2 , 2)

                        elif grid2[j][k] == "5":
                            collide_five(j,k,a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,sx,sy,speedx,speedy)                      

        update_struct(width,height,grid,grid2)

    def checkcoll2(self , a ,b ,c , d , grid2 , height , width , grid , brd , placepower,powergrid,activate,brick,rainbow,boss,present_screen):     
        ball_inst = Scene()
        b = -b
        d = -d
        sx = c-a
        sy = d-b
        n1 = (c-a)/10
        n2 = (d-b)/10
        p = 1
        # print("%d %d %d %d",a,b,c,d)
        # print(c)
        # print(b)
        # print(d)
        if c!=a:
            p=1
            slope = (d-b)/(c-a)
            intercept = b - slope*a
        else:
            p=0
            slope =1
            intercept = - c
        done = 0
        for i in range(5):
            a = a+n1
            b = b+n2
            if done ==1 and activate[5] == 0:
                break

            for j in range (height):
                if done == 1 and activate[5] == 0:
                    break
                for k in range (width):
                    if done == 1 and activate[5] == 0:
                        break
                    if grid2[j][k]!=" ":
                        # if present_screen!=3:
                        y1 = -j
                        y2 = -j-1
                        x1 = k
                        x2 = k+1
                        # else:
                        #     y1 = -j
                        #     y2 = -j-1
                        #     x1 = k
                        #     x2 = k+1

                        if n1 >=0 and n2 >=0 and a+2>=x1 and a<=x2 and b>=y2 and b<=y1:
                            os.system("aplay sounds/sound_collision_brick.wav -q &")
                            
                            done=1
                            # print("down left")
                            # time.sleep(2)
                            # print(x1)
                            # print(y1)
                            
                            num1 = p*y1 - slope*x1 - intercept
                            num2 = p*y2 - slope*x1 - intercept
                            # print(slope)
                            # print(intercept)
                            # print(num1)
                            # print(num2)
                            # time.sleep(2)
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_left(x1-1,b,grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_down(a,y2,grid,brd)
                        
                        if n1 >=0 and n2 <= 0 and a+1>=x1 and a<=x2 and b-1<=y1 and b>=y2:
                            
                            done=1
                            # print("up left")
                            # time.sleep(2)
                            num1 = p*y1 - slope*x1 - intercept
                            num2 = p*y2 - slope*x1 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_left(x1-1,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_up((int)(a),y1-1,grid,brd)
                        
                        if n1 <= 0 and n2 >=0 and a-1>=x1 and a-1<=x2 and b<=y1 and b>=y2:
                            
                            done=1
                            # print("down right")
                            # time.sleep(2)
                            num1 = p*y1 - slope*x2 - intercept
                            num2 = p*y2 - slope*x2 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_right(x2,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_down((int)(a),y2,grid,brd)

                        if n1 <= 0 and n2 <= 0 and a-1>=x1 and a-1<=x2 and b-1<=y1 and b>=y2:
                            
                            done=1
                            # print("up right")
                            # time.sleep(2)
                            num1 = p*y1 - slope*x2 - intercept
                            num2 = p*y2 - slope*x2 - intercept
                            num1 = num1*num2
                            b = -b
                            y1 = -y1
                            y2 = -y2
                            if num1 < 0:
                                num3 = (int)(b)
                                num4 = num3+1
                                if b-num3 <= num4-b:
                                    b=num3
                                else:
                                    b=num4
                                ball_inst.update_right(x2,(int)(b),grid,brd)
                            else:
                                num3 = (int)(a)
                                num4 = num3+1
                                if a-num3 <= num4-a:
                                    a=num3
                                else:
                                    a=num4
                                ball_inst.update_up((int)(a),y1-1,grid,brd)

                    if done == 1:
                        
                        # print("%d %d",j,k)
                        # print(grid2[j][k])
                        # time.sleep(2)
                        boss._lives-=1
        
        # update_struct(width,height,grid,grid2)
        
                        
                