from itertools import permutations


def compute_list(in_dat, inputs):
    input_iter = iter(inputs)
    idx = 0
    i_count = 0

    def get_real_val(par_pos):
        return in_dat[idx + par_pos + 1] if len(mode_switches) > par_pos and mode_switches[par_pos] else in_dat[
            in_dat[idx + par_pos + 1]]

    while idx in range(len(in_dat)):

        op_code = int("".join([x for x in str(in_dat[idx])][len(str(in_dat[idx])) - 2:]))
        mode_switches = [bool(int(x)) for x in str(in_dat[idx])][:len(str(in_dat[idx])) - 2][::-1] if len(
            str(in_dat[idx])) > 2 else []
        if op_code == 1:
            in_dat[in_dat[idx + 3]] = get_real_val(0) + get_real_val(1)
            idx += 4
        elif op_code == 2:
            in_dat[in_dat[idx + 3]] = get_real_val(0) * get_real_val(1)
            idx += 4
        elif op_code == 3:
            in_dat[in_dat[idx + 1]] = next(input_iter)
            i_count += 1
            idx += 2
        elif op_code == 4:
            yield in_dat[in_dat[idx + 1]]
            idx += 2

        elif op_code == 5:
            if get_real_val(0) != 0:
                idx = get_real_val(1)
            else:
                idx += 3
        elif op_code == 6:
            if get_real_val(0) == 0:
                idx = get_real_val(1)
            else:
                idx += 3
        elif op_code == 7:
            in_dat[in_dat[idx + 3]] = 1 if get_real_val(0) < get_real_val(1) else 0
            idx += 4
        elif op_code == 8:
            in_dat[in_dat[idx + 3]] = 1 if get_real_val(0) == get_real_val(1) else 0
            idx += 4
        elif op_code == 99:
            return in_dat
    return in_dat


def amplifiers(program, sequence, feedback=0):  # <- Thanks to nylocx (https://github.com/nylocx/adventofcode2019)
    def amplifier_input(index):
        yield sequence[index]

        if index == 0:
            while True:
                yield feedback

        yield from compute_list(program.copy(), amplifier_input(index - 1))

    for feedback in compute_list(program.copy(), amplifier_input(len(sequence) - 1)):
        pass

    return feedback


with open('input.txt', 'r') as file:
    data = [int(x) for x in file.read().replace('\n', '').strip().split(",")]
    max_output = 0
    for seq in permutations(range(0, 5), 5):
        last_res = 0
        for i in seq:
            last_res = next(compute_list(data.copy(), [i, last_res]))
        max_output = last_res if last_res > max_output else max_output
    print(max_output)

    max_output = 0
    for sequence in permutations(range(5, 10), 5):
        output = amplifiers(data, sequence)
        max_output = output if output > max_output else max_output
    print(max_output)
