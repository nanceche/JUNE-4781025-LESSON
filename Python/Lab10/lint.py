'''My function'''
def count(sequence, item):
    '''This function counts'''
    my_variable = 0
    for num in sequence:
        if num == item:
            my_variable += 1
    return my_variable
