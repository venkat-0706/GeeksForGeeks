<h2><a href="https://www.geeksforgeeks.org/problems/word-search/1">Word Search</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">You are given a <strong>two-dimensional</strong> <strong>mat[][]</strong> of <strong>size n*m</strong> containing English alphabets and a string <strong>word</strong>. Check if the word exists on the mat. The word can be constructed by using letters from <strong>adjacent</strong> cells, either horizontally or vertically. The same cell cannot be used more than <strong>once</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
<strong>Output: </strong>true
<strong>Explanation:</strong>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/886266/Web/Other/blobid4_1737981964.png" alt="" width="220" height="200"><br>The letter cells which are used to construct the "GEEK" are colored.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
<strong>Output: </strong>false
<strong>Explanation:</strong>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/886266/Web/Other/blobid5_1737981964.png" alt="" width="220" height="199"><br>It is impossible to construct the string word from the mat using each cell only once.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
<strong>Output: </strong>true
<strong>Explanation:</strong>
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/886266/Web/Other/blobid6_1737981964.png" alt="" width="222" height="184"><br>There are multiple ways to construct the word "AB".</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ n, m ≤ 100<br>1 ≤ L ≤ n*m</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>Intuit</code>&nbsp;<code>Apple</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>DFS</code>&nbsp;<code>Graph</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;