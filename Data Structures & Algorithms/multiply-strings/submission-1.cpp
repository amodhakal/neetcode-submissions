class Solution {
public:
    string multiply(string num1, string num2) {
        unsigned long long int1 = 0;
        unsigned long long int2 = 0;

        for ( const auto ch: num1) {
            int1 *= 10;
            int1 += ch - '0';
        }

        for ( const auto ch: num2) {
            int2 *= 10;
            int2 += ch - '0';
        }

        unsigned long long value = int1 * int2;
        return to_string(value);
    }
};
