"""

th distance
Difficulty: EasyAccuracy: 48.69%Submissions: 44K+Points: 2

Given an unsorted array arr and a number k which is smaller than the size of the array. Return true if the array contains any duplicate within k distance throughout the array else false.

Examples:

Input: arr[] = [1, 2, 3, 4, 1, 2, 3, 4], k = 3
Output: false
Explanation: All duplicates are more than k distance away.

Input: arr[] = [1, 2, 3, 1, 4, 5], k = 3
Output: true
Explanation: 1 is repeated at distance 3.

Input: arr[] = [6, 8, 4, 1, 8, 5, 7], k = 3
Output: true
Explanation: 8 is repeated at distance 3.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ k < arr.size()
1 ≤ arr[i] ≤ 105
"""


def Duplicatewithi_k(arr,k):  ## This solution pass all the text cases in the platform
    seen = set()
    for i in range(len(arr)):
        if arr[i] in seen:
            return True
        seen.add(arr[i])
        if len(seen)>k:
            seen.remove(arr[i-k])
    return False


arr = [6, 8, 4, 1, 8, 5, 7]
k = 3
print(Duplicatewithi_k(arr,k))



# def Duplicate_within_k(arr,k):   ## This solution pass some tast case so do not use this solution
#     n=len(arr)
#     l=0
#     r= len(arr)-1
#     while l<r:
#         if arr[l]==arr[r] and arr[l-r+1]==k: 
#             return True
#         else:

#             r-=1

#     return False


# arr = [6, 8, 4, 1, 8, 5, 7]
# k = 3
# print(Duplicate_within_k(arr,k))