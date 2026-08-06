class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = []
        hashmap = {}
        if len(s)<1:
            return 0
        else:            
            for i in range(len(s)):
                if s[i] not in window:
                    window.append(s[i])
                    hashmap[len(window)] = window

                else:
                    while s[i] in window: 
                        window.pop(0) 
                    window.append(s[i])
                    hashmap[len(window)] = window

    
            return max(hashmap.keys(), default=len(window))  