<h2><a href="https://www.geeksforgeeks.org/problems/subsets-1613027340/1">Subsets</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[]</strong> of distinct positive integers, your task is to find all its subsets. The subsets should be returned in lexicographical order.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr = [1, 2, 3]
<strong>Output: </strong>[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
<strong>Explanation: <br></strong>The subsets of [1, 2, 3] in lexicographical order are:
[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr = [1, 2]
<strong>Output: </strong>[[], [1], [1, 2], [2]]
<strong>Explanation:</strong>
The subsets of [1, 2] in lexicographical order are:
[], [1], [1, 2], [2]</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr = [10]
<strong>Output: </strong>[[], [10]]
<strong>Explanation: </strong>For the array with a single element [10]<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">, the subsets are [ ] </span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">and [10]</span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">.</span></span></pre>
<div><span style="font-size: 14pt;"><strong>Constraints :</strong></span></div>
<div><span style="font-size: 14pt;">1 ≤ arr.size() ≤ 10</span></div>
<div><span style="font-size: 14pt;">1 ≤ arr[i] ≤ </span><span style="font-size: 14pt;">10</span></div></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Algorithms</code>&nbsp;