import os

lines = ["Readme", str(12345)]

f = open('readme.txt', 'a')

f.write("a line")
f.write('\n')

f.close()