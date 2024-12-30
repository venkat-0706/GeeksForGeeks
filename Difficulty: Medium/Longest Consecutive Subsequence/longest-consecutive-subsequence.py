 #User function Template for python3
 


class Solution:
    def longestConsecutive(self,arr):
        arr=sorted(set(arr))
        mx=lth=1
        prv=-float('inf')
        for ve in arr:
            if ve==prv+1:
                lth+=1
                mx=max(mx,lth)
            else:
                lth=1
            prv=ve
        return mx
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends