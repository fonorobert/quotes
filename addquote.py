#!/usr/bin/env python3
import os


def add_quote(quote, person):
    with open("quotes.txt", "a") as f:
        f.write(quote)
        f.write("\n")
        f.write("/" + person + "/")
        f.write("\n")
        f.write("---")
        f.write("\n")
    return True

def sanitize_quote(quote):
    quote = quote.replace("'", "'\\''")
    return quote

print("Welcome to my quote collection. Please add your quote!")
print("")
quote = input("Quote:")
person = input("Person:")
tweet = input("Do you want to tweet this? (y/n)")

if add_quote(quote, person):
    if tweet is "Y" or tweet is "y":
        os.system("echo '\"" + sanitize_quote(quote) + "\"' /" + person + "/ | tweet")

    print("")
    print("Quote added. Thanks for contributing. Cheers, ~frs")
