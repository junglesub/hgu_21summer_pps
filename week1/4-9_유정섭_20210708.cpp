// 공식 진짜 없는것인가..

#include <iostream>

using namespace std;

int main(void) {
  int e, s, m;
  cin >> e >> s >> m;
  int year = 1;

  while(true) {
    if(year % 15 == e % 15 && year % 28 == s % 28 && year % 19 == m % 19) {
      cout << year;
      return 0;
    }
    year++;
  }
  return 0;
}