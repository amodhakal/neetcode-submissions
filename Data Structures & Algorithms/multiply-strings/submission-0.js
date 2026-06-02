class Solution {
    /**
     * @param {string} num1
     * @param {string} num2
     * @return {string}
     */
    multiply(num1, num2) {
        let int1 = 0
        let int2 = 0

        for (const ch of num1) {
            const digit = ch - '0'
            int1 *= 10;
            int1 += digit
        }

        for (const ch of num2) {
            const digit = ch - '0'
            int2 *= 10;
            int2 += digit
        }

        return (int1 * int2).toString()
    }
}
