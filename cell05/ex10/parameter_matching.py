#!/usr/bin/env python3

import sys

if len(sys.argv) - 1 != 1:
    print("none")
    sys.exit()

if input("What was the parameter? ") == sys.argv[1]:
    print("Good job!")
else:
    print("Nope, sorry...")
