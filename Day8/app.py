res = (25, 6)
with open('input.txt', 'r') as file:
    in_dat = [int(i) for i in list(file.read().strip())]
    in_dat = [in_dat[i:i + (res[0] * res[1])] for i in range(0, len(in_dat), (res[0] * res[1]))]
    found = in_dat[0]
    for layer in in_dat:
        found = layer if layer.count(0) < found.count(0) else found
    print(found.count(1) * found.count(2))  # Part 1

    final_img = []
    for i in range(res[0] * res[1]):
        for layer in in_dat:
            if layer[i] != 2:
                final_img.append(layer[i])
                break
    for i in range(0, len(final_img), (res[0])):
        print(''.join([str(x) for x in final_img[i:i + (res[0])]]).replace('0', ' ').replace('1', '█'))  # Part 2
