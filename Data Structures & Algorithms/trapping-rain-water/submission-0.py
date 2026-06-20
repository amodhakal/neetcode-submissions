class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]
        rightmax = [0 for i in range(len(height))]
        count = 0

        for i in range(1, len(height)):
            size = height[i]
            leftmax.append(max(size, leftmax[i - 1]))

        for i in range(len(height) - 2, -1, -1):
            size = height[i]
            rightmax[i] = (max(size, rightmax[i + 1]))
        
        for i in range(len(height)):
            minholder = min(leftmax[i], rightmax[i])
            difference = minholder - height[i]
            if difference > 0:
                count += difference

        return count