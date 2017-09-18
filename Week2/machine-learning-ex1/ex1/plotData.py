import csv
from collections import defaultdict


columns = defaultdict(list)

with open('ex1data1.txt') as f:
    reader = csv.