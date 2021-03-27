
thisdict = {
    # "word": "definition",
    # 'operation': 'argument',
    # 'acc': '+'
    # 'jmp':
    # 'nop': +1
}

acc_val = 0
instructions_list = []
curr_index = 0
inf_loop_status = False


def read_instructions():
    f = open("day08_input", "r")
    return f.readlines()


def check_instructions(val):
    global acc_val
    global curr_index
    templist = val.split(' ')
    operation = templist[0]
    arg = int(templist[1])
    if operation == "jmp":
        curr_index += arg
    elif operation == "acc":
        curr_index += 1
        acc_val += arg
    elif operation == "nop":
        curr_index += 1
    return operation, arg


def run_instructions(inst_list, i_start):
    global instructions_list
    global inf_loop_status
    this_inst = inst_list[i_start]
    if instructions_list[i_start] is None:
        instructions_list[i_start] = this_inst
        op, arg = check_instructions(this_inst)
        return
    else:
        inf_loop_status = True
        print("About to start infinite loop. Stop!")
    # while type(inst_list[i]) == 'str' and len(inst_list[i]) >= 4:
    #     check_instructions(this_inst, i)


def initialize_instructions(list):
    return [None] * len(list)


def main_p1():
    global inf_loop_status
    global acc_val
    global instructions_list
    global curr_index
    inst_list = read_instructions()
    instructions_list = initialize_instructions(inst_list)
    run_instructions(inst_list, 0)
    while not(inf_loop_status):
        if curr_index >= len(inst_list):
            print("Terminate!")
            return acc_val
        else:
            run_instructions(inst_list, curr_index)

    # while type(inst_list[i]) == 'str' and len(inst_list[i]) >= 4:

    # for i, val in enumerate(inst_list):
    #     curr_index = check_instructions(val, i)

    return acc_val


"""
For Part 2, could try:
    - NEW: make a list of nop operations and the index locations (list_nop)
    - NEW: make a list of jmp operations and the index locations (list_jmp)
        contains a list of ints to refer to index positions
    - NEW: iterate through either list_nop or list_jmp to make a single operation change
        - use main_p1() to check individual, modified instruction lists
        - will need to modify to not read the list each time...?
"""

if __name__ == "__main__":
    print(main_p1())
