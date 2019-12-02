from math import floor


def hacky_solution(in_dat):
    int_list = [int(val) for val in in_dat.read().split('\n')]
    print(sum([int_list.append(x // 3 - 2) or x // 3 - 2 for x in int_list if (x // 3 - 2) > 0]))


def more_convenient_solution(in_dat):
    def append_with_return(to_append, target):
        return target.append(to_append) or to_append if to_append > 0 else 0

    int_list = [int(val) for val in in_dat.read().split('\n')]
    print(sum([append_with_return(x // 3 - 2, int_list) for x in int_list]))


with open('input.txt', 'r') as file:
    hacky_solution(file)
    # more_convenient_solution(file)
