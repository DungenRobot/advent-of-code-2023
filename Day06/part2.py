
test = [71530, 940200]
input = [47707566, 282107911471062]
target = input
time, distance = target

num_solutions = 0

for i in range(time):
    predicted_distance = i * (time - i)
    if predicted_distance > distance:
        num_solutions += 1


print(num_solutions)
