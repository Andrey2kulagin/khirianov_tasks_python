#!/usr/bin/python3

from pyrob.api import *
def cell_str(n):
    while wall_is_on_the_right()==0:
        fill_cell()
        move_right()

def set_null_pos():
    move_down()
    while wall_is_on_the_left()==0:
        move_left()
    move_right()


@task(delay=0.05)
def task_4_11():
    while wall_is_beneath()==0:
        cell_str()
    cell_str()


if __name__ == '__main__':
    run_tasks()
