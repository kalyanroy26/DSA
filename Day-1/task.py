# program to find diagonal in a matrix
list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,7,2],
    [1,2,3,4]
]

is_diagonal = False

for sub in list:
    if len(sub)==len(list):
        is_diagonal = True
    else:
        print('Not a Square Matrix')

if is_diagonal:
    i = 0
    diagonal = []
    for sub in list:
        diagonal.append(sub[i])
        i+=1
print("diagonal: "+diagonal)

#program to find max length in matrix

matrix = [
    [1,2,3,4],
    [5,6,7,8,10,14],
    [9,0,7,2,4],
    [1,2,3,4]
]

def max_ele(list):
    max = list[0]

    for sub in list:
        if len(sub)>len(max):
            max = sub
    return max

print("max sublist: " + max_ele(matrix))


