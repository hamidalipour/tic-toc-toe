import Game
class MainBoard():
    def __init__(self):
        pass

    @staticmethod
    def run():
        while True:
            print("choose on of the three options")
            print("type S for starting the game")
            print("type V for visiting game history")
            print("type Q for quit")

            input_ = input()
            if input_ == "S":
                player1 = input("Player 1: ")
                player2 = input("Player 2: ")
                game = Game.Game(player1, player2)
                result = game.play()
            if input_ == "V":
                pass
            if input_ == "Q":
                print("see you later")
                break
if __name__ == '__main__':
    print("welcome to tic toc toe!")
    MainBoard.run()


