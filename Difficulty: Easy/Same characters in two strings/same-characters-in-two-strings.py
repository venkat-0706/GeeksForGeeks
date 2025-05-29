#User function Template for python3

class Solution:

    def sameChar(self, A, B):
        # code here
        A=A.lower()
        B=B.lower()
        count=0
        for i in range(len(A)):
            if A[i]==B[i]:
                count+=1
        return count
            
