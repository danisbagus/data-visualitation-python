import matplotlib.pylab as plt
import json

year = []
population = []
with open('population.json') as json_file:
    data = json.load(json_file)
    for value in data:
        year.append(value['year'])
        population.append(value['population'])

plt.plot(year,population)
plt.title('data population')
plt.xlabel('years')
plt.ylabel('population')
plt.legend(['Population'])
plt.show()