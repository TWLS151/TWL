"""
0. My initial struggles
Ah, I struggled so much because I didn't know the rules of the 2048 game.
I thought swiping lef only swapped the positions of two blocks,
but actually, all blocks slide all the way to the left.
Moreover, it's not just one row sliding, but all rows slide at once.
And I completely missed the rule that said: "Already merged blocks cannot be merged again"

1. Brainstorming
I need to find the optimal value within 5 moves.
Initially, I thought of using DFS for Brute force.
BFS is for the shortest path or minimum time, which doesn't fit here/
If I use DFS, I thought I could alse solve it using permutations.
There are 4 possibilities per swipe (Up, Down, Left, Right).
Since 4 directions can be repeated over 5 chances in a specific order,
I should use Cartesian product.
The other options are 'combinations' (no repetition, unordered)
'permutations (no repetition, oredered)
or 'combinations_with_replacement' (repetition, unordered).
This results in 4^5, which is 1024 possible cases.
Now, I need to design the DFS.
Variables to pass: (board, count, direction, max_value?)
I need to use backtracking -> I don't know how to do this.
I always get stuch here.
I must implement block movement when swiping.
And I have to implement merging when identical numbers meet/
Input: The matrix size on one line, followed by the matrix itself.
The board size is 1 <= N <= 20.

2. Decision Criteria: DFS vs itertools.product
Conclusion: DFS is better. The reason is that it uses less memory.
When 'product' is good: It is intuitive for beginners(like me) who struggle to design DFS
When 'DFS' is good: It is great for eliminating overlapping/duplicate states.
For example, after calculating 'Up-Up-Up-UP-Up', 'producht' has to recalculate from scratch
when checking 'Up-Up-Up-Up-Down'. But DFS only needs to backtrack an change the very last move.

3. Lessons learned
3-1. In DFS, depending on whether it's pathfinding or starte exploration
    you either use 'visited = True' or pass the entire board as an argument.
    Learn to judge between the two!
3-2. The code written below a recursive function call only executes after the recursion hits
    a 'return' and starts popping off the call stack.
3-3. Don't blindly use 'for' loops just because it's a matrix. If you need to skip
    certain indices(like in this problem), use a 'while' loop to manually control the index.
3-4. Memorize the 90-degree rotation algorithm: 'list(map(list, zip(*array[::-1])))'
3-5. Recursive function parameters: There is no need to pass the maximum value as a parameter;
    just manage it globally using the 'global' keyword.

"""



import sys

sys.stdin = open('boj-12100-2048easy.txt')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_val = 0

## Receive the 2D list (Board)
# def dfs(board, count, direction, max_block)
#   # I wasn't really sure what should go inside this DFS function.
#   # I guess the sliding and merging logic should go here?
#   # How can I most efficiently exclude the empty spaces (0s)?
#   # Should I loop through and `pop(i)` if it's 0? Seems inefficient.
#   # Instead of popping, let's just extract the non-zere numbers using a loop.
#   # nums = [x for x in row if x != 0]
#
#   # for vs while
#   # **Since the colums of the matrix are fixed, I thought 'for' was right,
#   # but 'while' turned out to be much better.
#   # Because indices that become 0 after a merge shouldn't be checked again;
#   # they need to be skipped.
#   # But a 'for' loop will stubbornly check them anyway.
#   # Hence, my conclusion is that a 'while' loop is better.

def merge_method_1(row):
    nums = [x for x in row if x != 0]
    merged = []
    i = 0
    while i < len(nums):
        if i + 1 < len(nums) and nums[i] == nums[i+1]:
            merged.append(nums[i] * 2)
            i += 2
        else:
            merged.append(nums[i])
            i += 1
    return merged + [0] * (N - len(merged))

def rotate_90(board):
    return list(map(list, zip(*board[::-1])))

# I need to write the DFS, but I don't know how to handle the recursion.
# I need to separate my thinking into two parts: termination condition and exploation.
# I initially thought I needed variables for max_value, direction, count, and the board.
# However, max_value can just be handled as a global variable.
# Direction doesn't need to be passed as an argument since I can just loop
# 4 times within the recursive function itself.
def dfs(n, board):
    global max_val

    if n == 5:
        for row in board:
            for val in row:
                if val > max_val:
                    max_val = val
        return
    
    for _ in range(4):
        # Need to create a new board for backtracking.
        # Among backtracking methods: changing visited nodes to False
        # vs. passing the whold board as an argument.
        # Use 'visited' for pathfinding; pass the whole board for state change.
        moved_board = []
        for row in board:
            moved_board.append(merge_method_1(row))
        
        dfs(n+1, moved_board)
        # I thought that if I call `dfs` above this line, the code `board = rotate_90(board)`
        # would never be read, causing an infinite recursive loop.
        # But because there is a `return` statement above, the final recursion finishes,
        # and then the previous recursive calls stacked in the call stack start executing.
        # The 'return' statement is very important.
        board = rotate_90(board)

dfs(0, board)
print(max_val)