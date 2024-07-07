class MainBoard():
    def __init__(self):
        pass

    @staticmethod
    def run():
        print("choose on of the three options")
        print("type S for starting the game")
        print("type V for visiting game history")
        print("type Q for quit")

        input_ = input()
        if input_ == "S":
            pass
        if input_ == "V":
            pass
        if input_ == "Q":
            print("see you later")
if __name__ == '__main__':
    print("welcome to tic toc toe!")
    MainBoard.run()


