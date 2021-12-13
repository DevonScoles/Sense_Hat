# An engineering project that teaches children patterns using the Sense Hat's LEDs to display arrows in a pattern
# There are 4 levels
# Each level gets harder, some taking more directional inputs, and some display the pattern faster.

from time import sleep
from sense_hat import SenseHat
import random as r


X = [255,0,0]
O = [255,255,255]
s = SenseHat()

s.show_message("Move Joystick in Direction of Arrows",scroll_speed = .07)
sleep(1)
s.show_message("LEVEL 1 BEGIN!",scroll_speed = 0.07,text_colour = (0,0,255))

arrow_up = [
O,O,O,X,X,O,O,O,
O,O,X,X,X,X,O,O,
O,X,X,X,X,X,X,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
]
arrow_right = [
O,O,O,O,O,O,O,O,
O,O,O,O,O,X,O,O,
O,O,O,O,O,X,X,O,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
O,O,O,O,O,X,X,O,
O,O,O,O,O,X,O,O,
O,O,O,O,O,O,O,O,
]
arrow_left = [
O,O,O,O,O,O,O,O,
O,O,X,O,O,O,O,O,
O,X,X,O,O,O,O,O,
X,X,X,X,X,X,X,X,
X,X,X,X,X,X,X,X,
O,X,X,O,O,O,O,O,
O,O,X,O,O,O,O,O,
O,O,O,O,O,O,O,O,
]
arrow_down = [
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,O,O,X,X,O,O,O,
O,X,X,X,X,X,X,O,
O,O,X,X,X,X,O,O,
O,O,O,X,X,O,O,O,
]
# level_1 begin
def level_1(score):
    #s.clear()
    level = [arrow_up,arrow_right,arrow_down,arrow_left]
    for i in range(len(level)):
        s.set_pixels(level[i])
        sleep(1)
        s.clear()
        
    event = s.stick.wait_for_event(emptybuffer=True)
    if event.direction == 'up':
        s.set_pixels(arrow_up)
        sleep(0.3)
        event = s.stick.wait_for_event(emptybuffer=True)
        if event.direction == 'right':
            s.set_pixels(arrow_right)
            sleep(0.3)
            event = s.stick.wait_for_event(emptybuffer=True)
            if event.direction == 'down':
                s.set_pixels(arrow_down)
                sleep(0.3)
                event = s.stick.wait_for_event(emptybuffer=True)
                if event.direction == 'left':
                    s.set_pixels(arrow_left)
                    sleep(0.3)
                    score+=4
                    s.show_message(f'Level 1 PASSED. SCORE = {score}',scroll_speed = 0.07,text_colour = (255,215,0))
                else:
                    s.show_message('Try Again :-)',text_colour = (0,200,0))
                    level_1(0)
            else:
                s.show_message('Try Again :)',text_colour = (0,200,0))
                level_1(0)
        else:
            s.show_message('Try Again :)',text_colour = (0,200,0))
            level_1(0)
    else:
        s.show_message('Try Again :)',text_colour = (0,200,0))
        level_1(0)
        

#level_2 begin
def level_2(score):
    #s.clear()
    level = [arrow_left,arrow_right,arrow_down,arrow_up]
    for i in range(len(level)):
        s.set_pixels(level[i])
        sleep(0.6)
    s.clear()
    event = s.stick.wait_for_event(emptybuffer=True)
    if event.direction == 'left':
        s.set_pixels(arrow_left)
        sleep(0.3)
        event = s.stick.wait_for_event(emptybuffer=True)
        if event.direction == 'right':
            s.set_pixels(arrow_right)
            sleep(0.3)
            event = s.stick.wait_for_event(emptybuffer=True)
            if event.direction == 'down':
                s.set_pixels(arrow_down)
                sleep(0.3)
                event = s.stick.wait_for_event(emptybuffer=True)
                if event.direction == 'up':
                    s.set_pixels(arrow_up)
                    sleep(0.3)
                    score+=6
                    s.show_message(f'Level 2 PASSED. SCORE = {score}',scroll_speed = 0.07, text_colour = (75,0,130))
                else:
                    s.show_message('Try Again :)',text_colour = (0,200,0))
                    level_2(4)
            else:
                s.show_message('Try Again :)',text_colour = (0,200,0))
                level_2(4)
        else:
            s.show_message('Try Again :)',text_colour = (0,200,0))
            level_2(4)
    else:
        s.show_message('Try Again :)',text_colour = (0,200,0))
        level_2(4)

#level_2 begin
def level_3(score):
    #s.clear()
    level = [arrow_down,arrow_right,arrow_down,arrow_up,arrow_left,arrow_up]
    for i in range(len(level)):
        s.set_pixels(level[i])
        sleep(0.8)
    s.clear()
    event = s.stick.wait_for_event(emptybuffer=True)
    if event.direction == 'down':
        s.set_pixels(arrow_down)
        sleep(0.3)
        event = s.stick.wait_for_event(emptybuffer=True)
        if event.direction == 'right':
            s.set_pixels(arrow_right)
            sleep(0.3)
            event = s.stick.wait_for_event(emptybuffer=True)
            if event.direction == 'down':
                s.set_pixels(arrow_down)
                sleep(0.3)
                event = s.stick.wait_for_event(emptybuffer=True)
                if event.direction == 'up':
                    s.set_pixels(arrow_up)
                    sleep(0.3)
                    event = s.stick.wait_for_event(emptybuffer=True)
                    if event.direction == 'left':
                        s.set_pixels(arrow_left)
                        sleep(0.3)
                        event = s.stick.wait_for_event(emptybuffer=True)
                        if event.direction == 'up':
                            s.set_pixels(arrow_up)
                            sleep(0.3)
                            score += 10
                            s.show_message(f'Level 3 PASSED. SCORE = {score}',scroll_speed = 0.07,text_colour = (153,50,204))
                        else:
                            s.show_message('Try Again :)',text_colour = (0,200,0))
                            level_3(10)
                    else:
                        s.show_message('Try Again :)',text_colour = (0,200,0))
                        level_3(10)
                else:
                    s.show_message('Try Again :)',text_colour = (0,200,0))
                    level_3(10)
            else:
                s.show_message('Try Again :)',text_colour = (0,200,0))
                level_3(10)
        else:
            s.show_message('Try Again :)',text_colour = (0,200,0))
            level_3(10)
    else:
        s.show_message('Try Again :)',text_colour = (0,200,0))
        level_3(10)
        
def level_4(score):
    #s.clear()
    level = [arrow_down,arrow_left,arrow_right,arrow_down,arrow_up,arrow_down]
    for i in range(len(level)):
        s.set_pixels(level[i])
        sleep(0.5)
    s.clear()
    event = s.stick.wait_for_event(emptybuffer=True)
    if event.direction == 'down':
        s.set_pixels(arrow_down)
        sleep(0.3)
        event = s.stick.wait_for_event(emptybuffer=True)
        if event.direction == 'left':
            s.set_pixels(arrow_left)
            sleep(0.3)
            event = s.stick.wait_for_event(emptybuffer=True)
            if event.direction == 'right':
                s.set_pixels(arrow_right)
                sleep(0.3)
                event = s.stick.wait_for_event(emptybuffer=True)
                if event.direction == 'down':
                    s.set_pixels(arrow_down)
                    sleep(0.3)
                    event = s.stick.wait_for_event(emptybuffer=True)
                    if event.direction == 'up':
                        s.set_pixels(arrow_up)
                        sleep(0.3)
                        event = s.stick.wait_for_event(emptybuffer=True)
                        if event.direction == 'down':
                            s.set_pixels(arrow_down)
                            sleep(0.3)
                            score += r.randint(1111,9999)
                            s.show_message(f'Level 4 PASSED. SCORE = {score}',scroll_speed = 0.07)
                        else:
                            s.show_message('Try Again :)',text_colour = (0,200,0))
                            level_4(20)
                    else:
                        s.show_message('Try Again :)',text_colour = (0,200,0))
                        level_4(20)
                else:
                    s.show_message('Try Again :)',text_colour = (0,200,0))
                    level_4(20)
            else:
                s.show_message('Try Again :)',text_colour = (0,200,0))
                level_4(20)
        else:
            s.show_message('Try Again :)',text_colour = (0,200,0))
            level_4(20)
    else:
        s.show_message('Try Again :)',text_colour = (0,200,0))
        level_4(20)
     
level_1(0)
level_2(4)
level_3(10)
level_4(20)
s.show_message('Thanks for Playing <3', scroll_speed = 0.06)
