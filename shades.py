#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.




# modules
from random import randint
import pygame as pg
from utils import drawrec, lindraw, elidraw, polydraw
from colour_palette import *

# init
pg.init()

# mainloop
def main():

    # variables
    width = 1920
    height = 1080

    screen = pg.display.set_mode((width, height))
    background = BLACK
    screen.fill(background)
    pg.mouse.set_visible(False)

    recx = 100
    recy = 100
    size_x = 120
    size_y = 120
    move_speed = 20
    
    # animation speed
    time_speed = 20
    
    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()

            # movement
            moveRight = False
            moveLeft = False
            moveUp = False
            moveDown = False
            ranMove = False

            # size
            sizeDown = False
            sizeUp = False
            
            # move speed
            time_speed_up = False
            time_speed_down = False
            draw_shd = False
            
            # bg switch
            switch = 1
            
            # initial colour
            current_palette = blue_palette
            count = 0
            count_2 = 5
            colour = current_palette[count]
            colour_2 = current_palette[count_2]
            
            while True:

                if colour == current_palette[-1]:
                    count = 0
                colour = current_palette[count]
                count += 1

                if colour_2 == current_palette[-1]:
                    count_2 = 0
                colour_2 = current_palette[count_2]
                count_2 += 1
                
                # move / resize colours
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_q:
                            pg.quit()
                        # select colour
                        elif event.key == pg.K_1:
                            current_palette = colour_list
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_2:
                            current_palette = red_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_3:
                            current_palette = orange_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_4:
                            current_palette = yellow_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_5:
                            current_palette = green_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_6:
                            current_palette = blue_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_7:
                            current_palette = cyan_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_8:
                            current_palette = violet_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        elif event.key == pg.K_9:
                            current_palette = gray_palette
                            count = 0
                            count_2 = 5
                            colour = current_palette[count]
                            colour_2 = current_palette[count_2]
                        
                        # clear screen
                        elif event.key == pg.K_SPACE:
                            background = BLACK
                            screen.fill(background)
                            pg.display.update()
                        
                        # movement speed
                        elif event.key == pg.K_LEFT:
                            moveRight = False
                            moveLeft = True
                        elif event.key == pg.K_RIGHT:
                            moveRight = True
                            moveLeft = False
                        elif event.key == pg.K_UP:
                            moveUp = True
                            moveDown = False
                        elif event.key == pg.K_DOWN:
                            moveUp = False
                            moveDown = True
                        
                        # size
                        elif event.key == pg.K_a:
                            sizeDown = True
                        elif event.key == pg.K_d:
                            sizeUp = True

                        elif event.key == pg.K_w:
                            time_speed_up = True
                        elif event.key == pg.K_s:
                            time_speed_down = True

                        # draw background
                        elif event.key == pg.K_z:
                            switch = 0
                            draw_shd = True
                        # draw colours
                        elif event.key == pg.K_x:
                            switch = 1
                            draw_shd = False
                        elif event.key == pg.K_c:
                            switch = 2
                            draw_shd = False
                        elif event.key == pg.K_v:
                            switch = 3
                            draw_shd = False
                        elif event.key == pg.K_b:
                            switch = 4
                            draw_shd = False
                        elif event.key == pg.K_n:
                            switch = 5
                            draw_shd = False
                        elif event.key == pg.K_m:
                            switch = 6
                            draw_shd = False


                    elif event.type == pg.KEYUP:    
                        if event.key == pg.K_LEFT:
                            moveLeft = False
                        elif event.key == pg.K_RIGHT:
                            moveRight = False
                        elif event.key == pg.K_UP:
                            moveUp = False
                        elif event.key == pg.K_DOWN:
                            moveDown = False

                        elif event.key == pg.K_a:
                            sizeDown = False
                        elif event.key == pg.K_d:
                            sizeUp = False

                        elif event.key == pg.K_w:
                            time_speed_up = False
                        elif event.key == pg.K_s:
                            time_speed_down = False

                        elif event.key == pg.K_z:
                            draw_shd = False
                        elif event.key == pg.K_x:
                            draw_shd = False
                        elif event.key == pg.K_c:
                            draw_shd = False
                        elif event.key == pg.K_v:
                            draw_shd = False
                        elif event.key == pg.K_b:
                            draw_shd = False
                        elif event.key == pg.K_n:
                            draw_shd = False
                        elif event.key == pg.K_m:
                            draw_shd = False

                # set max
                if moveRight:
                    recx += move_speed
                    if recx > width - (size_x / 2):
                        recx = width - (size_x / 2)
                if moveLeft:
                    recx -= move_speed
                    if recx < 0 - (size_x / 2):
                        recx = 0 - (size_x / 2)
                if moveUp:
                    recy -= move_speed
                    if recy < 0 - (size_y / 2):
                        recy = 0 - (size_y / 2)
                if moveDown:
                    recy += move_speed
                    if recy > height - (size_y / 2):
                        recy = height - (size_y / 2)

                if sizeDown:
                    size_x -= 5
                    size_y -= 5
                    if size_x and size_y <= 20:
                        size_x = 20
                        size_y = 20
                if sizeUp:
                    size_x += 5
                    size_y += 5
                    if size_x and size_y >= 600:
                        size_x = 600
                        size_y = 600

                if time_speed_up:
                    time_speed -= 10
                    if time_speed <= 0:
                        time_speed = 0
                if time_speed_down:
                    time_speed += 10
                    if time_speed >= 50:
                        time_speed = 50
                
                
                # set switch
                # draw background
                if switch == 0:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    drawrec(screen, background, recx, recy, size_x, size_y)
                # draw square (fill)
                elif switch == 1:
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    drawrec(screen, colour, recx, recy, size_x, size_y)
                # draw square (outline)
                elif switch == 2:
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    drawrec(screen, colour, recx, recy, size_x, size_y, 1)
                # draw circle (fill)
                elif switch == 3:
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                # draw circle (outline)
                elif switch == 4:
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    elidraw(screen, colour_2, recx, recy, size_x, size_y, 1)
                # draw square/circle (fill)
                elif switch == 5:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    drawrec(screen, colour, recx, recy, size_x, size_y)
                # draw square/circle (outline)
                elif switch == 6:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y, 1)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    pg.display.update()
                    pg.time.wait(time_speed)
                    drawrec(screen, colour, recx, recy, size_x, size_y, 1)



            pg.display.update()
            screen.fill(background)

if __name__ == '__main__':
    main()
