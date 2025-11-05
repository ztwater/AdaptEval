total = 6000
barsize = 60
print_frequency = max(min(total//barsize, 100), 1)
print("Start Task..", flush=True)
for i in range(1, total+1):
  if i%print_frequency == 0 or i == 1:
    print_progressbar(total, i, barsize)
print("\nFinished", flush=True)
