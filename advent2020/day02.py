# str is a string
def isvalid(str):
    # could return everything below in a separate function

    thispass = str.split('-')
    min = int(thispass[0])
    thispass2 = thispass[1].split(' ')
    max = int(thispass2[0])
    letter = thispass2[1][0]
    thispassword = thispass2[2]
    # print("min is ", min, ". max is ", max, ". letter is ", letter, ". thispassword is ", thispassword, ".")

    # check if password is valid
    count = 0
    for i in thispassword:
        if letter == i:
            count += 1
        if count > max:
            return False

    if count >= min and count <= max:
        return True


def isvalid_p2(str):
    # could return everything below in a separate function

    thispass = str.split('-')
    min = int(thispass[0])
    thispass2 = thispass[1].split(' ')
    max = int(thispass2[0])
    letter = thispass2[1][0]
    thispassword = thispass2[2]
    # print("min is ", min, ". max is ", max, ". letter is ", letter, ". thispassword is ", thispassword, ".")

    # check if password is valid
    count = 0
    letter_min = thispassword[min-1]
    letter_max = thispassword[max-1]
    if letter_min == letter:
        count += 1
    if letter_max == letter:
        count += 1

    if count == 1:
        return True
    return False


def readinput():
    f = open("day02_input", "r")
    return f.readlines()


def main():
    allpass = readinput()
    numvalid = 0
    for i in allpass:
        # print(i)
        if isvalid(i):
            numvalid += 1
    return numvalid


def main_p2():
    allpass = readinput()
    numvalid = 0
    for i in allpass:
        if isvalid_p2(i):
            numvalid += 1
    return numvalid


if __name__ == "__main__":
    # print(main())
    # s = '2-4 j: jgjjh'
    # print(isvalid(s))
    print(main_p2())