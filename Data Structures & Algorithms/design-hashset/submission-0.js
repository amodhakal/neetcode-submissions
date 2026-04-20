class MyHashSet {
    items

    constructor() {
        this.items = []
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        if ( this.contains(key)) {
            return
        }

        this.items.push(key)
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        this.items = this.items.filter(item => item != key)
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        return this.items.filter(item => item == key).length > 0
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
