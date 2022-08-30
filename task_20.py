#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    flag = 1;
    for i in range(2,14):
        for j in range(2,29):
            if flag>0:
                move_right()
            else:
                move_left()
            fill_cell()
        move_down()
        if flag>0:
            move_right()
        else: move_left()
        flag*=-1
    move_right()
        


if __name__ == '__main__':
    run_tasks()
