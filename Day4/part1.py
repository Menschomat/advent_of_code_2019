in_range = (264360, 746325)


def rule_check(int_val):
    digits = [int(x) for x in str(int_val)]
    adjacent_same = False
    for idx, val in enumerate(digits):
        if idx + 1 < len(digits) and val == digits[idx + 1]:
            adjacent_same = True
        if idx + 1 < len(digits) and val > digits[idx + 1]:
            return False
    return adjacent_same


print(len([x for x in range(*in_range) if rule_check(x)]))
