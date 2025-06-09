# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        #code here
        if a==b:
            return 1
        return 0