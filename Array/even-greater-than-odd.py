
"""

Even Greater than Odd
Difficulty: EasyAccuracy: 49.91%Submissions: 12K+Points: 2

Given an array arr, rearrange the array according to the following relations :

    arr[i] >= arr[i-1], if i is even.
    arr[i] <= arr[i-1], if i is odd.
    [Considering 1-base indexed array]

Return the rearranged array.

Note: The driver code will print "true" if your output array satisfies the conditions; otherwise, it will print "false".

Example:

Input: arr[] = [1, 2, 2, 1]
Output: [1, 2, 1, 2]
Explanation: Both 2s are at even positions and 1s at odd positions, satisfying the given conditions.

Input: arr[] = [1, 3, 2]
Output: [1, 3, 2]
Explanation: The array is already arranged according to the conditions.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
"""










def evenisgrsterthanodd(arr):
    for i in range(1,len(arr)):
        if i %2 ==1:
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
        else:
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]

    return arr



arr=[1, 2, 2, 1]
print(evenisgrsterthanodd(arr)) 