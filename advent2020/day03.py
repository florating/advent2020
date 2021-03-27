def readinput():
    f = open("day03_input", "r")
    return f.readlines()


def traverse(list, x_inc, y_inc):
    xpos = 0
    ypos = 0
    numtrees = 0
    max_x = len(list[0]) - 2
    # for i, val in enumerate(list):
    while ypos < len(list):
        row = list[ypos]
        if "#" == row[xpos]:
            numtrees += 1
        print("xpos is", xpos, ". ypos is", ypos, ". numtrees is", numtrees, ". row length is ", len(row), ". maximum ypos is ", len(list) - 1)
        print("terrain is ", row[xpos])
        xpos += x_inc
        if xpos > max_x:
            xpos = xpos - max_x - 1
        ypos += y_inc
    return numtrees


def main():
    terrain = readinput()
    prod = 1
    prod *= traverse(terrain, 1, 1)
    prod *= traverse(terrain, 3, 1)
    prod *= traverse(terrain, 5, 1)
    prod *= traverse(terrain, 7, 1)
    prod *= traverse(terrain, 1, 2)
    return prod


if __name__ == "__main__":
    print(main())
    # print(main_p2())