def find_closest_to_value_v2(target, table, x, y, reverse = False):
    # searches (interpolates) clossest value to target in table in column x then matches (closest) value in the same string of the column y
    # reverse = False is in case i is in ascending order
    
    closest_value = 0
    found = False
    counter = 0
    
    for i in range(len(table)):
        counter = i
        if target == table[i][x]:
            return table[i][y]
        if reverse == True and target > table[i][x]:
            found = True
            break
        if reverse == False and target < table[i][x]:
            found = True
            break

    #approximating linearly
    if found == True and counter != 0:
        #d_target_down = target - table[counter][1]
        d_target_up = table[counter-1][x] - target
        difference = table[counter-1][x] - table[counter][x]
        d_value = table[counter][y] - table[counter-1][y]
        #print(d_value)
        d_ratio = d_target_up/(difference)
        #print(d_ratio)
        closest_value = table[counter-1][y] + d_value * d_ratio
    elif counter == 0:
        difference = table[0][x] - table[1][x]
        d_value = table[1][y] - table[0][y]
        slope = d_value / difference
        closest_value = table[0][y] - slope * (target-table[0][x])
    elif found == False:
        difference = table[-1][x] - table[-2][x]
        d_value = table[-2][y] - table[-1][y]
        slope = d_value / difference
        closest_value = table[-1][y] - slope * (target-table[-1][x])

    return closest_value


def find_value_from_function(function_value, function, increment = 1.0, start_value = 0):
    # recursively calculates x (value) from fucntionl (f) knowing apropriate function value (f(x))
    # by iterating over start_start value with increment (*approaching from below)
    # increment and start_value are optional - maybe usefull in the futur
    # IMPORTANT: function is the function of 1 variable!
    return find_value_from_function_r(function_value, function, increment, start_value)
    
def find_value_from_function_r(function_value, function, increment, current_value): #approaching the goal from one side
    function_value_current = function(current_value)
    
    if function_value_current > function_value:
        current_value -= increment
        increment /= 10

    if increment <= 0.0001: #breaking the loop
        return current_value
    
    current_value += increment
    return find_value_from_function_r(function_value, function, increment, current_value)