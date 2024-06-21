def fun(d, row, col, path, c):
    rows = len(d)
    cols = len(d[0])

    # Base case: If the destination is reached
    if row == rows - 1 and col == cols - 1:
        path.append((row, col))
        c += 1
        print(" -> ".join(map(str, path)))
        path.pop()
        return c

    # Mark the current cell as part of the path
    path.append((row, col))

    # Move right if possible
    if col + 1 < cols:
        c = fun(d, row, col + 1, path, c)

    # Move down if possible
    if row + 1 < rows:
        c = fun(d, row + 1, col, path, c)

    # Backtrack: Unmark the current cell
    path.pop()

    return c

# Matrix initialization
d = [[0] * 4 for _ in range(3)]
path = []
start_row, start_col = 0, 0
end_row, end_col = 2, 3
c = 0

# Function call
total_paths = fun(d, start_row, start_col, path, c)
print("Total number of paths:", total_paths)