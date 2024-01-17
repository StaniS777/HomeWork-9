with open("classmate.txt") as file:
    sum = 0
    # Number line
    number = 1
    for i in file:
        i = i.split()
        value = int(i[2])
        sum += value
        number += 1
        if value < 3:
            print(f"Line №{number}", *i)
