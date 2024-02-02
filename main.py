from time import sleep
import os
from dicts import alphabet, reverse_alp


def turning_func():
    mode = input('''
|----------MODE-----------|
| 1 - Text -> Morse code  |
| 2 - Text <- Morse code  |
| 99 - Exit               |
|-------------------------|
|-> ''')

    try:
        sleep(1)
    
        translated = ""
        as_text = ""
    
        # Text - Code Section
    
        if mode == "1":
            while True:
                message = input("""
    -------------------------------------
    Message: """).lower()
    
                if message == "99":
                    break
    
                for inp in list(message):
                    if inp in alphabet.keys():
                        print("\nChange mode to translate morse code!\n")
                        break
    
                    elif inp not in reverse_alp.keys():
                        print("Invalid characters!")
                        break
    
                    translated += inp
    
                    as_text += f"{reverse_alp.get(inp)}/"
    
                    os.system(f"say {inp}")
    
                    sleep(0.05)
    
                print(f"""\n
    Morse Code: {as_text}
    -------------------------------------""")
    
                os.system(f"say your message is {translated}")
                as_text = ""
                translated = ""
    
        # Code - Text Section
    
        elif mode == "2":
            while True:
                code = input("""\n
    -------------------------------------
    Morse Code (Ex: ••••/–––/•) : """).split("/")
    
                for _ in code:
                    if _ not in alphabet.keys():
                        print("!!! Invalid characters included !!!")
    
                    as_text += f"{alphabet.get(_)}"
    
                    os.system(f"say {alphabet.get(_)}")
    
                    sleep(0.1)
    
                os.system(f"say your message is {as_text}")
                print(f"""\n
    Message: {as_text.capitalize()}
    -------------------------------------
    """)
                as_text = ""

    except ValueError or Exception:
        print("Error!")
        
    except KeyboardInterrupt:
        print("Exiting")
        exit()
        

turning_func()
