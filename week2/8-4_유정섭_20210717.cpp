#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      int cnt = 0;
      int last = -101;
      for(int i = 0; i < nums.size(); i++) {
        if(nums[i] != last) {
          cnt++;
          last = nums[i];
        } else {
          nums.erase(next(nums.begin(), i--));
        }
      }
      return cnt;
    }
};

// TC
int main(int argc, char const *argv[])
{
  vector<int> tv;
  tv.push_back(1);
  tv.push_back(2);
  tv.push_back(2);

  Solution s;
  cout << s.removeDuplicates(tv) << endl;

  for(int val : tv) {
    cout << val << endl;
  }
  return 0;
}
