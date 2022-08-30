#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    cell_count = 0
    while wall_is_on_the_right()==0:
        if cell_is_filled():
            cell_count+=1
        if cell_count==5:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
