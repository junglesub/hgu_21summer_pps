class Solution:
    def isPalindrome(self, s: str) -> bool:
        fs = filter(lambda c: c.isalnum(), s)
        fs = "".join(fs)
        fs = fs.lower()
        return "".join(reversed(fs)) == fs

# TC
t1 = Solution.isPalindrome(None, "race a car")
print(t1)