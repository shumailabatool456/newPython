#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#Nesting list in a dictionary
Travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting dictionary in a dictionary
Travel_log = {
    "France": {"visited_cities" :["Paris", "Lille", "Dijon"], "total_visits": 10 },
    "Germany": {"visited_cities" :["Berlin", "Hamburg", "Stuttgart"], "total_visits":5},
}

#nesting dictionary in a list
Travel_log = [
    {
        "country": "France", 
        "cities" :["Paris", "Lille", "Dijon"], "visits": 12
    },
    {
        "country":"Germany",
        "cities" :["Berlin", "Hamburg", "Stuttgart"], "visits":5
    },
]
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    Travel_log.append(new_country)

    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(Travel_log)

