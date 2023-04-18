from sys import stdin
from itertools import chain
lines = [i.split(" ") for i in stdin.read().split("\n")]

print(chain(lines))