def print_board(b):
    for r in b: print(" ".join(map(str, r)))
    print()

def is_safe(b, row, col, n):
    for i in range(row):
        if b[i][col] or (col - row + i >= 0 and b[i][col - row + i]) or (col + row - i < n and b[i][col + row - i]):
            return False
    return True

def solve(b, row, n):
    if row == n:
        print_board(b)
        return
    if 1 in b[row]:
        solve(b, row + 1, n)
        return
    for col in range(n):
        if is_safe(b, row, col, n):
            b[row][col] = 1
            solve(b, row + 1, n)
            b[row][col] = 0

n = int(input("N: "))
b = [[0]*n for _ in range(n)]
r, c = map(int, input("First queen (row col): ").split())
b[r-1][c-1] = 1
print("\nInitial board:"); print_board(b)
print("Solutions:\n")
solve(b, 0, n)
