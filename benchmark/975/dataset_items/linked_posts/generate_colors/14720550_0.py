colors = "bgrcmykw"
color_index = 0

for X,Y in data:
    scatter(X,Y, c=colors[color_index])
    color_index += 1
