#include <iostream>
using namespace std;

int main(void) {
  string input;
  cin >> input;
  for(int i = 0; i < input.length(); i++) {
    cout << input[i];
    if((i + 1) % 10 == 0) cout << endl;
  }
  return 0;  
}