r = 7
for x in range(0,490):
        for y in range(0,490):
                if mask[x,y] < r:
                        mask[x,y] = 0
                elif mask[x,y] >= r:
                        mask[x,y] = 256

maskimg = plt.imshow(mask,cmap="gray")
plt.show()
