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
            self.en_passant = (self.letter2int(FEN[3][0:1])) + (8-int(FEN[3][1:2]))*self.height
        else:
            self.en_passant = False
        self.halfmove_clock = int(FEN[4])
        self.fullmove_number = int(FEN[5])

    def white_pawn_possible_moves(self, position):
        if position < 8:
            return []
        else:
            possible_moves = []
            if self.board[position - 8] == 0:
                possible_moves.append(position - 8)
            if position % self.width != 0:
                if self.board[position - 9] & self.black:
                    possible_moves.append(position - 9)
            if position % self.width != 7:
                if self.board[position - 7] & self.black:
                    possible_moves.append(position - 7)
            if position // self.width == 6:
                if self.board[position - 16] == 0:
                    possible_moves.append(position - 16)
            if self.en_passant != False:
                if position % self.width != 0:
                    if self.en_passant == position - 9:
                        possible_moves.append(position - 9)
                if position % self.width != 7:
                    if self.en_passant == position - 7:
                        possible_moves.append(position - 7)
            return possible_moves

    def black_pawn_possible_moves(self, position):
        if position > (self.height-1)*self.width-1:
            return []
        else:
            possible_moves = []
            if self.board[position + 8] == 0:
                possible_moves.append(position + 8)
            if position % self.width != 0:
                if self.board[position + 7] & self.white:
                    possible_moves.append(position + 7)
            if position % self.width != 7:
                if self.board[position + 9] & self.white:
                    possible_moves.append(position + 9)
            if position // self.width == 1:
                if self.board[position + 16] == 0:
                    possible_moves.append(position + 16)
            if self.en_passant != False:
                if position % self.width != 0:
                    if self.en_passant == position + 7:
                        possible_moves.append(position + 7)
                if position % self.width != 7:
                    if self.en_passant == position + 9:
                        possible_moves.append(position + 9)
            return possible_moves
    def possible_moves(self, position):
        if self.board[position] & self.pawn:
            if self.board[position] & self.white:
                return self.white_pawn_possible_moves(position)


    def set_up(self):
        self.FEN_to_binary('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

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
        self.moving_side = None
        self.en_passant = None
        self.castling = None
        self.halfmove_clock = None
        self.fullmove_number = None
        self.FEN_to_binary('rnbqkbnr/pp2pppp/2p5/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3')


class chess_terminal:



    def print_board(self):
        text = ''
        for i in range(-1, self.chess_board.height+1):
            for j in range(-1, self.chess_board.width+1):
                if i == -1:
                    if j == -1 or j == self.chess_board.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + self.int2letter(j) + " ", "white", "dark_brown")
                elif j == -1:
                    if i == self.chess_board.height:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(self.chess_board.height-i) + " ", "white", "dark_brown")
                elif i == self.chess_board.height:
                    if j == -1 or j == self.chess_board.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + self.int2letter(j) + " ", "white", "dark_brown")
                elif j == self.chess_board.width:
                    if i == -1:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(self.chess_board.height-i) + " ", "white", "dark_brown")
                else:
                    if (i + j) % 2 == 0:
                        backround = "white"
                    else:
                        backround = "black"
                    if self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.pawn | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.pawn | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.knight | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.knight | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.bishop | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.bishop | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.rook | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.rook | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.queen | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.queen | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_black", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.king | self.chess_board.white):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_white", backround)
                    elif self.chess_board.board[i * self.chess_board.width + j] == (self.chess_board.king | self.chess_board.black):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_black", backround)
                    else:
                        text += self.colour.ansi_background_coloring(str( i * self.chess_board.height + j)+" ", backround)
            text += "\n"
        print(text)


    def __init__(self, chess_board):
        import friedas_lil_lib as fll
        self.i2l_l2i = fll.letter_and_int()
        self.int2letter = self.i2l_l2i.int_to_caps_letter
        self.letter2int = self.i2l_l2i.caps_letter_to_int
        self.colour = fll.colour({
            'black': "#B58863",
            'white': "#F0D9B5",
            'full_black': "#000000",
            'full_white': "#FFFFFF",
            'dark_brown': "#432C1C"
        })
        self.chess_board = chess_board



