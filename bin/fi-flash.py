"""Finnish flash cards

Usage: fi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
"""
import requests
from docopt import docopt
from sanakirja import *


def fi(url, n=10):
    sanakirja = SanaKirja(url)
    try:
        for i in range(n):
            r = sanakirja.rand()
            sana = Sana(r)
            input(f"{sana.exp}?")
            print(f"{sana.exp}: {sana.desc}")
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
    url = "https://sanakirja.pythonanywhere.com"
    if args["--local"]:
        url = "http://localhost:5000"
    fi(url, n)
