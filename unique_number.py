def find_uniq(arr):
    lsts = []
    lists = {}
    for i in arr:
        a = arr.count(i)
        lists[a] = i
        print(f'{i} повторений {a}')
    lsts.append(lists.keys())
    b = min(lsts)
    for m in b:
        lsts.clear()
        lsts.append(m)
    min_key = min(lsts)

    n = lists.setdefault(min_key)
    print(lists)
    print(lsts)
    print(min_key)
    print(n)
    return n 

find_uniq([0, 1, 1, 1, 1, 1, 1, 1])