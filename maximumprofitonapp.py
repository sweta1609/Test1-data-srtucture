def maximumProfit(arr):
    num=len(arr)
    arr.sort()
    m=0
    for i in arr:
        if m<i*num:
            m=i*num
        num-=1
    return m

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)
