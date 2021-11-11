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


def fi(word, lang=None, is_local=False):
    try:
        sanakirja = SanaKirja(is_local=is_local)
        if not lang:
            res = sanakirja.en(word)
        else:
            req = sanakirja.fi(word)
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
    lang = None
    if args["--fi"]:
        lang = 'fi'
    fi(args['<word>'], lang, is_local=args['--local'])
