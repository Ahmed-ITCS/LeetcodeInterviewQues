class Solution {
public:
    string longestPalindrome(string s) {
        string longest = "";
        for (int i = 0; i < s.size(); i++) {
            for (int j = i; j < s.size(); j++) {
                string substr = s.substr(i, j - i + 1);
                if (substr == string(rbegin(substr), rend(substr)) && substr.size() > longest.size()) {
                    longest = substr;
                }
            }
        }
        return longest;
    }
};
