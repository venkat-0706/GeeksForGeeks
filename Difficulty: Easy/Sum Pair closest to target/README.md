<h2><a href="https://www.geeksforgeeks.org/problems/pair-in-array-whose-sum-is-closest-to-x1124/1">Sum Pair closest to target</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]</strong> and a number <strong>target</strong>, find a pair of elements (a, b) in <strong>arr[],&nbsp;</strong>where a&lt;=b whose sum is closest to <strong>target.</strong><br></span><strong><span style="font-size: 18px;">Note:&nbsp;</span></strong><span style="font-size: 18px;">Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [10, 30, 20, 5], target = 25
<strong>Output:</strong> [5, 20]
<strong>Explanation:</strong> As 5 + 20 = 25 is closest to 25.
</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [5, 2, 7, 1, 4], target = 10
<strong>Output:</strong> [2, 7]
<strong>Explanation:</strong> As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. </span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> arr[] = [10], target = 10
<strong>Output:</strong> []
<strong>Explanation:</strong> As the input array has only 1 element, return an empty array.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= arr.size() &lt;= 2*10<sup>5</sup><br>0 &lt;= target&lt;= 2*10<sup>5</sup><br>0 &lt;= arr[i] &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Ola Cabs</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;