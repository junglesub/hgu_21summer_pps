#include <iostream>
#include <unordered_set>

using namespace std;

int main(int argc, char** argv) {
  int test_case;
  int T;
  cin >> T;
  /*
     여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
  */
  for (test_case = 1; test_case <= T; ++test_case) {
    int a = 0, b = 0, c = 0;
    string s;
    cin >> s;

    // Use enhanced for-loop if c++11 works.
    for (int i = 0; i < s.length(); i++) {
      switch(s[i]) {
        case 'a':
          a++;
          break;
        case 'b':
          b++;
          break;
        case 'c':
          c++;
          break;
      }
    }
    unordered_set<int> counter; // Cant use {a, b, c} method. c++11 is not supported
    counter.insert(a);
    counter.insert(b);
    counter.insert(c);

    // cout << counter.size();

    


    cout << "#" << test_case << " ";
    
    if(a < 1 && b < 1 && c < 1) cout << "YES";
    else if(counter.size() == 1) cout << "YES";
    else if (counter.size() == 2) {
      unordered_set<int>::iterator it = counter.begin();
      int a = *it;
      int b = *++it;
      // cout << a << b;
      cout << (abs(a - b) <= 1 ? "YES" : "NO"); // 여기도 생각이 약간 꼬임..
    }
    else cout << "NO";
    cout << endl;

    /////////////////////////////////////////////////////////////////////////////////////////////
    /*
             이 부분에 여러분의 알고리즘 구현이 들어갑니다.
     */
    /////////////////////////////////////////////////////////////////////////////////////////////
  }
  return 0;  //정상종료시 반드시 0을 리턴해야합니다.
}