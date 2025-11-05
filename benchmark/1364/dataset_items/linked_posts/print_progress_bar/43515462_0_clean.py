def printProgressBar (iteration, total, prefix = '', suffix = '',decimals = 1, length = 100, fill = '#'):

percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
filledLength = int(length * iteration // total)
bar = fill * filledLength + '-' * (length - filledLength)
print'\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix),
sys.stdout.flush()
# Print New Line on Complete                                                                                                                                                                                                              
if iteration == total:
    print()
