class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.turn = 1

    def valid_coordinates(self, x, y):
        return True
    def put_in_board(self, x, y):
        pass
    def print_board(self):
        pass

    def calculate_result(self):
        pass
    def game_over(self):
        return False
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

