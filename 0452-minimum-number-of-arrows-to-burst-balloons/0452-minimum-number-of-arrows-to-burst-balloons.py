class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
Created on Wed Aug 19 14:54:14 2026

@author: mahmed2


Sorted by xstart: [1,6], [2,8], [7,12], [10,16] (already sorted here).

Step 1: Start with balloon [1,6]. Set arrow_pos = 6. Arrow count = 1 
    (you know you'll need at least this one arrow).

Step 2: Next balloon [2,8]. Compare its xstart (2) to arrow_pos (6). Is 2 <= 6? 
    Yes → it overlaps → this balloon is popped by the same arrow, so arrow count stays at 1. 
    Now update: arrow_pos = min(6, 8) = 6. (Still 6, unchanged this time.)

Step 3: Next balloon [7,12]. Compare its xstart (7) to arrow_pos (6). 
    Is 7 <= 6? No → it does not overlap → this needs a new arrow → arrow count becomes 2. 
    Reset arrow_pos = 12 (the xend of this new balloon).

Step 4: Next balloon [10,16]. Compare its xstart (10) to arrow_pos (12). 
    Is 10 <= 12? Yes → overlaps with the second arrow's group → count stays at 2. 
    Update arrow_pos = min(12, 16) = 12.

Done. Final count = 2. Matches the expected answer.

"""
        count = 1
        points.sort()
        arrow_pos = points[0][1]
        for i in points[1:]:
            if (len(points)==1):
                return 1 
            if (i[0] <= arrow_pos):
                arrow_pos = min(arrow_pos, i[1])
            else:
                arrow_pos = i[1]
                count += 1
        return count
        