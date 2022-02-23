# Function that returns the median of an array whose length is odd

def median(arrArg):
    num = len(arrArg)
    mid = num // 2
    for i in range(num):
        min = i
        for j in range(i, num):
            if arrArg[j] < arrArg[min]:
                min = j
        arrArg[i], arrArg[min] = arrArg[min], arrArg[i]
        
    return arrArg[mid]
        

print(median([4, 10, 7, 6, 3, 1, 2]))