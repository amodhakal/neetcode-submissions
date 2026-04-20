class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsets(nums) {
        return nums.reduce((prev, curr) => prev.concat(prev.map((k) => [...k, curr])), [[]]);
    }
}
