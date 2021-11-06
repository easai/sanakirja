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
from fi_lib import *


url = "https://sanakirja.pythonanywhere.com"
wrong = []
pause = 3


def quiz(n=10, n_choices=5):
    try:
        sanakirja = SanaKirja(url)
        n_words = int(n)
        for i in range(n_words):
            res = sanakirja.nrand(n_choices)
            n = len(res)
            r = random.randrange(0, n)
            ans = Sana(res[r])
            print(f"Which of the following best describes [{ans.desc}]?")
            for j in range(n_choices):
                opt = Sana(res[j])
                print(f"{opt.exp}")
            try:
                choice = input("Enter the word: ")
                if unidecode.unidecode(choice) == unidecode.unidecode(ans.exp):
                    print(f"Correct.")
                else:
                    wrong.append(ans)
                    print(f"Incorrect.")
            except Exception as e:
                wrong.append(ans)
            ans.dump()
            time.sleep(pause)
            print()
        if wrong:
            print("Review the following word(s):")
            sanakirja.dump(wrong)
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
