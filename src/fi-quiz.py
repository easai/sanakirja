"""Finnish vocabulary quiz.

Usage: fi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
"""
import requests
from docopt import docopt
import random
import time
from fi_lib import *


url = "https://sanakirja.pythonanywhere.com"
wrong = []


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
            print()
            for j in range(n_choices):
                opt = res[j]
                print(f"{j+1}: {opt['description']}")
            try:
                choice = int(input(f"Which best describes the word [{exp}]? "))
                if choice - 1 == r:
                    print(f"Correct.")
                else:
                    wrong.append(ans)
                    print(f"Incorrect.")
                    wrong.append(res[choice])
                    dump(res[choice])
            except Exception as e:
                wrong.append(ans)
            dump(ans)
            time.sleep(3)
            print()
        if wrong:
            print("Review the following word(s):")
            dump_list(wrong)
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
            print("n must be an integer")
    if args['-m']:
        try:
            m = int(args['-m'])
        except ValueError:
            print("m must be an integer")
    if args["--local"]:
        url = "http://localhost:5000"
    quiz(n, m)
