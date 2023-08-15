def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
           sum += 1
    return sum

print(count([5,3,4,2,2,2,2,2,2],2))