
def all_are_not_zero(h: list):
    for i in h:
        if i != 0:
            return True
    return False


def main():
    total = 0
    with open("input.txt") as f:
        for line in f.readlines():
            line.strip()

            numbers = [int(i) for i in line.split(' ')]

            history = [numbers[-1]]

            while all_are_not_zero(numbers):
                new = []

                for i in range(len(numbers) - 1):
                    new.append(numbers[i + 1] - numbers[i])
                
                numbers = new

                history.append(numbers[-1])

            difference = history.pop()

            while len(history) > 0:
                difference += history.pop()


            total += difference


    print(total)



if __name__ == "__main__":
    main()

