def findsumofsubaaray(arr):
    currentsum=0
    for i in range(0,len(arr)):
        temp=0
        for j in range(i,len(arr)):
            temp+=arr[j]
            currentsum+=temp
            
    return currentsum

arr=[1, 2, 3]
print(findsumofsubaaray(arr))
