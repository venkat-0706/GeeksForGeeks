<h2><a href="https://www.geeksforgeeks.org/problems/k-sum-paths/1">K Sum Paths</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a <strong>binary tree</strong> and an integer <strong>k</strong>, determine the number of <strong>downward-only</strong> paths where the sum of the node values in the path equals <strong>k</strong>. A path can <strong>start and end at any node</strong> within the tree but must always move <strong>downward</strong> (from parent to child).</span></p>
<p><strong><span style="font-size: 18px;">Examples:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>k = 7   <br><strong><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700575/Web/Other/blobid0_1738924888.webp" width="318" height="243"><br>Output:</strong> 3</span>
<span style="font-size: 18px;"><strong>Explanation: </strong>The following paths sum to k <br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700575/Web/Other/blobid0_1722330388.jpg" width="313" height="313"> </span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>k = 3<strong><br></strong>   1
  /  \
2     3</span>
<span style="font-size: 18px;"><strong>Output:</strong> 2</span>
<span style="font-size: 18px;"><strong>Explanation:</strong>
Path 1 : 1 -&gt; 2 (Sum = 3)
Path 2 : 3 (Sum = 3)</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">1 ≤ number of nodes ≤ 10<sup>4</sup></span></li>
<li><span style="font-size: 18px;">-100 ≤ node value ≤ 100</span></li>
<li><span style="font-size: 18px;">-10<sup>9</sup> ≤ k ≤ 10<sup>9</sup></span></li>
</ul></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Walmart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;