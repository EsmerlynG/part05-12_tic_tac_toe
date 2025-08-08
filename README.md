# Tic-Tac-Toe Play Turn Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A Python function that handles player moves in Tic-Tac-Toe, validating coordinates and placing symbols on the game board. This solution demonstrates input validation, boundary checking, and the critical importance of understanding coordinate system conventions.

---

## 📖 Problem Description

Write a function `play_turn(game_board: list, x: int, y: int, piece: str)` that places a player's symbol at the specified coordinates on a 3×3 Tic-Tac-Toe board.

### Requirements
- Place the given symbol (`"X"` or `"O"`) at coordinates `(x, y)`
- **Important**: `x` represents the **column**, `y` represents the **row** (opposite of typical matrix notation)
- Return `True` if the move was successful
- Return `False` if the square is occupied or coordinates are invalid
- Coordinates range from 0 to 2 for a 3×3 board

### Board Representation
- `""`: Empty square
- `"X"`: Player 1 symbol  
- `"O"`: Player 2 symbol

### Example
```python
game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(game_board, 2, 0, "X"))  # True
print(game_board)  # [['', '', 'X'], ['', '', ''], ['', '', '']]
```

---

## 💻 Code Implementation

```python
def play_turn(game_board: list, r_num: int, c_num: int, player: str):
    valid_row_range = len(game_board) - 1
    valid_column_range = len(game_board[0]) - 1
    
    if valid_row_range < r_num or valid_column_range < c_num:
        return False
    
    if r_num < 0 or c_num < 0:
        return False
    
    if game_board[c_num][r_num] != "":
        return False
    
    game_board[c_num][r_num] = player
    return True

if __name__ == "__main__":
    game_board = [["o", "", ""], ["x", "o", ""], ["", "", "o"]]
    print(play_turn(game_board, 2, 1, "X"))
    print(game_board)
```

**Output:**
```
True
[['o', '', ''], ['x', 'o', 'X'], ['', '', 'o']]
```

---

## 🧠 Algorithm Explanation

### **Validation-First Approach**
```python
# 1. Calculate valid ranges
valid_row_range = len(game_board) - 1
valid_column_range = len(game_board[0]) - 1

# 2. Check upper bounds
if valid_row_range < r_num or valid_column_range < c_num:
    return False

# 3. Check lower bounds  
if r_num < 0 or c_num < 0:
    return False

# 4. Check if square is occupied
if game_board[c_num][r_num] != "":
    return False

# 5. Place symbol and return success
game_board[c_num][r_num] = player
return True
```

**Key Insight**: Validate inputs **before** attempting to access the matrix to prevent index errors.

**Time Complexity:** O(1) - Constant time operations  
**Space Complexity:** O(1) - No additional data structures needed

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 tic_tac_toe.py
```

Or import the function in your own code:

```python
from tic_tac_toe import play_turn

# Create empty 3x3 board
board = [["" for _ in range(3)] for _ in range(3)]

# Play some moves
print(play_turn(board, 1, 1, "X"))  # Center position
print(play_turn(board, 0, 0, "O"))  # Top-left corner
print(play_turn(board, 1, 1, "X"))  # Try to overwrite - should return False

print("Final board:")
for row in board:
    print(row)
```

---

## 🧪 Test Cases

```python
# Test case 1: Valid moves
board1 = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(board1, 0, 0, "X"))  # True - top-left
print(play_turn(board1, 2, 2, "O"))  # True - bottom-right
print(play_turn(board1, 1, 1, "X"))  # True - center

# Test case 2: Invalid coordinates
board2 = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(board2, 3, 1, "X"))  # False - column out of range
print(play_turn(board2, 1, 3, "O"))  # False - row out of range
print(play_turn(board2, -1, 1, "X")) # False - negative column
print(play_turn(board2, 1, -1, "O")) # False - negative row

# Test case 3: Occupied squares
board3 = [["X", "", ""], ["", "O", ""], ["", "", ""]]
print(play_turn(board3, 0, 0, "O"))  # False - square occupied by X
print(play_turn(board3, 1, 1, "X"))  # False - square occupied by O
print(play_turn(board3, 2, 0, "X"))  # True - empty square

# Test case 4: Edge positions
board4 = [["", "", ""], ["", "", ""], ["", "", ""]]
print(play_turn(board4, 0, 0, "X"))  # True - top-left corner
print(play_turn(board4, 2, 0, "O"))  # True - top-right corner
print(play_turn(board4, 0, 2, "X"))  # True - bottom-left corner
print(play_turn(board4, 2, 2, "O"))  # True - bottom-right corner

print("Final board:")
for row in board4:
    print(row)
```

---

## ✨ Key Learning Highlights

This problem taught crucial lessons about **input validation**, **coordinate systems**, and **requirement specification**:

### **Input Validation Order**
```python
# WRONG - Check validity AFTER accessing
if game_board[r_num][c_num] != "":  # This can cause IndexError!
    return False

# CORRECT - My validation approach
valid_row_range = len(game_board) - 1
valid_column_range = len(game_board[0]) - 1

if valid_row_range < r_num or valid_column_range < c_num:
    return False

if r_num < 0 or c_num < 0:
    return False
```

### **Coordinate System Conventions**
- **Problem Specification**: `x` (column) comes first, `y` (row) comes second
- **Matrix Access**: `game_board[row][column]` - row comes first in implementation
- **Critical Insight**: Always verify coordinate conventions in requirements

### **Edge Case Handling**
- **Boundary Validation**: Check both upper and lower bounds
- **Occupied Square Check**: Ensure empty string before placing symbol
- **Error Prevention**: Validate before accessing to prevent runtime errors

---

## 🎯 Design Philosophy

### **Why This Approach?**
1. **Safety First**: Validate all inputs before any operations
2. **Clear Logic Flow**: Sequential validation steps are easy to follow
3. **Fail Fast**: Return immediately when invalid conditions are detected
4. **Defensive Programming**: Prevent errors rather than handling exceptions

### **Clean Code Principles Applied**
- **Guard Clauses**: Early returns for invalid conditions
- **Descriptive Variables**: `valid_row_range` and `valid_column_range` show intent
- **Single Responsibility**: Function validates and places symbol
- **Predictable Behavior**: Clear True/False return values

---

## 🔄 Problem-Solving Journey

### **Initial Challenge: Premature Access**
```python
# WRONG - Accessing before validation
if game_board[r_num][c_num] != "":  # IndexError when out of bounds!
    return False
```

### **First Fix: Proper Validation Order**
```python
# MY APPROACH - Calculate valid ranges first
valid_row_range = len(game_board) - 1
valid_column_range = len(game_board[0]) - 1

if valid_row_range < r_num or valid_column_range < c_num:
    return False

if r_num < 0 or c_num < 0:
    return False
```

### **Major Revelation: Coordinate Convention Mix-up**
```python
# MY ASSUMPTION - Standard matrix notation
game_board[row][column]

# ACTUAL REQUIREMENT - x,y coordinate system
# x = column (first parameter)
# y = row (second parameter)
# Access: game_board[y][x] or game_board[c_num][r_num]
```

### **Final Solution: Correct Implementation**
```python
def play_turn(game_board: list, r_num: int, c_num: int, player: str):
    # Validate bounds first
    # Use game_board[c_num][r_num] to match x,y convention
```

---

## 🎓 Learning Outcomes

* **Input Validation Mastery**: Always validate before accessing data structures
* **Coordinate System Awareness**: Understanding different conventions (matrix vs cartesian)
* **Requirement Analysis**: The critical importance of understanding specifications exactly
* **Edge Case Handling**: Comprehensive boundary and state checking
* **Defensive Programming**: Writing code that fails gracefully
* **Testing-Driven Development**: Understanding how test expectations drive implementation

---

## 💡 Developer Reflection

> *"This was an interesting and challenging problem, not because it was inherently difficult. In all honesty, the only thing that really had me confused for a bit was handling my edge cases.*
> 
> *Most of my tests were producing errors because I was accessing the location I needed to replace too early, and this threw errors if the inputs were out of range for the list or matrix. But that ended up being an easy fix. All I had to do was move that check after my `if` statements that made sure the inputs were even in range to begin with, before checking if the spot I was trying to add a player to was empty.*
> 
> *Now the difficult part came in understanding why my tests kept failing even though my code was running how I intended. And that's the key word, I. The code was doing what I wanted, but not what the tests were expecting.*
> 
> *After looking over the failed test cases, I realized the problem was that the way the tests were accessing the matrix was the reverse of how I was doing it. I had it set up so the first input was the row and the second was the column (which is how I learned matrices), but the test cases were using the first number as the column and the second as the row.*
> 
> *That really threw me off because it was the complete opposite of what I was used to. I spent a good 45 minutes confused over it before I finally realized what was going on. Once I spotted it, though, the fix was super simple. I just flipped the row and column when accessing the matrix.*
> 
> *All in all, this problem really taught me how important it is to slow down and make sure I fully understand how the code is expected to behave, not just how I think it should work."*

### **Key Takeaways**
1. **Validate first, access second** - Prevent runtime errors through proper input checking
2. **Coordinate conventions matter** - Don't assume standard matrix notation
3. **Requirements are king** - Your logic must match the specification, not your assumptions
4. **Test-driven understanding** - Failed tests often reveal requirement misunderstandings
5. **Debugging persistence** - Sometimes the issue isn't in your logic, but in your assumptions
6. **Slow down and verify** - Take time to fully understand expected behavior vs personal assumptions

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
