<h2><a href="https://www.geeksforgeeks.org/problems/find-all-triplets-with-zero-sum/1">Find All Triplets with Zero Sum</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array&nbsp;<strong>arr[]</strong>, find all possible triplets <strong>i, j, k</strong> in the&nbsp;<strong>arr[]</strong> whose sum of elements is equals to <strong>zero</strong>.&nbsp;<br>Returned triplet should also be internally sorted i.e.&nbsp;<strong>i&lt;j&lt;k.</strong></span></p>
<p><strong style="font-size: 18px;">Examples:</strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong></span><span style="font-size: 18px;">arr[] = [0, -1, 2, -3, 1]</span><span style="font-size: 18px;">
<strong>Output: </strong>[[0, 1, 4], [2, 3, 4]]<strong>
Explanation: </strong></span><span style="font-size: 18px;">Triplets with sum 0 are:<br></span><span style="font-size: 14pt;"><span style="font-size: 18.6667px;">arr[0] + arr[1] + arr[4] = 0 + (-1) + 1 = 0
arr[2] + arr[3] + arr[4] = 2 + (-3) + 1 = 0</span></span></pre>
<pre><span style="font-size: 14pt;"><strong style="font-size: 14pt;">Input: </strong><span style="font-size: 14pt;">arr[] = [</span><span style="font-size: 18.6667px;">1, -2, 1, 0, 5</span><span style="font-size: 14pt;">]
</span><strong style="font-size: 14pt;">Output: </strong><span style="font-size: 14pt;">[[0, 1, 2]]</span><strong style="font-size: 14pt;">
Explanation: </strong></span><span style="font-size: 18.6667px;">Only triplet which satisfies the condition is arr[0] + arr[1] + arr[2] = 1 + (-2) + 1 = 0</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [2, 3, 1, 0, 5]</span><span style="font-size: 18px;">
<strong>Output: </strong>[[]]</span><span style="font-size: 14pt;"><strong>
Explanation: </strong></span><span style="font-size: 18.6667px;">There is no triplet with sum 0.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:<br></strong>3 &lt;= arr.size() &lt;= 10<sup>3</sup><strong><br></strong></span><span style="font-size: 18px;">-10<sup>4</sup> &lt;= arr[i] </span><span style="font-size: 18px;">&lt;= 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Sorting</code>&nbsp;<code>Arrays</code>&nbsp;<code>Hash</code>&nbsp;