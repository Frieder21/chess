def Perft0():
    print("perft(0)")
    import chess
    chess_board = chess.chess_board()
    value = chess_board.perft(0)
    if value == 1:
        print("Test1 passed")
        return True
    else:
        print("Test1 failed")
        print("value = ", value, "expected = ", 1)
        return False

def Perft1():
    print("perft(1)")
    import chess
    chess_board = chess.chess_board()
    value = chess_board.perft(1)
    if value == 20:
        print("Test2 passed")
        return True
    else:
        print("Test2 failed")
        print("value = ", value, "expected = ", 20)
        return False

def Perft2():
    print("perft(2)")
    import chess
    chess_board = chess.chess_board()
    value = chess_board.perft(2)
    if value == 400:
        print("Test3 passed")
        return True
    else:
        print("Test3 failed")
        print("value = ", value, "expected = ", 400)
        return False

def Perft3():
    print("perft(3)")
    import chess
    chess_board = chess.chess_board()
    value = chess_board.perft(3)
    if value == 8902:
        print("Test4 passed")
        return True
    else:
        print("Test4 failed")
        print("value = ", value, "expected = ", 8902)
        return False

def Perft4():
    print("perft(4)")
    import chess
    chess_board = chess.chess_board()
    value = chess_board.perft(4)
    if value == 197281:
        print("Test5 passed")
        return True
    else:
        print("Test5 failed")
        print("value = ", value, "expected = ", 197281)
        return False

def FEN_2_game():
    print("Test FEN_to_binary")
    import chess
    chess_board = chess.chess_board()
    chess_board.FEN_2_game("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    board = [20, 18, 19, 21, 22, 19, 18, 20,
             17, 17, 17, 17, 17, 17, 17, 17,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             9, 9, 9, 9, 9, 9, 9, 9,
             12, 10, 11, 13, 14, 11, 10, 12]
    if chess_board.board == board:
        print("Fen_to_binary passed")
    else:
        print("Fen_to_binary failed")
        print("chess_board.board = ", chess_board.board)
        print("board = ", board)


def pawn_moves():
    print("Test pawn_moves")
    import chess
    chess_board = chess.chess_board()
    chess_board.FEN_2_game("8/8/8/8/8/8/4P3/8 w KQkq - 0 1")
    board = [0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 9, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0]
    if chess_board.board == board:
        print("FEN passed")
    else:
        print("FEN failed")
        print("chess_board.board = ", chess_board.board)
        print("board = ", board)
        return False
    if chess_board.chess_notation_to_index("e2") == 52:
        print("chess_notation_to_index passed")
    else:
        print("chess_notation_to_index failed")
        print("chess_board.chess_notation_to_index('e2') = ", chess_board.chess_notation_to_index("e2"))
        return False
    if chess_board.chess_notation_to_index("e4") == 36:
        print("chess_notation_to_index passed")
    else:
        print("chess_notation_to_index failed")
        print("chess_board.chess_notation_to_index('e4') = ", chess_board.chess_notation_to_index("e4"))
        return False
    if chess_board.chess_notation_to_index("e3") == 44:
        print("chess_notation_to_index passed")
    else:
        print("chess_notation_to_index failed")
        print("chess_board.chess_notation_to_index('e3') = ", chess_board.chess_notation_to_index("e3"))
        return False
    if chess_board.do_move_chess_notation("e2", "e4"):
        print("do move e2 to e4 passed")
    else:
        print("do move e2 to e4 failed")
        return False
    chess_board.undo_move()
    if chess_board.board == board:
        print("undo_move passed")
    else:
        print("undo_move failed")
        print("chess_board.board = ", chess_board.board)
        print("board = ", board)
        return False
    if chess_board.do_move_chess_notation("e2", "e3"):
        print("do_move_chess_notation passed")
    else:
        print("do_move_chess_notation failed")
        return False
    return True


def en_passant():
    print("Test en_passant")
    import chess
    chess_board = chess.chess_board()
    chess_board.FEN_2_game("8/8/8/3pP3/8/8/8/8 w KQkq d6 0 1")
    board = [0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 17, 9, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0]
    if chess_board.board == board:
        print("FEN passed")
    else:
        print("FEN failed")
        print("chess_board.board = ", chess_board.board)
        print("board = ", board)
        return False
    if chess_board.chess_notation_to_index("e5") == 28:
        print("chess_notation_to_index passed")
    else:
        print("chess_notation_to_index failed")
        print("chess_board.chess_notation_to_index('e5') = ", chess_board.chess_notation_to_index("e5"))
        return False
    if chess_board.chess_notation_to_index("d5") == 27:
        print("chess_notation_to_index passed")
    else:
        print("chess_notation_to_index failed")
        print("chess_board.chess_notation_to_index('d5') = ", chess_board.chess_notation_to_index("d5"))
        return False
    if chess_board.do_move_chess_notation("e5", "d6"):
        print("do move f5 to d6 passed")
    else:
        print("do move f5 to d6 failed")
        return False
    chess_board.undo_move()
    if chess_board.board == board:
        print("undo_move passed")
    else:
        print("undo_move failed")
        print("chess_board.board = ", chess_board.board)
        print("board = ", board)
        return False



def Test1():
    print("Test game __init__")
    try:
        import chess
    except:
        print("import chess failed")
        return False
    else:
        try:
            chess_board = chess.chess_board()
            print("chess_board __init__ passed")
        except:
            print("chess_board __init__ failed")
            return False
        else:
            try:
                chess_terminal_output = chess.chess_terminal(chess_board)
                print("chess_terminal_output __init__ passed")
            except:
                print("chess_terminal_output __init__ failed")
                return False
            else:
                return True




def Test2():
    print("Test perft values")
    Perft0()
    Perft1()
    Perft2()
    Perft3()
    Perft4()

def Test3():
    print("Test FEN to binary")
    FEN_2_game()
    pawn_moves()
    en_passant()

def main():
    print("Tests started")
    Test1()
    Test2()
    Test3()
    print("Tests finished")

if __name__ == '__main__':
    main()