from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
t=0
grass.draw_now(400,30)
character.draw_now(400,90)

def  move_rect(x,y):
    while(x<770):                                #move right
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 5
        delay(0.01)

    while(y<550):                              #move up
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 5
        delay(0.01)

    while(x>0):                                 #move left    
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 5
        delay(0.01)

    while(y>90):                                #move down
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 5
        delay(0.01)

def  move_circle(t):
    while(t<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400+370*(math.cos(t/360*2*math.pi)),320+230*(math.sin(t/360*2*math.pi)))
        t = t + 3
        delay(0.01)


while(True):
    move_rect(x,y)
    move_circle(t)

close_canvas()
