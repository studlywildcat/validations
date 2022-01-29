#!/usr/bin/env python3

import validations
import sys

def main():
    usrname = input('Enter your usename: ')
    if validations.vailidate_user(username=usrname, minlen=8):
        print("Valid Username")
        sys.exit(0)
    else:
        print("Invalid Username")
        sys.exit(1)

if __name__ == "__main__":
    main()
