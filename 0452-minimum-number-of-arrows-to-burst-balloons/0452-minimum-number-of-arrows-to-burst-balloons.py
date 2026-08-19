class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
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
        