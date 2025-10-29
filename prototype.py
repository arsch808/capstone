import csv
import random

#defining the main 4x4 attributes
#STRINGS
#right now these are strings but i have the feeling as they are linked to a button press they will become a 0,1 integer of some sort 
#really just making my life harder rn i think for the sake of understanding my own code
Distance = ["Close", "Inner", "Outer", "Distant" ]
Size = ["Small", "Medium", "Giant", "Supergiant" ]
Density = ["Solid", "Varied", "Watery", "Puffy"]
Temp = ["Cold", "Varied", "Temperate", "Hot"]



#hab scores for each attribute, uses these for the final score
hab_temp = (1, 2, 3, 1)
hab_distance = (1, 3, 2, 1)
hab_size = (1, 3, 3, 2)
hab_density = (1, 2, 3, 1)

target = []
def main():
    d = input("Distance:")
    p = input("Density:")
    s = input("Size:")
    t = input("Temp:")
    global target
    target = [d,p,s,t]

    dscore = pscore = sscore = tscore = 0
    dlabel = plabel = slabel = tlabel = "Invalid"

    try:
        d = int(d)
        p = int(p)
        s = int(s)
        t = int(t)
    except ValueError:
        print("Please enter numbers 1-4 for each attribute.")
        return

    if d == 1:
        dlabel = "Close"
        dscore = 1
    elif d == 2:
        dlabel = "Inner"
        dscore = 3
    elif d == 3:
        dlabel = "Outer"
        dscore = 2
    elif d == 4:
        dlabel = "Distant"
        dscore = 1
    else:
        print("Invalid Distance input.")

    if p == 1:
        plabel = "Solid"
        pscore = 1
    elif p == 2:
        plabel = "Varied"
        pscore = 2
    elif p == 3:
        plabel = "Watery"
        pscore = 3
    elif p == 4:
        plabel = "Puffy"
        pscore = 1
    else:
        print("Invalid Density input.")
    
    if s == 1:
        slabel = "Small"
        sscore = 1
    elif s == 2:
        slabel = "Medium"
        sscore = 3
    elif s == 3:
        slabel = "Giant"
        sscore = 3
    elif s == 4:
        slabel = "Supergiant"
        sscore = 2
    else:
        print("Invalid Size input.")

    if t == 1:
        tlabel = "Cold"
        tscore = 1
    elif t == 2:
        tlabel = "Varied"
        tscore = 2
    elif t == 3:
        tlabel = "Temperate"
        tscore = 3
    elif t == 4:
        tlabel = "Hot"
        tscore = 1
    else:
        print("Invalid Temp input.")

    score = dscore + pscore + sscore + tscore
    print('parameters:', dlabel, plabel, slabel, tlabel)
    print("Hab Score:", score)

main()



def compare(filename, target):
    best_match_arrays = []
    max_matches = -1
    
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            current_matches = 0
            # Only compare elements at indices 1,2,3,4 (rows 2,3,4,5)
            for i in range(0, min(len(target), len(row))):
                if target[i] == row[i]:
                    current_matches += 1

            if current_matches > max_matches:
                max_matches = current_matches
                best_match_arrays = [row]  # Reset list with new best match
            elif current_matches == max_matches:
                best_match_arrays.append(row)  # Add to list of equally good matches

        # Choose random match from best matches
        if best_match_arrays:
            best_match_array = random.choice(best_match_arrays)
            print("Best matching row from CSV:", best_match_array[0])
        else:
            print("No matching row found in the CSV file.")

compare('ss_test.csv', target)

