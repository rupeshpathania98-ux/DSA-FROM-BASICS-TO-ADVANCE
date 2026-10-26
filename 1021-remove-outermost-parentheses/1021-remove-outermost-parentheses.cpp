
class Solution {
public:
    string removeOuterParentheses(string s) {
        string ans;
        int n = s.size();

        for (int start = 0; start < n; ) {
            int end = start;
            int balance = 0;

            while (end < n) {
                if (s[end] == '(') {
                    balance++;
                } else {
                    balance--;
                }

                end++;

                if (balance == 0) {
                    break;
                }
            }

            // Remove the outermost parentheses
            for (int i = start + 1; i < end - 1; i++) {
                ans += s[i];
            }

            start = end;
        }

        return ans;
    }
};
