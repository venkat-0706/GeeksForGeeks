#User function Template for python3

class Solution:
     def nQueen(self, n):
        
        def get_diagonal(row, col):
            return n - 1 - col + row
            
        def get_antidiagonal(row, col):
            return col + row
        
        # True values indicate these aren't used yet
        rows = [True] * n
        diagonals = [True] * (2 * n - 1)
        antidiagonals = [True] * (2 * n - 1)
        
        def dfs(col=0, acc=[], paths=[]):
            if col == n:
                paths.append(acc.copy())
                return paths
            for row in range(n):
                d = get_diagonal(row, col)
                ad = get_antidiagonal(row, col)
                if rows[row] and diagonals[d] and antidiagonals[ad]:
                    rows[row] = diagonals[d] = antidiagonals[ad] = False
                    acc.append(row + 1)
                    dfs(col + 1)
                    acc.pop()
                    rows[row] = diagonals[d] = antidiagonals[ad] = True
            return paths
        
        return dfs()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends