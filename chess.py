class chess_board:
    def FEN_to_binary(self, FEN):
        chess_field = 0
        for i in range(len(FEN)):
            if FEN[i] == 'P':
                self.board[chess_field] = self.board[chess_field] | self.pawn
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'p':
                self.board[chess_field] = self.board[chess_field] | self.pawn
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == 'N':
                self.board[chess_field] = self.board[chess_field] | self.knight
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'n':
                self.board[chess_field] = self.board[chess_field] | self.knight
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == 'B':
                self.board[chess_field] = self.board[chess_field] | self.bishop
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'b':
                self.board[chess_field] = self.board[chess_field] | self.bishop
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == 'R':
                self.board[chess_field] = self.board[chess_field] | self.rook
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'r':
                self.board[chess_field] = self.board[chess_field] | self.rook
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == 'Q':
                self.board[chess_field] = self.board[chess_field] | self.queen
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'q':
                self.board[chess_field] = self.board[chess_field] | self.queen
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == 'K':
                self.board[chess_field] = self.board[chess_field] | self.king
                self.board[chess_field] = self.board[chess_field] | self.white
                chess_field += 1
            elif FEN[i] == 'k':
                self.board[chess_field] = self.board[chess_field] | self.king
                self.board[chess_field] = self.board[chess_field] | self.black
                chess_field += 1
            elif FEN[i] == '/':
                continue
            else:
                chess_field += int(FEN[i])

    def white_pawn_possible_moves(self, position):
        if position < 8:
            return []
        else:
            possible_moves = []
            if self.board[position - 8] == 0:
                possible_moves.append(position - 8)
            if position % 8 != 0:
                if self.board[position - 9] & self.black:
                    possible_moves.append(position - 9)
            if position % 8 != 7:
                if self.board[position - 7] & self.black:
                    possible_moves.append(position - 7)
            if (self.height - 2) * self.width < position < self.height * (self.width - 1):
                if self.board[position - 16] == 0:
                    possible_moves.append(position - 16)
            return possible_moves

    def possible_moves(self, position):
        if self.board[position] & self.pawn:
            if self.board[position] & self.white:
                return self.white_pawn_possible_moves(position)


    def binary_to_FEN(self):
        pass

    def __init__(self):
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
        self.FEN_to_binary('rnbqkbnr/pppppppp/8/8/8/3p4/PPPPPPPP/RNBQKBNR')


class chess_terminal:



    def print_board(self):
        text = ''
        for i in range(-1,self.height+1):
            for j in range(-1,self.width+1):
                if i == -1:
                    if j == -1 or j == self.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(j+1) + " ", "white", "dark_brown")
                elif j == -1:
                    if i == self.height:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(self.int2letter(self.height-i-1)) + " ", "white", "dark_brown")
                elif i == self.height:
                    if j == -1 or j == self.width:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(j+1) + " ", "white", "dark_brown")
                elif j == self.width:
                    if i == -1:
                        text += self.colour.ansi_text_and_background_coloring("   ", "white", "dark_brown")
                    else:
                        text += self.colour.ansi_text_and_background_coloring(" " + str(self.int2letter(self.height-i-1)) + " ", "white", "dark_brown")
                else:
                    if (i + j) % 2 == 0:
                        backround = "black"
                    else:
                        backround = "white"
                    if self.board[i * self.width + j] == (self.pawn | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.pawn | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" P ", "full_black", backround)
                    elif self.board[i * self.width + j] == (self.knight | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.knight | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" N ", "full_black", backround)
                    elif self.board[i * self.width + j] == (self.bishop | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.bishop | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" B ", "full_black", backround)
                    elif self.board[i * self.width + j] == (self.rook | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.rook | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" R ", "full_black", backround)
                    elif self.board[i * self.width + j] == (self.queen | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.queen | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" Q ", "full_black", backround)
                    elif self.board[i * self.width + j] == (self.king | self.white):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_white", backround)
                    elif self.board[i * self.width + j] == (self.king | self.black):
                        text += self.colour.ansi_text_and_background_coloring(" K ", "full_black", backround)
                    else:
                        text += self.colour.ansi_background_coloring("   ", backround)
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
        self.height = chess_board.height
        self.width = chess_board.width
        self.board = chess_board.board
        self.pawn = chess_board.pawn
        self.knight = chess_board.knight
        self.bishop = chess_board.bishop
        self.rook = chess_board.rook
        self.queen = chess_board.queen
        self.king = chess_board.king
        self.white = chess_board.white
        self.black = chess_board.black


