with open("data.txt") as work_file:
    work = work_file.read()
    result = []
    i = 0
    while i < len(work):
        int_line = ""
        while i < len(work) and "0" <= work[i] <= "9":
            int_line += work[i]
            i += 1
        i += 1
        if int_line != "":
            result.append(int(int_line))
    print(f"Сумма чисел в файле: {sum(result)}")
