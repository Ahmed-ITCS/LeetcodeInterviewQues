class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = ""
        check = ""
        for i in s:
            if i in check:
                return int(len(answer))
            else:
                check = check +  i
                answer= answer + i
        return int(len(answer))