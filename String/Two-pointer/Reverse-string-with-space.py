"""
Reverse a string with spaces intact
Difficulty: BasicAccuracy: 48.48%Submissions: 12K+Points: 1
Given a string, your task is to reverse the string keeping the spaces intact to their positions.

Example 1:

Input:
S = "Help others"
Output: sreh topleH
Explanation: The space is intact at index 4
while all other characters are reversed.
Example 2:

Input: 
S = "geeksforgeeks"
Output: skeegrofskeeg
Explanation: No space present, hence the
entire string is reversed.

Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseWithSpacesIntact() which takes the string S as input and returns the resultant string by reversing the string while keeping all the spaces intact.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


"""


def reversethestringwithoutloosingposition(str):
    str =list(str)
    start=0
    end=len(str)-1
    while start<end:
        if str[start]==' ':
            start+=1
        elif str[end]==' ':
            end-=1
        else:
            str[start],str[end]=str[end],str[start]
            start+=1
            end-=1
    return "".join(str)



str="Deepak Gupta Baliram"
print(reversethestringwithoutloosingposition(str))