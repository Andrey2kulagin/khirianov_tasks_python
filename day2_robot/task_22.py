#!/usr/bin/python3

from pyrob.api import *
def cell_str():
    while wall_is_on_the_right()==0:
        fill_cell()
        move_right()
    fill_cell()

def set_null_pos():
    move_down()
    while wall_is_on_the_left()==0:
        move_left()
   


@task(delay=0.05)
def task_5_10():
    while wall_is_beneath()==0:
        cell_str()
        set_null_pos()
    cell_str()
    if wall_is_above()==0:
        move_up()
        set_null_pos()


if __name__ == '__main__':
    run_tasks()
