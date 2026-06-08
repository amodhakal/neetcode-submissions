class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxdict = { num: [] for num in nums}
        for idx in range(len(nums)):
            num = nums[idx]
            idxdict[num].append(idx)

        for idx in range(len(nums)):
            num = nums[idx]
            required = target - num
            if required not in idxdict:
                continue

            availableidxs = idxdict[required]
            for available in availableidxs:
                if idx == available:
                    continue
                
                return [idx, available ]

        return [0, 0]

            
        