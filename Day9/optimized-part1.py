#this is a version of my part one that I modified after completing part two
def main():
    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line.strip()

            numbers = [int(i) for i in line.split(' ')]

            total += numbers[-1]

            while sum(numbers) > 0:
                numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

                total += numbers[-1]

    print(total)



if __name__ == "__main__":
    main()

