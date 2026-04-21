class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;

        while ( n > 0) {
            int map = n & 1;
            if (map == 1) {
                count++;
            }

            n = n >> 1;
        }

        return count;
    }
};
