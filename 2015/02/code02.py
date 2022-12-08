arr = []
with open('data02.txt') as f:
    for line in f:
        arr.append(line)

total_wrapping = 0
total_ribbon = 0
for box in arr:
    l, w, h = box[:-1].split('x')
    l, w, h = int(l), int(w), int(h)

    areas = l*w, w*h, h*l
    perimeters = 2*(l+w), 2*(l+h), 2*(h+w)

    extra_ribbon = l * w * h
    extra_area = min(areas)

    area = 2*sum(areas) + extra_area
    ribbon = min(perimeters) + extra_ribbon

    total_wrapping += area
    total_ribbon += ribbon

print(total_wrapping)
print(total_ribbon)

