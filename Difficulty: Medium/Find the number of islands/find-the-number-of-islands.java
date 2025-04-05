//{ Driver Code Starts
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();
        while (tc-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            char[][] grid = new char[n][m];

            // Read the grid input
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    grid[i][j] = scanner.next().charAt(0);
                }
            }
            Solution obj = new Solution();
            int ans = obj.countIslands(grid);
            System.out.println(ans);
            System.out.println("~");
        }
        scanner.close();
    }
}

// } Driver Code Ends


class Solution {
    // Directions for 8 neighbors: N, NE, E, SE, S, SW, W, NW
    int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    // Check if the cell is within bounds and is land
    private boolean isValid(int i, int j, int n, int m, char[][] grid) {
        return (i >= 0 && j >= 0 && i < n && j < m && grid[i][j] == 'L');
    }

    public int countIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int count = 0;

        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 'L') {
                    count++;
                    queue.offer(new int[]{i, j});
                    grid[i][j] = 'S'; // Mark as visited

                    while (!queue.isEmpty()) {
                        int[] current = queue.poll();
                        int x = current[0];
                        int y = current[1];

                        for (int k = 0; k < 8; k++) {
                            int newX = x + dx[k];
                            int newY = y + dy[k];

                            if (isValid(newX, newY, n, m, grid)) {
                                grid[newX][newY] = 's'; // Mark as visited
                                queue.offer(new int[]{newX, newY});
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
}