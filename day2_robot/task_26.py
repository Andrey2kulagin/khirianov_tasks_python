#!/usr/bin/python3

from pyrob.api import *
import time
def draw_line():
    a = 1
    for j in range(38): 
        if j==(a-1):
            move_down()
            fill_cell()
            move_right(n = 2)
            fill_cell()
            move_left(n = 2)
            move_up()         
        if j==a:
            a+=4
            for k in range(2):
                fill_cell()
                move_down()
            fill_cell()
            for m in range(2):
                move_up()
        move_right()
    move_down()
    while wall_is_on_the_left()==0:
        move_left()

@task(delay=0.02)
def task_2_4():
    for i in range(5):
        draw_line()
        if i+1!=5:
            move_down(3)
    move_up()

if __name__ == '__main__':
    run_tasks()
