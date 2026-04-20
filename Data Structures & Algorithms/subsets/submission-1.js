class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        const newArray = [[]]
        for ( const num of nums) {
            const newValues = []

            for (const item of newArray) {
                newValues.push([...item, num])
            }

            newArray.push(...newValues)
        }

        return newArray
    }
}
