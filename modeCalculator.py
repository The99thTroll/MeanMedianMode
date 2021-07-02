from collections import Counter

def calculate(input):
    new_data = input
        
    data = Counter(new_data)
    mode_data = {
        "90-110": 0,
        "110-130": 0,
        "130-150": 0,
    }

    for height, occurance in data.items():
        if 90 < float(height) < 110:
            mode_data["90-110"] += occurance
        elif 110 < float(height) < 130:
            mode_data["110-130"] += occurance
        elif 130 < float(height) < 150:
            mode_data["130-150"] += occurance

    mode_range, mode_occurance = 0, 0

    for range, occurance in mode_data.items():
        if occurance > mode_occurance:
            mode_range, mode_occurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
            
    mode = float((mode_range[0]+mode_range[1])/2)
    return mode