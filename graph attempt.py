import matplotlib.pyplot as plt
import csv
from tkinter import filedialog


FileName = filedialog.askopenfilename(title = 'select MatchList file')
    
x = []
y = []

with open(FileName, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='|')
    line_count = 1
    for row in plots:
        x.append(int(row[2]))
        y.append(int(row[3]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.grid(True)
plt.legend()
plt.show()