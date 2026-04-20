class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const result = [[]]
        for (const num of nums) {
            const newValues = []
            for (const item of result) {
                newValues.push(([...item, num]))
            }

            result.push(...newValues)
        }

        return result
    }
}
