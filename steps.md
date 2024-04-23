# Steps on solving the board (using backtracking)
1) Pick an empty square.
2) Try all numbers (1 , 2, 3, 4, 5, 6, 7, 8, 9).
3) Find one such number that works, as soon as we get that number, we move on to the next square.
4) Repeat the above steps.
5) As soon as we get to a point where the solution cannot be completed with the above numbers which we concluded, we backtrack.

# # Functions
- print_board(board)
- find_empty(board) : returns the empty position of the board: tupple - (i, j)
- valid_board(board) : Checks if the board is valid board or not.