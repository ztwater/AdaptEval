combo = []
for i in range(60000):
    combo.append((images[i], labels[i]))

shuffle(combo)

im = []
lab = []
for c in combo:
    im.append(c[0])
    lab.append(c[1])
images = np.asarray(im)
labels = np.asarray(lab)
