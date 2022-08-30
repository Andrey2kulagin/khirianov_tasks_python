#!/usr/bin/python3

from pyrob.api import *
def cure_move(i):
    for j in range(i):
        if wall_is_on_the_right()==0:
            move_right()
        else: return 0

@task
def task_7_5():
    move_right()
    fill_cell()
    i = 1
    while wall_is_on_the_right()==0:
        if cure_move(i)!=0:
            fill_cell()
            i+=1


if __name__ == '__main__':
    run_tasks()
