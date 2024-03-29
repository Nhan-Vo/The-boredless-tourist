destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt", "Tây Ninh, Việt Nam"]
traveler1 = ['Trần Cao Kỳ Duyên', 'Tây Ninh, Việt Nam',['food', 'beautiful view', 'drinks']]
traveler2 = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_des_index(destination):
    index = destinations.index(destination)
    return index
attractions = [[] for i in range(len(destinations))]
def add_attraction(des, attract):
    index = get_des_index(des)
    attractions[index].append(attract)
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Tây Ninh, Việt Nam", ["Eden Cafe",["drinks", "relax"]])
add_attraction("Tây Ninh, Việt Nam", ["Bầu Sen restaurant",["food"]])
add_attraction("Tây Ninh, Việt Nam", ["Ma Thiên Lãnh", ["beautiful view"]])
def find_attraction(desti, interests):    
    possible_attraction = []
    attractions_in_city = attractions[get_des_index(desti)]
    for attraction in attractions_in_city:
        for interest in attraction[1]:
            if interest in interests:
                possible_attraction.append(attraction[0])
    return possible_attraction
def get_attract_for_traveler(traveler):
    attract = find_attraction(traveler[1], traveler[2])
    string = "Hi "+ traveler[0] +", we think you'll like these places around "+ traveler[1]+": "
    for i in range(len(attract)):
        string += attract[i]
        if i != len(attract) - 1:
            string += ", "
    return string
print(get_attract_for_traveler(traveler1))