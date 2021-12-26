#!/usr/bin/env python
""" Checks generated sentences against gold set (no duplicates) 
    Also creates text file of ungrammatical sentences"""

import argparse
import re


def main(args: argparse.Namespace):
    sent_count = 0
    grammatical = 0
    grammatical_set = []
    ungram_txt = re.sub(r'.txt','ungr.txt',args.txt) 

    with open(args.txt,'r') as hyp:
        with open(ungram_txt,'w') as sink:
            for gen in hyp:
                sent_count += 1
                with open(args.gold,"r") as gold:
                    for sent in gold:
                        if gen.strip() == sent.strip():
                            grammatical += 1
                            grammatical_set.append(gen)
                if gen not in grammatical_set:
                    print(gen.strip(),file=sink)
                

    print(f'{grammatical}/{sent_count} = {(100*grammatical/sent_count):.2f}%')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('txt')
    parser.add_argument('gold')

    main(parser.parse_args())