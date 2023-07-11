def main():
    import chess
    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_terminal.print_board()
    print(chess_board.white_pawn_possible_moves(52))
    print(chess_board.white_pawn_possible_moves(44))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
