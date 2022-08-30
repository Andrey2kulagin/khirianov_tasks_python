#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while (wall_is_beneath()==1 or wall_is_above()==1) and wall_is_on_the_right()==0:
        if wall_is_beneath()==0 or wall_is_above()==0:
            fill_cell()
        move_right()


if __name__ == '__main__':
    run_tasks()
