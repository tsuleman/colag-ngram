#!/usr/bin/env python
""" removes duplicate sentences """

import argparse
import re

def main(args: argparse.Namespace):
    sentences = []
    text = args.txt
    new_text = re.sub(r'.txt','sentences.txt',text)
    with open(text,'r') as source, open(new_text,'w') as new:
        for line in source:
            if line.strip() not in sentences:
                sentences.append(line.strip())
                print(line.strip(),file=new)
                

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('txt',help='text to deduplicate')

    main(parser.parse_args())