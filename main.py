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


def do_moves_deep(chess_board, color: str = "white", deep: int = 2) -> dict:
    if deep == 0:
        return {}
    else:
        possible_moves = chess_board.all_possible_moves_side(color=color)
        if possible_moves == {}:
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
                    moves[str(i) + ", " + str(j)] = do_moves_deep(chess_board, color, deep - 1)
                    chess_board.undo_move()
            return moves


def deep_search(dict: dict, deep: int = 2) -> int:
    count = 0
    if deep == 0:
        return 0
    for i in dict:
        if dict[i] == {}:
            count += 1
        else:
            count += deep_search(dict[i], deep - 1)
    return count


def count_possible_moves_deep(chess_board, color: str = "white", deep: int = 2) -> int:
    dict = do_moves_deep(chess_board, color, deep)
    return deep_search(dict, deep)


def main():
    import chess
    import time

    chess_board = chess.chess_board()
    chess_terminal = chess.chess_terminal(chess_board)
    chess_board.set_up()
    print(count_possible_moves_deep(chess_board, "white", 4))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
