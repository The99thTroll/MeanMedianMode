def calculate(input):
    new_data = input
        
    n = len(new_data)
    new_data.sort()

    if n % 2 == 0:
        median1 = float(new_data[n//2])
        median2 = float(new_data[n//2-1])
        median = (median1 + median2)/2
    else:
        median = new_data[n//2]

    return median