#!/usr/bin/env python
"""Create .txt file for generated sentences by selected language."""

import subprocess
import re
import argparse

def main(args: argparse.Namespace):

    num = args.num
    lm = args.lang_model + '.lm'
    hold = args.lang_model + "_hold.txt"
    txt = args.lang_model + f'{num}.txt'
    

    with open(hold,"w") as sink:
        print(subprocess.getoutput(f'ngramrandgen --max_sents={num} {lm} | farprintstrings'),file=sink)
    with open(hold,"r") as source:
        with open(txt,"w") as sink:
            for line in source:
                line = re.sub(r'<epsilon>','',line)
                line = re.sub(r'\s\s+',' ',line)
                print(line.rstrip(),file=sink)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lang_model",help="language model (eg. L#_bi)")
    parser.add_argument("num",help="number of sentences")

main(parser.parse_args())