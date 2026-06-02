class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    sortArray(nums) {
        let maxNum = 0
        for ( const num of nums) {
            if ( num > maxNum) {
                maxNum = num
            }
        }

        const maxDigit = `${maxNum}`.length
        console.log(maxDigit)

        let collected = nums
        for ( let currentDigit = 0; currentDigit < maxDigit; currentDigit++) {
            const buckets = [[], [], [], [], [], [], [], [], [], [], []]

            for ( const num of collected) {
                const index = Math.floor(num / (10 **currentDigit)) % 10
                buckets[index].push(num)
            }

            collected = []
            for ( const bucket of buckets) {
                for ( const value of bucket) {
                    collected.push(value)
                }
            }

            console.log(collected)
        }

        return collected
    }
}
