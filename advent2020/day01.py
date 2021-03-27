def readinput():
    f = open("day01_input", "r")
    return f.readlines()


def main_p1():
    l = readinput()
    numa, numb = 0, 0
    for i in range(len(l)):
        numa = int(l[i])
        numb = 0
        expnum = 2020 - numa
        for j in range(len(l)):
            if int(l[j]) == expnum and i != j:
                numb = expnum
                break
        if numa + numb == 2020:
            break
    return numa * numb
# next time, could try to RETURN instead of BREAK in the code above


def main_p2():
    l = readinput()
    numa, numb, numc, i = 0, 0, 0, 0
    while i < len(l) - 3:
        numa = int(l[i])
        j = i + 1
        while j < len(l) - 2:
            numb = int(l[j])
            k = j + 1
            while k < len(l) - 1:
                numc = int(l[k])
                if numa + numb + numc == 2020:
                    return numa * numb * numc
                k += 1
            j += 1
        i += 1
    return


"""
# ints is a list
for idx, val in enumerate(ints):
    print(idx, val)
"""


if __name__ == "__main__":
    print(main_p1())
    print(main_p2())
