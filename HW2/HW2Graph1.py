import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('ReturnToWorkBreakdownCS.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))  
plt.bar(x, y, color = 'b', width = 0.72)
plt.xlabel('Return to Work Strategy', fontweight='bold')
plt.ylabel('# of Companies', fontweight='bold')
plt.title('Number of tech companies using each return to work strategy')
plt.legend()
plt.show()