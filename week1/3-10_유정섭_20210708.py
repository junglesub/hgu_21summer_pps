from typing import List

import re

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        # if 4 numbers assume that one each.
        if len(s) == 4:
          return ['.'.join(list(s))]
        # leading zero check
        l0 = re.compile("0.")
        for a in range(1, len(s)):
          fir = s[:a]
          if int(fir) > 255 or l0.match(fir): continue
          for b in range(a + 1, len(s)):
            sec = s[a:b]
            if int(sec) > 255 or l0.match(sec): continue
            for c in range(b + 1, len(s)):
              thrd = s[b:c]
              fort = s[c:]
              if int(thrd) > 255 or int(fort) > 255 or l0.match(thrd) or l0.match(fort): continue
              answer.append("%s.%s.%s.%s" % (fir, sec, thrd, fort))
        return answer

# Test Case
t1 = Solution.restoreIpAddresses(None, "25525511135")
print(t1)