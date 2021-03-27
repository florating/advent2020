def read_input():
    f = open("day05_input", "r")
    return f.read().splitlines()


def determine_row(boarding_pass):
    # F is lower half, B is upper half; there are 0 to 127 rows
    row_code = boarding_pass[:7]
    high = 127
    low = 0
    for c in row_code:
        half = (high - low + 1) // 2
        if c == "F":
            high = low + half - 1
            # print("half is ", half, ", c is ", c, ", low is ", low, ", high is ", high)
        else:
            low = high - half + 1
            # print("half is ", half, ", c is ", c, ", low is ", low, ", high is ", high)
    return low


def determine_col(boarding_pass):
    # L is lower half, R is upper half; there are 0 to 7 columns
    col_code = boarding_pass[-3:]
    high = 7
    low = 0
    for c in col_code:
        half = (high - low + 1) // 2
        if c == "L":
            high = low + half - 1
            # print("col_code =", col_code, ", half is ", half, ", c is ", c, ", low is ", low, ", high is ", high)
        else:
            low = high - half + 1
            # print("col_code =", col_code, ", half is ", half, ", c is ", c, ", low is ", low, ", high is ", high)
    return low


def determine_seat_id(row, col):
    return row * 8 + col


def find_seat(list):
    curr = list[0]
    next = list[1]
    # print("list is", list, "and curr is", curr, "and next is", next)

    for i, val in enumerate(list):
        if i < len(list) - 2:
            if next - curr > 1:
                print("done! at i:", i, ", curr:", curr, ", next:", next)
                return next - 1
            else:
                # prev = curr
                curr = next
                next = list[i+2]
                # print("i:", i, ", curr:", curr, ", next:", next)


def main():
    all_passes = read_input()
    max_id = 0
    all_seats = []
    for i, val in enumerate(all_passes):
        r = determine_row(val)
        c = determine_col(val)
        id = determine_seat_id(r, c)
        all_seats.append(id)
        if id > max_id:
            max_id = id
    all_seats.sort()
    print(all_seats)
    return find_seat(all_seats)
    # return max_id


if __name__ == "__main__":
    print(main())
    # print(determine_col('FBFBBFFRLR'))
    # test = [0, 1, 2, 3, 5, 6]
    # print(find_seat(test))