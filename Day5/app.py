def compute_list(in_dat):
    idx = 0

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
            in_dat[in_dat[idx + 1]] = int(input("Enter a number: "))
            idx += 2
        elif op_code == 4:
            print(in_dat[in_dat[idx + 1]])
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


with open('input.txt', 'r') as file:
    data = file.read().replace('\n', '')
    print(compute_list(([int(x) for x in data.split(",")])))
