#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
  public:
  bool isPalindrome(ListNode *head) {
    if(head->next == nullptr) return true;
    ListNode *rabbit = head;
    ListNode *turtle = head;
    ListNode *prev = nullptr;
    ListNode *tnext = nullptr;
    bool isEven = true;
    // Rush to center
    while(rabbit != nullptr && isEven) {
      // Move Rabbit
      if (rabbit->next == nullptr) {
        cout << "Is ODD\n";
        isEven = false;
        rabbit = nullptr;
      } else rabbit=rabbit->next->next;

      tnext = turtle->next;
      turtle->next = prev;
      prev = turtle;
      turtle = tnext; // Move turtle
    }

    cout << "prev: " << prev->val << "  curr" << turtle->val << endl;

    // EVEN Check
    if (isEven) {
      if(turtle->val != prev->val) return false;
      // turtle = turtle->next;
    } else {
      prev = prev->next;
    }

    // Check match
    while(prev != nullptr && turtle != nullptr) {
      cout << "CMP - prev: " << prev->val << "  turtle" << turtle->val << endl;
      if(prev->val != turtle->val) return false;
      prev = prev->next;
      turtle = turtle->next;
    }
    return true;
  }
};

// TC
int main(void) {
  ListNode *ln;
  Solution so;
  ln = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(2, new ListNode(1)))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
  ln = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(2, new ListNode(2)))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
  ln = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(1, new ListNode(1)))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
  ln = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(1))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
  ln = new ListNode(1, new ListNode(2, new ListNode(2, new ListNode(2))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
  ln = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(1))));
  cout << (so.isPalindrome(ln) ? "YES" : "NO") << "\n" << endl;
}