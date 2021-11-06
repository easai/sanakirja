"""Finnish vocabulary quiz (type in the word).

Usage: fi-write.py [--help|-h] [--local|-l] [-n N] [-m M] [--pause|-p PAUSE]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
    -p, --pause PAUSE  number of seconds before going on
"""
import requests
from docopt import docopt
import random
import unidecode
import time


url = "https://sanakirja.pythonanywhere.com"
wrong = []
pause = 3


def quiz(n=10, n_choices=5):
    try:
        n_words = int(n)
        for i in range(n_words):
            req = requests.get(f"{url}/nrand/{n_choices}")
            res = req.json()
            n = len(res)
            r = random.randrange(0, n)
            ans = res[r]
            exp = ans['expression']
            desc = ans['description']
            print(f"Which of the following best describes [{desc}]?")
            for j in range(n_choices):
                opt = res[j]
                print(f"{opt['expression']}")
            try:
                choice = input("Enter the word: ")
                if unidecode.unidecode(choice) == unidecode.unidecode(exp):
                    print(f"Correct.")
                else:
                    wrong.append(ans)
                    print(f"Incorrect.")
            except Exception as e:
                pass
            print(f"[{exp}] means [{desc}].")
            time.sleep(pause)
            print()
        if wrong:
            print("Review the following word(s):")
            for item in wrong:
                print(f"[{item['expression']}] means [{item['description']}].")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    n = 10
    m = 5
    if args["-n"]:
        try:
            n = int(args['-n'])
        except ValueError:
            print("N must be an integer")
    if args['-m']:
        try:
            m = int(args['-m'])
        except ValueError:
            print("M must be an integer")
    if args["--local"]:
        url = "http://localhost:5000"
    if args['--pause']:
        try:
            pause = int(args['--pause'][0])
        except ValueError:
            print("PAUSE must be an integer")
    quiz(n, m)
