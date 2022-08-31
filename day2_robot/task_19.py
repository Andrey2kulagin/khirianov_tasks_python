#!/usr/bin/python3

from pyrob.api import *

def out_of_box():
    flag = False
    while wall_is_on_the_left()==0:
        move_left()
        if wall_is_above()==0 and wall_is_beneath()==0:
            move_up()
            flag = True
            break
    if flag==False:
        while wall_is_on_the_right()==0:
            move_right()
            if wall_is_above()==0 and wall_is_beneath()==0:
                move_up()
                flag = True
                break
    return flag
@task
def task_8_29():
    a = out_of_box()
    print(a)
    if a:
        while wall_is_on_the_left()==0:
            move_left()
        while wall_is_above()==0:
            move_up()


if __name__ == '__main__':
    run_tasks()
