#!/usr/bin/python3

from pyrob.api import *
def x():
    if wall_is_above():
        move_right()
        for i in range(3):
            fill_cell()
            move_right()

@task(delay=0.01)
def task_9_3():
    while 


if __name__ == '__main__':
    run_tasks()
