from collections import Counter
from pprint import pprint as pp
raw_coordinates = open('input.txt', 'r').read().strip().split('\n')
coordinate_strings = [x.split('->') for x in raw_coordinates]
parsed_coordinates = [[y.split(',') for y in coordinates] for coordinates in coordinate_strings]

start, end = zip(*parsed_coordinates)

width_of_elements = 10
depth_of_elements = 10

# vent_map = [[[0 for c in range(width_of_coordinates)] for e in range(width_of_elements)] for d in range(depth_of_elements)]
vent_map = [[0 for e in range(width_of_elements)] for d in range(depth_of_elements)]

# pp(parsed_coordinates)

for st, en in zip(start, end):
    x1 = int(st[0])
    x2 = int(en[0])

    y1 = int(st[1])
    y2 = int(en[1])

    path = []

    # diagonals
    if x1 != x2 and y1 != y2:
        if x1 < x2:
            x_diff = x2 - x1
        else:
            x_diff = x1 - x2

        if y1 < y2:
            y_diff = y2 - y1
        else:
            y_diff = y1 - y2

        for x in range(x1, x2 + 1):
            if y2 > y1:
                y = y1 + (x - x1)
            else:
                y = y1 - (x - x1)

            # path.append([x, y])
        import ipdb; ipdb.set_trace()


    #     continue
    if x1 != x2 and y1 == y2:
        if x1 < x2:
            diff = x2 - x1
            path = [[x1 + d, y1] for d in range(diff + 1)]
        else:
            diff = x1 - x2
            path = [[x1 - d, y1] for d in range(diff + 1)]
    elif y1 != y2 and x1 == y2:
        if y1 < y2:
            diff = y2 - y1
            path = [[x1, y1 + d] for d in range(diff + 1)]
        else:
            diff = y1 - y2
            path = [[x1, y1 - d] for d in range(diff + 1)]

    for item in path:
        try:
            vent_map[item[1]][item[0]] += 1
        except IndexError:
            import ipdb; ipdb.set_trace()

pp(vent_map)

# count = sorted(
#     Counter(list(zip(*vent_map))).most_common(), key=lambda x: (x[1], x[0])
# )

count = 0
for i in vent_map:
    for j in i:
        if j > 1:
            count += 1
pp(count)

#
# d = [[int(x) for x in l.replace(" -> "," ").replace(","," ").split()] for l in open("input.txt","rt")]
# a = {}
# b = {}
# for x1,y1,x2,y2 in d:
#   if x1==x2:
#     if y1>y2: y1,y2=y2,y1
#     for y in range(y1,y2+1):
#       a[(x1,y)]=a.get((x1,y),0)+1
#       b[(x1,y)]=b.get((x1,y),0)+1
#   elif y1==y2:
#     if x1>x2: x1,x2=x2,x1
#     for x in range(x1,x2+1):
#       a[(x,y1)]=a.get((x,y1),0)+1
#       b[(x,y1)]=b.get((x,y1),0)+1
#   else:
#     if x1>x2: x1,x2, y1,y2 = x2,x1, y2,y1
#     for x in range(x1,x2+1):
#       if y2>y1: y = y1+(x-x1)
#       else:     y = y1-(x-x1)
#       b[(x,y)]=b.get((x,y),0)+1
# print( sum(v>1 for v in a.values()) )
# print( sum(v>1 for v in b.values()) )

# 5306
# 17787