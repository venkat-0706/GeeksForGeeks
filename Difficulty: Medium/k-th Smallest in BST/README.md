<h2><a href="https://www.geeksforgeeks.org/problems/find-k-th-smallest-element-in-bst/1">k-th Smallest in BST</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a BST and an integer <strong>k, </strong>the task is to find the <strong>kth</strong> smallest element in the BST. If there is no kth smallest element present then return -1.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> root = [2, 1, 3], k = 2
&nbsp;   <img style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700236/Web/Other/blobid1_1738413633.png" alt="" width="269" height="217">
<strong>Output: </strong>2
<strong>Explanation:</strong> 2 is the 2nd smallest element in the BST.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> root = [2, 1, 3], k = 5
    <img style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700236/Web/Other/blobid1_1738413633.png" alt="" width="274" height="221">
<strong>Output: </strong>-1
<strong>Explanation:</strong> There is no 5th smallest element in the BST as the size of BST is 3.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], k = 3<br></span><span style="font-size: 18px;">    <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700498/Web/Other/blobid1_1736918049.jpg" width="270" height="241"> <br></span><span style="font-size: 18px;"><strong>Output: </strong>10
<strong>Explanation:</strong> 10 is the 3rd smallest element in the BST.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br></span></p>
<ul>
<li><span style="font-size: 18px;">1 &lt;= number of nodes, k &lt;= 10<sup>5<br></sup></span></li>
<li><span style="font-size: 18px;">1 &lt;= node-&gt;data &lt;= 10<sup>5</sup><sup><br></sup></span></li>
</ul></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Data Structures</code>&nbsp;