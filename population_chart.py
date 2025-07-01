import matplotlib.pyplot as plt

countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Russia', 'Japan', 'Mexico']
population = [1444216107, 1393409038, 332915073, 276361783, 240485658, 216422446, 213401323, 144104080, 125507472, 127504125]


plt.figure(figsize=(10,6))
plt.bar(countries, population, color='skyblue')
plt.title('Population by Country (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()


plt.savefig("population_chart.png")


plt.show()