#include <iostream>

#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

string biggest = "0";
unordered_set<string> visited;

void rem_char(string s, int target, int pi = 0) {
  for(int i = s.length() - pi - 1; i >= 0 ; i--) {
    string newStr = s;
    newStr.erase(i, 1);
    // Check if it is already visited
    if(visited.count(newStr)) {
      cout << "Already checked\n";
      continue;
    }
    if(newStr.length() > target) {
      int npi = newStr.length() - i;
      // cout << newStr << " " << npi << endl;
      rem_char(newStr, target, npi);
    } else {
      cout << newStr << endl;
      if(biggest.compare(newStr)<0) {
        biggest = newStr;
      }
    }
    visited.insert(newStr);
  }
}

string solution(string number, int k) {
    string answer = "";

    rem_char(number, number.length() - k);

    // int largest = biggest;

    // answer = to_string(largest);
    return biggest;
}

int main(void) {
  cout << "Test" << endl;
  // rem_char("1111", 2);
  cout << solution("123424123123331231231237890", 15) << endl;
  // cout << solution("1924", 2) << endl;
  // cout << solution("1231234", 3) << endl;
  // cout << solution("1111", 2) << endl;
  return 0;
}