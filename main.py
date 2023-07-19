def count_possible_moves_side(possible_moves: dict) -> int:
    if possible_moves != {}:
        count = 0
        for i in possible_moves:
            count += len(possible_moves[i])
        return count
    elif possible_moves == {}:
        return 0
    else:
        return "wrong dict"

def do_moves_deep(colour:str="white", deep:int=2):
    pass

def main():
    import chess
    import time

    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    chess_terminal.print_board()
    time.sleep(1)
    chess_terminal.clear()
    chess_terminal.print_board(hovered_field=52, possible_moves=chess_board.possible_moves(52)[1])
    time.sleep(1)
    chess_terminal.clear()
    chess_board.do_move(52, 36)
    chess_terminal.print_board()
    time.sleep(1)
    chess_terminal.clear()
    chess_terminal.print_board(hovered_field=11, possible_moves=chess_board.possible_moves(11)[1])
    time.sleep(1)
    chess_terminal.clear()
    chess_board.do_move(11, 27)
    chess_terminal.print_board()
    time.sleep(1)
    chess_terminal.clear()
    chess_terminal.print_board(hovered_field=36, possible_moves=chess_board.possible_moves(36)[1])
    time.sleep(1)
    chess_terminal.clear()
    chess_board.do_move(36, 27)
    chess_terminal.print_board()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
