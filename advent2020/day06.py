import re


def readinput():
    f = open("day06_input", "r")
    return f.read().splitlines()


def organize_groups(list):
    organized_list = []
    temp = set()
    for i, val in enumerate(list):
        print("i:", i, ", val:", val)
        if val == "\n" or val == "":
            organized_list.append(temp)
            temp = set()

        elif i == len(list) - 1:
            for c in val:
                temp.add(c)
            organized_list.append(temp)
            return organized_list

        else:
            for c in val:
                temp.add(c)
            # print("sublist is ", templist, "and val is ", val)
    return organized_list


def organize_groups_shared(list):
    organized_list = []
    temp = []

    for i, val in enumerate(list):
        print("i:", i, ", val:", val)
        if val == "\n" or val == "":
            organized_list.append(temp)
            temp = []

        elif i == len(list) - 1:
            temp.append(val)
            organized_list.append(temp)
            print("organize_groups_shared produced this list:", organized_list)
            return organized_list

        else:
            temp.append(val)
            # print("sublist is ", templist, "and val is ", val)

    return organized_list


def count_and_sum_unique(organized_list):
    count = 0
    for i, val in enumerate(organized_list):
        count += len(val)
    return count


def count_and_sum_shared(list_p1, list_p2):
    count = 0

    for i, val in enumerate(list_p1):
        # this iterates through the organized list of SETS of all unique answers per group

        for c in val:
            # this iterates through each character in the SET
            members_of_group = len(list_p2[i])
            tempcount = 0

            for k, ans in enumerate(list_p2[i]):
                # this iterates through the organized list of LISTS of each unique answer per group

                if re.search('['+c+']', ans):
                    # this regex checks if the character is present in this unique answer
                    tempcount += 1
                else:
                    break

                if k == members_of_group - 1 and tempcount == members_of_group:
                    count += 1

    return count


# def unique_answers(list):
# # checks for unique answers in each group
#     u = []
#     for i, val in enumerate(list):
#         # u.append(re.search(r'[a-z]', val))
#         # print("i: ", i, ", val:", val, ", list of unique answers:", u)
#         pass
#
#     for c in str:
#         str.count()
#     return u


def main():
    all_answers = readinput()
    orglist_p1 = organize_groups(all_answers)
    # return count_and_sum_unique(orglist_p1)
    orglist_p2 = organize_groups_shared(all_answers)
    return count_and_sum_shared(orglist_p1, orglist_p2)


if __name__ == "__main__":
    print(main())