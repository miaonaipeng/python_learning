places = ['China', 'New York', 'Silicon Valley', 'Zhejiang', 'France']
# print("The first three items in the list are:")
# print(places[:3])
# print("Three items from the middle of the list are:")
# print(places[1:4])
# print("The last three items in the list are:")
# print(places[-3:])
places_duplicate = places[:]
places.append("California")
places_duplicate.append("Tokyo")

print("The places is:")
for place in places:
    print(place.upper())

print("The places_duplicate is:")
for place in places_duplicate:
    print(place.upper())
