"""Finnish vocabulary quiz.

Usage: fi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
"""
import requests
import platform
from docopt import docopt
import random


ossystem = platform.uname()[0]
url = "https://sanakirja.pythonanywhere.com"


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
            print()
            for j in range(n_choices):
                opt = res[j]
                print(f"{j+1}: {opt['description']}")
            choice = int(input(f"Which best describes the word [{exp}]? "))
            if choice - 1 == r:
                print(
                    f"Correct. [{ans['expression']}] means [{ans['description']}]")
            else:
                print(
                    f"Incorrect. [{ans['expression']}] means [{ans['description']}]")
            print()
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
