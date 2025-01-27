<h2><a href="https://www.geeksforgeeks.org/problems/lru-cache/1">LRU Cache</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Design a data structure that works like a LRU Cache. Here&nbsp;<strong>cap</strong>&nbsp;denotes&nbsp;the capacity of the cache and&nbsp;<strong>Q</strong>&nbsp;denotes the number of queries. Query can be&nbsp;</span><span style="font-size: 18px;">of two types:</span></p>
<ol>
<li><span style="font-size: 18px;"><strong>PUT</strong>&nbsp;<strong>x</strong>&nbsp;<strong>y</strong>: sets the value of the key&nbsp;<strong>x</strong>&nbsp;with value&nbsp;<strong>y</strong></span></li>
<li><span style="font-size: 18px;"><strong>GET</strong>&nbsp;<strong>x</strong>: gets the key of&nbsp;<strong>x</strong>&nbsp;if present else returns&nbsp;<strong>-1</strong>.</span></li>
</ol>
<p><span style="font-size: 18px;">The LRUCache class has two methods&nbsp;<strong>get</strong>() and&nbsp;<strong>put</strong>() which are defined as follows.</span></p>
<ol>
<li><span style="font-size: 18px;"><strong>get(key)</strong>: returns the value of the key if it&nbsp;already exists in the cache otherwise returns&nbsp;<strong>-1.</strong></span></li>
<li><span style="font-size: 18px;"><strong>put(key, value)</strong>: if the key is already present, update its value. If not present, add the key-value pair to the cache. If the cache reaches its capacity it should remove the least recently used item before inserting the new item.</span></li>
<li><span style="font-size: 18px;">In the&nbsp;<strong>constructor</strong>&nbsp;of the class the capacity of the cache should be initialized.</span></li>
</ol>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>cap = 2, Q = 2, Queries = [["PUT", 1, 2], ["GET", 1]]
<strong>Output: </strong>[2]<strong>
Explanation: </strong>Cache Size = 2
["PUT", 1, 2] will insert the key-value pair (1, 2) in the cache,
["GET", 1] will print the value corresponding to Key 1, ie 2.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>cap = 2, Q = 8, Queries = [["PUT", 1, 2], ["PUT", 2, 3], ["PUT", 1, 5], ["PUT", 4, 5], ["PUT", 6, 7], ["GET", 4], ["PUT", 1, 2], ["GET", 3]]<br><strong>Output: </strong>[5, -1]<strong>
Explanation: </strong>Cache Size = 2
["PUT", 1, 2] will insert the pair (1,2) in the cache.
["PUT", 2, 3] will insert the pair (2,3) in the cache: 1-&gt;2, 2-&gt;3(the most recently used one is kept at the rightmost position)&nbsp;
["PUT", 1, 5] will replace the value of 1 from 2 to 5 : 2 -&gt; 3, 1 -&gt; 5
["PUT", 4, 5] : 1 -&gt; 5, 4 -&gt; 5 (Cache size is 2, hence we delete the least recently used key-value pair)
["PUT", 6, 7] : 4 -&gt; 5, 6 -&gt; 7&nbsp;
["GET", 4] : Prints 5 (The cache now looks like 6 -&gt; 7, 4-&gt;5)
["PUT", 1, 2] : 4 -&gt; 5, 1 -&gt; 2  (Cache size is 2, hence we delete the least recently used key-value pair)
["GET", 3] : No key value pair having key = 3. Hence, -1 is printed.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= cap &lt;= 10<sup>3</sup><br>1 &lt;= Q &lt;= 10<sup>5</sup><br>1 &lt;= x, y &lt;= 10<sup>4</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Paytm</code>&nbsp;<code>Zoho</code>&nbsp;<code>Flipkart</code>&nbsp;<code>Morgan Stanley</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>OYO Rooms</code>&nbsp;<code>Samsung</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>Hike</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Ola Cabs</code>&nbsp;<code>Visa</code>&nbsp;<code>Walmart</code>&nbsp;<code>Goldman Sachs</code>&nbsp;<code>Adobe</code>&nbsp;<code>Google</code>&nbsp;<code>Yahoo</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>doubly-linked-list</code>&nbsp;<code>Hash</code>&nbsp;<code>Queue</code>&nbsp;<code>Design-Pattern</code>&nbsp;<code>Data Structures</code>&nbsp;