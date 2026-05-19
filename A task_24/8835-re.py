from re import *

with open(r'files/24-371.txt') as file:
    data = file.readline()

pattern = r'([^M\.]*[M]){112}[^M\.]*[\.]'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))