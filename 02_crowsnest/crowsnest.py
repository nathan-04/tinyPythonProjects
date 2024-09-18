#!/usr/bin/env python3
"""
Author : nathan <nathan@localhost>
Date   : 2024-09-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='a word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    first_letter = word[0].lower()

    article = 'a'
    if first_letter in 'aeiou' :
        article = 'an'

    print('Ahoy, Captain,', article, word, 'off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
