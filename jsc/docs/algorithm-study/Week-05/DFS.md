# DFS

DFS stands for Depth-First Search. When there are multiple pathes to change from, this method focuses on exploring as deeply as possible along one path before backtracking.

There are generally two ways to implement the nodes:
1. Processing the node when it is pushed onto the stack
2. Processing the node when it is popped from the stack

Key considerations for DFS
When desiging a FS alogorithm, you must focus on these three essential elements
1. Exploration conditions: The logic that determines which neighboring nodes are valid to visit next.
2. Termination Conditions: The base case that defines when the search should stop to prevent infinite loops
3. Parameters: The data and state variables passed through each recursive call to keep track of the progress