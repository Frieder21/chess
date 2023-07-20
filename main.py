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

def do_moves_deep(chess_board, color:str="white", deep:int=2)->dict:
    if deep == 0:
        return {}
    else:
        possible_moves = chess_board.all_possible_moves_side(color=color)

        if count_possible_moves_side(possible_moves) == 0:
            return {}
        else:
            moves = {}
            if color == "white":
                color = "black"
            elif color == "black":
                color = "white"
            for i in possible_moves:
                for j in possible_moves[i]:
                    chess_board.do_move(i, j)
                    moves[i, j] = do_moves_deep(chess_board, color, deep-1)
                    chess_board.undo_move()
            return moves


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
    chess_board.set_up()
    chess_terminal.print_board()
    print(do_moves_deep(chess_board, "white", 2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
