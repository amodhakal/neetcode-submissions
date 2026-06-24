class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Choose a middle row where row[0] is <= val and val <= row[-1] 
        # Based on that move to left or right row

        rowl, rowr = 0, len(matrix) - 1

        # 0, 2
        # 1
        # 10, 13

        #0, 3


        while rowl <= rowr:
            mid = (rowl + rowr) // 2
            current = matrix[mid]
            start, end = current[0], current[-1]

            if start <= target and target <= end:
                coll, colr = 0, len(current) - 1

                while coll <= colr:
                    midcol = (coll + colr) // 2
                    midval = current[midcol]

                    if midval == target:
                        return True

                    if target > midval:
                        coll = midcol + 1

                    if target < midval:
                        colr = midcol - 1

                return False

            if target > end:
                rowl = mid + 1
            
            if target < start:
                rowr = mid - 1
        
        return False


