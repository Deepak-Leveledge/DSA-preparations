

"""
You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.

Examples:

Input: arr = [1, 4, 3, 2, 6, 5]
Output: [5, 6, 2, 3, 4, 1]
Explanation: The elements of the array are 1 4 3 2 6 5. After reversing the array, the first element goes to the last position, the second element goes to the second last position and so on. Hence, the answer is 5 6 2 3 4 1.
Input: arr = [4, 5, 2]
Output: [2, 5, 4]
Explanation: The elements of the array are 4 5 2. The reversed array will be 2 5 4.
Input: arr = [1]
Output: [1]
Explanation: The array has only single element, hence the reversed array is same as the original.
Constraints:
1<=arr.size()<=105
0<=arr[i]<=105
"""

def reverse_array(arr):
    start=0
    end= len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1



result = [1, 4, 3, 2, 6, 5]
arr=[1,32,5,41,65,1,8,5,1,5,21,8,2]

reverse_array(arr)
print(arr)