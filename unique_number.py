def find_uniq(arr):
    for i in arr:
        a = arr.count(i)
        print(f'{i}) {a}')
    
    # return n 

find_uniq([ 1, 1, 1, 2, 1, 1 ])