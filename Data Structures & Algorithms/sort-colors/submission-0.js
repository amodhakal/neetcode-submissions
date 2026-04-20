class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums) {
        const colorCount = [ 0, 0, 0]
        for ( const num of nums) {
            colorCount[num]++
        }

        let currentIdx = 0;
        for ( let count = 0; count < colorCount[0]; count++) {
            nums[currentIdx++] = 0
        }

        for ( let count = 0; count < colorCount[1]; count++) {
            nums[currentIdx++] = 1
        }

        for ( let count = 0; count < colorCount[2]; count++) {
            nums[currentIdx++] = 2
        }
    }


}
