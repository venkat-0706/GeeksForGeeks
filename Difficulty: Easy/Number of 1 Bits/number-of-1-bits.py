#User function Template for python3
class Solution:
	def setBits(self, n):
	    count = 0
	    while(n):
	        count+= n&1
	        n>>=1
	    return count
		# code here