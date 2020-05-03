import matplotlib.pylab as plt

x = [2001,2002,2003,2004,2005,2006,2007]
y = [12,34,56,43,65,70,91]

plt.plot(x,y)
plt.title('data population')
plt.xlabel('years')
plt.ylabel('population')
plt.legend(['Population'])
plt.show()