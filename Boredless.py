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
add_attraction("Tây Ninh, Việt Nam", ["Bầu Sen restaurant",["food", "beautiful view"]])
add_attraction("Tây Ninh, Việt Nam", ["Ma Thiên Lãnh", ["beautiful view"]])
#hoc lam viec nghi ngoi ngu da dang se
print(attractions)
