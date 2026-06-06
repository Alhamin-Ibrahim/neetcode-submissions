class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        middle = None
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                middle = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else: 
                l = mid + 1
        
        if middle is None:
            return False
        
        l, r = 0, len(matrix[middle])
        while l <= r:
            mid = (l + r) // 2
            if matrix[middle][mid] == target:
                return True
            elif target < matrix[middle][mid]:
                r = mid - 1
            else: 
                l = mid + 1
        return False