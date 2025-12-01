### GIVES CORRECT ANSWER
directions = []
dial_location = 50
times_at_zero = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        directions.append(line.strip())

#print(directions)

for direction in directions:
    left_or_right = direction[0]
    distance = int(direction[1:5])

    if (distance > 99):
        turns = distance // 100
        #print(f"{distance} > 99. Goes around 0 {turns} times")
        times_at_zero += turns
        distance %= 100
        #print(f'New distance after turns is {distance}')
        #print("\n")
    
    old_location = dial_location
    if (left_or_right == "L"):
        print(f"old location: {old_location}")
        print(f"LEFT {distance} ticks")

        dial_location -= distance

        if (dial_location < 0):
            if (old_location != 0 and dial_location != 0):
                print("+1 time around 0")
                times_at_zero += 1
            dial_location += 100
        print(f"new location: {dial_location}")
    else:
        print(f"old location: {old_location}")
        print(f"RIGHT {distance} ticks")

        dial_location += distance

        if (dial_location > 99):
            if (old_location != 0 and dial_location != 100):
                print("+1 time around 0")
                times_at_zero += 1
            dial_location -= 100
        print(f"new location: {dial_location}")

    if (dial_location == 0):
        print("+1 time around 0")
        times_at_zero += 1

    print('\n')


print(f"Times at zero: {times_at_zero}")