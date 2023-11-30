#!/usr/bin/python3
import re

import hidden_4
lists = dir(hidden_4)

if __name__ == "__main__":
    for name in lists:
        if "__" not in name:
            print("{}".format(name))
