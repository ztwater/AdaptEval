import time
from progressbar import ProgressBar

count = 150
print("starting things:")

with ProgressBar(count) as bar:
    for i in range(count + 1):
        bar.value += 1
        time.sleep(0.01)

print("done")
