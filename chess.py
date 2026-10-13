import tkinter as tk
from tkinter import messagebox

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

original = [row[:] for row in puzzle]

def valid(grid, r, c, n):
    for i in range(9):
        if grid[r][i] == n or grid[i][c] == n:
            return False
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == n:
                return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if valid(grid, r, c, n):
                        grid[r][c] = n
                        if solve(grid):
                            return True
                        grid[r][c] = 0
                return False
    return True

def draw():
    for r in range(9):
        for c in range(9):
            cells[r][c].config(text=str(puzzle[r][c] or ""),
                               fg="navy" if original[r][c] else "darkgreen")

def solve_game():
    if solve(puzzle):
        draw()
        messagebox.showinfo("Sudoku", "Puzzle solved!")
    else:
        messagebox.showerror("Sudoku", "No solution found.")

def reset_game():
    for r in range(9):
        puzzle[r] = original[r][:]
    draw()

root = tk.Tk()
root.title("AI Sudoku Solver")
cells = []
for r in range(9):
    row = []
    for c in range(9):
        cell = tk.Label(root, width=3, height=1, font=("Arial", 16),
                        relief="solid", borderwidth=1)
        cell.grid(row=r, column=c, padx=(2 if c % 3 == 0 else 0),
                  pady=(2 if r % 3 == 0 else 0))
        row.append(cell)
    cells.append(row)

tk.Button(root, text="Solve", command=solve_game).grid(row=9, column=2, pady=8)
tk.Button(root, text="Reset", command=reset_game).grid(row=9, column=6, pady=8)
draw()
root.mainloop()
