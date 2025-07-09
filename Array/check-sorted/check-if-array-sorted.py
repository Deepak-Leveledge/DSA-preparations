"""
Check if array is sorted
Difficulty: EasyAccuracy: 39.37%Submissions: 269K+Points: 2Average Time: 15m

Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.

Constraints:
1 ≤ arr.size ≤ 106
- 109 ≤ arr[i] ≤ 109

"""


def check_sorted(arr):
     n=len(arr)
     if (n==0 or n==1):
          return True
     for i in range(1,n):
          if arr[i-1]>arr[i]:
               return False
     return True


arr=[10,20,30,40,50]
arr1=[90,80,100,70,40,30]
arr2=[1,2,3,4,5]
print(check_sorted(arr))
print(check_sorted(arr1))
print(check_sorted(arr2))