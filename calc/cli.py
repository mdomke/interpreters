from itertools import count
from termcolor import colored

from interpreter import Calculator


def run(parser, **kwargs):
    for i in count(1):
        s = None
        try:
            while not s:
                s = raw_input(colored('\nIn [%d]: ' % i, 'green'))
        except (EOFError, KeyboardInterrupt):
            break

        result = Calculator(parser.parse(s, **kwargs))()
        if result:
            print('{}: {}'.format(colored('Out[{}]'.format(i), 'red'), result))
