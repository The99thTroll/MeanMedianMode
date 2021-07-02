def calculate(input):
    new_data = input
        
    n = len(new_data)
    total = 0

    for x in new_data:
        total += x
        
    mean = total/n
    return mean