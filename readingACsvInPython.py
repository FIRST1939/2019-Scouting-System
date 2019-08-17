# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:43:38 2019

@author: Mason
"""

import csv
from tkinter import filedialog

teams = []

with open(filedialog.askopenfilename(title = 'select MatchList file')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            teams.append(row[2])
            line_count += 1
    print(f'Processed {line_count} lines.')
    row = 0
    print(row)
    
with open(filedialog.askopenfilename(title = 'select MatchList file')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0    
    for row in csv_reader:
        print (row)
        if '\'1723\'' == teams[row]:
            print("True")
        line_count += 1