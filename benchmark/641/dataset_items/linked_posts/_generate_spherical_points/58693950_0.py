import random
R = 2

def sample_circle(center):
    a = random.random() * 2 * np.pi
    r = R * np.sqrt(random.random())
    x = center[0]+ (r * np.cos(a))
    y = center[1] + (r * np.sin(a))
    return x,y

ps = np.array([sample_circle((0,0)) for i in range(100)])

plt.plot(ps[:,0],ps[:,1],'.')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()
