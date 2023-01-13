cities = {
    'New York': {
        'country': 'The US',
        'population': '10000000',
        'fact': "It's very rich.",
    },
    'Beijing': {
        'country': 'China',
        'population': '80000000',
        'fact': "There are many riches and pools.",
    },
    'Paris': {
        'country': 'French',
        'population': '20000000',
        'fact': "There are source of popularity.",
    },

}
for city, city_info in cities.items():
    print("City_name: " + city)
    print("\tCountry: " + city_info['country'])
    print("\tPopulation: " + str(city_info['population']))
    print("\tFact: " + city_info['fact'])
