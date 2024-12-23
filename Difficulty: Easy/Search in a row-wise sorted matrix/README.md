<h2><a href="https://www.geeksforgeeks.org/problems/search-in-a-row-wise-sorted-matrix/1">Search in a row-wise sorted matrix</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given a row-wise sorted 2D matrix <strong>mat</strong>[][] of size <strong>n x m&nbsp;</strong>and<strong>&nbsp;</strong>an integer <strong>x,</strong> find whether element <strong>x</strong> is present in the matrix.<br>Note: In a row-wise sorted matrix, each row is sorted in itself, i.e. for any i, j within bounds, mat[i][j] &lt;= mat[i][j+1].</span><br style="font-size: 18px;"><br><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[3, 4, 9],[2, 5, 6],[9, 25, 27]], x = 9
<strong>Output</strong>: true
<strong>Explanation</strong>: 9 is present in the matrix, so the output is true.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[19, 22, 27, 38, 55, 67]], x = 56<br><strong>Output</strong>: false
<strong>Explanation</strong>: 56 is not present in the matrix, so the output is false.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input</strong>: mat[][] = [[1, 2, 9],[65, 69, 75]], x = 91</span><br><span style="font-size: 14pt;"><strong>Output</strong>: false
<strong>Explanation</strong>: 91 is not present in the matrix.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:<br></strong>1 &lt;= n, m &lt;= 1000<br>1 &lt;= mat[i][j] &lt;= 10<sup>5</sup><br>1 &lt;= x &lt;= 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search</code>&nbsp;<code>Arrays</code>&nbsp;<code>Matrix</code>&nbsp;