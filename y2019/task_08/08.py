from Helpers.helpers import read_newest_list
from operator import itemgetter

data = read_newest_list()
data = [int(d) for d in str(data[0])]
img_x = 25
img_x_act = 0
img_y = 6
img_y_act = 0
img = [[[]]]
layer = 0
layer_counts = {0:{}}

for dat in data:
    img[layer][img_y_act].append(dat)
    img_x_act += 1
    if dat == 0:
        layer_counts[layer][0] = layer_counts[layer].get(0, 0) + 1
    elif dat == 1:
        layer_counts[layer][1] = layer_counts[layer].get(1, 0) + 1
    elif dat == 2:
        layer_counts[layer][2] = layer_counts[layer].get(2, 0) + 1
    if img_x_act >= img_x:
        img_x_act = 0
        img_y_act += 1
        if img_y_act >= img_y:
            img_y_act = 0
            layer += 1
            img.append([[]])
            layer_counts[layer] = {}
        else:
            img[layer].append([])
del img[layer]
del layer_counts[layer]
print(layer_counts)
print(min([val.get(0, 0) for val in layer_counts.values()]))
min_layer = min(enumerate([val.get(0, 0) for val in layer_counts.values()]), key=itemgetter(1))[0]
print(layer_counts[min_layer][1] * layer_counts[min_layer][2])

# Part2

final_img = [['.']*img_x for i in range(img_y)]
for layer in reversed(img):
    for idx_y, y in enumerate(layer):
        for idx_x, x in enumerate(y):
            if x == 1 :
                final_img[idx_y][idx_x] = '#'
            elif x == 0:
                final_img[idx_y][idx_x] = ' '

for row in final_img:
    print(''.join(row))


