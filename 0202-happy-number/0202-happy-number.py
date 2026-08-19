class Solution:
    def isHappy(self, n: int, seen: set = None) -> bool:
        if seen is None:
            seen = set()
        
        if n == 1:
            return True
        
        digits = [int(d) for d in str(n)]
        result = sum(d**2 for d in digits)
        
        if result in seen:
            return False
        
        seen.add(result)
        
        return self.isHappy(result, seen)