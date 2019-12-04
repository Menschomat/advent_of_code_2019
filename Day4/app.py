in_range = (264360, 746325)


def rule_check(int_val):
    digits = [int(x) for x in str(int_val)]
    adjacent_same = {}
    for idx, val in enumerate(digits):
        if idx + 1 < len(digits) and val == digits[idx + 1]:
            if val not in adjacent_same.keys():
                adjacent_same[val] = 0
            adjacent_same[val] += 1
        if idx + 1 < len(digits) and val > digits[idx + 1]:
            return False
    return list(adjacent_same.values()) or False


print(len([x for x in range(*in_range) if rule_check(x)]))  # Part1
print(len([x for x in range(*in_range) if rule_check(x) and 1 in rule_check(x)]))  # Part2
