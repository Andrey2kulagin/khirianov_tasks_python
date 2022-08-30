#!/usr/bin/python3

from pyrob.api import *

def  to_up_cell():
    count =0
    while wall_is_above()==0:
        move_up()
        if cell_is_filled()==1:
            count+=1
        else: fill_cell()
    while wall_is_beneath()==0:
        move_down()
    return count

@task(delay=0.01)
def task_8_18():
    count = 0    
    while wall_is_beneath()==1:
        if wall_is_above()==0:
            count+=to_up_cell()
        else: fill_cell()
        move_right()
        
    ax = 32
    print(ax)
        


if __name__ == '__main__':
    run_tasks()
