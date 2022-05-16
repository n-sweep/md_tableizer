#!/usr/bin/env python3

import pyperclip
import numpy as np
import pandas as pd


def makerow(row, pad=0):
    """
        Formats one row of data with pipes ( | )

        Parameters
        -------------------
        row: A row of data
        pad (int): Pad size - the length of the longest string
            in the data to create consistently sized columns

        Returns
        -------------------
        Markdown-formatted row string
        eg. | Here     | is       | an       | example  |
    """
    if type(pad) in (list, tuple):
        padded = [item.ljust(width) for item, width in zip(row, pad)]
    else:
        padded = [item.ljust(pad) for item in row]
    return f"| {' | '.join(padded)} |"


def tableize(inp, clip=False):
    """
        Turns a table of data into a formatted table string for Markdown

        Parameters
        -------------------
        inp: A table of data. List of lists, numpy array, pandas dataframe
        clip (bool): Set to True to copy the output to your clipboard
            rather than return the string.

        Returns
        -------------------
        Markdown-formatted table string
    """

    inp = np.array(inp)   # This handles pandas dataframes nicely

    # Get longest word in each column
    col_widths = [max([len(c) for c in inp[:, i]]) for i in range(inp.shape[1])]

    # Create separator - this normalizes the width of every
    # column to the longest word in the table
    separator = makerow(['-' * w for w in col_widths])

    # Pad words to padlen
    padded = [makerow(row, col_widths) for row in inp]
    # Insert separator
    padded.insert(1, separator)
    output = '\n'.join(padded)

    if clip:
        # Copy output to clipboard
        pyperclip.copy(output)
    else:
        # Return output string
        return output


def main():
    toy_data = [
        ['Here', 'Are', 'Some', 'Titles'],
        ['Here', 'is', 'some', 'data'],
        ["Here's", 'some', 'more', 'data']
    ]

    print(tableize(toy_data))


if __name__ == '__main__':
    main()
