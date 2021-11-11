"""Finnish vocabulary quiz.

Usage: fi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M] [--pause|-p PAUSE]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
    -p, --pause PAUSE  number of seconds before going on
"""
from docopt import docopt
import random
import time
from sanakirja import *

wrong = []
pause = 3


def quiz(n=10, n_choices=5, is_local=False):
    try:
        sanakirja = SanaKirja(is_local=is_local)
        n_words = int(n)
        for i in range(n_words):
            res = sanakirja.nrand(n_choices)
            n = len(res)
            r = random.randrange(0, n)
            ans = Sana(res[r])
            print()
            for j in range(n_choices):
                opt = Sana(res[j])
                print(f"{j+1}: {opt.desc}")
            try:
                choice = int(
                    input(f"Which best describes the word [{ans.exp}]? ")) - 1
                if choice == r:
                    print(f"Correct.")
                else:
                    wrong.append(ans)
                    print(f"Incorrect.")
                    sel = Sana(res[choice])
                    print(f"{choice=}")
                    print(sel)
                    wrong.append(sel)
                    sel.dump()
            except Exception as e:
                wrong.append(ans)
            ans.dump()
            time.sleep(3)
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
            print("n must be an integer")
    if args['-m']:
        try:
            m = int(args['-m'])
        except ValueError:
            print("m must be an integer")
    if args['--pause']:
        try:
            pause = int(args['--pause'][0])
        except ValueError:
            print("PAUSE must be an integer")
    quiz(n, m, is_local=args['--local'])
