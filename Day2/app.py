def compute_list(in_dat):
    op_c_list = in_dat[::4]
    for op_c_idx in range(len(op_c_list)):
        real_idx = 4 * op_c_idx
        if op_c_list[op_c_idx] == 1:
            in_dat[in_dat[real_idx + 3]] = in_dat[in_dat[real_idx + 1]] + in_dat[in_dat[real_idx + 2]]
        elif op_c_list[op_c_idx] == 2:
            in_dat[in_dat[real_idx + 3]] = in_dat[in_dat[real_idx + 1]] * in_dat[in_dat[real_idx + 2]]
        elif op_c_list[op_c_idx] == 99:
            return in_dat
        op_c_list = in_dat[::4]


def part1_test(test_data):
    test_data[1] = 12
    test_data[2] = 2
    print(','.join(map(str, compute_list(test_data))))


def part2_test(test_data):
    target = 19690720
    for noun in range(99):
        for verb in range(99):
            test_data[1] = noun
            test_data[2] = verb
            result = compute_list(test_data.copy())
            if result[0] == target:
                print(100 * result[1] + result[2])
                exit()


with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')
    # part1_test([int(x) for x in data.split(",")])
    part2_test([int(x) for x in data.split(",")])
