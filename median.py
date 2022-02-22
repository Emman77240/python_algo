# Function that returns the median of an array whose length is odd

def median(arrArg):
    num = len(arrArg)
    for i in range(num):
        min = i
        for j in range(i, num):
            if arrArg[j] < arrArg[min]:
                min = j
        arrArg[i], arrArg[min] = arrArg[min], arrArg[i]
        
    return arrArg
        

print(median([5, 10, 7, 5, 3, 1, 2]))