class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        flag = False
        j = 0

        if s == "":
            return True
        
        elif len(s) > len(t):
            return False
        
        else:
            for i in range(len(t)):
                if j < len(s) and t[i] == s[j]:
                    flag = True
                    j += 1

                if j == len(s):
                    return True

            return False