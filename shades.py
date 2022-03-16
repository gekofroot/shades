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
from pygame.locals import *
from utils import drawrec, lindraw, elidraw, polydraw
from colour_palette import *


# mainloop
def main():

    # init
    pg.init()
    
    global current_palette
    global count
    global count_2
    global count_3
    global bg_count
    global current_bg
    global palette_set
    global strobe_palette_set
    global switch_2
    global switch_4
    global switch_6
    global switch_1
    global switch_3
    global switch_5
    global switch
    global draw_shd

    # variables
    width = 1920
    height = 1080

    screen = pg.display.set_mode((width, height), FULLSCREEN)
    pg.display.set_caption("Shades")
    icon_img = pg.image.load("shades_icon.jpg")
    pg.display.set_icon(icon_img)
    bg_count = 0
    current_bg = bg_colour_list[bg_count]
    screen.fill(current_bg)
    pg.mouse.set_visible(False)

    recx = 100
    recy = 100
    size_x = 120
    size_y = 120
    linesize = 1
    move_speed = 20
    
    # animation speed
    time_speed = 20
    
    running = True
    while running:

        # movement
        moveRight = False
        moveLeft = False
        moveUp = False
        moveDown = False
        ranMove = False

        # size
        size_down = False
        size_up = False

        # line size
        linesize_down = False
        linesize_up = False
        

        # move speed
        time_speed_up = False
        time_speed_down = False
        draw_shd = False
        
        # shade
        shade_up = False
        shade_down = False
        
        # bg switch
        switch = 1
        
        # strobe on/off
        strobe = 1
 
        # initial colour
        current_palette = gray_palette
        current_palette_2 = gray_palette
        count = 0
        count_2 = 5
        count_3 = 0
        colour = current_palette[count]
        colour_2 = current_palette[count_2]
        colour_3 = current_palette[count_3]
        
        while True:
            
            if strobe == 0:
                if colour_3 == current_palette[-1]:
                    colour_3 = current_palette[-1]
                colour_3 = current_palette[count_3]

            elif strobe == 1:
                if colour == current_palette[-1]:
                    count = 0
                colour = current_palette[count]
                count += 1

                if colour_2 == current_palette[-1]:
                    count_2 = 0
                colour_2 = current_palette[count_2]
                count_2 += 1
            
            # traverse bg colour
            def get_prev_bg():

                global bg_colour_list
                global bg_count
                global current_bg

                if bg_count == 0:
                    bg_count = 0
                else:
                    bg_count - 1
                    bg_count -= 1
                
                current_bg = bg_colour_list[bg_count]
                screen.fill(current_bg)
                pg.display.update()

            def get_next_bg():

                global bg_colour_list
                global bg_count
                global current_bg

                if bg_count >= len(bg_colour_list) - 1:
                    bg_count = len(bg_colour_list) - 1
                else:
                    bg_count += 1
                
                current_bg = bg_colour_list[bg_count]
                screen.fill(current_bg)
                pg.display.update()
            
            # traverse shade
            def get_prev_shade():

                global current_palette
                global count_3
                
                if count_3 == 0:
                    count_3 = 0
                else:
                    count_3 - 1
                    count_3 -= 1

            def get_next_shade():

                global current_palette
                global count_3

                if count_3 >= len(current_palette) - 1:
                    count_3 = len(current_palette) - 1
                else:
                    count_3 += 1
            
            # set palette
            def palette_set(palette):
                
                global current_palette
                global count_3

                current_palette = palette
                if count_3 > len(current_palette) - 1:
                    count_3 = len(current_palette) -1
                colour_3 = current_palette[count_3]
            
            # set palette strobe
            def strobe_palette_set(palette):
                
                global current_palette
                global count
                global count_2

                current_palette = palette
                count = 0
                count_2 = 5
                colour = current_palette[count]
                colour_2 = current_palette[count_2]
            
            
            palette_sc = {
                    (K_1, KMOD_LCTRL): 'palette_set(colour_list)',
                    (K_2, KMOD_LCTRL): 'palette_set(red_palette)',
                    (K_3, KMOD_LCTRL): 'palette_set(orange_palette)',
                    (K_4, KMOD_LCTRL): 'palette_set(yellow_palette)',
                    (K_5, KMOD_LCTRL): 'palette_set(green_palette)',
                    (K_6, KMOD_LCTRL): 'palette_set(blue_palette)',
                    (K_7, KMOD_LCTRL): 'palette_set(cyan_palette)',
                    (K_8, KMOD_LCTRL): 'palette_set(violet_palette)',
                    (K_9, KMOD_LCTRL): 'palette_set(gray_palette)',
                    }
            

            strobe_palette_sc = {
                    (K_1, KMOD_LCTRL): 'strobe_palette_set(colour_list)',
                    (K_2, KMOD_LCTRL): 'strobe_palette_set(red_palette)',
                    (K_3, KMOD_LCTRL): 'strobe_palette_set(orange_palette)',
                    (K_4, KMOD_LCTRL): 'strobe_palette_set(yellow_palette)',
                    (K_5, KMOD_LCTRL): 'strobe_palette_set(green_palette)',
                    (K_6, KMOD_LCTRL): 'strobe_palette_set(blue_palette)',
                    (K_7, KMOD_LCTRL): 'strobe_palette_set(cyan_palette)',
                    (K_8, KMOD_LCTRL): 'strobe_palette_set(violet_palette)',
                    (K_9, KMOD_LCTRL): 'strobe_palette_set(gray_palette)',
                    }
            
            def palette_key(event):

                global palette_set

                k = event.key
                m = event.mod
                if (k, m) in palette_sc:
                    exec(palette_sc[k, m])

            def palette_strobe_key(event):

                global strobe_palette_set

                k = event.key
                m = event.mod
                if (k, m) in palette_sc:
                    exec(strobe_palette_sc[k, m])
            
            # create function for these
            def switch_1():
                
                global switch
                switch = 1
                draw_shd = False
            
            def switch_2():
                
                global switch
                switch = 2
                draw_shd = False

            def switch_3():
                
                global switch
                switch = 3
                draw_shd = False
            
            def switch_4():
                
                global switch
                switch = 4
                draw_shd = False
            
            def switch_5():

                global switch
                switch = 5
                draw_shd = False
            
            def switch_6():
                
                global switch
                switch = 6
                draw_shd = False

            fill_sc = {
                    (K_x, KMOD_LSHIFT): 'switch_2()',
                    (K_c, KMOD_LSHIFT): 'switch_4()',
                    (K_v, KMOD_LSHIFT): 'switch_6()',
                    (K_x, KMOD_LCTRL): 'switch_1()',
                    (K_c, KMOD_LCTRL): 'switch_3()',
                    (K_v, KMOD_LCTRL): 'switch_5()',
                    }

            def shape_fill_key(event):

                global switch_2
                global switch_4
                global switch_6
                global switch_1
                global switch_3
                global switch_5
                global switch

                k = event.key
                m = event.mod
                if (k, m) in fill_sc:
                    exec(fill_sc[k, m])

            # move / resize colours
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    shape_fill_key(event)
                    if event.key == K_ESCAPE:
                        pg.quit()
                    
                    if strobe == 0:
                        
                        # select colour
                        palette_key(event)
                        shape_fill_key(event)
                        
                    elif strobe == 1:
                        
                        # select colour
                        palette_strobe_key(event)
                        shape_fill_key(event)
                    
                    # clear screen
                    if event.key == pg.K_SPACE:
                        screen.fill(current_bg)
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
                        size_down = True
                    elif event.key == pg.K_d:
                        size_up = True
                    # line size
                    elif event.key == pg.K_e:
                        linesize_down = True
                    elif event.key == pg.K_r:
                        linesize_up = True

                    elif event.key == pg.K_w:
                        time_speed_up = True
                    elif event.key == pg.K_s:
                        time_speed_down = True

                    # draw background
                    elif event.key == pg.K_z:
                        switch = 0
                        draw_shd = True
                    
                    # set strobe
                    elif event.key == pg.K_o:
                        strobe = 1
                    elif event.key == pg.K_p:
                        strobe = 0

                    # traverse shade
                    if event.key == pg.K_g:
                        shade_down = True
                    elif event.key == pg.K_f:
                        shade_up = True

                    # traverse background colour
                    if event.key == pg.K_h:
                        get_prev_bg()
                    elif event.key == pg.K_j:
                        get_next_bg()

                # if keyup
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
                        size_down = False
                    elif event.key == pg.K_d:
                        size_up = False
                    
                    elif event.key == pg.K_e:
                        linesize_down = False
                    elif event.key == pg.K_r:
                        linesize_up = False

                    elif event.key == pg.K_w:
                        time_speed_up = False
                    elif event.key == pg.K_s:
                        time_speed_down = False

                    elif event.key == pg.K_z:
                        draw_shd = False
                    
                    elif event.key == pg.K_g:
                        shade_down = False
                    elif event.key == pg.K_f:
                        shade_up = False
                    
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

            if size_down:
                size_x -= 5
                size_y -= 5
                if size_x and size_y <= 20:
                    size_x = 20
                    size_y = 20
            if size_up:
                size_x += 5
                size_y += 5
                if size_x and size_y >= 700:
                    size_x = 700
                    size_y = 700
            
            if linesize_down:
                linesize -= 1
                if linesize <= 1:
                    linesize = 1
            if linesize_up:
                linesize += 1
                if linesize >= 350:
                    linesize = 350

            if time_speed_up:
                time_speed -= 10
                if time_speed <= 0:
                    time_speed = 0
            if time_speed_down:
                time_speed += 10
                if time_speed >= 50:
                    time_speed = 50
            
            if shade_up:
                get_prev_shade()
            if shade_down:
                get_next_shade()

            
            
            def refresh():
                pg.display.update()
                pg.time.wait(time_speed)
                pg.display.update()
                pg.time.wait(time_speed)

            # set strobe
            if strobe == 0:

                # set switch
                # draw background
                if switch == 0:
                    elidraw(screen, colour_3, recx, recy, size_x, size_y)
                    refresh()
                    drawrec(screen, current_bg, recx, recy, size_x, size_y)
                # draw square (fill)
                elif switch == 1:
                    refresh()
                    drawrec(screen, colour_3, recx, recy, size_x, size_y)
                # draw square (outline)
                elif switch == 2:
                    refresh()
                    drawrec(screen, colour_3, recx, recy, size_x, size_y, linesize)
                # draw circle (fill)
                elif switch == 3:
                    refresh()
                    elidraw(screen, colour_3, recx, recy, size_x, size_y)
                # draw circle (outline)
                elif switch == 4:
                    refresh()
                    elidraw(screen, colour_3, recx, recy, size_x, size_y, linesize)
                # draw square/circle (fill)
                elif switch == 5:
                    elidraw(screen, colour_3, recx, recy, size_x, size_y)
                    refresh()
                    drawrec(screen, colour_3, recx, recy, size_x, size_y)
                # draw square/circle (outline)
                elif switch == 6:
                    elidraw(screen, colour_3, recx, recy, size_x, size_y, linesize)
                    refresh()
                    drawrec(screen, colour_3, recx, recy, size_x, size_y, linesize)
            elif strobe == 1:
                
                # set switch
                # draw background
                if switch == 0:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                    refresh()
                    drawrec(screen, current_bg, recx, recy, size_x, size_y)
                # draw square (fill)
                elif switch == 1:
                    refresh()
                    drawrec(screen, colour, recx, recy, size_x, size_y)
                # draw square (outline)
                elif switch == 2:
                    refresh()
                    drawrec(screen, colour, recx, recy, size_x, size_y, linesize)
                # draw circle (fill)
                elif switch == 3:
                    refresh()
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                # draw circle (outline)
                elif switch == 4:
                    refresh()
                    elidraw(screen, colour_2, recx, recy, size_x, size_y, linesize)
                # draw square/circle (fill)
                elif switch == 5:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y)
                    refresh()
                    drawrec(screen, colour, recx, recy, size_x, size_y)
                # draw square/circle (outline)
                elif switch == 6:
                    elidraw(screen, colour_2, recx, recy, size_x, size_y, linesize)
                    refresh()
                    drawrec(screen, colour, recx, recy, size_x, size_y, linesize)

        #pg.display.update()
        screen.fill(current_bg)
        pg.display.update()


if __name__ == '__main__':
    main()
