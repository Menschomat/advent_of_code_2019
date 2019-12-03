x_dir = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
y_dir = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def convert_to_tuple_list(in_str):
    return [(x[:1], int(x[1:])) for x in in_str]


def generate_path(command_list):
    path = []
    path_cursor = -1
    for direction, length in command_list:
        for i in range(length):
            y, x = path[path_cursor + i] if bool(path) else (0, 0)
            path.append(
                (y + y_dir[direction], x + x_dir[direction]))
        path_cursor += length
    return path


with open('full_input.txt', 'r') as in_dat:
    path1 = generate_path(convert_to_tuple_list(in_dat.readline().strip().split(',')))
    path2 = generate_path(convert_to_tuple_list(in_dat.readline().split(',')))
    print(min([abs(p[0]) + abs(p[1]) for p in set(path1).intersection(set(path2))]))
    print(min([path1.index(p) + path2.index(p) for p in
               set(path1).intersection(set(path2))]) + 2)  # +2 because, we dont have (0,0) in our lists
