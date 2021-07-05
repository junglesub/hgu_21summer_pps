#include <vector>
#include <iostream>
using namespace std;

bool isPrime(int num) {
  for(int i = 2; i < num / 2; i++) {
    if(num % i == 0)
      return false;
  }
  return true;
}

int solution(vector<int> nums) {
    int answer = 0;

    for(int i = 0; i < nums.size(); i++) {
      for(int j = i + 1; j < nums.size(); j++) {
        for(int h = j + 1; h < nums.size(); h++) {
          if(isPrime(nums[i] + nums[j] + nums[h])) answer++;
        }
      }
    }
    return answer;
}

int main() {
  vector<int> tv;
  for(int i = 01; i <= 4; i++)
  tv.push_back(i);
  
  cout << solution(tv);
  return 1;
}