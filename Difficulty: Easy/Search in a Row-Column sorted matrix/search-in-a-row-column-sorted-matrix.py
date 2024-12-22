#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
	    n  = len(mat)
	    m = len(mat[0])
	    for i in range(n):
	        for j in range(m):
	            if mat[i][j] == x: 
	                return True
	    return False
	        
		# Complete this function


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends