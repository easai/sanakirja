"""Finnish flash cards

Usage: fi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
"""
import requests
import platform
from docopt import docopt


ossystem = platform.uname()[0]
url = "https://sanakirja.pythonanywhere.com"


def fi(n=10):
    try:
        for i in range(n):
            r = requests.get(url + "/rand")
            res = r.json()
            exp = res['expression']
            input(f"{exp}?")
            print(f"{exp}: {res['description']}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    n = 10
    if args["-n"]:
        try:
            n = int(args['-n'])
        except ValueError:
            print("n must be an integer")
    if args["--local"]:
        url = "http://localhost:5000"
    fi(n)
