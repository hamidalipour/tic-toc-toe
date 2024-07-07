import Game
class MainBoard():
    def __init__(self):
        pass

    @staticmethod
    def print_history():
        with open('history.txt', 'r') as f:
            history = f.readlines()
            for line in history:
                print(line)
            print()

    @staticmethod
    def save_result(result, player1, player2):
        with open('history.txt', 'a') as f:
            data = f'{player1} played with {player2} and {result}'
            f.write(f"\n{data}")

    @staticmethod
    def run():
        while True:
            print("choose one of the three options")
            print("type S for starting the game")
            print("type V for visiting game history")
            print("type Q for quit")

            input_ = input()
            if input_ == "S":
                player1 = input("Player 1: ")
                player2 = input("Player 2: ")
                game = Game.Game(player1, player2)
                result = game.play()
                print(result)
                MainBoard.save_result(result, player1, player2)
            if input_ == "V":
                MainBoard.print_history()
            if input_ == "Q":
                print("see you later")
                break
if __name__ == '__main__':
    print("welcome to tic toc toe!")
    MainBoard.run()


