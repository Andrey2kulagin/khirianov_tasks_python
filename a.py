def all_param(car_weight_without_bag, car_height_without_bag, piano_weight, 
piano_height,fridge_weight, fridge_height, max_weight, max_height):
    max_all_weight = car_weight_without_bag+piano_weight+fridge_weight
    max_all_height = car_height_without_bag+max(piano_height,fridge_height)
    min_all_weight = car_weight_without_bag+piano_weight
    min_all_height = car_height_without_bag+fridge_height
    param = [max_all_weight,max_all_height,min_all_weight,min_all_height]
    return param

def is_pass(param, max_weight, max_height):
    if param [0]<=max_weight and param[1]<=max_height:
        print("YES")
    elif param[1]<=max_height and param[2]<=max_weight:
        print("YES")
    elif param[3]<=max_height and param[0]<=max_weight:
        print("YES")
    else: print("NO")


car_weight_without_bag = int(input())
car_height_without_bag = int(input())
piano_weight = int(input())
piano_height = int(input())
fridge_weight = int(input())
fridge_height = int(input())
max_weight = int(input())
max_height = int(input())
param = all_param(car_weight_without_bag, car_height_without_bag, piano_weight, 
piano_height,fridge_weight, fridge_height, max_weight, max_height)
is_pass(param, max_weight, max_height)