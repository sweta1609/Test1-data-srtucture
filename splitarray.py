def split(arr, i, sumLeft, sumRight):
    
    if (i == len(arr)):
        return sumLeft == sumRight

    if (arr[i] % 5 == 0):
        sumLeft += arr[i]

    elif (arr[i] % 3 == 0):
        sumRight += arr[i]
    else:
        return (split(arr,i + 1, sumLeft + arr[i], sumRight) or split(arr, i + 1, sumLeft, sumRight + arr[i]));

    return split(arr, i + 1, sumLeft, sumRight)

    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr,0,0,0)
if ans is True:
    print('true')
else:
    print('false')
