from itertools import combinations_with_replacement, product

from Helpers.helpers import read_newest_dataframe
from math import gcd
import pandas as pd
data = read_newest_dataframe()
# data = pd.DataFrame([[
#     '.','#','.','.','#'],[
#     '.','.','.','.','.'],[
#     '#','#','#','#','#'],[
#     '.','.','.','.','#'],[
#     '.','.','.','#','#']
# ])

# data = pd.DataFrame([[
# '.','#','.','.','#','#','.','#','#','#','.','.','.','#','#','#','#','#','#','#',],[
# '#','#','.','#','#','#','#','#','#','#','#','#','#','#','#','.','.','#','#','.',],[
# '.','#','.','#','#','#','#','#','#','.','#','#','#','#','#','#','#','#','.','#',],[
# '.','#','#','#','.','#','#','#','#','#','#','#','.','#','#','#','#','.','#','.',],[
# '#','#','#','#','#','.','#','#','.','#','.','#','#','.','#','#','#','.','#','#',],[
# '.','.','#','#','#','#','#','.','.','#','.','#','#','#','#','#','#','#','#','#',],[
# '#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',],[
# '#','.','#','#','#','#','.','.','.','.','#','#','#','.','#','.','#','.','#','#',],[
# '#','#','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#',],[
# '#','#','#','#','#','.','#','#','.','#','#','#','.','.','#','#','#','#','.','.',],[
# '.','.','#','#','#','#','#','#','.','.','#','#','.','#','#','#','#','#','#','#',],[
# '#','#','#','#','.','#','#','.','#','#','#','#','.','.','.','#','#','.','.','#',],[
# '.','#','#','#','#','#','.','.','#','.','#','#','#','#','#','#','.','#','#','#',],[
# '#','#','.','.','.','#','.','#','#','#','#','#','#','#','#','#','#','.','.','.',],[
# '#','.','#','#','#','#','#','#','#','#','#','#','.','#','#','#','#','#','#','#',],[
# '.','#','#','#','#','.','#','.','#','#','#','.','#','#','#','.','#','.','#','#',],[
# '.','.','.','.','#','#','.','#','#','.','#','#','#','.','.','#','#','#','#','#',],[
# '.','#','.','#','.','#','#','#','#','#','#','#','#','#','#','#','.','#','#','#',],[
# '#','.','#','.','#','.','#','#','#','#','#','.','#','#','#','#','.','#','#','#',],[
# '#','#','#','.','#','#','.','#','#','#','#','.','#','#','.','#','.','.','#','#',]])

# data = pd.DataFrame([[
# '.','#','.','.','.','.','#','#','#','#','#','.','.','.','#','.','.',],[
# '#','#','.','.','.','#','#','.','#','#','#','#','#','.','.','#','#',],[
# '#','#','.','.','.','#','.','.','.','#','.','#','#','#','#','#','.',],[
# '.','.','#','.','.','.','.','.','X','.','.','.','#','#','#','.','.',],[
# '.','.','#','.','#','.','.','.','.','.','#','.','.','.','.','#','#',]])

def search_asteroid(data, loc_x, loc_y, angle):
    loc_x_search = loc_x + angle[0]
    loc_y_search = loc_y + angle[1]
    while data.shape[0] > loc_x_search >= 0 and data.shape[1] > loc_y_search >= 0:
        if data.loc[loc_x_search, loc_y_search] == '#':
            # print("{}, {} --> {}, {}".format(loc_x, loc_y, loc_x_search, loc_y_search))
            return True
        else:
            loc_x_search += angle[0]
            loc_y_search += angle[1]
            continue
    return False


def count_asteroids(data, loc_x, loc_y):
    asteroids_found = 0
    for i in range(-data.shape[0], data.shape[0]+1):
        for j in range(-data.shape[1], data.shape[1]+1):
            angle = [i, j]
            if (abs(i) == 0 and abs(j) == 1) or (abs(j) == 0 and abs(i) == 1) :
                asteroids_found += search_asteroid(data, loc_x, loc_y, angle)
            elif ((i == 0 and j == 0)
                    or ((i+j == i
                         or i+j == j)
                        and (i != 1
                             or j != 1))
                    or (gcd(i, j) != 1)):
                continue
            else:
                asteroids_found += search_asteroid(data, loc_x, loc_y, angle)
    return asteroids_found


result = {}
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data.loc[i, j] == '#':
            result[(i, j)] = count_asteroids(data, i, j)

print(result)
location = (max(result, key=result.get))
print(result[max(result, key=result.get)])


#Part 2
# Switched X and Y in part 1!
possible_angles = product(range(max(data.shape)+1), range(1, max(data.shape)+1))
possible_angles_df = pd.DataFrame([[i, j, i/j] for i, j in possible_angles if gcd(i, j) == 1])
possible_angles_df_sorted = possible_angles_df.sort_values(2).reset_index()
angles = list(zip(-possible_angles_df_sorted[1], possible_angles_df_sorted[0])) + \
         list(zip(possible_angles_df_sorted[0], possible_angles_df_sorted[1])) + \
         list(zip(possible_angles_df_sorted[1], -possible_angles_df_sorted[0])) + \
         list(zip(-possible_angles_df_sorted[0], -possible_angles_df_sorted[1]))
def shoot_laser(data, angle, location, destroyed):
    loc_x, loc_y = location
    loc_x_search = loc_x + angle[0]
    loc_y_search = loc_y + angle[1]
    while data.shape[0] > loc_x_search >= 0 and data.shape[1] > loc_y_search >= 0:
        if data.loc[loc_x_search, loc_y_search] == '#':
            print("{} Hitted {}, {} with angle ({}, {})".format(destroyed+1, loc_x_search, loc_y_search, angle[0], angle[1]))
            data.at[loc_x_search, loc_y_search] = str(destroyed+1)
            return data, True
        else:
            loc_x_search += angle[0]
            loc_y_search += angle[1]
            continue
    return data, False

destroyed = 0
while destroyed < 200:
    for angle in angles:
        hit = False
        data, hit = shoot_laser(data, angle, location, destroyed)
        destroyed += hit

