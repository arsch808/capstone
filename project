import random

#defining the main 4x4 attributes
#STRINGS
#right now these are strings but i have the feeling as they are linked to a button press they will become a 0,1 integer of some sort 
#really just making my life harder rn i think for the sake of understanding my own code
Water = ["Desert", "Lakes", "Ocean", "Megaocean"]
Distance = ["Close", "Inner", "Outer", "Distant" ]
Size = ["Small", "Medium", "Giant", "Supergiant" ]
Atmosphere = ["Thin & Light", "Thin & Dense", "Thick & Light", "Thick & Dense" ]



#hab scores for each attribute, uses these for the final score
hab_water = (1, 2, 3, 3)
hab_distance = (1, 3, 2, 1)
hab_size = (1, 3, 3, 2)
hab_atmosphere = (1, 2, 3, 1)

def hab_score(w, d, s, a):
    score = hab_water[Water.index(w)] + hab_distance[Distance.index(d)] + hab_size[Size.index(s)] + hab_atmosphere[Atmosphere.index(a)]
    return score



#pull facts for each attribute, several facts per attribute 
#water
desertfact = ["1desert", "2desert", "3desert"]
lakefact = ["1lake", "2lake", "3lake"]  
oceanfact = ["1ocean", "2ocean", "3ocean"]      
megafact = ["1mega", "2mega", "3mega"] 

#distance
closefact = ["1close", "2close", "3close"]
innerfact = ["1inner", "2inner", "3inner"]
outerfact = ["1outer", "2outer", "3outer"]
distantfact = ["1distant", "2distant", "3distant"]

#size
smallfact = ["1small", "2small", "3small"]
mediumfact = ["1medium", "2medium", "3medium"]
giantfact = ["1giant", "2giant", "3giant"]
superfact = ["1super", "2super", "3super"]

#atmosphere
thinlightfact = ["1thinlight", "2thinlight", "3thinlight"]
thindensefact = ["1thindense", "2thindense", "3thindense"]
thicklightfact = ["1thicklight", "2thicklight", "3thicklight"]
thickdensefact = ["1thickdense", "2thickdense", "3thickdense"]

#creates a new list of ALL facts of all chosen attributes, stores this in variable factsheet
def create_factsheet(w, d, s, a):
    factsheet = []
    if w == "Desert":
        factsheet.extend(desertfact)
    elif w == "Lakes":
        factsheet.extend(lakefact)
    elif w == "Ocean":
        factsheet.extend(oceanfact)
    elif w == "Megaocean":
        factsheet.extend(megafact)

    if d == "Close":
        factsheet.extend(closefact)
    elif d == "Inner":
        factsheet.extend(innerfact)
    elif d == "Outer":
        factsheet.extend(outerfact)
    elif d == "Distant":
        factsheet.extend(distantfact)

    if s == "Small":
        factsheet.extend(smallfact)
    elif s == "Medium":
        factsheet.extend(mediumfact)
    elif s == "Giant":
        factsheet.extend(giantfact)
    elif s == "Supergiant":
        factsheet.extend(superfact)

    if a == "Thin & Light":
        factsheet.extend(thinlightfact)
    elif a == "Thick & Light":
        factsheet.extend(thindensefact)
    elif a == "Thin & Dense":
        factsheet.extend(thicklightfact)
    elif a == "Thick & Dense":
        factsheet.extend(thickdensefact)
    return factsheet

#randomly selects 3 facts from the factsheet to show, stores in displaysheet
def create_displaysheet(factsheet):
    displaysheet = random.sample(factsheet, 3)
    return displaysheet    



def main():
        w = input("Choose Water:")
        d = input("Choose Distance:")
        s = input("Choose Size:")
        a = input("Choose Atmosphere:")
        score = hab_score(w, d, s, a)
        factsheet = create_factsheet(w, d, s, a)
        displaysheet = create_displaysheet(factsheet)
        print("Hab Score:", score)
        print(factsheet)
        print("Display Facts:", displaysheet)

main()