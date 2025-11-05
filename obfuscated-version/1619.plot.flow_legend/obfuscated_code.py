var_0 = np.linspace(0, 2*np.pi, 13)
var_1 = np.cos(var_0)
var_2 = np.sin(var_0)
var_3 = np.cos(var_0)
var_4 = np.sin(var_0)
var_5 = arctan2(var_3, var_4)

var_6 = Normalize()
var_6.autoscale(var_5)
# we need to normalize our colors array to match it colormap domain
# which is [0, 1]

var_7 = cm.inferno
# pick your colormap here, refer to 
# http://matplotlib.org/examples/color/colormaps_reference.html
# and
# http://matplotlib.org/users/colormaps.html
# for details
plt.figure(figsize=(6, 6))
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.quiver(var_1, var_2, var_3, var_4, color=var_7(var_6(var_5)),  angles='xy', 
           scale_units='xy', scale=1, pivot='mid')
