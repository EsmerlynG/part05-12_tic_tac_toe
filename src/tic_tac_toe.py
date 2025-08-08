# Write your solution here
def play_turn(game_board: list,r_num: int, c_num: int, player: str):
    
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