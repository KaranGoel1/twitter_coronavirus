#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

'''    
df = pd.DataFrame(columns = ['labels', 'values'])
labels = [item[0] for item in items[:10]]
values = [item[1] for item in items[:10]]
df['labels'] = labels
df['values'] = values
df_sorted = df.sort_values('values')
'''
labels = [item[0] for item in items[:10]]
values = [item[1] for item in items[:10]]

plt.bar(labels, values)
plt.savefig(f'{args.key}_{args.input_path[8:]}.png')
