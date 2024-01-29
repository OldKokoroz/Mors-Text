from time import sleep
import os
from dicts import alphabet, reverse_alp


def turning_func():
    mode = input('''
|----------MODE-----------|
| 1 - Text -> Morse code  |
| 2 - Text <- Morse code  |
|-------------------------|
|-> ''')

    sleep(1)

    as_text = ""

    # Text - Code Section

    if mode == "1":
        message = input("\nMessage: ").lower()
        msg_chars = ""
        translated = ""

        count = 0
        for inp in message[count]:
            if inp not in reverse_alp.keys():
                print("\nEnter a text/message or change mode!\n")
                exit()

            msg_chars += inp

            as_text += f"{reverse_alp.get(inp)}/"

            count += 1

        for _ in msg_chars:
            translated += _
            os.system(f"say {_}")

            sleep(0.05)

        print(f"\nMorse Code: {as_text}")

        os.system(f"say your message is {translated}")

    # Code - Text Section

    elif mode == "2":
        code = input("\nMorse Code (Ex: ••••/–––/•) : ").split("/")

        for _ in code:
            if _ == "•":
                _ = "."

            as_text += f"{alphabet.get(_)}"

            os.system(f"say {alphabet.get(_)}")

            sleep(0.1)

        os.system(f"say your message is {as_text}")
        print(f"\nMessage: {as_text.capitalize()}")


turning_func()
