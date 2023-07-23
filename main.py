def main():
    import chess
    import time

    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    time.sleep(0.5)
    print(chess_board.perft(3, "white"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
