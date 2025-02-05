<h2><a href="https://www.geeksforgeeks.org/problems/construct-tree-1/1">Construct Tree from Inorder & Preorder</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given two arrays representing the <strong>inorder</strong> and <strong>preorder</strong> traversals of a binary tree, construct the tree and return the root node of the constructed tree.</span></p>
<p><span style="font-size: 14pt;">Note: The output is written in postorder traversal.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
<strong>Output: </strong>[8, 7, 6, 1]<br><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Explanation: </strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">The tree will look like<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700586/Web/Other/blobid0_1738646717.png" width="378" height="335"></span><br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
<strong>Output: </strong>[3, 4, 1, 5, 2, 0]<strong>
Explanation: </strong>The tree will look like<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700586/Web/Other/blobid1_1738646749.png" width="373" height="330"></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>inorder[] = [2, 5, 4, 1, 3], preorder[] = [1, 4, 5, 2, 3]
<strong>Output: </strong>[2, 5, 4, 3, 1]<br><strong style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Explanation: </strong><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">The tree will look like<br><img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700586/Web/Other/blobid2_1738647091.png" width="370" height="327"></span><br></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ number of nodes ≤ 10<sup>3</sup><br>0 ≤ nodes -&gt; data ≤ 10<sup>3</sup><br>Both the inorder and preorder arrays contain unique values.</span></p>
<div id="highlighter--hover-tools" style="display: none;">
<div id="highlighter--hover-tools--container">
<div class="highlighter--icon highlighter--icon-copy" title="Copy">&nbsp;</div>
<div class="highlighter--icon highlighter--icon-change-color" title="Change Color">&nbsp;</div>
<div class="highlighter--icon highlighter--icon-delete" title="Delete">&nbsp;</div>
</div>
</div>
<div id="highlighter--hover-tools" style="display: none;">
<div id="highlighter--hover-tools--container">
<div class="highlighter--icon highlighter--icon-copy" title="Copy">&nbsp;</div>
<div class="highlighter--icon highlighter--icon-change-color" title="Change Color">&nbsp;</div>
<div class="highlighter--icon highlighter--icon-delete" title="Delete">&nbsp;</div>
</div>
</div></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;