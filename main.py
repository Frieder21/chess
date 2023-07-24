def main():
    import chess
    import time

    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    time.sleep(0.5)
    print(chess_terminal.chess_board.board)
    print(chess_terminal.perft_terminal(3, "white", 0.05))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
