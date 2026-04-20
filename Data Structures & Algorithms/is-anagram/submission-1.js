class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const foundItems = new Map()
        for ( const item of s) {
            if (foundItems.has(item)) {
                const count = foundItems.get(item)
                foundItems.set(item, count + 1)
                continue
            }

            foundItems.set(item, 1)
        }

        for ( const item of t) {
            if (!foundItems.has(item)) {
                return false
            }

            const count = foundItems.get(item)
            if ( count == 1) {
                foundItems.delete(item)
                continue
            }

            foundItems.set(item, count - 1)
        }

        return foundItems.size == 0
    }
}
