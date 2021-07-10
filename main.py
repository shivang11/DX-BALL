import os
import time
import signal
import random
from colorama import Fore, init,Back, Style

from inputtake import *
from brick_structure import *
from screen import *
from scene import *
from powerup import *
from boss import *

# os.system("aplay -q sounds/theme.wav &")
def show_message(msg):

    if msg == "Game over":
        print("\t\t\t _______  _______  __   __  _______    _______  __   __  _______  ______\n" +  
              "\t\t\t|       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |\n"  +
              "\t\t\t|    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||\n"  +
              "\t\t\t|   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_\n" +
              "\t\t\t|   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |\n"+
              "\t\t\t|   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |\n"+
              "\t\t\t|_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|\n")
        os.system("aplay funstuff/gameover.wav -q &")

    elif msg == "You Won":
        print( "\t\t\t __   __  ___   _______  _______  _______  ______    __   __\n" +   
               "\t\t\t|  | |  ||   | |       ||       ||       ||    _ |  |  | |  |\n" +  
               "\t\t\t|  |_|  ||   | |      _||_     _||   _   ||   | ||  |  |_|  |\n" +  
               "\t\t\t|       ||   | |     |    |   |  |  | |  ||   |_||_ |       |\n" +  
               "\t\t\t|       ||   | |     |    |   |  |  |_|  ||    __  ||_     _|\n" +  
               "\t\t\t |     | |   | |     |_   |   |  |       ||   |  | |  |   |\n" +    
               "\t\t\t  |___|  |___| |_______|  |___|  |_______||___|  |_|  |___|\n" )
        
        os.system("aplay sounds/sound_victory.wav -q &")

prtime = time.time()
starttime = time.time()
bricktime = time.time()
rainbowtime = time.time()
bosstime = time.time()

width = 150
height = 50
present_screen = 1

gm_back = Screen()
gm_back.create_screen(width,height)
gm_back.create_border(width,height)

boss = Boss(width,height)

brd = Scene()
brd.create_board(width,height,gm_back.get_grid())
brd.create_ball(width,height,gm_back.get_grid())

brick = Brick(width,height)
brick.create_grid(width,height)
brick.create_rainbow_grid(width,height)
brick_structure = create_struct(width,height,gm_back.get_grid(),brick.get_grid(),brick.get_placepower(),brick.get_rainbow())
brick_structure2 = create_struct2(width,height,gm_back.get_grid2(),brick.get_grid2(),brick.get_placepower2(),brick.get_rainbow2())
brick_structure3 = create_struct3(width,height,gm_back.get_grid3(),brick.get_grid3())


ball_brickcoll = brick_ball(width,height)

powerup = Powerup(width,height)
powerup.create_struct(width,height)
os.system("clear")

# print(Back.BLACK)
# for i in range(50):
#     for j in range(70):
#         print(' ',end='')
#     print()

print(Back.MAGENTA)
for i in range(1):
    for j in range(width):
        print(' ', end='')
    print()
print(Back.RESET)

grid = np.zeros((height,width),dtype='<U20')
grid[:] = ' '

grid8 = np.zeros((height,width),dtype='<U20')
grid8[:] = ' '

powergrid = np.zeros((height,width),dtype='<U20')
powergrid[:] = ' '

placepower = np.zeros((height,width),dtype='<U20')
placepower[:] = ' '

rainbow = np.zeros((height,width),dtype='<U20')
rainbow[:] = ' '

activate = np.zeros(10 , dtype=int)

grid = gm_back.get_grid()
powergrid = powerup.get_powergrid()
placepower = brick.get_placepower()
activate = powerup.get_activate()
grid2 = brick.get_grid()
grid8 = boss.get_boss_grid()
rainbow = brick.get_rainbow()
done = 0
cnt1=0
cnt2=0

while(True):
    
    if time.time() - prtime >= 0.15:
        prtime = time.time()

        text = input_to()
        # print(text)
        
        if text == "2":
            prtime = time.time()
            starttime = time.time()
            present_screen = 2
            rainbow = brick.get_rainbow2()
            grid = gm_back.get_grid2()
            grid2 = brick.get_grid2()
            powergrid = powerup.get_powergrid2()
            powerup._speedx[:] = ' '
            powerup._speedy[:] = ' '
            placepower = brick.get_placepower2()
            activate = powerup.get_activate2()
            brd.create_board(width,height,gm_back.get_grid2())
            brd.create_ball(width,height,gm_back.get_grid2())
            brd.stick = 1

        if text == "3":
            prtime = time.time()
            starttime = time.time()
            present_screen = 3
            grid = gm_back.get_grid3()
            grid2 = brick.get_grid3()
            grid8 = boss.get_boss_grid()
            activate = np.zeros(10 , dtype=int)
            brd.create_board(width,height,grid)
            brd.create_ball(width,height,grid)
            boss.place_boss(width,height,brd.get_middle(),grid,grid8)
            brd.stick = 1            


        if text == "q":
            print("quit")
            break

        elif text == "a":
            brd.board_movea(width , height , grid)
            if present_screen == 3:
                boss.place_boss(width,height,brd.get_middle(),grid,grid8)
            

        elif text == "d":
            brd.board_moved(width , height , grid)
            if present_screen == 3:
                boss.place_boss(width,height,brd.get_middle(),grid,grid8)

        elif text == " ":
            brd.stick = 0
        # print(3)
        if brd.stick == 0:
            brd.ball_move(width , height ,grid,activate)
            # if brd.stick == 0:
            
            ball_brickcoll.checkcoll(brd.get_old_x() ,brd.get_old_y() , brd.get_new_x() , brd.get_new_y() , grid2 , height , width,grid , brd , placepower , powergrid, activate,brick,rainbow,boss,present_screen,powerup._speedx,powerup._speedy)
            if present_screen == 3:
                ball_brickcoll.checkcoll2(brd.get_old_x() ,brd.get_old_y() , brd.get_new_x() , brd.get_new_y() , grid8 , height , width,grid , brd , placepower , powergrid, activate,brick,rainbow,boss,present_screen)

        else:
            update_struct(width,height,grid,grid2)
        #     else:
        #         ball_brickcoll.checkcoll2(brd.get_old_x() ,brd.get_old_y() , brd.get_new_x() , brd.get_new_y() , grid2 , height , width,grid , brd ,brick)
        # #   # create_struct(width,height,gm_back.get_grid(),brick.get_grid())
            # print(1)
        
        if present_screen == 3:
            boss.move_bomb(width,height,grid,boss.get_bombgrid(),brd)
        
        else:
            powerup.move_powerup(width,height,grid,powergrid,activate,brd,powerup._speedx,powerup._speedy)

            st = time.time()
            if st-bricktime >= brick._fall_time:
                bricktime = time.time()
                rainbowtime = time.time()
                temp = np.zeros((height,width),dtype='<U20')
                temp[:] = ' '
                temp2 = np.zeros((height,width),dtype='<U20')
                temp2[:] = ' '
                temp3 = np.zeros((height,width),dtype='<U20')
                temp3[:] = ' '
                temp4 = np.zeros((height,width),dtype='<U20')
                temp4[:] = ' '
                for i in range(height):
                    for j in range(width):
                        if grid2[i][j]!= " ":
                            temp[i+1][j] = grid2[i][j]
                            grid2[i][j] = " "
                            grid[i:i+3,j:j+8] = " "
                        
                        if powergrid[i][j]!=" ":
                            temp2[i+1][j] = powergrid[i][j]
                            powergrid[i][j] = " "
                            grid[i:i+2,j:j+2] = " "  

                        if placepower[i][j]!=" ":
                            temp3[i+1][j] = placepower[i][j]
                            placepower[i][j] = " "
                        
                        if rainbow[i][j]!=" ":
                            temp4[i+1][j] = rainbow[i][j]
                            rainbow[i][j] = " "

                for i in range(height):
                    for j in range(width):
                        grid2[i][j] = temp[i][j]
                        powergrid[i][j] = temp2[i][j]
                        placepower[i][j] = temp3[i][j]
                        rainbow[i][j] = temp4[i][j]

                        if grid2[height-6][j]!= " ":
                            done=1
                        
                        if grid2[i][j] == "1":
                            nump4 = brick._lev1
                            grid[i:i+3,j:j+8] = np.tile(nump4,2)

                        if grid2[i][j] == "2":
                            nump6 = brick._lev2
                            grid[i:i+3,j:j+8] = np.tile(nump6,2)

                        if grid2[i][j] == "3":
                            nump2 = brick._lev3
                            grid[i:i+3,j:j+8] = np.tile(nump2,2)

                        if grid2[i][j] == "5":
                            nump3 = brick._lev5
                            grid[i:i+3,j:j+8] = np.tile(nump3,2)

                        if grid2[i][j] == "20":
                            nump5 = brick._lev20
                            grid[i:i+3,j:j+8] = np.tile(nump5,2)

                        if powergrid[i][j] == "1":
                            grid[i:i+2,j:j+2] = powerup._power1
                        if powergrid[i][j] == "2":
                            grid[i+1:i+3,j:j+2] = powerup._power2
                        if powergrid[i][j] == "3":
                            grid[i+1:i+3,j:j+2] = powerup._power3
                        if powergrid[i][j] == "4":
                            grid[i+1:i+3,j:j+2] = powerup._power4
                        if powergrid[i][j] == "5":
                            grid[i+1:i+3,j:j+2] = powerup._power5
                        if powergrid[i][j] == "6":
                            grid[i+1:i+3,j:j+2] = powerup._power6
                        
                

            if done == 1:
                show_message("Game Over")
                break

            if time.time() - rainbowtime >= 2:
                rainbowtime = time.time()
                brick.change_color(width,height,rainbow,grid,grid2)

            stay = powerup._staytime
            for i in range(10):
                if activate[i] != 0:
                    if st - activate[i] > stay :
                        activate[i] = 0
                        if i == 1 or i==2:
                            brd.normal_boardlength(width,height,grid)
                        if i == 6:
                            brd.normal_stick()
                        if i==4:
                            brd.normal_speed()
            
        if present_screen == 3 and time.time()-bosstime >= 1.5:
            bosstime = time.time()
            boss.add_bomb(grid,boss.get_bombgrid(),brd.get_middle(),25)
        
        if present_screen == 3 and boss._lives <= 11 and cnt1 == 0:
            cnt1+=1
            class13(width,height,grid,grid2)

        if present_screen == 3 and boss._lives <= 3 and cnt2 == 0:
            cnt2+=1
            class13(width,height,grid,grid2)

                
        
        print("\033[%d;%dH" % (0, 0))
        print(Back.MAGENTA + "Time:",
              (round(time.time()) - round(starttime)), '  ' , end = "\t\t ")
        print(Back.MAGENTA + "Lives:" , brd.get_lives(), '  ' , end = " \t\t")
        # print()
        print(Back.MAGENTA + "Score:" , brick.get_score(), '  ' , end = " ")

        if present_screen == 3: 
            print(Back.MAGENTA + "Boss Lives:" , boss._lives, '  ' , end = " ")
            


        print(Style.RESET_ALL)
        gm_back.show_screen(grid)

        if boss._lives == 0 and present_screen == 3:
                show_message("You Won")
                break

os.system("killall aplay -q")
print(Back.RESET)