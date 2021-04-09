import pyperclip
import numpy as np
import pandas as pd


def makerow(row, pad=0):
    """
        Formats one row of data with pipes ( | )

        Parameters
        -------------------
        row: A row of data

        Returns
        -------------------
        Markdown-formatted row string
        eg. | Here     | is       | an       | example  |
    """
    padded = [item.ljust(pad) for item in row]
    return '| ' + ' | '.join(padded) + ' |'


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

    # Get longest row & longest word
    rowlen = len(inp[0])
    padlen = max([max([len(item) for item in row]) for row in inp])

    # Create separator - this normalizes the width of every
    # column to the longest word in the table
    separator = makerow(['-'*padlen for _ in range(rowlen)])

    # Pad words to padlen
    padded = [makerow(row, padlen) for row in inp]
    # Insert separator
    padded.insert(1, separator)
    output = '\n'.join(padded)
    
    if clip:
        # Copy output to clipboard
        pyperclip.copy(output)
    else:
        # Return output string
        return output
