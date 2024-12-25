<h2><a href="https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1">Set Matrix Zeroes</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given a 2D matrix <strong>mat</strong>[][] of size </span><span style="font-size: 18px;"><strong>n×m</strong>.&nbsp;</span><span style="font-size: 18px;">The task is to modify the matrix such that if <strong>mat[i][j]</strong> is 0, all the elements in the&nbsp;</span><span style="font-size: 18px;"><strong>i</strong>-th row and </span><span style="font-size: 18px;"><strong>j</strong>-th column are set to 0 </span><span style="font-size: 18px;">and do it in <strong>constant space complexity</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">mat[][] = [[1, -1, 1],
                [-1, 0, 1],
                [1, -1, 1]]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;"> </span></span><span style="font-size: 18px;">mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.</span></pre>
<pre><span style="font-size: 18px;"><strong style="font-size: 18px;">Input: </strong><span style="font-size: 18px;">mat[][] = [[0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]]
</span><strong style="font-size: 18px;">Output:</strong><span style="font-size: 18px;"> [[0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]]
</span><strong style="font-size: 18px;">Explanation:</strong><span style="font-size: 18px;"> </span></span><span style="font-size: 18px;">mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ n, </span><span style="font-size: 18px;">m</span><span style="font-size: 18px;"> ≤ 500</span><sup><br></sup><span style="font-size: 18px;">- 2<sup>31</sup> ≤ mat[i][j] ≤ 2<sup>31</sup> - 1</span></p></div>