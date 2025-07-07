"""
14. Longest Common Prefix
Easy
Topics
premium lock iconCompanies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.


"""
strs = ["dog","racecar","car"]

def longestCommonPrefix(strs):
    if not strs:
        return " "
    

    shortest_str = min(strs,key=len)


    for i , char in enumerate(shortest_str): ##  {0:"f", 1:"l", 2:"o", 3:"w"}
        for s  in strs:
            if s[i]!=char:
                return shortest_str[:i]
                
    return shortest_str

result = longestCommonPrefix(strs)
print(result)


 