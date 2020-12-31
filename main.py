import os.path


class checkfile():
    def __init__():
        if os.path.exists("passwords.txt"):
            self.file = open("passwords.txt")
        else:
            self.file = open("passwords.txt", 'w')


if __name__ == '__main__':
    print_hi('yo')

