import numpy as np
from colorama import Fore, init, Back, Style

class Screen:
    
    def create_screen(self , a , b):

        self.__rows = b
        self.__columns = a
        self.__grid = np.zeros((b,a),dtype='<U20')
        self.__grid[:] = ' '
        self.__grid4 = np.zeros((b,a),dtype='<U20')
        self.__grid4[:] = ' '
        self.__grid6 = np.zeros((b,a),dtype='<U20')
        self.__grid6[:] = ' '

    def show_screen(self,grid):

        for i in range (self.__rows):
            for j in range (self.__columns):
                # print(self.__grid[i][j],end=' ')
                print(grid[i][j], end='')
            print()

    def create_border(self , a , b):
        
        self.__bordertop = np.array([Fore.LIGHTCYAN_EX + Back.CYAN+'-'+Style.RESET_ALL])
        self.__grid[4:6,0:a] = np.tile(self.__bordertop , a)
        self.__grid4[4:6,0:a] = np.tile(self.__bordertop , a)
        self.__grid6[4:6,0:a] = np.tile(self.__bordertop , a)

        self.__borderunder = np.array([Fore.LIGHTCYAN_EX+ Back.CYAN+'-'+Style.RESET_ALL])
        self.__grid[b-2:b,0:a] = np.tile(self.__borderunder , a)
        self.__grid4[b-2:b,0:a] = np.tile(self.__borderunder , a)
        self.__grid6[b-2:b,0:a] = np.tile(self.__borderunder , a)

        self.__bordertop = np.array([Fore.LIGHTCYAN_EX + Back.CYAN+'||'+Style.RESET_ALL])
        self.__grid[4:b,a-2:a] = np.tile(self.__bordertop , 1)
        self.__grid4[4:b,a-2:a] = np.tile(self.__bordertop , 1)
        self.__grid6[4:b,a-2:a] = np.tile(self.__bordertop , 1)

        self.__bordertop = np.array([Fore.LIGHTCYAN_EX+Back.CYAN+'||'+Style.RESET_ALL])
        self.__grid[4:b,0:2] = np.tile(self.__bordertop , 1)
        self.__grid4[4:b,0:2] = np.tile(self.__bordertop , 1)
        self.__grid6[4:b,0:2] = np.tile(self.__bordertop , 1)

    def get_grid(self):
        return self.__grid
    
    def get_grid2(self):
        return self.__grid4

    def get_grid3(self):
        return self.__grid6
        



