#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s== s[::-1]:
            return True
        else:
            return False
		# code here