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
    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    chess_terminal.print_board(hovered_field=29, possible_moves=chess_board.white_bishop_possible_moves(29))
    print(chess_board.all_possible_moves_side("white"))
    print(chess_board.move_possible(52, 36))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
