def evennumber(l):
    enum = []
    for i in l:
        if i % 2 == 0:
            enum.append(i)
    return enum
print(evennumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))

