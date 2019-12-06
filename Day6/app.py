with open('input.txt', 'r') as file:
    in_dat = dict(reversed(line.strip().split(")")) for line in file)


    def get_path_from_item(item, cf=None):
        out = [item[0]]
        if item[1] in in_dat.keys():
            out.extend(get_path_from_item((item[1], in_dat[item[1]]), cf if cf else item[0]))
        return out


    paths = {i[0]: get_path_from_item(i) for i in in_dat.items()}
    print(sum([len(p) for p in paths.values()]))  # Part 1
    print(len(set(paths["YOU"]) ^ set(paths["SAN"])) - 2)  # Part 2
