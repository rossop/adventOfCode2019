pw_range = (273025,767253)

def pw_check(int_num):
    '''
    This is a more elegant solution aided by different reddits
    :param int_num: Integer number
    :return: count of adjacecies or False if the pw does not satisfy conditions
    '''
    digits = [int(x) for x in str(int_num)]
    adj_same = {}
    for idx, val in enumerate(digits):
        if idx + 1 < len(digits) and val == digits[idx + 1]:
            if val not in adj_same.keys():
                adj_same[val] = 0
            adj_same[val] += 1
        if idx + 1 < len(digits) and val > digits[idx + 1]:
            return False
    return list(adj_same.values()) or False

print(len([x for x in range(*pw_range) if pw_check(x)]))  # Part1
print(len([x for x in range(*pw_range) if pw_check(x) and 1 in pw_check(x)]))  # Part2
