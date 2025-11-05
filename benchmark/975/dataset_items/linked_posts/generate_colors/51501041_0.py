import numpy as np
from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
all_colors = [k for k,v in pltc.cnames.items()]

fracs = np.array([600, 179, 154, 139, 126, 1185])
labels = ["label1", "label2", "label3", "label4", "label5", "label6"]
explode = ((fracs == max(fracs)).astype(int) / 20).tolist()

for val in range(2):
    colors = sample(all_colors, len(fracs))
    plt.figure(figsize=(8,8))
    plt.pie(fracs, labels=labels, autopct='%1.1f%%', 
            shadow=True, explode=explode, colors=colors)
    plt.legend(labels, loc=(1.05, 0.7), shadow=True)
    plt.show()
