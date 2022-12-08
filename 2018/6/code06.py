lines = []
area = [] 
w, h = 0, 0

def create_grid():
    ''' Produce an empty matrix of sizes w,h
    and an array of dictionaires of locations containing
        x: [number]
        y: [number]
        id: [number]'''
    global area, lines, w, h
    with open('data06.txt') as f:
        id = 1
        for i in f:
            coords = {}
            coords['x'] = int(i.split(',')[0])
            coords['y'] = int(i.split(',')[1][:-1])
            coords['id'] = id
            lines.append(coords)
            id += 1

    # find the largest values for x and y
    w = 0
    h = 0
    for coords in lines:
        x = coords['x']
        y = coords['y']
        if x > w:
            w = x
        if y > h:
            h = y

    # create empty array
    w,h = w+1, h+1
    area = []
    for y in range(h):
        area.append([])
        for x in range(w):
            area[y].append(0) 



def part_one():
    # fill every cell with the id of the closest location
    for y in range(h):
        for x in range(w):
            min_dist = 100000
            for coords in lines:
                loc_x = coords['x']
                loc_y = coords['y']
                loc_id = coords['id']
                dist_x = abs(loc_x - x)
                dist_y = abs(loc_y - y)
                mhtn_dist = dist_x + dist_y
                if mhtn_dist < min_dist:
                    min_dist = mhtn_dist
                    val = loc_id
                elif mhtn_dist == min_dist:
                    val = '.'
            area[y][x] = val 

    # find all locations with infinite size
    infinite_loc = []
    for y in range(h):
        if y in [0,h-2]:
            for x in range(w):
                if area[y][x] not in infinite_loc:
                    infinite_loc.append(area[y][x])
        else: 
            for x in [0,w-1]:
                if area[y][x] not in infinite_loc:
                    infinite_loc.append(area[y][x])

    # find the location with the largest size
    sizes = {}
    for y in range(h):
        for x in range(w):
            val = area[y][x]
            if val == 0:
                print('something wrong?')
            elif val in infinite_loc:
                continue
            if val in sizes:
                sizes[val] += 1
            else:
                sizes[val] = 1
    largest_area_size = 0
    for i in sizes:
        if sizes[i] > largest_area_size:
            largest_area_size = sizes[i]
            largest_area = i
    return largest_area_size

                
def part_two():
    max_dist = 10000
    size_closest_region = 0
    for y in range(h):
        for x in range(w):
            total_mhtn_dist = 0
            for coords in lines:
                loc_x = coords['x']
                loc_y = coords['y']
                loc_id = coords['id']
                dist_x = abs(loc_x - x)
                dist_y = abs(loc_y - y)
                mhtn_dist = dist_x + dist_y
                total_mhtn_dist += mhtn_dist
            if total_mhtn_dist < max_dist:
                size_closest_region += 1
    return size_closest_region


create_grid()
print('largest_area_size for part one is:',part_one())
print('size of the region for part two is:',part_two())
