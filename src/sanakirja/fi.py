"""Finnish online dictionary.

Usage: fi.py [--help|-h] [--local|-l] [--fi|-f] <word>

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -f, --fi    the word is Finnish
"""
import requests
from docopt import docopt
import time
from sanakirja import *


url = SANAKIRJA_API


def fi(word, lang=None):
    try:
        if not lang:
            req = requests.get(f"{url}/{word}")
        else:
            req = requests.get(f"{url}/fi/{word}")
        res = req.json()
        n = len(res)
        if type(res) is list:
            for item in res:
                sana = Sana(item)
                sana.dump()
        else:
            print('That is not in my dictionary (sorry!).')
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    args = docopt(__doc__)
    if args["--local"]:
        url = "http://localhost:5000"
    lang = None
    if args["--fi"]:
        lang = 'fi'
    fi(args['<word>'], lang)
