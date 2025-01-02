<h2><a href="https://www.geeksforgeeks.org/problems/subarrays-with-sum-k/1">Subarrays with sum K</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number <strong>k</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong><strong> </strong>arr = [10, 2, -2, -20, 10], k = -10
<strong>Output:</strong> 3
<strong>Explaination:</strong> Subarrays: arr[0...3], arr[1...4], arr[3...4] have sum exactly equal to -10.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr = [9, 4, 20, 3, 10, 5], k = 33
<strong>Output:</strong> 2
<strong>Explaination:</strong> Subarrays: arr[0...2], arr[2...4] have sum exactly equal to 33.<br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [1, 3, 5], k = 0<br></span><span style="font-size: 14pt;"><strong>Output:</strong> 0
<strong>Explaination: </strong>No subarray with 0 sum.</span></pre>
<p><strong style="font-size: 14pt; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">Constraints:</strong></p>
<ul>
<li><span style="font-size: 14pt;">1 ≤ arr.size() ≤ 10<sup>5</sup></span></li>
<li><span style="font-size: 14pt;">-10<sup>3</sup> ≤ arr[i] ≤ 10<sup>3</sup></span></li>
<li><span style="font-size: 14pt;">-10<sup>7</sup>&nbsp;≤ k&nbsp;≤ 10<sup>7</sup></span></li>
</ul></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Hash</code>&nbsp;<code>Data Structures</code>&nbsp;