import math

"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""


def file_to_text(filename):
    infile = open(filename, 'r', encoding=" ISO-8859-15")
    contents = infile.read()
    infile.close()
    return contents


def get_lines(filename):
    input_text = file_to_text(filename)
    lines = input_text.split('\n')
    if len(lines[-1]) == 0:
        lines.pop()
    return lines


"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""


def new_matrix(r, c, fill):
    r = r if r >= 2 else 2
    c = c if c >= 2 else 2
    return [[fill] * c for i in range(r)]
