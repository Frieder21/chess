def Perft0():
    print("perft(0)")
    import chess
    chess_board = chess.chess_board()
    chess_board.set_up()
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
    chess_board.set_up()
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
    chess_board.set_up()
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
    chess_board.set_up()
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
    chess_board.set_up()
    value = chess_board.perft(4)
    if value == 197281:
        print("Test5 passed")
        return True
    else:
        print("Test5 failed")
        print("value = ", value, "expected = ", 197281)
        return False

def Test1():
    print("Test Perft values")
    Perft0()
    Perft1()
    Perft2()
    Perft3()
    Perft4()
def main():
    print("Tests started")
    Test1()
    print("Tests finished")

if __name__ == '__main__':
    main()