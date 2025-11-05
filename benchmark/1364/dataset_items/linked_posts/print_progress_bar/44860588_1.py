from time import sleep, time
start_time = time()
for i in range(10):
    pref = str((i+1) * 10) + "% "
    complete_text = "done in %s sec" % str(round(time() - start_time))
    sleep(1)
    bar(10, i + 1, length=20, prefix=pref, oncomp=complete_text)
