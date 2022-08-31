#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    a = 1
    move_down()
    for j in range(18): 
        if j==(a-1):
            move_down()
            fill_cell()
            move_right(n = 2)
            fill_cell()
            move_left(n = 2)
            move_up()
        if j==(a+1):
            move_down()
            fill_cell()
            move_up()         
        if j==a:
            a+=4
            for k in range(3):
                fill_cell()
                move_down()
            for m in range(3):
                move_up()
        move_right()
    move_left(n = 2)


if __name__ == '__main__':
    run_tasks()
