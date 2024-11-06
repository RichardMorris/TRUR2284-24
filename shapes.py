# Shapes.py
# Code to generate a set of ASCII art shapes

# Return a line on n-stars
# return an empty string for n<1

def stars(n):
    if n < 1:
        return ""
    s = ""
    for i in range(0,n):
        s += "*"
    return s