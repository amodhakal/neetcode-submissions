class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {
        let res = 0
        let currsum = 0
        const prefix_map = new Map()
        prefix_map.set(0, 1)
        for ( const num of nums) {
            currsum += num
            const diff = currsum - k

            res += prefix_map.get(diff) || 0;
            prefix_map.set(currsum, 1 + (prefix_map.get(currsum) || 0))
        }

        return res
    }
}
