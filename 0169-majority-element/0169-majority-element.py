class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        
        candidate = -1
        votes = 0
            
        # Finding majority candidate
        for i in range (len(arr)):
            if (votes == 0):
                candidate = arr[i]
                votes = 1
            else:
                if (arr[i] == candidate):
                    votes += 1
                else:
                    votes -= 1
                    
        count = 0
        for i in range(len(arr)):
            if arr[i] == candidate:
                count += 1

        if count > len(arr) // 2:
            return(candidate)
        else:
            return("-1")
             
        