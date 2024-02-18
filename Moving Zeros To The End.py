def move_zeros(lst):
    list_zero = []
    lists = []
    for i in lst:
        if i == 0:
            list_zero.append(i)
        else:
            lists.append(i)
    a = lists + list_zero
    print(a)

    return lst


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])