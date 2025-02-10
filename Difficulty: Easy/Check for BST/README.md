<h2><a href="https://www.geeksforgeeks.org/problems/check-for-bst/1">Check for BST</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given the root of a&nbsp;binary tree. Check whether it is a BST or not.<br><strong>Note: </strong>We are considering that BSTs can not contain duplicate Nodes.</span><br><span style="font-size: 18px;">A&nbsp;<strong>BST</strong>&nbsp;is defined as follows:</span></p>
<ul>
<li>
<div><span style="font-size: 18px;">The left subtree of a node contains only nodes with keys <strong>less than</strong> the node's key.</span></div>
</li>
<li>
<div><span style="font-size: 18px;">The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node's key.</span></div>
</li>
<li>
<div><span style="font-size: 18px;">Both the left and right subtrees must also be binary search trees.</span></div>
</li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> root = [2, 1, 3, N, N, N, 5]
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700149/Web/Other/blobid0_1739182093.jpg" width="249" height="220"></span><br><br><span style="font-size: 18px;"><strong>Output: </strong>true 
<strong>Explanation: </strong></span><span style="font-size: 18px;">The left subtree of every node contains smaller keys and right subtree of every node contains greater keys. Hence, the tree is a BST.<br></span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>root = [2, N, 7, N, 6, N, 9] </span><br><br><span style="font-size: 18px;"><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700149/Web/Other/blobid2_1739182131.jpg" width="238" height="211"></span><br><br><span style="font-size: 18px;"><strong>Output: </strong>false 
<strong>Explanation: </strong>Since the node to the right of node with key 7 has lesser key value, hence it is not a valid BST.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>root = [10, 5, 20, N, N, 9, 25]
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700149/Web/Other/blobid3_1739182159.jpg" width="240" height="212"></span><br><br><span style="font-size: 18px;"><strong>Output: </strong>false
<strong>Explanation: </strong>The node with key 9 present in the right subtree has lesser key value than root node.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:<br></strong></span><span style="font-size: 18px;">1 ≤ number of nodes ≤ 10<sup>5<br></sup></span><span style="font-size: 18px;">1 ≤ node-&gt;data ≤ 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>VMWare</code>&nbsp;<code>Flipkart</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Samsung</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>FactSet</code>&nbsp;<code>Hike</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Ola Cabs</code>&nbsp;<code>Walmart</code>&nbsp;<code>Goldman Sachs</code>&nbsp;<code>MAQ Software</code>&nbsp;<code>Adobe</code>&nbsp;<code>Linkedin</code>&nbsp;<code>Qualcomm</code>&nbsp;<code>Boomerang Commerce</code>&nbsp;<code>GreyOrange</code>&nbsp;<code>Wooker</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;