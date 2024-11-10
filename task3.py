import tkinter as tk
from tkinter import messagebox

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def solve_puzzle():
    grid = [[int(entries[i][j].get()) if entries[i][j].get() else 0 for j in range(9)] for i in range(9)]
    if solve(grid):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(grid[i][j]))
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists.")

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[tk.Entry(root, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j, padx=5, pady=5)

tk.Button(root, text="Solve", command=solve_puzzle).grid(row=10, column=0, columnspan=9, pady=10)
root.mainloop()
