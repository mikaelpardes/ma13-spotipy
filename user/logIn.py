from user.client import User


def signIn(user):
    file = open("users.txt", "a+")
    file.write("\n")
    file.write(user.__str__())
    file.close()


def checkIfUserExsist(user):
    file = open("users.txt")
    search_word = user.userName
    if (search_word in file.read()):
        print("wellcome back")
    else:
        print("you need to sign in click y or n")
        answer = input()
        if answer == "y":
            signIn(user)


