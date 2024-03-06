from _datetime import *
with open("rocket_part.txt", "r", encoding="utf-8") as f:

    a = f.readlines()[1:]
    a1 = []
    allp = []

    for i in a:
        a1.append(i.split(" "))

    for i in a1:
        if i[1] == "":
            allp.append([i[1], i[5]])

    for i in allp:
        i[1] = datetime.strptime(i[1], "%Y-%m-%d")
    maxt = -10000
    orig = "количество шифров"
    fake_stuff = "номер месяца"

    for i in allp:
        if datetime.toordinal(i[1]) > maxt:
            maxt = datetime.toordinal(i[1])


    for i in allp:
        if datetime.toordinal(i[1]) == maxt:
            orig = i[0]

        fake_stuff += i[0] + ", "

    print("В : было получено ", fake_stuff, " : шифров", orig)