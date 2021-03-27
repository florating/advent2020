import re


def readrules():
    f = open("day07_input", "r")
    # the above is the same as: return f.readlines()
    return f.read().split("\n")


# def parse_rules(rules):
#     bag_containers = []
#     bag_contents = []
#
#     for i, val in enumerate(rules):
#         splits = re.split(' bags contains? ', val)
#         # contents_nobags = re.split(' bags?', splits[1])
#         # for val in contents_nobags:
#         #     nopunc = re.sub('[^\w\s]', '', val)
#
#         bag_containers.append(splits[0])
#         bag_contents.append(splits[1])
#
#     return bag_containers, bag_contents


def parse_rules(rules):
    bag_rules = []

    for i, val in enumerate(rules):
        splits = re.split(' bags contains? ', val)
        # contents_nobags = re.split(' bags?', splits[1])
        # for val in contents_nobags:
        #     nopunc = re.sub('[^\w\s]', '', val)

        bag_rules.append((splits[0], splits[1]))

    return bag_rules


def part1(bag_tuple, target_bag_set):
    possible_containers = set()

    if len(target_bag_set) == 0:
        return 0

    for container, contents in bag_tuple:
        # print("Length of bag_tuple:", len(bag_tuple), ", container:", container, ", contents:", contents)
        for bag in target_bag_set:
            # print(bag, "added. Length of target_bag_set:", len(target_bag_set))
            possible_containers.add(bag)
            if re.search(bag, contents):
                possible_containers.add(container)
                # print(container, "added. Length of possible_containers:", len(possible_containers))
    # print("target_bag_set:", target_bag_set)
    # print("possible_containers:", possible_containers)
    if len(target_bag_set) < len(possible_containers):
        # print("Recursion with possible_containers:", possible_containers)
        return part1(bag_tuple, possible_containers)
    else:
        # print("End. Return:", len(possible_containers))
        return len(possible_containers)
    # return len(possible_containers)

    # i = 0
    # count = 0
    # while i < len(containers):
    #     if len(contents) == 0:
    #         return 0
    #     if re.search('shiny gold', contents[i]):
    #         possible_containers.append(containers[i])
    #     i += 1
    #
    # count = len(possible_containers)
    #
    # if count > 0:
    #     print("")
    #     return part1(containers, possible_containers)
    #
    # return count


def count_bags(bag_rules, target_bag):
    if re.search("no other", target_bag):
        return 1
    else:
        num = 1
        new_bag = str()
        for container, contents in bag_rules:
            if re.search(target_bag, container):
                # following only works for contents of 1 type
                num = re.search('[\d]', contents)

                # need something else for contents of >1 type
        #     may want to consider splitting the contents part of the tuple in order
        #     to find recursively handle the rest...
        #     or don't use tuples!

        #     for example:
        #         'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.'
        #     means I will have to:
        #         1) count_bags(bag_rules, 'dark olive')
        #         2) count_bags(bag_rules, 'vibrant plum')

        return num * count_bags(bag_rules, target_bag)


def main():
    bag_rules = parse_rules(readrules())
    # print("containers:", containers)
    # print("contents:", contents)

    part1_target = set()
    part1_target.add('shiny gold')

    count = part1(bag_rules, part1_target)
    return count - 1

    # return bag_rules


if __name__ == "__main__":
    print(main())
    # print(readrules())
