<h2><a href="https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1">Count the number of possible triangles</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an integer array <strong>arr[]</strong>. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle.&nbsp;</span></p>
<blockquote>
<p><span style="font-size: 18px;">A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.</span></p>
</blockquote>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [4, 6, 3, 7]
<strong>Output</strong>: 3
<strong>Explanation</strong>: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.  <br></span></pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [10, 21, 22, 100, 101, 200, 300]
<strong>Output</strong>: 6
<strong>Explanation</strong>: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], [100, 101, 200] and [101, 200, 300]</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [1, 2, 3]
<strong>Output</strong>: 0
<strong>Explanation</strong>: No triangles are possible.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>3 &lt;= arr.size() &lt;= 10<sup>3</sup></span><br><span style="font-size: 18px;">1 &lt;= arr[i] &lt;= 10</span><sup>5</sup></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Sorting</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;