from part1 import hash

boxes : dict[int, list[tuple[str, int]]] = {}


def find_tuple(target: str, l: list[tuple[str, int]]) -> int:
    for i in range(len(l)):
        s, _ = l[i]
        if s == target: return i
    return -1


def main():
    instructions: list[str] = []
    with open("input.txt") as f:
        instructions = f.readline().strip().split(',')
    
    for i in range(256):
        boxes[i] = []
    
    for line in instructions:
        if '=' in line:
            label, focal = line.split('=')
            focal = int(focal)
            box_num = hash(label)
            index = find_tuple(label, boxes[box_num])
            if index == -1:
                boxes[box_num].append((label, focal))
            else:
                boxes[box_num][index] = (label, focal)
        else:
            label = line.strip('-')
            box_num = hash(label)
            index = find_tuple(label, boxes[box_num])
            if index != -1:
                boxes[box_num].pop(index)
    
    total = 0
    for key in boxes:
        if boxes[key] == []: continue

        for i, lense in enumerate(boxes[key]):
            _, focal = lense
            total += (key + 1) * (i + 1) * focal
    print(total)
            


if __name__ == "__main__":
    main()