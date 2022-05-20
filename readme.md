`md_tableizer` is a small utility for turning a table of data into a markdown-formatted table.

Currently supports a list-of-lists, Numpy array or Pandas DataFrame as inputs.

```
pip install numpy
pip install pandas
pip install pyperclip
```
\* see note on `pyperclip` below

# Example Usage:

```
toy_data = [
    ['Here', 'Are', 'Some', 'Titles'],
    ['Here', 'is', 'some', 'data'],
    ["Here's", 'some', 'more', 'data']
]

# Return the string
tbl = tableize(toy_data)
 > | Here   | Are  | Some | Titles |
 > | ------ | ---- | ---- | ------ |
 > | Here   | is   | some | data   |
 > | Here's | some | more | data   |

# OR copy output to your clipboard
tableize(toy_data, clip=True)
```

# Note:

This module relies on `pyperclip` by [Al Sweigart](https://github.com/asweigart/pyperclip) for clipboard functionality.  

Install with `pip install pyperclip`

From the `pyperclip` documentation:

>On Windows, no additional modules are needed.
>On Mac, this module makes use of the pbcopy and pbpaste commands, which should come with the os.
>On Linux, this module makes use of the xclip or xsel commands, which should come with the os. Otherwise run "sudo apt-get install xclip" or "sudo apt-get install xsel" (Note: xsel does not always seem to work.)
>Otherwise on Linux, you will need the gtk or PyQt4 modules installed.
