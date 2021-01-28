import itertools

from Helpers.helpers import read_newest

data = read_newest()
data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split('\n')
dat = data[0]
ingredients, allergens = [], []
all_ingredients, all_allergens = [], []
for dat in data:
    idx = dat.index('(')
    ingredients.append(set(dat[:(idx-1)].split(' ')))
    all_ingredients.extend(ingredients[-1])
    allergens.append(set(dat[(idx + 10):-1].split(', ')))
    all_allergens.extend(allergens[-1])

all_allergens = set(all_allergens)

possible_allergens = {}
all_possible_allergens = []
for allergen in all_allergens:
    this_ingredients = []
    for idx, itm in enumerate(allergens):
        if allergen in itm:
            this_ingredients.append(ingredients[idx])

    possible_allergens[allergen] = set(set.intersection(*this_ingredients))
    all_possible_allergens.extend(set(set.intersection(*this_ingredients)))
all_possible_allergens = set(all_possible_allergens)

counter = 0
for ingr in all_ingredients:
    if ingr not in all_possible_allergens:
        counter += 1
print(counter)

dairy thvm
eggs jmdg
nuts qrsczjv
peanuts hlmvqh
sesame zmb
shellfish mrfxh
soy ckqq
wheat zrgzf

thvm,jmdg,qrsczjv,hlmvqh,zmb,mrfxh,ckqq,zrgzf
