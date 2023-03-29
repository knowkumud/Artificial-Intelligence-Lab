import random
def objective_function(x):
    if x<=10 and x>=-10:
        return x
    else: return -100

def Hill_Climbing_Search(starting_point,step_size,max_iteration):
    current_point = starting_point
    current_value = objective_function(current_point)
    for i in range(max_iteration):
        neighbour = current_point + step_size*(random.randint(-10,10))
        neighbour_value = objective_function(neighbour)
        if(neighbour_value > current_value) and neighbour_value!=-100:
            current_point = neighbour
            current_value = neighbour_value
    return [current_point,current_value]
result = Hill_Climbing_Search(8,-0.5,50)
print("Current Value: ", result[0])
print("Current Point: ", result[1])

#To find minimum 

import random
def objective_function(x):
    if x<=10 and x>=-10:
        return x
    else: return -100

def Hill_Climbing_Search(starting_point,step_size,max_iteration):
    current_point = starting_point
    current_value = objective_function(current_point)
    for i in range(max_iteration):
        neighbour = current_point + step_size*(random.randint(-10,10))
        neighbour_value = objective_function(neighbour)
        if(neighbour_value < current_value) and neighbour_value!=-100:
            current_point = neighbour
            current_value = neighbour_value
    return [current_point,current_value]
result = Hill_Climbing_Search(-9,0.5,50)
print("Current Value: ", result[0])
print("Current Point: ", result[1])
