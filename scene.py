import numpy as np
from colorama import Fore, init,Back, Style
import random
import time
import os

class Scene:

    def __init__(self):
        self.stick = 1
        self.lives = 7
    
    def get_lives(self):
        return self.lives

    def create_board(self, a , b , grid):

        self.__board = np.array([Fore.LIGHTBLACK_EX + Back.YELLOW+'-'+Style.RESET_ALL])
        self.__size = 8
        self.__x1 = (int)(a/2)-self.__size
        self.__x2 = (int)(a/2)+self.__size
        grid[b-3:b-2,self.__x1:self.__x2] = np.tile(self.__board,16)

    def create_ball(self , a , b, grid):

        self.__ball = np.array([Fore.LIGHTBLACK_EX + Back.WHITE+'O'+Style.RESET_ALL])
        num1 = random.randint(self.__x1,self.__x2)
        self.__ball_y = -1
        self.__ball_x = num1 - self.__x1 - self.__size
        self.__ball_x = (int)(self.__ball_x/3)
        # print(self.__ball_y)
        # print(self.__ball_x)
        # time.sleep(2)
        self.__ball_posx = num1
        self.__ball_posy = b-4 
        grid[b-4:b-3,num1:num1+1] = np.tile(self.__ball,1)

    def board_moved(self , a , b , grid):

        if self.stick == 1:
            grid[self.__ball_posy:self.__ball_posy+1 , self.__ball_posx : self.__ball_posx+1] = " "

        grid[b-3:b-2,self.__x1:self.__x2] = " "
        if self.__x2 + 4 >= a-2:
            self.__x1 += a-2 - self.__x2
            self.__x2 = a-2
            if self.stick == 1:
                self.__ball_posx += a-2 - self.__x2
                grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1)
        else:
            self.__x1 = self.__x1 + 4
            self.__x2 = self.__x2 + 4
            if self.stick == 1:
                self.__ball_posx += 4
                grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1)
        grid[b-3:b-2,self.__x1:self.__x2] = self.__board
        # grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1)
    
    def board_movea(self , a , b , grid):

        if self.stick == 1:
            grid[self.__ball_posy:self.__ball_posy+1 , self.__ball_posx : self.__ball_posx+1] = " "

        grid[b-3:b-2,self.__x1:self.__x2] = " "
        if self.__x1 - 4 <= 2:
            self.__x2 = self.__x2 - (self.__x1 - 2)
            self.__x1 = 2
            if self.stick == 1:
                self.__ball_posx = self.__ball_posx - self.__x1 + 2
                grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1)
        else:
            self.__x1 = self.__x1 - 4
            self.__x2 = self.__x2 - 4
            if self.stick == 1:
                self.__ball_posx = self.__ball_posx - 4
                grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1)

        grid[b-3:b-2,self.__x1:self.__x2] = self.__board
        # grid[b-4:b-3,self.__ball_posx:self.__ball_posx+1] = np.tile(self.__ball,1) 

    def ball_move(self , a , b , grid , activate):
        self.__old_x  = self.__ball_posx
        self.__old_y = self.__ball_posy
        grid[self.__ball_posy:self.__ball_posy+1 , self.__ball_posx : self.__ball_posx+1] = " "
        self.__ball_posx = self.__ball_posx + self.__ball_x
        self.__ball_posy = self.__ball_posy + self.__ball_y
        if self.__ball_x == 0 and self.__ball_y == 0:
            self.__ball_x = 1
            self.__ball_y = 1

        if self.__ball_posx > a-3:
            os.system("aplay sounds/sound_paddle.wav -q &")
            num1 = self.__ball_posx - a + 2
            self.__ball_posx = a-3 - num1
            self.__ball_x = -self.__ball_x

        elif self.__ball_posx < 3:
            os.system("aplay sounds/sound_paddle.wav -q &")
            num1 = 2 - self.__ball_posx 
            self.__ball_posx = 2 + num1
            self.__ball_x = -self.__ball_x

        if self.__ball_posy < 7:
            os.system("aplay sounds/sound_paddle.wav -q &")
            num1 = 6 - self.__ball_posy 
            self.__ball_posy = 6 + num1
            self.__ball_y = -self.__ball_y

        elif self.__ball_posy > b-5:

            if grid[b-3:b-2 , self.__ball_posx : self.__ball_posx+1] != " ":
                os.system("aplay sounds/sound_paddle.wav -q &")
                if activate[6] != 0:
                    
                    if self.__ball_x != 0:
                        slope = self.__ball_y / self.__ball_x
                        intercept = self.__ball_posy - slope*self.__ball_posx
                        self.__ball_posx = (int)((b-3 - intercept) / slope)
                    self.__ball_posy = b-4
                    self.__ball_y = -self.__ball_y
                    self.__ball_x = (int)((self.__ball_posx - self.__x1 - self.__size)/3)
                    self.stick = 1
                else:
                    num1 = self.__ball_posy - b + 4
                    self.__ball_posy = b-4 - num1
                    self.__ball_y = -self.__ball_y
                    self.__ball_x = self.__ball_x + (int)((self.__ball_posx - self.__x1 - self.__size)/3)

            else: 
                os.system("aplay sounds/sound_out.wav -q &")
                # print(self.__x1)
                # print(self.__x2)
                # time.sleep(2) 
                num1 = random.randint(self.__x1,self.__x2)
                self.__ball_y = -1
                self.__ball_x = num1 - self.__x1 - self.__size
                self.__ball_x = (int)(self.__ball_x/3)
                self.__ball_posx = num1
                self.__ball_posy = b-4 
                grid[b-4:b-3,num1:num1+1] = np.tile(self.__ball,1)

                # for i in range(10):
                #     activate[i] = -20
                self.stick = 1
                self.lives -= 1

        
        grid[self.__ball_posy:self.__ball_posy+1 , self.__ball_posx : self.__ball_posx+1] = np.tile(self.__ball,1)

    def get_old_x(self):

        return self.__old_x

    def get_old_y(self):
    
        return self.__old_y

    def get_new_x(self):
    
        return self.__ball_posx

    def get_new_y(self):
    
        return self.__ball_posy
    
    def get_middle(self):
        return (int)((self.__x1+self.__x2)/2)

    def update_left(self , a , b , grid , brd):
        # print("in update left")
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = " "
        brd.__ball_posx = a
        brd.__ball_posy = b
        brd.__ball_x = -brd.__ball_x
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = np.tile(brd.__ball,1)

    def update_down(self , a , b , grid , brd):
        # print("in update down")
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = " "
        brd.__ball_posx = a
        brd.__ball_posy = b
        brd.__ball_y = -brd.__ball_y
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = np.tile(brd.__ball,1)

    def update_right(self , a , b , grid , brd):
        # print("in update right")
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = " "
        brd.__ball_posx = a
        brd.__ball_posy = b
        brd.__ball_x = -brd.__ball_x
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = np.tile(brd.__ball,1)
    
    def update_up(self , a , b , grid , brd):
        # print(brd.__ball_posx)
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = " "
        brd.__ball_posx = a
        brd.__ball_posy = b
        brd.__ball_y = -brd.__ball_y
        grid[brd.__ball_posy:brd.__ball_posy+1 , brd.__ball_posx : brd.__ball_posx+1] = np.tile(brd.__ball,1)

    def normal_boardlength(self,width,height,grid):

        t1 = self.__x1
        t2 = self.__x2


        # print(t1)
        # print(t2)
        # time.sleep(2)
        # if t2 - t1 == 16:
        #     return 

        grid[height-3:height-2,t1:t2] = " "
        self.__size = 8 
        if t2 - t1 > 16:
            t2-=4
            t1+=4
            self.__x1 = t1
            self.__x2 = t2
            grid[height-3:height-2,self.__x1:self.__x2] = np.tile(self.__board,16)

        elif t2 - t1 < 16:
            if t1 < 4:
                t2 += 4 - t1 - 2
                t1 = 2
            else:
                t2+=2
                t1-=2
            self.__x1 = t1
            self.__x2 = t2
            self.__size = 16
            grid[height-3:height-2,self.__x1:self.__x2] = np.tile(self.__board,16)
        
        if self.__ball_posy == height - 4:
            grid[height-4:height-3,self.__ball_posx:self.__ball_posx+1] = " "
            num1 = random.randint(self.__x1,self.__x2)
            self.__ball_y = -1
            self.__ball_x = num1 - self.__x1 - self.__size
            self.__ball_x = (int)(self.__ball_x/3)
            # print(self.__ball_y)
            # print(self.__ball_x)
            # time.sleep(2)
            self.__ball_posx = num1
            self.__ball_posy = width-4 
            grid[height-4:height-3,num1:num1+1] = np.tile(self.__ball,1)

    def normal_stick(self):
        self.stick = 0

    def normal_speed(self):
        if self.__ball_x < 0:
            self.__ball_x +=1
        elif self.__ball_x > 0:
            self.__ball_x -=1

        if self.__ball_y < 0:
            self.__ball_y += 1
        elif self.__ball_y > 0:
            self.__ball_y -= 1
    
    def increase_length(self,width,height,grid):
        t1 = self.__x1
        t2 = self.__x2
        # print(self.__x1)
        # print(self.__x2)
        # time.sleep(1)

        grid[height-3:height-2,t1:t2] = " "

        if t1 < 6:
            t2 += 8 - t1 + 2
            t1 = 2
        else:
            t2+=4
            t1-=4
        self.__x1 = t1
        self.__x2 = t2
        self.__size = 12

        # print(self.__x1)
        # print(self.__x2)
        # time.sleep(2)
        grid[height-3:height-2,self.__x1:self.__x2] = np.tile(self.__board,24)
    
    def decrease_length(self,width,height,grid):
        t1 = self.__x1
        t2 = self.__x2

        grid[height-3:height-2,t1:t2] = " "
        self.__size = 6

        t1+=2
        t2-=2
        self.__x1 = t1
        self.__x2 = t2
        grid[height-3:height-2,self.__x1:self.__x2] = np.tile(self.__board,12)

    def increase_speed(self):
        if self.__ball_x < 0:
            self.__ball_x -=1
        elif self.__ball_x > 0:
            self.__ball_x +=1

        if self.__ball_y < 0:
            self.__ball_y -= 1
        elif self.__ball_y > 0:
            self.__ball_y += 1

    




