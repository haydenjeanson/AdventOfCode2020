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
    lines.pop()
    return lines
