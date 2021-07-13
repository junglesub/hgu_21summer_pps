#include <iostream>
// #include <vector>

using namespace std;

class Solution {
public:
    string removeDuplicates(string s) {
        // vector<char> result;
        string sresult;
        for(int i = 0; i < s.length(); i++) {
            if(!sresult.empty() && sresult.back() == s[i]) {
                // while(result.back() == s[i]){ // 2개 이상일경우.
                //     i++;
                // }
                // i--; // 맞추기.
                sresult.pop_back();
            } else {
                sresult.push_back(s[i]);
            }
        }
        // for(int i = 0; i < result.size(); i++) sresult = sresult + result[i];
        return sresult;
    }
};

// TC
int main(void){
    Solution s;
    cout << s.removeDuplicates("abbaca") << endl;
    return 0;
}