# This Function sorts a list without comparing list items

def optimizedSort(ar):
    optArr = []
    uniqArr = []
    modelArr = [0] * (max(ar) + 1)

    for i in ar:
        if i not in uniqArr:
            uniqArr.append(i)
    
    for i in range(len(modelArr)):
        for j in ar:
            if j == i:
                modelArr[i] += 1
    
    for i, val in enumerate(modelArr):
        if modelArr[i] != 0:
            for j in range(val):
                optArr.append(i)

    return optArr



print(optimizedSort([5, 2, 3, 8, 8, 1, 2]))
# prints [1, 2, 2, 3, 5, 8, 8]