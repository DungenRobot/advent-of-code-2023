import bisect

def get_falling(path):
    falling = []
    with open(path) as f:
        for line in f.readlines():
            first_corner, second_corner = line.strip().split('~')
            first_corner = [int(x) for x in first_corner.split(',')]
            second_corner = [int(x) for x in second_corner.split(',')]
            x1, y1, z1 = first_corner
            x2, y2, z2 = second_corner
            bottom = [min(x1, x2), min(y1, y2), min(z1, z2)]
            top = [max(x1, x2), max(y1, y2), max(z1, z2)]
            rect = [bottom, top]
            
            bisect.insort(falling, rect, key=lambda x: x[0][2])
    return falling


def check_overlap(rect1, rect2) -> bool:
    rect_1_bottom, rect_1_top = rect1
    rect_2_bottom, rect_2_top = rect2
    r1bx, r1by, r1bz = rect_1_bottom
    r1tx, r1ty, r1tz,= rect_1_top
    r2bx, r2by, r2bz = rect_2_bottom
    r2tx, r2ty, r2tz,= rect_2_top
    #we are going to define rect 1 as containing lower values than rect2
    if r1bx > r2bx: 
        r1bx, r2bx = r2bx, r1bx
        r1tx, r2tx = r2tx, r1tx
    if r1by > r2by: 
        r1by, r2by = r2by, r1by
        r1ty, r2ty = r2ty, r1ty
    if r1bz > r2bz: 
        r1bz, r2bz = r2bz, r1bz
        r1tz, r2tz = r2tz, r1tz
    
    x_overlapping = (r1bx <= r2bx <= r1tx)
    y_overlapping = (r1by <= r2by <= r1ty)
    z_overlapping = (r1bz <= r2bz <= r1tz)

    return x_overlapping and y_overlapping and z_overlapping


def overlaps_with_any(rect1, stack) -> bool:
    for other_rect in stack:
        if other_rect is rect1: continue #originally I checked if other_rect == rect1 but this was bad
        if check_overlap(rect1, other_rect):
            return True
    return False


def do_fall(falling: list[list[list[int]]]):
    stack = []
    falling = falling.copy()

    while len(falling) > 0:
        rect = falling.pop(0)

        while True:
            rect[0][2] -= 1
            rect[1][2] -= 1

            if (rect[0][2] <= 0) or overlaps_with_any(rect, stack):
                break
        rect[0][2] += 1
        rect[1][2] += 1

        stack.append(rect)
    return name_stack(stack)


def name_stack(unnamed_stack: list):
    name = 0
    named_stack = {}
    unnamed_stack = unnamed_stack.copy()

    while len(unnamed_stack) > 0:
        rect = unnamed_stack.pop(0)
        named_stack[str(name)] = rect
        name += 1
    return named_stack


def find_all_overlapping(name, named_stack):
    rect = named_stack[name]
    overlapping = []

    for key in named_stack:
        if key == name: continue
        other_rect = named_stack[key]
        if check_overlap(rect, other_rect):
            overlapping.append(key)
    return overlapping


def find_supporting(named_stack):
    support_dict = {}
    for key in named_stack:
        rect = named_stack[key]
        rect[1][2] += 1
        supporting = find_all_overlapping(key, named_stack)
        support_dict[key] = supporting
        rect[1][2] -= 1
    return support_dict


def count_supporting(supporting: dict):
    #create a dict of form key: rect name and value: how many blocks support it
    counts = {}
    for supported in supporting.values():
        for s in supported:
            counts[s] = counts.get(s, 0) + 1

    total = 0
    for base in supporting.keys():
        total += 1
        for supported in supporting[base]:
            # if any block that the base supports is only supported by that block: it cannot be removed
            if counts.get(supported, 0) == 1:
                total -= 1
                break
    return total


def main():
    falling = get_falling("input.txt") #gets a list of all the rects in the air
    print("collected")
    stack = do_fall(falling) #makes them fall into a stack. Returns a named stack of rectangles
    print("fell")
    supporting = find_supporting(stack) #returns what rects are supporting what others
    print("checked")
    counts = count_supporting(supporting)

    print(counts)


if __name__ == "__main__":
    main()