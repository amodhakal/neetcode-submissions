class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        let commonStr = Array.from(strs[0])

        for ( const item of strs) {
            const itemLength = item.length
            commonStr = commonStr.filter((_, idx) => idx < itemLength - 1)

            for ( let idx = 0; idx < item.length; idx++) {
                console.log(commonStr)
                if (idx > commonStr.length - 1) {
                    break
                }

                const commonItem = commonStr[idx]
                if (commonItem != item[idx]) {
                    commonStr = commonStr.filter((item, idx2) => idx2 < idx)
                    break
                }
            }
        }

        let returningString = ""
        for ( const ch of commonStr) {
            returningString += ch
        }

        return returningString
    }
}
