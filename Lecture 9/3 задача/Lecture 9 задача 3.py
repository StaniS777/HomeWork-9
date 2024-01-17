with open("qwe.txt") as string_1:
    string_1 = string_1.read()


def finder(string):
    words = string.lower().split()
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print("Количество повторений: ", max(counter.values()))

    return max(counter, key=counter.get)


print(finder(string_1))
