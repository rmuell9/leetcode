# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        strs.remove(strs[0])
        for str in strs:
            while res not in str[:len(res)]:
                res = res[:-1]
        return res
