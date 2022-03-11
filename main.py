from base64 import *
from base32 import *
from base_32_64_dict import *


def menu():

    case = input("1 - чтение из файла\n2 - ввод с клавиатуры\n>>>\t")

    text = None
    finish = None

    if case == "1":

        with open("input.txt", "r") as file:
            text = file.read()

    elif case == "2":

        text = input("Input:\t")



    choose = input('Кодирование - 1\nДекодирование - 2\n>>>\t')

    if choose == "1":
        choice = input("1 - BASE64\n2 - BASE32\n>>>\t")

        if choice == "1":
            finish = to_base64(text)

        elif choice == "2":
            finish = to_base32(text)

    elif choose == "2":
        choice = input("1 - BASE64\n2 - BASE32\n>>>\t")

        if choice == "1":
            finish = to_ascii32(text)

        if choice == "2":
            finish = to_base32(text)

    with open('output.txt', 'w') as file:
        file.write(finish)


menu()
