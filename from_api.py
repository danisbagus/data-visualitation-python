import matplotlib.pylab as plt
import requests

BASE_URL = "https://testapi.io/api/danisbagus"

response = requests.get(f"{BASE_URL}/population")

data = response.json()

year = []
population = []

for value in data:
    print(value['year'])
    year.append(value['year'])
    population.append(value['population'])

plt.plot(year,population)
plt.title('data population')
plt.xlabel('years')
plt.ylabel('population')
plt.legend(['Population'])
plt.show()