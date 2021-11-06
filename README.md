# sanakirja
A collection of client side apps for sanakirja API.

fi-flash.py -- Finnish flash cards
<pre>
Usage: fi-flash.py [--help|-h] [--local|-l] [-n N]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
</pre>

fi-quiz.py -- Finnish vocabulary quiz.
<pre>
Usage: fi-quiz.py [--help|-h] [--local|-l] [-n N] [-m M]

Options:
    -h, --help  show this help message and exit
    -l, --local  run locally
    -n N    number of tests (default: 10)
    -m M    number of choices (default: 5)
</pre>
A sample session would look as follows:
<pre>
1: bread
2: banana
3: stone, rock
4: wolf
5: pulla (traditional, Finnish sweet bread)
Which best describes the word [kivi]? 3
Correct. [kivi] means [stone, rock]
</pre>
