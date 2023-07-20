class chess_board:
    def clear_board(self):
        self.board = [0b0 for i in range(self.height * self.width)]

    def FEN_to_binary(self, FEN):
        self.clear_board()
        chess_field = 0
        FEN = FEN.split(' ')
        board_FEN = FEN[0]
        for i in range(len(board_FEN)):
            if board_FEN[i] == 'P':
                self.board[chess_field] = self.board[chess_field] | self.pawn
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'p':
                self.board[chess_field] = self.board[chess_field] | self.pawn
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == 'N':
                self.board[chess_field] = self.board[chess_field] | self.knight
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'n':
                self.board[chess_field] = self.board[chess_field] | self.knight
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == 'B':
                self.board[chess_field] = self.board[chess_field] | self.bishop
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'b':
                self.board[chess_field] = self.board[chess_field] | self.bishop
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == 'R':
                self.board[chess_field] = self.board[chess_field] | self.rook
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'r':
                self.board[chess_field] = self.board[chess_field] | self.rook
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == 'Q':
                self.board[chess_field] = self.board[chess_field] | self.queen
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'q':
                self.board[chess_field] = self.board[chess_field] | self.queen
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == 'K':
                self.board[chess_field] = self.board[chess_field] | self.king
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif board_FEN[i] == 'k':
                self.board[chess_field] = self.board[chess_field] | self.king
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif board_FEN[i] == '/':
                continue
            else:
                chess_field += int(board_FEN[i])
        if FEN[1] == 'w':
            self.moving_side = True
        else:
            self.moving_side = False
        self.castling = FEN[2]
        if FEN[3] != '-':
            self.en_passant = (self.letter2int(FEN[3][0:1])) + (8 - int(FEN[3][1:2])) * self.height
        else:
            self.en_passant = False
        self.halfmove_clock = int(FEN[4])
        self.fullmove_number = int(FEN[5])

    def moves_in_direction(self, position: int, direction: int, color: bin) -> list:
        possible_moves = []
        while True:
            position += direction
            if position < 0 or position >= self.height * self.width:
                break
            if self.board[position] == 0:
                possible_moves.append(position)
            elif self.board[position] & color:
                break
            else:
                possible_moves.append(position)
                break
        return possible_moves

    def white_pawn_possible_moves(self, position):
        if position < self.height:
            return []
        else:
            possible_moves = []
            if self.board[position - (self.width)] == 0:
                possible_moves.append(position - (self.width))
            if position % self.width != 0:
                if self.board[position - (self.width + 1)] & self.black:
                    possible_moves.append(position - (self.width + 1))
            if position % self.width != (self.width - 1):
                if self.board[position - (self.width - 1)] & self.black:
                    possible_moves.append(position - (self.width - 1))
            if position // self.width == (self.height - 2):
                if self.board[position - (self.width * 2)] == 0:
                    possible_moves.append(position - (self.width * 2))
            if self.en_passant != False:
                if position % self.width != 0:
                    if self.en_passant == position - (self.width + 1):
                        possible_moves.append(position - (self.width + 1))
                if position % self.width != (self.width - 1):
                    if self.en_passant == position - (self.width - 1):
                        possible_moves.append(position - (self.width - 1))
            return possible_moves

    def black_pawn_possible_moves(self, position):
        if position > (self.height - 1) * self.width - 1:
            return []
        else:
            possible_moves = []
            if self.board[position + self.width] == 0:
                possible_moves.append(position + self.width)
            if position % self.width != 0:
                if self.board[position + (self.width - 1)] & self.white:
                    possible_moves.append(position + (self.width - 1))
            if position % self.width != (self.width - 1):
                if self.board[position + (self.width + 1)] & self.white:
                    possible_moves.append(position + (self.width + 1))
            if position // self.width == 1:
                if self.board[position + (self.width * 2)] == 0:
                    possible_moves.append(position + self.width * 2)
            if self.en_passant != False:
                if position % self.width != 0:
                    if self.en_passant == position + (self.width - 1):
                        possible_moves.append(position + (self.width - 1))
                if position % self.width != (self.width - 1):
                    if self.en_passant == position + (self.width + 1):
                        possible_moves.append(position + (self.width + 1))
            return possible_moves

    def white_knight_possible_moves(self, position):
        possible_moves = []
        if position % self.width < (self.width - 2):
            if position > (self.width - 1):
                possible_moves.append(position - (self.width - 2))
            if position < ((self.height - 1) * self.width):
                possible_moves.append((position + (self.width + 2)))
        if position % self.width > 1:
            if position > (self.width - 2):
                possible_moves.append(position - (self.width + 2))
            if position < ((self.height - 1) * self.width):
                possible_moves.append(position + (self.width - 2))
        if position > (self.width * 2) - 1:
            if position % self.width < (self.width - 1):
                possible_moves.append(position - (self.width * 2) + 1)
            if position % self.width > 0:
                possible_moves.append(position - (self.width * 2) - 1)
        if position < ((self.height - 2) * self.width):
            if position % self.width < (self.width - 1):
                possible_moves.append(position + (self.width * 2) + 1)
            if position % self.width > 0:
                possible_moves.append(position + (self.width * 2) - 1)
        for i in possible_moves:
            if self.board[i] & self.white:
                possible_moves.remove(i)
        return possible_moves

    def black_knight_possible_moves(self, position):
        possible_moves = []
        if position % self.width < (self.width - 2):
            if position > (self.width - 1):
                possible_moves.append(position - (self.width - 2))
            if position < ((self.height - 1) * self.width):
                possible_moves.append((position + (self.width + 2)))
        if position % self.width > 1:
            if position > (self.width - 2):
                possible_moves.append(position - (self.width + 2))
            if position < ((self.height - 1) * self.width):
                possible_moves.append(position + (self.width - 2))
        if position > (self.width * 2) - 1:
            if position % self.width < (self.width - 1):
                possible_moves.append(position - (self.width * 2) + 1)
            if position % self.width > 0:
                possible_moves.append(position - (self.width * 2) - 1)
        if position < ((self.height - 2) * self.width):
            if position % self.width < (self.width - 1):
                possible_moves.append(position + (self.width * 2) + 1)
            if position % self.width > 0:
                possible_moves.append(position + (self.width * 2) - 1)
        for i in possible_moves:
            if self.board[i] & self.black:
                possible_moves.remove(i)
        return possible_moves

    def white_bishop_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width - 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width + 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width - 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width + 1, self.white)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def black_bishop_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width - 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width + 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width - 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width + 1, self.black)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def white_rook_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -1, self.white)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def black_rook_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -1, self.black)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def white_queen_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width - 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width + 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width - 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width + 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, 1, self.white)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -1, self.white)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def black_queen_possible_moves(self, position):
        possible_moves = []
        list = self.moves_in_direction(position, self.width - 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width + 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width - 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width + 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, self.width, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -self.width, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, 1, self.black)
        if list != []:
            possible_moves.extend(list)
        list = self.moves_in_direction(position, -1, self.black)
        if list != []:
            possible_moves.extend(list)
        return possible_moves

    def white_king_possible_moves(self, position):
        possible_moves_return = []
        possible_moves = [position - self.width - 1, position - self.width, position - self.width + 1,
                          position - 1, position + 1,
                          position + self.width + 1, position + self.width, position + self.width + 1]
        for i in possible_moves:
            if 0 < i < self.height * self.width:
                if not self.board[i] & self.white:
                    is_king = [i - self.width - 1, i - self.width, i - self.width + 1,
                               i - 1, i + 1,
                               i + self.width + 1, i + self.width, i + self.width + 1]
                    allowed = True
                    for j in is_king:
                        if 0 < i < self.height * self.width:
                            if self.board[j] & self.king | self.black:
                                allowed = False
                    if allowed:
                        possible_moves_return.append(i)
                    print(i)
        if "K" in self.castling:
            if self.board[position + 1] == 0 and self.board[position + 2] == 0:
                possible_moves_return.append(position + 2)
        if "Q" in self.castling:
            if self.board[position - 1] == 0 and self.board[position - 2] == 0 and self.board[position - 3] == 0:
                possible_moves_return.append(position - 2)
        return possible_moves_return

    def black_king_possible_moves(self, position):
        possible_moves_return = []
        possible_moves = [position - self.width - 1, position - self.width, position - self.width + 1,
                          position - 1, position + 1,
                          position + self.width + 1, position + self.width, position + self.width + 1]
        for i in possible_moves:
            if 0 < i < self.height * self.width:
                if not self.board[i] & self.black:
                    is_king = [i - self.width - 1, i - self.width, i - self.width + 1,
                               i - 1, i + 1,
                               i + self.width + 1, i + self.width, i + self.width + 1]
                    allowed = True
                    for j in is_king:
                        if 0 < i < self.height * self.width:
                            if self.board[j] & self.king | self.white:
                                allowed = False
                    if allowed:
                        possible_moves_return.append(i)
        if "k" in self.castling:
            if self.board[position + 1] == 0 and self.board[position + 2] == 0:
                possible_moves_return.append(position + 2)
        if "q" in self.castling:
            if self.board[position - 1] == 0 and self.board[position - 2] == 0 and self.board[position - 3] == 0:
                possible_moves_return.append(position - 2)
        return possible_moves_return

    def possible_moves(self, position):
        if self.board[position] == self.pawn + self.white:
            return "pawn", self.white_pawn_possible_moves(position)
        elif self.board[position] == self.pawn + self.black:
            return "pawn", self.black_pawn_possible_moves(position)
        elif self.board[position] == self.knight + self.white:
            return "knight", self.white_knight_possible_moves(position)
        elif self.board[position] == self.knight + self.black:
            return "knight", self.black_knight_possible_moves(position)
        elif self.board[position] == self.bishop + self.white:
            return "bishop", self.white_bishop_possible_moves(position)
        elif self.board[position] == self.bishop + self.black:
            return "bishop", self.black_bishop_possible_moves(position)
        elif self.board[position] == self.rook + self.white:
            return "rock", self.white_rook_possible_moves(position)
        elif self.board[position] == self.rook + self.black:
            return "rock", self.black_rook_possible_moves(position)
        elif self.board[position] == self.queen + self.white:
            return "queen", self.white_queen_possible_moves(position)
        elif self.board[position] == self.queen + self.black:
            return "queen", self.black_queen_possible_moves(position)
        elif self.board[position] == self.king + self.white:
            return "king", self.white_king_possible_moves(position)
        elif self.board[position] == self.king + self.black:
            return "king", self.black_king_possible_moves(position)
        else:
            return [], []

    def move_possible(self, start_pos: int, end_pos: int) -> bool:
        """

        :param start_pos:
        :param end_pos:
        :return:
        """
        return end_pos in self.possible_moves(start_pos)[1]


    def do_move(self, start_pos: int, end_pos: int) -> None:
        """

        :param start_pos:
        :param end_pos:
        :return:
        """
        if self.move_possible(start_pos, end_pos):
            self.move_list.append(
                (start_pos, end_pos, self.board[start_pos], self.board[end_pos], self.en_passant, self.castling))
            if self.board[start_pos] == self.pawn + self.white:
                if self.en_passant != False:
                    if start_pos % self.width != 0 and self.en_passant == start_pos - (self.width + 1):
                        self.board[start_pos - 1] = 0
                    if start_pos % self.width != (self.width - 1) and self.en_passant == start_pos - (self.width - 1):
                        self.board[start_pos + 1] = 0
                if end_pos - start_pos == 2 * self.width:
                    self.en_passant = end_pos - self.width
                self.board[start_pos] = 0
                self.board[end_pos] = self.pawn + self.white
            elif self.board[start_pos] == self.pawn + self.black:
                if self.en_passant != False:
                    if start_pos % self.width != 0 and self.en_passant == start_pos + (self.width - 1):
                        self.board[start_pos - 1] = 0
                    if start_pos % self.width != (self.width - 1) and self.en_passant == start_pos + (self.width + 1):
                        self.board[start_pos + 1] = 0
                if end_pos - start_pos == -2 * self.width:
                    self.en_passant = end_pos + self.width
                self.board[start_pos] = 0
                self.board[end_pos] = self.pawn + self.black
            elif self.board[start_pos] == self.king + self.white:
                if start_pos == self.white_king_pos and end_pos == self.white_king_pos + 2:
                    self.board[start_pos + 3] = 0
                    self.board[start_pos + 1] = self.rook + self.white
                elif start_pos == self.white_king_pos and end_pos == self.white_king_pos - 2:
                    self.board[start_pos - 4] = 0
                    self.board[start_pos -1] = self.rook + self.white
                self.board[start_pos] = 0
                self.board[end_pos] = self.king + self.white
                self.castling = self.castling.replace("K", "")
                self.castling = self.castling.replace("Q", "")
            elif self.board[start_pos] == self.king + self.black:
                if start_pos == self.black_king_pos and end_pos == self.black_king_pos + 2:
                    self.board[start_pos + 3] = 0
                    self.board[start_pos + 1] = self.rook + self.black
                elif start_pos == self.black_king_pos and end_pos == self.black_king_pos - 2:
                    self.board[start_pos - 4] = 0
                    self.board[start_pos - 1] = self.rook + self.black
                self.board[start_pos] = 0
                self.board[end_pos] = self.king + self.black
                self.castling = self.castling.replace("k", "")
                self.castling = self.castling.replace("q", "")
            elif self.board[start_pos] == self.rook + self.white:
                if start_pos == self.white_rook_pos[0]:
                    self.castling = self.castling.replace("Q", "")
                elif start_pos == self.white_rook_pos[1]:
                    self.castling = self.castling.replace("K", "")
                self.board[start_pos] = 0
                self.board[end_pos] = self.rook + self.white
            elif self.board[start_pos] == self.rook + self.black:
                if start_pos == self.black_rook_pos[0]:
                    self.castling = self.castling.replace("q", "")
                elif start_pos == self.black_rook_pos[1]:
                    self.castling = self.castling.replace("k", "")
                self.board[start_pos] = 0
                self.board[end_pos] = self.rook + self.black
            else:
                self.board[start_pos] = 0
                self.board[end_pos] = self.board[start_pos]



    def undo_move(self) -> None:
        """

        :return:
        """
        if len(self.move_list) > 0:
            move = self.move_list.pop()
            self.board[move[0]] = move[2]
            self.board[move[1]] = move[3]
            self.en_passant = move[4]
            self.castling = move[5]






    def all_possible_moves_side(self, color, with_piece_type: bool = False):
        possible_moves = {}
        possible_moves_piece = {}
        if color == "white":
            for i in range(self.height * self.width):
                if self.board[i] & self.white:
                    moves = self.possible_moves(i)
                    if moves[1] != []:
                        possible_moves[i] = moves[1]
                        if not str(moves[0]) in possible_moves_piece:
                            possible_moves_piece[str(moves[0])] = {}
                        possible_moves_piece[str(moves[0])][i] = moves[1]
        elif color == "black":
            for i in range(self.height * self.width):
                if self.board[i] & self.black:
                    moves = self.possible_moves(i)
                    if moves[1] != []:
                        possible_moves[i] = moves[1]
                        if not str(moves[0]) in possible_moves_piece:
                            possible_moves_piece[str(moves[0])] = {}
                        possible_moves_piece[str(moves[0])][i] = moves[1]
        if with_piece_type:
            return possible_moves_piece
        else:
            return possible_moves

    def set_up(self):
        self.FEN_to_binary('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        self.move_list = []

    def binary_to_FEN(self):
        pass

    def __init__(self):
        import friedas_lil_lib as fll
        self.i2l_l2i = fll.letter_and_int()
        self.letter2int = self.i2l_l2i.lower_letter_to_int
        self.move = 0
        self.height = 8
        self.width = 8
        self.board = [0b0 for i in range(self.height * self.width)]
        self.pawn = 0b00001
        self.knight = 0b00010
        self.bishop = 0b00011
        self.rook = 0b00100
        self.queen = 0b00101
        self.king = 0b00110
        self.white = 0b01000
        self.black = 0b10000
        self.white_king_pos = 4
        self.black_king_pos = 60
        self.white_rook_pos = [self.width*(self.height-1), self.width*self.height-1]
        self.black_rook_pos = [0, self.width-1]
        self.moving_side = None
        self.en_passant = None
        self.castling = None
        self.halfmove_clock = None
        self.fullmove_number = None
        self.move_list = []
        self.FEN_to_binary('rnbqkbnr/pp2pppp/2p5/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3')


class chess_terminal:

    def print_board(self, hovered_field=None, possible_moves=[]):
        text = ''
        for i in range(-1, self.chess_board.height + 1):
            for j in range(-1, self.chess_board.width + 1):
                if i == -1:
                    if j == -1 or j == self.chess_board.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + self.int2letter(j) + " ", "white",
                                                                              "dark_brown")
                elif j == -1:
                    if i == self.chess_board.height:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(
                            " " + str(self.chess_board.height - i) + " ", "white", "dark_brown")
                elif i == self.chess_board.height:
                    if j == -1 or j == self.chess_board.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + self.int2letter(j) + " ", "white",
                                                                              "dark_brown")
                elif j == self.chess_board.width:
                    if i == -1:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(
                            " " + str(self.chess_board.height - i) + " ", "white", "dark_brown")
                else:
                    if (i + j) % 2 == 0:
                        backround = "white"
                    else:
                        backround = "black"
                    if i * self.chess_board.height + j in possible_moves:
                        if backround == "white":
                            backround = "light_red"
                        else:
                            backround = "red"
                    if i * self.chess_board.height + j == hovered_field:
                        if backround == "white":
                            backround = "hover_red"
                        else:
                            backround = "hover_dark_red"
                    if self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.pawn | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.pawn | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.knight | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.knight | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.bishop | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.bishop | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.rook | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.rook | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.queen | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.queen | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.king | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (
                            self.chess_board.king | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_black", backround)
                    else:
                        text += self.colour.ansi_background_coloring(str(i * self.chess_board.height + j) + " ",
                                                                     backround)
            text += "\n"
        print(text)

    def clear(self):
        clear_text = ""
        for i in range(self.chess_board.height+3):
            for j in range(self.chess_board.width+3):
                clear_text += "   "
            clear_text += "\n"
        self.c2s(clear_text)


    def __init__(self, chess_board):
        import friedas_lil_lib as fll
        self.i2l_l2i = fll.letter_and_int()
        self.c2s = fll.clear_to_start
        self.int2letter = self.i2l_l2i.int_to_caps_letter
        self.letter2int = self.i2l_l2i.caps_letter_to_int
        self.colour = fll.colour({
            'black': "#B58863",
            'white': "#F0D9B5",
            'full_black': "#000000",
            'full_white': "#FFFFFF",
            'dark_brown': "#432C1C",
            'light_red': "#D07979",
            'red': "#E63F3F",
            'hover_red': "#A21313",
            'hover_dark_red': "#730505"
        })
        self.chess_board = chess_board
