#!/usr/bin/env python3
import sys
import random

def parse_file(input_file):
    f_list = []
    strip_lines = ("---", "", " ", "\n")
    with open(input_file, "r") as f:
        f_list = [line.strip() for line in f if line.strip() not in strip_lines]
        quotes = f_list[::2]
        people = f_list[1::2]
        result = []
        for k, v in enumerate(quotes):
            result.append('"' + v + '" ' + people[k])
    return result

def random_quote(input_file):
    quotes = parse_file(input_file)
    rand = random.randrange(0, len(quotes))
    randquote = quotes[rand]
    return randquote

try:
    path = sys.argv[1]
    print(random_quote(path))
except:
    print(random_quote("/home/frs/quotes/quotes.txt"))
