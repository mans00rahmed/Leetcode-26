class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        if len(s)<=1:
            return True
        else:
            flag=False
            j = len(s)-1
            for i in range(len(s)):
                if s[i]==s[j]:
                    flag =True
                    j=j-1
                else:
                    flag=False
                    break
            return(flag)
                