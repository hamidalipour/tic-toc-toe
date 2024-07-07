class Game:
    PLAYER1 = "player 1 is winner"
    PLAYER2 = "player 2 is winner"
    FULL = "it's a draw!"
    CONTINUE = "the game continues"
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.turn = 1

    def valid_coordinates(self, x, y):
        if x >= 0 and x < 3 and y >= 0 and y < 3:
            if self.board[x][y] == '-':
                return True
            else:
                print("this coordinate is not empty")
                return False
        print("invalid coordinates")
        return False

    def put_in_board(self, x, y):
        if self.turn == 1:
            self.board[x][y] = 'X'
        else:
            self.board[x][y] = 'O'

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end='')
            print()

    def board_is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def check_winner_rows(self):
        for i in range(3):
            score1 = 0
            score2 = 0
            for j in range(3):
                if self.board[i][j] == 'X':
                    score1 += 1
                if self.board[i][j] == 'O':
                    score2 += 1
            if score1 == 3:
                return self.PLAYER1
            if score2 == 3:
                return self.PLAYER2
        return None

    def check_winner_columns(self):
        for j in range(3):
            score1 = 0
            score2 = 0
            for i in range(3):
                if self.board[i][j] == 'X':
                    score1 += 1
                if self.board[i][j] == 'O':
                    score2 += 1
            if score1 == 3:
                return self.PLAYER1
            if score2 == 3:
                return self.PLAYER2
        return None

    def check_winner_diameters(self):
        score1_d1 = 0
        score2_d1 = 0
        score1_d2 = 0
        score2_d2 = 0
        for i in range(3):
            if self.board[i][i] == 'X':
                score1_d1 += 1
            if self.board[i][i] == 'O':
                score2_d1 += 1
            if self.board[i][3 - i - 1] == 'X':
                score1_d2 += 1
            if self.board[i][3 - i - 1] == 'O':
                score2_d2 += 1
        if score1_d1 == 3 or score1_d2 == 3:
            return self.PLAYER1
        if score2_d1 == 3 or score2_d2 == 3:
            return self.PLAYER2

        return None

    def calculate_result(self):
        rows_winner = self.check_winner_rows()
        columns_winner = self.check_winner_columns()
        diameters_winner = self.check_winner_diameters()

        if rows_winner == self.PLAYER1 or columns_winner == self.PLAYER1 or diameters_winner == self.PLAYER1:
            return self.PLAYER1
        if rows_winner == self.PLAYER2 or columns_winner == self.PLAYER2 or diameters_winner == self.PLAYER2:
            return self.PLAYER2
        if self.board_is_full():
            return self.FULL
        return self.CONTINUE

    def game_over(self):
        result = self.calculate_result()
        if result == self.CONTINUE:
            return False
        return True

    def play(self):
        while not self.game_over():
            self.print_board()
            if self.turn == 1:
                try:
                    x, y = map(int, input(f"{self.player1}'s turn. type the coordinate of your next move ").split())
                except:
                    print("Invalid coordinate")
                    continue

            else:
                try:
                    x, y = map(int, input(f"{self.player2}'s turn. type the coordinate of your next move ").split())
                except:
                    print("Invalid coordinate")
                    continue

            if self.valid_coordinates(x, y):
                self.put_in_board(x, y)
                self.turn *= -1


        return self.calculate_result()

