
test = [
    [7, 9],
    [15, 40],
    [30, 200]
]

input = [
    [47, 282],
    [70, 1079],
    [75, 1147],
    [66, 1062]
]

target = input

total = 1

for time, distance in target:
    num_solutions = 0
    for i in range(time):
        predicted_distance = i * (time - i)
        if predicted_distance > distance:
            num_solutions += 1

    print(num_solutions)
    total *= num_solutions

print(total)
