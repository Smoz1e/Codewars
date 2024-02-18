def persistence(n):
    lists = []
    lists2 = []
    for i in str(n):
        lists.append(i)
    print(lists)
    
    while len(lists)>1:
        for i in lists:
            i = int(i)* int(i)
            print(i)
            break
            


persistence(39)