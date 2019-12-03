def convert_to_tuple_list(in_str):
    return [(x[:1], int(x[1:])) for x in in_str]


def generate_path(command_list):
    path = [(0, 0)]
    path_cursor = 0
    for idx in range(len(command_list)):
        for i in range(command_list[idx][1]):
            current_point = path[path_cursor + i]
            if command_list[idx][0] == 'U':
                path.append((current_point[0] + 1, current_point[1]))
            elif command_list[idx][0] == 'D':
                path.append((current_point[0] - 1, current_point[1]))
            elif command_list[idx][0] == 'R':
                path.append((current_point[0], current_point[1] + 1))
            elif command_list[idx][0] == 'L':
                path.append((current_point[0], current_point[1] - 1))
        path_cursor += command_list[idx][1]
    return path


def part1():
    with open('full_input.txt', 'r') as in_dat:
        path1 = set(generate_path(convert_to_tuple_list(in_dat.readline().strip().split(','))))
        path2 = set(generate_path(convert_to_tuple_list(in_dat.readline().split(','))))
        print(min([abs(p[0]) + abs(p[1]) for p in path1.intersection(path2) if sum(p) != 0]))


def part2():
    with open('full_input.txt', 'r') as in_dat:
        path1 = generate_path(convert_to_tuple_list(in_dat.readline().strip().split(',')))
        path2 = generate_path(convert_to_tuple_list(in_dat.readline().split(',')))
        print(min([path1.index(p) + path2.index(p) for p in set(path1).intersection(set(path2)) if p != (0, 0)]))


part1()
part2()
