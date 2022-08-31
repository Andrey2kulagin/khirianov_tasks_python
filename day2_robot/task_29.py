#!/usr/bin/python3

from pyrob.api import *

def counter():
     while wall_is_on_the_right()==0:
        count = 0
        move_right()
        while cell_is_filled():
            count +=1
            if wall_is_on_the_right()==0:
                if count ==3:
                    return 0
                move_right()
            if count ==3:
                return 0
@task
def task_7_7():
    counter()


if __name__ == '__main__':
    run_tasks()
