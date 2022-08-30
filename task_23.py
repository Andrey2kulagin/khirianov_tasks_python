#!/usr/bin/python3

from pyrob.api import *
def to_right():
    while wall_is_on_the_right()==0:
        move_right()

def  to_up_cell():
    while wall_is_above()==0:
        move_up()
        fill_cell()
    while wall_is_beneath()==0:
        move_down()


@task(delay=0.01)
def task_6_6():    
    to_right()
    while wall_is_beneath()==1:
        if wall_is_above()==0:
            to_up_cell()
        move_left()

if __name__ == '__main__':
    run_tasks()
