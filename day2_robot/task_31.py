#!/usr/bin/python3

from pyrob.api import *
def right():
    while wall_is_on_the_right()==0:
        if wall_is_beneath()==0:
            move_down()
            return 1
        else: move_right()
def left():
    while wall_is_on_the_left()==0:
        if wall_is_beneath()==0:
            move_down()
            return 1
        else: move_left()
@task(delay=0.01)
def task_8_30():
    while 1:
        if right()!=1:
            if left()!=1:
                break
            



if __name__ == '__main__':
    run_tasks()
