import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv('population.csv')
year = data.year
population = data.population

plt.plot(year,population)
plt.title('data population')
plt.xlabel('years')
plt.ylabel('population')
plt.legend(['Population'])
plt.show()