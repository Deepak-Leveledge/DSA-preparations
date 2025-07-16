def closestToZero(arr, n):
    arr.sort()
    l = 0
    r = n - 1
    max_sum = arr[l] + arr[r]
    minabs = abs(max_sum)
    while l < r:
        current_sum = arr[l] + arr[r]
        mincurret_sum = abs(current_sum)
        
        if mincurret_sum < minabs:
            minabs = mincurret_sum
            max_sum = current_sum
            
        if current_sum < 0:
            l += 1
        else:
            r -= 1
            
    return max_sum


arr = [-8 -66 -60]
n = len(arr)
print(closestToZero(arr,n))
      