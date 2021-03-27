import re

"""
Look at dictionaries.
Field-value etc.
Lambdas?
"""

def readinput():
    f = open("day04_input", "r")
    # if there is a completely empty line, then this should be a new list of passenger passport credentials
    return f.readlines()


def readinput_test():
    f = open("day04_invalid", "r")
    return f.readlines()


def organize_creds(list):
    organized_list = []
    templist = []
    for i, val in enumerate(list):
        if i == len(list) - 1:
            templist = templist + val.split(' ')
            organized_list.append(templist)
            return organized_list
        if val == "\n":
            organized_list.append(templist)
            templist = []
        else:
            templist = templist + val[:-1].split(' ')
            # print("sublist is ", templist, "and val is ", val)
    return organized_list


def check_creds(list):
    if len(list) < 7:
        return False
    if len(list) > 7:
        return True
    for i, val in enumerate(list):
        temp = val.split(":")
        if temp[0] == "cid":
            return False
    return True


def check_creds_better(list):
    if not(check_creds(list)):
        return False

    for i, val in enumerate(list):
        temp = val.split(":")
        cred = temp[0]
        v = temp[1]

        print("cred is ", cred, " and v is ", v)

        if cred == "byr":
            intv = int(v)
            if not(len(v) == 4 and intv >= 1920 and intv <= 2002):
                print("False")
                return False

        if cred == "iyr":
            intv = int(v)
            if not(len(v) == 4 and intv >= 2010 and intv <= 2020):
                print("False")
                return False

        if cred == "eyr":
            intv = int(v)
            if not(len(v) == 4 and intv >= 2020 and intv <= 2030):
                print("False")
                return False

        if cred == "hgt":
            print("value is ", v, " and hgt is ", v[:-2])
            if len(v) <= 2:
                print("False")
                return False
            try:
                num = int(v[:-2])
                if v[-2:] == "cm":
                    if not(num >= 150 and num <= 193):
                        print("False")
                        return False
                elif v[-2:] == "in":
                    if not(num >= 59 and num <= 76):
                        print("False")
                        return False
                else:
                    print("False")
                    return False
            except ValueError:
                print("False with ValueError")
                return False

        if cred == "hcl":
            if v[0] == "#" and len(v) == 7:
                # uses regular expressions :o
                if not(re.search(r'[0-9a-f]{6}', v[1:])):
                    print("False")
                    return False
            else:
                return False

        if cred == "ecl":
            if not(len(v) == 3 and (v == "amb" or v == "blu" or v == "brn" or v == "gry" or v == "grn" or v == "hzl" or v == "oth")):
                print("False")
                return False

        if cred == "pid":
            if len(v) == 9:
                try:
                    a = int(v)
                except ValueError:
                    print("False with Exception")
                    return False
            else:
                return False
    return True


def main():
    list = readinput()
    # list = readinput_test()
    finallist = organize_creds(list)
    numvalid = 0
    for i, val in enumerate(finallist):
        if check_creds_better(val):
            numvalid += 1
    # print("testlist is ", testlist)
    # print("final list is ", finallist)
    return numvalid


if __name__ == "__main__":
    print(main())
