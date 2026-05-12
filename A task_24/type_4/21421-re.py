from re import *

with open(r'../files/24_21421.txt') as file:
    data = file.readline()

pattern = r'[1-9A-B][0-9A-B]*[02468A]'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))