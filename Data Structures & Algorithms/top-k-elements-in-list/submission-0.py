class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 1
                continue
            frequencyMap[num] += 1

        frequencyHeap = []
        heapq.heapify(frequencyHeap)

        for num, count in frequencyMap.items():
            result = (-count, num)
            print(result)
            heapq.heappush(frequencyHeap, result)

        toReturn = []
        for i in range(k):
            count, num = heapq.heappop(frequencyHeap)
            toReturn.append(num)

        return toReturn
        