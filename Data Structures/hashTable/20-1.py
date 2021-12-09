def getDuplicates(array1, array2):
    hashMap1 = {}
    arrayAns = []
    for i in array1:
        hashMap1[i["first_name"] + " " + i["last_name"]] = True
    
    for i in array2:
        name = i["first_name"] + " " + i["last_name"]
        if hashMap1.get(name):
            arrayAns.append(name)
    
    return arrayAns

basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

print(getDuplicates(basketball_players, football_players))