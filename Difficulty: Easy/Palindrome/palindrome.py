class Solution:
    def isPalindrome(self, n):
        temp = str(n)
        if temp == temp[::-1]:
            return True
        else:
            return False
            
		# code here