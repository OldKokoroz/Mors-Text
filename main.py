from time import sleep
import os
from dicts import alphabet, reverse_alp


def turning_func():
    mode = input("Mode: ")

    code = input("Message: ").lower().split("/")
    code_chars = ""

    as_text = ""
    translated = ""

    if mode == "1":

        count = 0
        for a in code[count]:
            if a == ".":
                a = "•"
                
            code_chars += a

            as_text += f"{reverse_alp.fromkeys(a)}"

            count += 1

        for _ in code_chars:
            translated += _
            os.system(f"say {_}")

            if _ in alphabet.keys():
                os.system(f"say {alphabet.values(_)}")

                sleep(0.1)

        print("Morse Code: " + as_text)

        os.system(f"say {translated}")

    elif mode == "2":
        for _ in code:
            translated += _

            as_text += f"{alphabet.fromkeys(_)}"

            os.system(f"say {_}")

            if _ in reverse_alp.keys():
                os.system(f"say {reverse_alp.values(_)}")

                sleep(0.1)

        print(as_text)
        os.system(f"say {translated}")


turning_func()
