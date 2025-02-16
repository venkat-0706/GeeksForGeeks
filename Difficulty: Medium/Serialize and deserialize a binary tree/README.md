<h2><a href="https://www.geeksforgeeks.org/problems/serialize-and-deserialize-a-binary-tree/1">Serialize and deserialize a binary tree</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions</span></p>
<ul>
<li><span style="font-size: 14pt;"><strong>serialize() :</strong>&nbsp;stores the tree into an array&nbsp;<strong>a</strong>&nbsp;and returns the array.</span></li>
<li><span style="font-size: 14pt;"><strong>deSerialize() :</strong>&nbsp;deserializes the array to the tree and returns the root of the tree.</span></li>
</ul>
<p><span style="font-size: 14pt;"><strong>Note:&nbsp;</strong>Multiple nodes can have the same data and the node values are&nbsp;<strong>always</strong>&nbsp;<strong>positive integers</strong>. Your code will be correct if the tree returned by&nbsp;<strong>deSerialize(serialize(input_tree))</strong>&nbsp;is same as the input tree. Driver code will print the in-order traversal of the tree returned by&nbsp;deSerialize(serialize(input_tree)).</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>root = [1, 2, 3]
&nbsp; &nbsp;&nbsp;  <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700281/Web/Other/blobid4_1739345069.png" alt="" width="250" height="203">
<strong>Output: </strong>[2, 1, 3]
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> root = [10, 20, 30, 40, 60, N, N]
&nbsp; &nbsp;   <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700281/Web/Other/blobid5_1739345069.png" alt="" width="248" height="234">
<strong>Output: </strong>[40, 20, 60, 10, 30]</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 &lt;= Number of nodes &lt;= 10<sup>4</sup><br>1 &lt;= Data of a node &lt;= 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Paytm</code>&nbsp;<code>Flipkart</code>&nbsp;<code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>MAQ Software</code>&nbsp;<code>Adobe</code>&nbsp;<code>Linkedin</code>&nbsp;<code>Quikr</code>&nbsp;<code>Yahoo</code>&nbsp;<code>InMobi</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;