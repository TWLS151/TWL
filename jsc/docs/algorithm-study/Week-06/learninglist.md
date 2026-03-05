1. Adjacency List
    1. Concept: Making two dimensional list, and check the relationship.
    2. Making two dimensional list; adj = [[] for _ in range(N)]
    3. Adding value on the list; adj[u].append(v)
    4. Adding value on another side; adj[v].append(u)
2. Union-Find
    
    ```python
    import sys
    
    def find(x):
    	if parent[x] == x:
    		return x
    		
    	parnet[x] = find(parent[x])
    	return parent[x]
    	
    def union(x,y):
    	root_x = find(x)
    	root_x = find(y)
    	
    	if root_x != root_y:
    		parent[root_y] = root_x
    
    for _ in range(M):
    	u, v = map(int, input().split())
    	union(u, v)
    	
    group_count = 0
    for i in range(1, N + 1):
    	if parent[i] == i:
    		group_count += 1
    		
    print({group_count})
    ```
    
3. Propagating values in DFS
    
    1. Checking existence (Boolean DFS)
    
    - Goal: Is there a way to the exit? Yes/ No
    - Code pattern

```python
if dfs(next_node):
	return True
```

1. Measuring length(Value-returning DFS)
- Goal: how many steps did it take to reach the exit?
- The reason I need the ‘result’ variable: If I only use ‘if …’, the number gets converted into a simple ‘True’ signal. The actual number evaporates.

```python
result = dfs(next_node, cnt + 1)
if result > 0:
	return result
```

1. Ways to Handle Variables in DFS

1. Using Return Values

This is the most "functional" approach. You pass the result of the recursive call back up the call stack. This is ideal for calculations like finding the sum of nodes or the maximum depth.

**Note:** As you mentioned, this is particularly straightforward for **Booleans** (e.g., checking if apath exists).

2. Using Global Variables

You can declare a variable in the global scope and use the `global` keyword (in Python) inside the function to modify it. While simple, it can make the code harder to debug in larger projects.

3. Using Classes (Instance Variables)

By encapsulating the DFS within a class, you can store the state in `self.variable`. This is often considered the cleanest way to maintain state in object-oriented programming without resorting to global variables.

4. Using Mutable Objects (Bonus)

In languages like Python, you can pass a **list** or **dictionary** as an argument. Since these are passed by reference, any changes made inside the function will persist outside of it without needing a return statement.