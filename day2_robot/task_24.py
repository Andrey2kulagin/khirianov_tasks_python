#!/usr/bin/python3

from pyrob.api import *

def set_start():
    move_down()
    move_right(2)


@task
def task_2_1():
    set_start()
    for i in range(3):
        fill_cell()
        move_down()
    move_right()
    move_up(n = 2)
    for i in range(3):
        fill_cell()
        move_left()
    move_up()
    move_right()


if __name__ == '__main__':
    run_tasks()
