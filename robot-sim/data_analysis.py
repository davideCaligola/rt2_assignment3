import os
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

def plot_data(filename, title):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(float(line))
        f.close()

    f, ax = plt.subplots()
    n, bins, patches = ax.hist(data,rwidth=0.9,bins=10,density=True)
    bin_centers = [(j+i)/2 for i, j in zip(bins[:-1], bins[1:])]
    labels = ['{:.2f}'.format(i) for i in bin_centers]
    ax.set_xticklabels(labels)
    ax.set_title(title)
    ax.set_xlabel('time [s]')
    ax.set_ylabel('# of events (normalized)')
    
    print(f'mean: {np.mean(data):.2f}')
    print(f'variance: {np.var(data):.2f}')

    # check data normality
    alpha = 0.01
    ksstat, pvalue = sm.stats.diagnostic.lilliefors(data)
    if pvalue > alpha:
        result = 'Normal'
    else:
        result = 'NOT Normal'

    print(f'Lilliefors: {result:>10s}')
    print(f'pvalue: {pvalue:.5f}')
    f.show()


path = f'{os.path.dirname(os.path.realpath(__file__))}'
files = [f'{path}/times_a.txt', f'{path}/times_b.txt']
names = ['Algorithm A', 'Algorithm B']

for idx, file in enumerate(files):
    plot_data(file, names[idx])
input()



