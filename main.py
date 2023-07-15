def main():
    import chess
    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    chess_terminal.print_board(hovered_field=29, possible_moves=chess_board.white_bishop_possible_moves(29))
    print(chess_board.white_knight_possible_moves(16))
    print(chess_board.white_knight_possible_moves(40))
    print(chess_board.white_bishop_possible_moves(29))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
