with open('input.txt', 'r') as file:
    in_dat = {x.split(')')[1]: x.split(')')[0] for x in file.read().split('\n')}


    def get_path_from_item(item, cf=None):
        coming_from = cf if cf else item[0]
        out = [item[0]]
        if item[1] in in_dat.keys():
            out.extend(get_path_from_item((item[1], in_dat[item[1]]), coming_from))
        return out


    paths = {i[0]: get_path_from_item(i) for i in in_dat.items()}
    print(sum([len(p) for p in paths.values()]))  # Part 1
    print(len(set(paths["YOU"]).symmetric_difference(set(paths["SAN"]))) - 2)  # Part 2
