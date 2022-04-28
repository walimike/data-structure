def non_divisible_subset(k, s):
    new_array = []
    # new_array.append(s[0])
    for item in s:
        for y in s[(s.index(item)):]:
            if ((item+y)%k) != 0:
                new_array.append(y)
                print(s[(s.index(item)):])
    # print(new_array)
non_divisible_subset(3, [1,7,2,4])